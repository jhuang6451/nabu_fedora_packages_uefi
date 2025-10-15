%define binname bzmenu-%{_arch}-linux-gnu

Name:           bzmenu
Version:        0.3.0
Release:        1%{?dist}
Summary:        Launcher-driven Bluetooth manager for Linux

License:        GPL-3.0-or-later
URL:            https://github.com/e-tho/bzmenu
Source0:        %{url}/releases/download/v%{version}/%{binname}
Source1:        %{url}/raw/v%{version}/LICENSE

# Runtime dependencies
Requires:       bluez
Requires:       dbus

%description
bzmenu (BlueZ Menu) manages Bluetooth through your launcher of choice (like rofi, dmenu, or fuzzel).
this spec file simply downloads a pre-built executable from github release and puts it into _bindir

%prep

%build
# Nothing to build

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}
install -d -m 755 %{buildroot}%{_docdir}/%{name}
install -p -m 644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/LICENSE

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%license %{_docdir}/%{name}/LICENSE

%changelog
* Wed Oct 15 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.3.0-1
- Initial release for bzmenu v0.3.0