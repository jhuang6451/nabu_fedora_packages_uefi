%global debug_package %{nil}

Name:           nabu-fedora-configs-core
Version:        0.1
Release:        1%{?dist}
Summary:        Core configuration files for Fedora on Xiaomi Pad 5 (nabu)
License:        MIT
URL:            https://github.com/jhuang6451/nabu-fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       dracut
Requires:       systemd-ukify

%description
This package contains the essential configuration files for running Fedora on the Xiaomi Pad 5 (nabu)

%prep
%autosetup

%build
# Nothing to build as we are just packaging files.

%install
# The source tarball contains the etc directory with the correct structure.
# We copy it directly into the buildroot.
cp -a etc %{buildroot}/

%files
%config(noreplace) %{_sysconfdir}/dracut.conf.d/99-nabu-generic.conf
%config(noreplace) %{_sysconfdir}/fstab
%config(noreplace) %{_sysconfdir}/os-release
%config(noreplace) %{_sysconfdir}/systemd/ukify.conf
%config(noreplace) %{_sysconfdir}/udev/rules.d/99-force-rtc1.rules

%post
# Create the EFI directory as a mount point for the ESP.
# This is required for UKI generation and bootloader installation.
mkdir -p /boot/efi

%changelog
* Tue Sep 30 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1-1
- Initial release, switched to clean source tarballs