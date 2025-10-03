%global debug_package %{nil}

Name:           nabu-fedora-configs-gnome
Version:        0.1
Release:        1%{?dist}
Summary:        Configurations for Fedora for Nabu Gnome builds
License:        MIT
URL:            https://github.com/jhuang6451/nabu_fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package contains configurations specific for Fedora for Nabu builds with Gnome DE

%prep
%autosetup

%build
# Nothing to build

%install
cp -a var %{buildroot}/

%files
%attr(644, gdm, gdm) %config(noreplace) %{_sharedstatedir}/gdm/.config/monitors.xml

%changelog
* Wed Oct 01 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1-1
- Initial release