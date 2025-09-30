%global debug_package %{nil}

Name:           nabu-fedora-configs-extra
Version:        0.1
Release:        1%{?dist}
Summary:        Extra configuration files for Fedora on Xiaomi Pad 5 (nabu)

License:        MIT
URL:            https://github.com/jhuang6451/nabu-fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
This package contains extra configuration files for running Fedora on the Xiaomi Pad 5 (nabu), such as display, input method, and performance tweaks

%prep
%autosetup

%build
# Nothing to build as we are just packaging files

%install
# The source tarball contains the etc and var directories with the correct structure.
# We copy them directly into the buildroot.
cp -a etc %{buildroot}/
cp -a var %{buildroot}/

%files
%config(noreplace) %{_sysconfdir}/environment.d/99-im.conf
%config(noreplace) %{_sysconfdir}/locale.conf
%config(noreplace) %{_sysconfdir}/systemd/system/qbootctl.service
%config(noreplace) %{_sysconfdir}/systemd/zram-generator.conf
%config(noreplace) %{_sharedstatedir}/gdm/.config/monitors.xml

%changelog
* Tue Sep 30 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1-1
- Initial release
