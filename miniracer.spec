Summary:	Racing game
Summary(pl):	Wy¶cigi samochodowe
Name:		miniracer
Version:	1.03
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f0f2c26390a4005a8ae0a057560f7ba4
Patch0:		%{name}-files.patch
URL:		http://miniracer.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_mixer-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Miniracer is a now cross-platform racing game. It's featuring
different cars and tracks. You can play it top-down or first-person.
Network play is also possible.

%description -l pl
Miniracer jest wieloplatformow± gr± w wy¶cigi samochodowe. Mo¿na
¶cigaæ siê wieloma samochodami i na wielu trasach. Mo¿na graæ przy
widoku z góry lub z perspektywy kierowcy. Kolejn± cech± jest mo¿liwo¶æ
gry sieciowej.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags} -I. -I/usr/X11R6/include -I/usr/include/SDL \
	-DVIDMODEXT_GAMMA_RAMP -DSOUND"

cp miniracer miniracer.tmp
cat miniracer.tmp | sed -e 's#/usr/share/games#%{_datadir}#' | \
	sed -e 's#/usr/lib#%{_libdir}#' > miniracer

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	datadir=%{_datadir} \
	bindir=%{_bindir} \
	libdir=%{_libdir} \
	mandir=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/engine.glx
%{_datadir}/MiniRacer
%{_mandir}/man6/%{name}.6*
