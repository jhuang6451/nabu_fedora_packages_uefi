%define theme_name sddm-astronaut-theme

Name:           %{theme_name}
Version:        1.0
Release:        1%{?dist}
Summary:        A beautiful SDDM theme

License:        GPL-3.0
URL:            https://github.com/Keyitdev/sddm-astronaut-theme
Source0:        sddm.conf
Source1:        virtualkbd.conf

BuildRequires:  git-core
BuildArch:      noarch
Requires:       sddm qt6-qtsvg qt6-qtvirtualkeyboard qt6-qtmultimedia

%description
%{summary}

%prep
git clone -b master --depth 1 %{url} %{theme_name}
cd %{theme_name}

%build
# No build steps needed

%install
install -d %{buildroot}%{_datadir}/sddm/themes/%{theme_name}
cp -a * %{buildroot}%{_datadir}/sddm/themes/%{theme_name}/
cp -r %{buildroot}%{_datadir}/sddm/themes/%{theme_name}/Fonts/* %{_datadir}/fonts/sddm-astronaut-theme-fonts/

install -d %{buildroot}%{_sysconfdir}/sddm.conf.d
install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/sddm.conf
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sddm.conf.d/virtualkbd.conf

# Optional: change default theme
sed -i 's#^ConfigFile=.*#ConfigFile=Themes/pixel_sakura.conf#' %{buildroot}%{_datadir}/sddm/themes/%{theme_name}/metadata.desktop

%files
%defattr(644, root, root, 755)
%{_datadir}/sddm/themes/%{theme_name}
%license %{theme_name}/LICENSE
%{_sysconfdir}/sddm.conf
%{_sysconfdir}/sddm.conf.d/virtualkbd.conf


%changelog
* Tue Oct 14 2025 jhuang6451 <xplayerhtz123@outlook.com> - 1.0-1
- Initial release