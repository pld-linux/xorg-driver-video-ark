Summary:	X.org video driver for ARK Logic video adapters
Summary(pl.UTF-8):	Sterownik obrazu X.org do kart graficznych ARK Logic
Name:		xorg-driver-video-ark
Version:	0.7.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-ark-%{version}.tar.xz
# Source0-md5:	cb5651b5b1e87383503e64cd8a58399f
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.12.901
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Requires:	xorg-lib-libpciaccess >= 0.12.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-ark < 1:7.0.0
Obsoletes:	XFree86-driver-ark < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for video adapters based on ARK Logic chipset.

%description -l pl.UTF-8
Sterownik obrazu X.org do kart graficznych opartych na układzie ARK
Logic.

%prep
%setup -q -n xf86-video-ark-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ark_drv.so
#%{_mandir}/man4/ark.4*
