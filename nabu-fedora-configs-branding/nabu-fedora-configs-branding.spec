%global debug_package %{nil}

Name:           nabu-fedora-configs-branding
Version:        0.6
Release:        1%{?dist}
Summary:        Custom branding info for Nabu for Fedora.
License:        MIT
URL:            https://github.com/jhuang6451/nabu-fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       fedora-release-common
Requires:       fedora-repos

%description
This package provides the /etc/os-release file to brand a Fedora system
for Nabu. It relies on the official fedora-release-* packages for core
functionality like repositories and GPG keys

%prep
%autosetup

%build
# Nothing to build as we are just packaging files.

%install
# Install our custom os-release to a non-conflicting location
install -D -m 644 etc/os-release %{buildroot}%{_datadir}/nabu-branding/os-release

%files
# Own the non-conflicting file
%attr(644, root, root) %{_datadir}/nabu-branding/os-release

%post
# Overwrite /etc/os-release with our custom version after installation
# This avoids a file conflict at the RPM database level.
cp %{_datadir}/nabu-branding/os-release /etc/os-release

%preun
# If the package is being uninstalled, restore the original os-release symlink
if [ $1 -eq 0 ] ; then
    rm -f /etc/os-release
    ln -s /usr/lib/os-release /etc/os-release
fi

%changelog
* Tue Sep 30 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.4-1
- Initial release
