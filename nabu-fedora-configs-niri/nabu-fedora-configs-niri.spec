%global debug_package %{nil}

Name:           nabu-fedora-configs-niri
Version:        0.1.5
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
cp -a etc %{buildroot}/
cp -a usr %{buildroot}/
cp -a var %{buildroot}/

%files
# General Configs
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/locale.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/environment.d/99-im.conf
%attr(644, root, root) %{_prefix}/lib/systemd/system/91-fcitx5-autostart.service
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
%attr(644, root, root) %{_sysconfdir}/skel/.config/waypaper/config.ini
%attr(644, root, root) %{_sysconfdir}/skel/.config/waypaper/style.css
# Scripts
%attr(755, root, root) %{_bindir}/wvkbd-toggle.sh
%attr(755, root, root) %{_bindir}/fuzzel-pw-menu.sh
%attr(755, root, root) %{_bindir}/niri-rotate-display.sh
# Wallpapers Dir
%defattr(644, root, root, 755)
%{_sysconfdir}/skel/Pictures/Wallpapers

%post
## bash
if [ -f /etc/skel/.bashrc ]; then
    echo "Appending custom configurations to /etc/skel/.bashrc"
    cat << 'EOF' >> /etc/skel/.bashrc

# ---- Added by nabu-fedora-configs-niri ----
alias code='code --ozone-platform=wayland'
fastfetch
# ---- End of nabu-fedora-configs-niri section ----
EOF
fi

%changelog
* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.5-1
- Remove deploy_user_configs.sh.

* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.4-1
- Fix fcitx5-autostart systemd preset name.

* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.3-1
- Postinstall script and some config updates.

* Sun Oct 12 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.2-1
- Initial release.