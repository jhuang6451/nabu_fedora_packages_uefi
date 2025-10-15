%global debug_package %{nil}

Name:           nabu-fedora-configs-niri
Version:        0.1.2
Release:        1%{?dist}
Summary:        Configurations for Fedora for Nabu with niri Composer
License:        MIT
URL:            https://github.com/jhuang6451/nabu_fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/test-%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

%description
This package contains configurations specific for Fedora for Nabu with niri composer

%prep
%autosetup

%build
# Nothing to build

%install
cp -a etc %{buildroot}/
cp -a usr %{buildroot}/
cp -a var %{buildroot}/

%files
# General Configs
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/locale.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/environment.d/99-im.conf
%attr(644, root, root) %{_prefix}/lib/systemd/system/fcitx5-autostart.service
%attr(644, root, root) %{_presetdir}/fcitx5-autostart.preset
# sddm Configs
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/sddm.conf.d/general.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/sddm.conf.d/wayland.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/sddm.conf.d/theme.conf
# sddm Session Config Presets
%attr(644, root, root) %config(noreplace) %{_sharedstatedir}/sddm/.config/niri/config.kdl
# User Config Presets
## Desktop Presets
%attr(644, root, root) %{_sysconfdir}/skel/.local/share/applications/code-url-handler.desktop
%attr(644, root, root) %{_sysconfdir}/skel/.local/share/applications/code.desktop
## fuzzel
%attr(644, root, root) %{_sysconfdir}/skel/.config/fuzzel/fuzzel.ini
## kitty
%attr(644, root, root) %{_sysconfdir}/skel/.config/kitty/kitty.conf
%attr(644, root, root) %{_sysconfdir}/skel/.config/kitty/current-theme.conf
## niri
%attr(644, root, root) %{_sysconfdir}/skel/.config/niri/config.kdl
## swaylock
%attr(644, root, root) %{_sysconfdir}/skel/.config/swaylock/config
## waybar
%attr(644, root, root) %{_sysconfdir}/skel/.config/waybar/config.jsonc
%attr(644, root, root) %{_sysconfdir}/skel/.config/waybar/style.css
## waypaper
%attr(644, root, root) %{_sysconfdir}/skel/.config/waypaper/config.jsonc
%attr(644, root, root) %{_sysconfdir}/skel/.config/waypaper/style.css
# Scripts
%attr(755, root, root) %{_bindir}/wvkbd-toggle.sh
%attr(755, root, root) %{_bindir}/fuzzel-pw-menu.sh
%attr(755, root, root) %{_bindir}/niri-rotate-display.sh
%attr(755, root, root) %{_bindir}/deploy-user-configs.sh

%post
echo "Running post-install script to deploy user configs..."
/usr/bin/deploy_configs.sh

%changelog
* Sun Oct 12 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.2-1
- Initial release.