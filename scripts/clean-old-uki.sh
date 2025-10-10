#!/bin/bash

# ==============================================================================
# Script to Automatically Delete Old Fedora UKI Files (Time Sorted)
#
# This script sorts UKI files by
# modification time, keeps only the newest one, and deletes all older versions.
#
# How to use: Run this script with root privileges: sudo ./your_script_name.sh
# ==============================================================================

# Set the directory where UKI files are located
UKI_DIR="/boot/efi/EFI/fedora"

# --- Script Body ---

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
  echo "Error: This script must be run as root." >&2
  echo "Please try using 'sudo'." >&2
  exit 1
fi


# Check if the UKI directory exists
if [ ! -d "${UKI_DIR}" ]; then
  echo "Error: Directory ${UKI_DIR} does not exist." >&2
  exit 1
fi

# Change to the UKI directory
cd "${UKI_DIR}" || exit

# Find and count the number of UKI (.efi) files
# Using an array is safer for filenames with spaces
uki_files=(*.efi)
num_uki_files=${#uki_files[@]}

if [ "$num_uki_files" -le 1 ]; then
  echo "Found ${num_uki_files} UKI file(s) in ${UKI_DIR}. No cleanup needed."
else
  echo "Found ${num_uki_files} UKI files in ${UKI_DIR}. Cleaning up old files..."

  # List files sorted by modification time (newest first), and select all but the first one.
  files_to_delete=$(ls -t *.efi | tail -n +2)

  if [ -z "$files_to_delete" ]; then
    echo "No old UKI files found to delete."
  else
    echo "The following files will be deleted:"
    echo "$files_to_delete"
    # Delete the files
    echo "$files_to_delete" | xargs -r rm -v
    echo "Old UKI files have been successfully deleted."
  fi
fi

# Return to the previous directory
cd - >/dev/null

echo "Script execution finished."
exit 0
