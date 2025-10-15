%define bz-binname bzmenu-%{_arch}-linux-gnu
%define iw-binname iwmenu-%{_arch}-linux-gnu
%define pw-binname pwmenu-%{_arch}-linux-gnu

Name:           e-thos-menu
Version:        0.3.0
Release:        1%{?dist}
Summary:        Launcher-driven managers for Linux by e-tho

License:        GPL-3.0-or-later
URL:            https://github.com/e-tho/
Source0:        %{url}/bzmenu/releases/download/v%{version}/%{bz-binname}
Source1:        %{url}/iwmenu/releases/download/v%{version}/%{iw-binname}
Source2:        %{url}/pwmenu/releases/download/v%{version}/%{pw-binname}

# Runtime dependencies
Requires:       bluez
Requires:       iwd
Requires:       pipewire
Requires:       dbus

%description
bzmenu (BlueZ Menu) manages Bluetooth through your launcher of choice (like rofi, dmenu, or fuzzel).
iwmenu (iNet Wireless Menu) manages Wi-Fi through your launcher of choice.
pwmenu (PipeWire Menu) manages audio through your launcher of choice.
this spec file simply downloads the pre-built executables from github release and puts them into _bindir

%prep

%build
# Nothing to build

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}/bzmenu
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/iwmenu
install -p -m 755 %{SOURCE2} %{buildroot}%{_bindir}/pwmenu

%files
%defattr(-,root,root,-)
%{_bindir}/bzmenu
%{_bindir}/iwmenu
%{_bindir}/pwmenu

%changelog
* Wed Oct 15 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.3.0-1
- Initial release for v0.3.0