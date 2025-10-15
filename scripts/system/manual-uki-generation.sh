#!/bin/bash

# ==============================================================================
#      A script to manually regenerate a Fedora UKI (Unified Kernel Image)
# ==============================================================================
#
# This script is designed to manually trigger a full UKI generation process
# for an installed kernel version in the system.
# It mimics the automated steps performed by Fedora's kernel RPM package
# during its post-transaction scriptlet (%posttrans).
#
# Use Cases:
#   - After modifying dracut configurations (e.g., adding new modules or drivers).
#   - After updating static configurations for systemd-ukify (e.g., changing the kernel command line).
#   - When you need to forcibly repackage the EFI file for an existing kernel version.
#
# Prerequisites:
#   - The corresponding kernel package is already installed (vmlinuz, modules, dtb files exist).
#   - `dracut` and `systemd-boot` (which provides ukify) are installed.
#   - Relevant configuration files are in place:
#     - dracut config: /etc/dracut.conf and /etc/dracut.conf.d/
#     - ukify  config: /etc/systemd/ukify.conf
#
# ==============================================================================

set -e  # Exit immediately if a command exits with a non-zero status.
set -u  # Treat unset variables as an error when substituting.
set -o pipefail # The return value of a pipeline is the status of the last command to exit with a non-zero status.

# --- Script Arguments ---
# If the user does not provide a kernel version on the command line,
# the currently running kernel version is used automatically.
# You can also specify one manually, e.g., ./regenerate-uki.sh 6.16-5.sm8150.aarch64
TARGET_UNAME_R=${1:-$(uname -r)}

echo "--- Preparing to regenerate UKI for kernel version ${TARGET_UNAME_R} ---"

# --- Check for required commands ---
command -v dracut >/dev/null 2>&1 || { echo >&2 "Error: 'dracut' command not found. Please install it first."; exit 1; }
command -v ukify >/dev/null 2>&1 || { echo >&2 "Error: 'ukify' command not found. It is usually provided by the 'systemd-boot' package."; exit 1; }
command -v depmod >/dev/null 2>&1 || { echo >&2 "Error: 'depmod' command not found. Please check if the 'kmod' package is installed."; exit 1; }

# --- Define and validate paths ---
KERNEL_PATH="/boot/vmlinuz-${TARGET_UNAME_R}"
INITRD_PATH="/boot/initramfs-${TARGET_UNAME_R}.img" # This is a temporary file
DTB_PATH="/usr/lib/modules/${TARGET_UNAME_R}/dtb/qcom/sm8150-xiaomi-nabu.dtb" # Hardcoded from the spec file
UKI_DIR="/boot/efi/EFI/fedora"

# Check if the required files exist
if [ ! -f "${KERNEL_PATH}" ]; then
    echo "Error: Kernel image not found: ${KERNEL_PATH}" >&2
    exit 1
fi

if [ ! -d "/usr/lib/modules/${TARGET_UNAME_R}" ]; then
    echo "Error: Kernel modules directory not found: /usr/lib/modules/${TARGET_UNAME_R}" >&2
    exit 1
fi

if [ ! -f "${DTB_PATH}" ]; then
    echo "Warning: Device Tree Blob (DTB) file not found: ${DTB_PATH}" >&2
    echo "If you don't need a separate DTB, you can ignore this message." >&2
    # Set the variable to empty so it gets ignored in the ukify command
    DTB_PATH=""
fi

# --- Determine the final output EFI filename ---
UKI_PATH="${UKI_DIR}/fedora-${TARGET_UNAME_R}.efi"

# Ensure the output directory exists
mkdir -p "$UKI_DIR"

# ==============================================================================
#                       UKI Generation Process Starts
# ==============================================================================

# --- Step 1: Regenerate module dependencies ---
echo "INFO: Running depmod for ${TARGET_UNAME_R}..."
depmod -a "${TARGET_UNAME_R}"
echo "SUCCESS: Module dependencies have been updated."

# --- Step 2: Generate a temporary initramfs using dracut ---
echo "INFO: Generating initramfs using dracut..."
# Use the --force option to ensure any existing file with the same name is overwritten
dracut --kver "${TARGET_UNAME_R}" --force "${INITRD_PATH}"
if [ ! -f "${INITRD_PATH}" ]; then
    echo "CRITICAL: dracut failed to create the initramfs file: ${INITRD_PATH}" >&2
    exit 1
fi
echo "SUCCESS: Temporary initramfs has been generated at ${INITRD_PATH}"

# --- Step 3: Package all components into a UKI using systemd-ukify ---
echo "INFO: Generating the final UKI using systemd-ukify..."

# Build the ukify command arguments
ukify_args=(
    build
    --linux="${KERNEL_PATH}"
    --initrd="${INITRD_PATH}"
    --output="${UKI_PATH}"
)

# Only add the --devicetree argument if the DTB path is valid
if [ -n "${DTB_PATH}" ]; then
    ukify_args+=(--devicetree="${DTB_PATH}")
    echo "INFO: Using device tree: ${DTB_PATH}"
fi

# Execute ukify
ukify "${ukify_args[@]}"

if [ ! -f "${UKI_PATH}" ]; then
    echo "CRITICAL: ukify failed to create the UKI file: ${UKI_PATH}" >&2
    # Clean up the temporary file left after a failure
    rm -f "${INITRD_PATH}"
    exit 1
fi
echo "SUCCESS: UKI has been successfully generated at: ${UKI_PATH}"

# --- Step 4: Clean up the temporary initramfs ---
echo "INFO: Cleaning up the temporary initramfs file..."
rm -f "${INITRD_PATH}"
echo "SUCCESS: Cleanup complete."

# ==============================================================================
echo "--- All operations have been completed successfully! ---"
# ==============================================================================