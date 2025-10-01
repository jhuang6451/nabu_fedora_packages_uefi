[简体中文](docs/README.zh.md)

# Nabu Fedora Packages

This repository contains RPM spec files and configurations for running Fedora on the Xiaomi Pad 5 (nabu).

## Packages

This repository manages the following packages:

- `kernel-sm8150`
- `xiaomi-nabu-firmware`
- `nabu-fedora-configs-core`
- `nabu-fedora-configs-extra`
- `nabu-fedora-configs-gnome`
- `nabu-fedora-dualboot-efi`

## Versioning and Release Process

This repository uses a hybrid model for versioning and releasing packages, handled automatically by GitHub Actions. Packages are divided into two categories based on their versioning strategy.

### Package Categories

#### 1. Automatically Versioned Packages

These are packages for which this repository is the source of truth. Their versions are determined automatically based on the commit history.

- `nabu-fedora-configs-core`
- `nabu-fedora-configs-extra`
- `nabu-fedora-configs-gnome`
- `nabu-fedora-dualboot-efi`

**Release Process:**

1.  **Make changes** to the files within one of the package directories.
2.  **Commit the changes** using the [Conventional Commits](https://www.conventionalcommits.org/) specification. The commit message `type` determines the version bump:
    - `feat:` results in a MINOR version increase (e.g., `1.1.0` -> `1.2.0`).
    - `fix:` results in a PATCH version increase (e.g., `1.1.0` -> `1.1.1`).
    - A `BREAKING CHANGE:` footer results in a MAJOR version increase (e.g., `1.1.0` -> `2.0.0`).
    - Other types such as `docs`, `style`, `refactor`, and `test` will not trigger version upgrades.
3.  **Push the commit(s)** to the `main` branch.

That's it! A GitHub Action (`version-and-tag.yml`) will detect the push, calculate the new version, and push a new package tag (e.g., `nabu-fedora-configs-core-v1.2.0`). This new tag will, in turn, trigger the `create-release-tarballs.yml` workflow to create a GitHub Release and trigger a COPR build.

#### 2. Manually Versioned (Upstream-Tracking) Packages

These packages track an external upstream source. Their `Version` should match the upstream version, and local packaging changes are tracked by the `Release` number.

- `kernel-sm8150`
- `xiaomi-nabu-firmware`

**Release Process:**

1.  **Manually edit the `.spec` file** inside the package directory.
    - To follow a new upstream release, update the `Version` field.
    - For local packaging fixes, increment the `Release` field.
2.  **Update the `%changelog`** in the `.spec` file with a description of the changes.
3.  **Commit** the changes to the `.spec` file.
4.  **Manually create and push a Git tag** that matches the package name and the `Version` from the spec file.
    ```bash
    # Example for a new kernel version
    git tag kernel-sm8150-v6.17.0
    git push origin kernel-sm8150-v6.17.0
    ```
5.  The push of this new tag will trigger the `create-release-tarballs.yml` workflow to create a GitHub Release and trigger a COPR build.

### Controlling Files

- `release-tarballs.txt`: A list of all package directories managed by this repository.
- `.no-auto-version`: A list of packages to be excluded from the automatic versioning process (i.e., the Manually Versioned packages).
