%global debug_package %{nil}

Name:           nabu-fedora-configs-niri
Version:        0.1.0
Release:        1%{?dist}
Summary:        Configurations for Fedora for Nabu with niri Composer
License:        MIT
URL:            https://github.com/jhuang6451/nabu_fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

%description
This package contains configurations specific for Fedora for Nabu with niri composer

%prep
%autosetup

%build
# Nothing to build

%install
cp -a var %{buildroot}/
cp -a etc %{buildroot}/
cp -a usr %{buildroot}/

%files
%attr(644, gdm, gdm) %config(noreplace) %{_sharedstatedir}/gdm/.config/monitors.xml.default
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/locale.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/environment.d/99-im.conf
%attr(644, root, root) %{_prefix}/lib/systemd/system/fcitx5-autostart.service
%attr(644, root, root) %{_presetdir}/fcitx5-autostart.preset

%post
if [ ! -f %{_sharedstatedir}/gdm/.config/monitors.xml ]; then
    install -D -p -m 644 -o gdm -g gdm %{_sharedstatedir}/gdm/.config/monitors.xml.default %{_sharedstatedir}/gdm/.config/monitors.xml
fi

%systemd_post fcitx5-autostart.service

%preun
%systemd_preun fcitx5-autostart.service

%postun
%systemd_postun_with_restart fcitx5-autostart.service

%changelog
* SUn Oct 12 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.0-1
- Initial release.