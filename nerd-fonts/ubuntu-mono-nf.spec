%global debug_package %{nil}

Name:           ubuntu-mono-nf
Version:        3.4.0
Release:        1%{?dist}
Summary:        UbuntuMono Nerd Fonts
BuildArch:      noarch
License:        MIT
URL:            https://github.com/ryanoasis/nerd-fonts
Source0:        %{url}/releases/download/v%{version}/UbuntuMono.tar.xz

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
%license LICENSE

%changelog
* Wed Oct 15 2025 jhuang6451 <xplayerhtz123@outlook.com> - 3.4.0-1
- Initial release.