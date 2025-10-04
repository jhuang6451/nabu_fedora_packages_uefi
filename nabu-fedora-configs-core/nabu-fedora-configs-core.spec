%global debug_package %{nil}

Name:           nabu-fedora-configs-core
Version:        0.3
Release:        2%{?dist}
Summary:        Core, audio and branding configuration files for Fedora on Xiaomi Pad 5 (nabu)
License:        MIT
URL:            https://github.com/jhuang6451/nabu_fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       dracut
Requires:       systemd-ukify
Requires:       rmtfs
Requires:       tqftpserv
Requires:       alsa-ucm
Requires:       qbootctl

%description
This package contains the essential core, audio, and branding configuration files for running Fedora on the Xiaomi Pad 5 (nabu)

%prep
%autosetup

%build
# Nothing to build

%install
cp -a etc %{buildroot}/
cp -a usr %{buildroot}/

%files
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/dracut.conf.d/99-nabu-generic.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/fstab
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/systemd/ukify.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/systemd/zram-generator.conf
%attr(644, root, root) %{_prefix}/lib/systemd/system/ath10k-shutdown.service
%attr(644, root, root) %{_prefix}/lib/udev/rules.d/99-force-rtc1.rules
%attr(644, root, root) %{_presetdir}/80-nabu-core.preset
%attr(644, root, root) %{_presetdir}/81-qbootctl.preset
%attr(644, root, root) %{_datadir}/alsa/ucm2/conf.d/sm8150/sm8150.conf
%attr(644, root, root) %{_datadir}/alsa/ucm2/Xiaomi/nabu/HiFi.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/pulse/daemon.conf.d/89-xiaomi_nabu.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/pulse/default.pa.d/nabu.pa

%post
# Create the EFI directory as a mount point for the ESP.
# This is required for UKI generation and bootloader installation.
mkdir -p /boot/efi

%systemd_post ath10k-shutdown.service qbootctl.service

%preun
%systemd_preun ath10k-shutdown.service rmtfs.service tqftpserv.service qbootctl.service

%postun
%systemd_postun_with_restart ath10k-shutdown.service rmtfs.service tqftpserv.service qbootctl.service

%changelog
* Tue Oct 4 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.3-2
- Moved some configs from extra to core.

* Tue Oct 4 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.2-2
- Removed "os-release".

* Tue Sep 30 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.2-1
- Added services, move os-release to a seperate package.

* Tue Sep 30 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1-1
- Initial release
