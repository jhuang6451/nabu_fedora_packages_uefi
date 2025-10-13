%global debug_package %{nil}

Name:           maple-mono-nf-cn-normal-unhinted
Version:        0.1.0
Release:        1%{?dist}
Summary:        Maple Mono font full CN, unhinted version with "--normal" preset
BuildArch:      noarch
License:        OFL-1.1
URL:            https://github.com/jhuang6451/nabu_fedora_packages
Source0:        MapleMonoNormal-NF-CN-unhinted.zip
Requires(post):   fontconfig
Requires(postun): fontconfig

%description
Maple Mono font full CN, unhinted version with "--normal" preset

%prep
%autosetup -c

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_fontdir}/%{name}
install -m 644 -p *.ttf %{buildroot}%{_fontdir}/%{name}/

%files
%{_fontdir}/%{name}

%post
fc-cache -f -v %{_fontdir}/%{name} || :

%postun
if [ $1 -eq 0 ] ; then
    fc-cache -f -v %{_fontdir}/%{name} || :
fi

%license LICENSE.txt

%changelog
* Sat Oct 04 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.0-1
- Initial release.