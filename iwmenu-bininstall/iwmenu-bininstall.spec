%define binname iwmenu-%{_arch}-linux-gnu

Name:           iwmenu
Version:        0.3.0
Release:        1%{?dist}
Summary:        Launcher-driven Bluetooth manager for Linux

License:        GPL-3.0-or-later
URL:            https://github.com/e-tho/iwmenu
Source0:        %{url}/releases/download/v%{version}/%{binname}

# Runtime dependencies
Requires:       iwd
Requires:       dbus

%description
iwmenu (iNet Wireless Menu) manages Wi-Fi through your launcher of choice.
this spec file simply downloads a pre-built executable from github release and puts it into _bindir

%prep

%build
# Nothing to build

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Wed Oct 15 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.3.0-1
- Initial release for iwmenu v0.3.0