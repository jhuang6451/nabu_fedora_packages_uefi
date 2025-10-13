%global debug_package %{nil}

Name:           maple-mono-nf-cn-normal-unhinted
Version:        7.7
Release:        1%{?dist}
Summary:        Maple Mono font full CN, unhinted version with "--normal" preset
BuildArch:      noarch
License:        OFL-1.1
URL:            https://github.com/subframe7536/maple-font
Source0:        %{url}/releases/download/v%{version}/MapleMonoNormal-NF-CN-unhinted.zip

Requires(post):   fontconfig
Requires(postun): fontconfig

%description
Maple Mono font full CN, unhinted version with "--normal" preset.

%prep
%autosetup -c

%build
# 无需构建

%install
mkdir -p %{buildroot}/usr/share/fonts/%{name}
install -m 644 -p *.ttf %{buildroot}/usr/share/fonts/

%post
fc-cache -f -v %{_fontdir}/%{name} || :

%postun
if [ $1 -eq 0 ] ; then
    fc-cache -f -v %{_fontdir}/%{name} || :
fi

%files
/usr/share/fonts/%{name}
%license LICENSE.txt

%changelog
* Sat Oct 04 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.0-1
- Initial release.