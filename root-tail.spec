Summary:	Displays (tails) a given file anywhere on your X root window
Summary(pl.UTF-8):	Wyświetla (tail) dany plik jako tło w Xach
Name:		root-tail
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goof.com/pcg/marc/data/%{name}-%{version}.tar.gz
# Source0-md5:	5a4b3c4c7ab3bed1f4575e9688aac5de
URL:		http://goof.com/pcg/marc/root-tail.html
BuildRequires:	rman
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-util-gccmakedep
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Displays a given file anywhere on your X11 root window with a
transparent background. It was made because I'm very lazy and this was
easier than making a new rxvt pixmap each time I changed my background
to simulate that transparent effect.

%description -l pl.UTF-8
Narzędzie umożliwiające wyświetlanie danego pliku w głównym oknie X11
z przezroczystym tłem. Powstało po to, żeby nie zmieniać tła rxvt przy
każdej zmianie tła desktopu.

%prep
%setup -q

%build
xmkmf -a
%{__make} \
	CXXDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D root-tail $RPM_BUILD_ROOT%{_bindir}/root-tail
install -D root-tail.man $RPM_BUILD_ROOT%{_mandir}/man1/root-tail.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/root-tail
%{_mandir}/man1/root-tail.1*
