%define	name	libdv
%define	version	1.0.0
%define	release	%mkrel 5

%define	major	4
%define	libname	%mklibname dv %{major}
%define develname %mklibname -d dv
%define staticname %mklibname -d -s dv

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		Video
Source0:	http://prdownloads.sourceforge.net/libdv/%name-%version.tar.bz2
URL:		http://libdv.sourceforge.net/
Patch0:		libdv-mmxdetect-athlon.patch
Patch4:		libdv-0.104-zap-config.h.patch
Patch5:		libdv-0.104-move-config.h-to-apps.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:	DV software video codec
BuildRequires:	popt-devel libxv-devel X11-devel

%description 
The Quasar DV codec (libdv) is a software codec for DV video.  DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface.  libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M.  See http://libdv.sourceforge.net/ for more.

%package	apps
Summary:	Binaries from libdv
Group:		Video
Provides:	%{_lib}dv2-apps = %{version}-%{release}
Obsoletes:	%{_lib}dv2-apps

%description	apps
The Quasar DV codec (libdv) is a software codec for DV video.  DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface.  libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M.  See http://libdv.sourceforge.net/ for more.
  
This is the libraries, include files and other resources you can use
to incorporate libdv into applications.


%package -n	%{libname}
Summary:	Libraries from libdv
Group:		System/Libraries

%description -n	%{libname}
The Quasar DV codec (libdv) is a software codec for DV video.  DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface.  libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M.  See http://libdv.sourceforge.net/ for more.

This is the libraries, include files and other resources you can use
to incorporate libdv into applications.

%package -n	%develname
Summary:	Devel files from libdv
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	popt-devel
Provides:	libdv-devel = %{version}-%{release}
Obsoletes: 	%mklibname -d dv 4
 
%description -n	%develname
The Quasar DV codec (libdv) is a software codec for DV video.  DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface.  libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M.  See http://libdv.sourceforge.net/ for more.
  
This is the libraries, include files and other resources you can use
to incorporate libdv into applications.

%package -n	%staticname
Group:		Development/C
Summary:	Static library of %{name}
Requires:	%develname = %{version}
Obsoletes:	%mklibname -s -d dv 4

%description -n	%staticname
This package contains the static library required for statically
linking applications based on %{name}.

%prep
%setup -q
%patch0 -p1 -b .mmx_athlon
%patch4 -p1 -b .zap_config
%patch5 -p1 -b .move_config

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  ./bootstrap
fi
%configure2_5x --enable-shared --disable-gtk

%make

%install
rm -rf %{buildroot}
%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files apps
%defattr(-,root,root)
%doc ChangeLog COPYING README AUTHORS NEWS INSTALL TODO COPYRIGHT
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr (- ,root,root)
%{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%doc ChangeLog COPYING README AUTHORS NEWS INSTALL TODO COPYRIGHT
%{_includedir}/libdv
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/libdv.pc

%files -n %staticname
%defattr(-,root,root)
%{_libdir}/*.a


