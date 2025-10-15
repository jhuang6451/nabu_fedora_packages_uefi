
Name:           bzmenu
Version:        0.3.0
Release:        1%{?dist}
Summary:        Launcher-driven Bluetooth manager for Linux

License:        GPL-3.0-or-later
URL:            https://github.com/e-tho/bzmenu
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  pkg-config
BuildRequires:  dbus-devel

# Runtime dependencies
Requires:       bluez
Requires:       dbus

%description
bzmenu (BlueZ Menu) manages Bluetooth through your launcher of choice (like rofi, dmenu, or fuzzel).

%prep
%autosetup -n %{name}-%{version}

%build
# %cargo_build is provided by cargo-rpm-macros
%cargo_build --release

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE

%changelog
* Wed Oct 15 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.3.0-1
- Initial release for bzmenu v0.3.0