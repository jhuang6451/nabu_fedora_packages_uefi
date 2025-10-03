%global debug_package %{nil}

Name:           nabu-fedora-configs-extra
Version:        0.11
Release:        1%{?dist}
Summary:        Extra configuration files for Fedora on Xiaomi Pad 5 (nabu)
License:        MIT
URL:            https://github.com/jhuang6451/nabu_fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       fcitx5
Requires:       qbootctl
Requires:       zram-generator

%description
This package contains extra configuration files for running Fedora on the Xiaomi Pad 5 (nabu), such as display, input method, and performance tweaks

%prep
# No prep needed, using local files

%build
# Nothing to build as we are just packaging files

%install
install -d -m 755 %{buildroot}%{_sysconfdir}/environment.d
install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/environment.d/99-im.conf
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/locale.conf
install -d -m 755 %{buildroot}%{_sysconfdir}/systemd
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/systemd/zram-generator.conf
install -d -m 755 %{buildroot}%{_presetdir}
install -m 644 %{SOURCE3} %{buildroot}%{_presetdir}/81-nabu-extra.preset
install -d -m 755 %{buildroot}%{_prefix}/lib/systemd/system
install -m 644 %{SOURCE4} %{buildroot}%{_prefix}/lib/systemd/system/qbootctl.service

%files
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/locale.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/environment.d/99-im.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/systemd/zram-generator.conf
%attr(644, root, root) %{_prefix}/lib/systemd/system/qbootctl.service
%attr(644, root, root) %{_presetdir}/81-nabu-extra.preset

%post
%systemd_post qbootctl.service

%preun
%systemd_preun qbootctl.service

%postun
%systemd_postun_with_restart qbootctl.service

%changelog
* Tue Sep 30 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.4-1
- Initial release