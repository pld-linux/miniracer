# Conditional build:
%bcond_without	gamma_ramp	# disable VidModeGammaRamp extension
#
Summary:	Racing game
Summary(pl):	Wy¶cigi samochodowe
Name:		miniracer
Version:	1.04
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9078a3820bda65fac66e8cfc8270c102
Patch0:		%{name}-files.patch
URL:		http://miniracer.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	sed >= 4.0
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
	OPTFLAGS="%{rpmcflags} \
	%{?with_gamma_ramp:-DVIDMODEXT_GAMMA_RAMP}"

sed -i -e 's#/usr/lib#%{_libdir}#' miniracer

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
