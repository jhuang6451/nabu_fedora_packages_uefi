Name:           xiaomi-nabu-firmware
Version:        %{version}
Release:        1%{?dist}
Summary:        Firmware for running linux on Xiaomi Pad 5 (Nabu)
License:        MIT
URL:            https://gitlab.postmarketos.org/panpanpanpan/nabu-firmware
Source0:        %{url}/-/archive/%{version}/nabu-firmware-%{version}.tar.gz
BuildArch:     aarch64
Requires:       qcom-firmware

%global _firmwaredir %{_prefix}/lib/firmware

%description
Firmware for running linux on Xiaomi Pad 5 (Nabu)

%prep
%autosetup -n nabu-firmware-%{version}

%install
mkdir -p %{buildroot}%{_firmwaredir}/qcom \
         %{buildroot}%{_firmwaredir}/qcom/sm8150/xiaomi/nabu \
         %{buildroot}%{_firmwaredir}/cirrus \
         %{buildroot}%{_firmwaredir}/novatek
cp -a a630_sqe.fw a640_gmu.bin %{buildroot}%{_firmwaredir}/qcom
cp -a a640_zap.mbn adsp.mbn cdsp.mbn modem* venus.mbn wlanmdsp.mbn %{buildroot}%{_firmwaredir}/qcom/sm8150/xiaomi/nabu
cp -a cs35l41* %{buildroot}%{_firmwaredir}/cirrus
cp -a novatek_nt36523_fw.bin %{buildroot}%{_firmwaredir}/novatek
find %{buildroot}%{_firmwaredir} -type f -exec chmod 0644 {} \;

%files
%{_firmwaredir}/qcom
%{_firmwaredir}/cirrus
%{_firmwaredir}/novatek
