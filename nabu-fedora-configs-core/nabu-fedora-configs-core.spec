%global debug_package %{nil}

Name:           nabu-fedora-configs-core
Version:        0.1
Release:        1%{?dist}
Summary:        Core, audio and branding configuration files for Fedora on Xiaomi Pad 5 (nabu)
License:        MIT
URL:            https://github.com/jhuang6451/nabu-fedora
Source0:        etc/dracut.conf.d/99-nabu-generic.conf
Source1:        etc/fstab
Source2:        etc/systemd/ukify.conf
Source3:        etc/pulse/daemon.conf.d/89-xiaomi_nabu.conf
Source4:        etc/pulse/default.pa.d/nabu.pa
Source5:        etc/os-release
Source6:        usr/lib/systemd/system-preset/80-nabu-core.preset
Source7:        usr/lib/systemd/system/ath10k-shutdown.service
Source8:        usr/lib/udev/rules.d/99-force-rtc1.rules
Source9:        usr/share/alsa/ucm2/conf.d/sm8150/sm8150.conf
Source10:       usr/share/alsa/ucm2/Xiaomi/nabu/HiFi.conf
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       dracut
Requires:       systemd-ukify
Requires:       rmtfs
Requires:       tqftpserv
Requires:       alsa-ucm
Requires:       fedora-release-common

%description
This package contains the essential core, audio, and branding configuration files for running Fedora on the Xiaomi Pad 5 (nabu)

%prep
# No prep needed, using local files

%build
# Nothing to build as we are just packaging files.

%install
install -d -m 755 %{buildroot}%{_sysconfdir}/dracut.conf.d
install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/dracut.conf.d/99-nabu-generic.conf
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/fstab
install -d -m 755 %{buildroot}%{_sysconfdir}/systemd
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/systemd/ukify.conf
install -d -m 755 %{buildroot}%{_sysconfdir}/pulse/daemon.conf.d
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pulse/daemon.conf.d/89-xiaomi_nabu.conf
install -d -m 755 %{buildroot}%{_sysconfdir}/pulse/default.pa.d
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pulse/default.pa.d/nabu.pa
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/os-release
install -d -m 755 %{buildroot}%{_presetdir}
install -m 644 %{SOURCE6} %{buildroot}%{_presetdir}/80-nabu-core.preset
install -d -m 755 %{buildroot}%{_prefix}/lib/systemd/system
install -m 644 %{SOURCE7} %{buildroot}%{_prefix}/lib/systemd/system/ath10k-shutdown.service
install -d -m 755 %{buildroot}%{_prefix}/lib/udev/rules.d
install -m 644 %{SOURCE8} %{buildroot}%{_prefix}/lib/udev/rules.d/99-force-rtc1.rules
install -d -m 755 %{buildroot}%{_datadir}/alsa/ucm2/conf.d/sm8150
install -m 644 %{SOURCE9} %{buildroot}%{_datadir}/alsa/ucm2/conf.d/sm8150/sm8150.conf
install -d -m 755 %{buildroot}%{_datadir}/alsa/ucm2/Xiaomi/nabu
install -m 644 %{SOURCE10} %{buildroot}%{_datadir}/alsa/ucm2/Xiaomi/nabu/HiFi.conf

%files
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/os-release
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/dracut.conf.d/99-nabu-generic.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/fstab
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/systemd/ukify.conf
%attr(644, root, root) %{_prefix}/lib/systemd/system/ath10k-shutdown.service
%attr(644, root, root) %{_prefix}/lib/udev/rules.d/99-force-rtc1.rules
%attr(644, root, root) %{_presetdir}/80-nabu-core.preset
%attr(644, root, root) %{_datadir}/alsa/ucm2/conf.d/sm8150/sm8150.conf
%attr(644, root, root) %{_datadir}/alsa/ucm2/Xiaomi/nabu/HiFi.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/pulse/daemon.conf.d/89-xiaomi_nabu.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/pulse/default.pa.d/nabu.pa

%post
# Create the EFI directory as a mount point for the ESP.
# This is required for UKI generation and bootloader installation.
mkdir -p /boot/efi
%systemd_post ath10k-shutdown.service

%preun
%systemd_preun ath10k-shutdown.service rmtfs.service tqftpserv.service

%postun
%systemd_postun_with_restart ath10k-shutdown.service rmtfs.service tqftpserv.service

%changelog
* Tue Sep 30 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.2-1
- Added services, move os-release to a seperate package.

* Tue Sep 30 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1-1
- Initial release
