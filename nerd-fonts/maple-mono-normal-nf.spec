%global debug_package %{nil}

Name:           maple-mono-normal-nf
Version:        7.7
Release:        1%{?dist}
Summary:        Maple Mono nerd font normal version (unhinted)
BuildArch:      noarch
License:        OFL-1.1
URL:            https://github.com/subframe7536/maple-font
Source0:        %{url}/releases/download/v%{version}/MapleMonoNormal-NF-unhinted.zip

Conflicts:      maple-mono-normal-nf-cn

Requires(post):   fontconfig
Requires(postun): fontconfig

%description
%{summary}

%prep
%autosetup -c

%build
# Nothing to build.

%install
mkdir -p %{buildroot}/usr/share/fonts/%{name}
install -m 644 -p *.ttf %{buildroot}/usr/share/fonts/%{name}

%post
fc-cache -f -v %{_fontdir}/%{name} || :

%postun
if [ $1 -eq 0 ] ; then
    fc-cache -f -v %{_fontdir}/%{name} || :
fi

%files
%defattr(644, root, root, 755)
/usr/share/fonts/%{name}
%license LICENSE.txt

%changelog
* Sat Oct 04 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.1.0-1
- Initial release.