%global debug_package %{nil}

Name:           nabu-fedora-configs-niri
Version:        0.1.0
Release:        1%{?dist}
Summary:        Configurations for Fedora for Nabu with niri Composer
License:        MIT
URL:            https://github.com/jhuang6451/nabu_fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

%description
This package contains configurations specific for Fedora for Nabu with niri composer

%prep
%autosetup

%build
# Nothing to build

%install
cp -a etc %{buildroot}/

%files
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/niri/config.kdl

%post


%changelog
* SUn Oct 12 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.0-1
- Initial release.