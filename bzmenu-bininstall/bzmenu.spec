%bcond_without check
%define version 0.2.1
%define crate bzmenu

Name:           bzmenu
Version:        %{version}
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

%generate_buildrequires
%if %{with check}
%cargo_generate_buildrequires
%endif

%description
bzmenu (BlueZ Menu) manages Bluetooth through your launcher of choice (like rofi, dmenu, or fuzzel).

%prep
%autosetup -n %{name}-%{version}
%cargo_prep

%build
# %cargo_build is provided by cargo-rpm-macros
%cargo_build
%cargo_license_summary
%cargo_license

%install
%cargo_install

%check
%if %{with check}
%cargo_test
%endif

%files
%{_bindir}/%{name}
%license LICENSE

%changelog
* Wed Oct 15 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.3.0-1
- Initial release for bzmenu v0.3.0