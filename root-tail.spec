Summary:	Displays (tails) a given file anywhere on your X root window.
Name:		root-tail
Version:	0.0.10
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):      X11/Applikationen
Group(pl):      X11/Aplikacje
Source0:	http://goof.com/pcg/marc/data/%{name}-%{version}.tar.gz
URL:		http://goof.com/pcg/marc/root-tail.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	XFree86
BuildPreReq:	XFree86-devel

%description
Displays a given file anywhere on your X11 root window with a
transparent background. It was made because I'm very lazy and this was
easier than making a new rxvt pixmap each time I changed my background
to simulate that transparent effect.

%description -l pl
Narzêdzie umo¿liwiaj±ce wy¶wietlanie danego pliku jako przezroczyste t³o
w X11.

%prep
%setup -q

%build
xmkmf -a
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}
strip root-tail
mv root-tail.man root-tail.1
gzip -9 root-tail.1
install -m 755 -D root-tail %{buildroot}%{_bindir}/root-tail
install -D root-tail.1.gz %{buildroot}%{_mandir}/man1/root-tail.1.gz

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/root-tail
%{_mandir}/man1/root-tail.1.gz
