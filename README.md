# Fedora Packages for Xiaomi Pad 5 (nabu)

This repository contains the source files and RPM `.spec` files for various packages required to run Fedora on the Xiaomi Pad 5 (nabu). It is structured as a "monorepo", managing multiple independent packages within a single Git repository.

These packages are intended to be built in a [COPR](https://copr.fedorainfracloud.org/) repository.

## Managed Packages

The following packages are managed in this repository:

- `kernel-sm8150`: The Linux kernel compiled for the SM8150 platform.
- `nabu-fedora-configs-core`: Core system configuration files.
- `nabu-fedora-configs-efi`: EFI bootloader configurations.
- `nabu-fedora-configs-extra`: Additional configurations for display, input methods, and performance tweaks.
- `xiaomi-nabu-audio`: Audio configuration files (PulseAudio and ALSA).
- `xiaomi-nabu-firmware`: Firmware files required for device hardware.
- `nabu_fedora_configs_branding`: Custom branding info for Nabu for Fedora.

## Automated Tarball Release Process

This repository uses a fully automated release process powered by GitHub Actions. This process simplifies releases and ensures that COPR has access to clean, versioned source code for each package.

The following packages are now managed by this process:
- `nabu-fedora-configs-core`
- `nabu-fedora-configs-efi`
- `nabu-fedora-configs-extra`
- `nabu_fedora_configs_branding`

### How It Works

1.  **Trigger**: The workflow is triggered whenever a new Git tag starting with `v` (e.g., `v0.1`, `v1.2.3`) is pushed to the repository.

2.  **Tarballs List**: The workflow reads the list of package directories from the `release-tarballs.txt` file in the repository root. This file acts as the single source of truth for which packages should be released.

3.  **Source Packaging**: For each package listed in `release-tarballs.txt`, the workflow runs `git archive` to create a clean source tarball (`.tar.gz`). This tarball contains only the files from that specific package's subdirectory, which is ideal for RPM building.

4.  **GitHub Release**: The workflow then creates a new GitHub Release corresponding to the Git tag.

5.  **Upload Assets**: Finally, all the generated source tarballs are uploaded as assets to the newly created GitHub Release.

The `.spec` files within each package are configured to use these uploaded tarballs as their `Source0`, allowing COPR to build them automatically.

### How to Create a New Release

To publish a new version of all packages, simply create and push a new tag:

```bash
# Example for releasing version 0.1
git tag -a v0.1 -m "Release version 0.1"
git push origin v0.1
```

The GitHub Actions workflow will handle the rest.

## How to Add a New Package

Adding a new package to the automated release process is straightforward:

1.  **Create the Directory**: Add a new directory for your package in the repository root (e.g., `my-new-package/`).

2.  **Add Package Files**: Place all necessary source files and the `.spec` file inside this new directory. Ensure the `.spec` file's `Source0` points to the future GitHub Release asset, like so:
    ```spec
    Source0: https://github.com/jhuang6451/nabu_fedora_packages/releases/download/v%{version}/%{name}-%{version}.tar.gz
    ```

3.  **Update Package List**: Add the name of the new directory (`my-new-package`) to a new line in the `release-tarballs.txt` file.

4.  **Commit and Push**: Commit the new files and the changes to `release-tarballs.txt`.

The next time a release is created, your new package will be automatically included in the process.