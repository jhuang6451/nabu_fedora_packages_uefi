%global debug_package %{nil}

Name:           nabu-fedora-configs-extra
Version:        1.1
Release:        1%{?dist}
Summary:        Extra configuration files for Fedora on Xiaomi Pad 5 (nabu)
License:        MIT
URL:            https://github.com/jhuang6451/nabu_fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       fcitx5
Requires:       zram-generator
Requires:       qbootctl

%description
This package contains extra configuration files for running Fedora on the Xiaomi Pad 5 (nabu), such as display, input method, and performance tweaks

%prep
%autosetup

%build
# Nothing to build

%install
cp -a etc %{buildroot}/
cp -a usr %{buildroot}/

%files
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/locale.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/environment.d/99-im.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/systemd/zram-generator.conf
%attr(644, root, root) %{_presetdir}/81-qbootctl.preset

%post
%systemd_post qbootctl.service

%preun
%systemd_preun qbootctl.service

%postun
%systemd_postun_with_restart qbootctl.service

%changelog
* Tue Sep 30 2025 jhuang6451 <xplayerhtz123@outlook.com> - 1.1-1
- Initial release