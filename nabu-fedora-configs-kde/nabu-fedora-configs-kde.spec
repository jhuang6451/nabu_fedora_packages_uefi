%global debug_package %{nil}

Name:           nabu-fedora-configs-kde
Version:        0.1
Release:        1%{?dist}
Summary:        Configurations for Fedora for Nabu kde builds
License:        MIT
URL:            https://github.com/jhuang6451/nabu_fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package contains configurations specific for Fedora for Nabu builds with kde DE

%prep
%autosetup

%build
# Nothing to build

%install
cp -a var %{buildroot}/

%files
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/locale.conf
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/environment.d/99-im.conf

%changelog
* Wed Oct 04 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1-1
- Initial release