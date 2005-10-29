Summary:	X.org video driver for ARK Logic video adapters
Summary(pl):	Sterownik obrazu X.org do kart graficznych ARK Logic
Name:		xorg-driver-video-ark
Version:	0.5.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-ark-%{version}.tar.bz2
# Source0-md5:	45e60d8b6d82911a561cbfc91fa2b1cc
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for video adapters based on ARK Logic chipset.

%description -l pl
Sterownik obrazu X.org do kart graficznych opartych na uk�adzie ARK
Logic.

%prep
%setup -q -n xf86-video-ark-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ark_drv.so
#%{_mandir}/man4/ark.4x*
