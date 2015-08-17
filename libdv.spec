%define major	4
%define libname	%mklibname dv %{major}
%define devname	%mklibname -d dv
%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	DV software video codec
Name:		libdv
Version:	1.0.0
Release:	21
License:	LGPLv2+
Group:		Video
Url:		http://libdv.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libdv/%{name}-%{version}.tar.bz2
Patch0:		libdv-mmxdetect-athlon.patch
Patch4:		libdv-0.104-zap-config.h.patch
Patch5:		libdv-0.104-move-config.h-to-apps.patch
BuildRequires:	pkgconfig(popt)

%description
The Quasar DV codec (libdv) is a software codec for DV video.  DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface.  libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M. See http://libdv.sourceforge.net/ for more.

%package	apps
Summary:	Binaries from libdv
Group:		Video
Provides:	%{_lib}dv2-apps = %{version}-%{release}

%description	apps
The Quasar DV codec (libdv) is a software codec for DV video.  DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface.  libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M.  See http://libdv.sourceforge.net/ for more.
  
%package -n	%{libname}
Summary:	Libraries from libdv
Group:		System/Libraries

%description -n	%{libname}
This package contains the shared library for %{name}.

%package -n	%{devname}
Summary:	Devel files from libdv
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}dv-static-devel < 1.0.0-13

%description -n	%{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  ./bootstrap
fi
%configure2_5x \
	--disable-static \
	--enable-shared \
	--disable-gtk

%make

%install
%makeinstall_std

%files apps
%doc README NEWS INSTALL TODO
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libdv.so.%{major}*

%files -n %{devname}
%doc ChangeLog COPYING AUTHORS COPYRIGHT
%{_includedir}/libdv
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdv.pc

