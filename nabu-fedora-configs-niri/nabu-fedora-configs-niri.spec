%global debug_package %{nil}

Name:           nabu-fedora-configs-niri
Version:        0.1.7
Release:        1%{?dist}
Summary:        Configurations for Fedora for Nabu with niri Composer
License:        MIT
URL:            https://github.com/jhuang6451/nabu_fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

Requires:       pipewire-pulse
Requires:       wireplumber

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
%attr(644, root, root) %{_presetdir}/91-fcitx5-autostart.preset
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

# ----------------------------------------------------------------------
# pipewire user services
#
# This script handles the systemd user services for PipeWire.
# We use 'systemctl --global' to enable/disable services for all
# users on the system.
#
# The changes will take effect for each user upon their next login.
# ----------------------------------------------------------------------

# 1. Mask the legacy pulseaudio services to prevent conflicts.
#    This ensures that pipewire-pulse can take over without issues.
#    The '|| :' part ensures the command doesn't fail if the service
#    doesn't exist on the system.
echo "Masking conflicting PulseAudio user services for all users..."
systemctl --global mask pulseaudio.service pulseaudio.socket || :

# 2. Enable the core PipeWire services for all users.
echo "Enabling PipeWire user services for all users..."
systemctl --global enable pipewire.service pipewire-pulse.service wireplumber.service || :


%postun
# ----------------------------------------------------------------------
# Post-uninstall script
#
# This runs if the package is being uninstalled (not upgraded).
# The '$1' argument is 0 on final removal, and >= 1 on upgrade.
# ----------------------------------------------------------------------
if [ $1 -eq 0 ] ; then
    # This is a final uninstall, not an upgrade.
    echo "Disabling PipeWire user services for all users..."
    systemctl --global disable pipewire.service pipepipe-pulse.service wireplumber.service || :

    echo "Unmasking PulseAudio user services for all users..."
    systemctl --global unmask pulseaudio.service pulseaudio.socket || :
fi

%changelog
* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.7-1
- Add postinstall script for pipwire user services.

* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.6-1
- Remove deploy_user_configs.sh.

* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.4-1
- Fix fcitx5-autostart systemd preset name.

* Thu Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.3-1
- Postinstall script and some config updates.

* Sun Oct 12 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.2-1
- Initial release.