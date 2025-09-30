%global debug_package %{nil}

Name:           nabu-fedora-configs-branding
Version:        0.4
Release:        1%{?dist}
Summary:        Custom branding info for Nabu for Fedora.
License:        MIT
URL:            https://github.com/jhuang6451/nabu-fedora
Source0:        https://github.com/jhuang6451/nabu_fedora_packages/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      aarch64
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
# The source tarball contains the etc directory with the correct structure.
# We copy it directly into the buildroot.
cp -a etc %{buildroot}/

%files
%config(noreplace) %{_sysconfdir}/os-release

%post
# 在安装后，移除那个悬空的软链接，虽然 dnf 通常会处理
rm -f /usr/lib/os-release
ln -s ../../etc/os-release /usr/lib/os-release
echo "Linked /usr/lib/os-release to custom /etc/os-release."


%changelog
* Tue Sep 30 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.4-1
- Initial release