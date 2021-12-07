Summary:	Displays (tails) a given file anywhere on your X root window
Summary(pl.UTF-8):	Wyświetla (tail) dany plik jako tło w Xach
Name:		root-tail
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dist.schmorp.de/root-tail/%{name}-%{version}.tar.gz
# Source0-md5:	76681b2823604af8d9ea56695d774933
URL:		http://software.schmorp.de/pkg/root-tail.html
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Displays a given file anywhere on your X11 root window with a
transparent background. It was made because I'm very lazy and this was
easier than making a new rxvt pixmap each time I changed my background
to simulate that transparent effect.

%description -l pl.UTF-8
Narzędzie umożliwiające wyświetlanie danego pliku w głównym oknie X11
z przezroczystym tłem. Powstało po to, żeby nie zmieniać tła rxvt przy
każdej zmianie tła pulpitu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	COPTS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -Dp root-tail $RPM_BUILD_ROOT%{_bindir}/root-tail
install -Dp root-tail.man $RPM_BUILD_ROOT%{_mandir}/man1/root-tail.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/root-tail
%{_mandir}/man1/root-tail.1*
