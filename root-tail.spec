Summary:	Displays (tails) a given file anywhere on your X root window
Summary(pl):	Wy¶wietla (tail) dany plik jako t³o w Xach
Name:		root-tail
Version:	0.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://goof.com/pcg/marc/data/%{name}-%{version}.tar.gz
# Source0-md5:	92c217c21c4388413b8fb3e0d9ffb6ac
URL:		http://goof.com/pcg/marc/root-tail.html
BuildRequires:	XFree86-devel
Requires:	XFree86
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Displays a given file anywhere on your X11 root window with a
transparent background. It was made because I'm very lazy and this was
easier than making a new rxvt pixmap each time I changed my background
to simulate that transparent effect.

%description -l pl
Narzêdzie umo¿liwiaj±ce wy¶wietlanie danego pliku w g³ównym oknie X11
z przezroczystym t³em. Powsta³o po to, ¿eby nie zmieniaæ t³a rxvt przy
ka¿dej zmianie t³a desktopu.

%prep
%setup -q

%build
xmkmf -a
%{__make} CXXDEBUGFLAGS="%{rpmcflags}"

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
%{_mandir}/man1/root-tail.1.*
