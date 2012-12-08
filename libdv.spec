%define major 4
%define libname %mklibname dv %{major}
%define develname %mklibname -d dv
%define staticname %mklibname -d -s dv

Summary:	DV software video codec
Name:		libdv
Version:	1.0.0
Release:	12
License:	LGPLv2+
Group:		Video
URL:		http://libdv.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libdv/%{name}-%{version}.tar.bz2
Patch0:		libdv-mmxdetect-athlon.patch
Patch4:		libdv-0.104-zap-config.h.patch
Patch5:		libdv-0.104-move-config.h-to-apps.patch
BuildRequires:	popt-devel

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

%package -n	%{develname}
Summary:	Devel files from libdv
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	popt-devel
Provides:	libdv-devel = %{version}-%{release}

%description -n	%{develname}
The Quasar DV codec (libdv) is a software codec for DV video.  DV is
the encoding format used by most digital camcorders, typically those
that support the IEEE 1394 (aka FireWire or i.Link) interface.  libdv
was developed according to the official standards for DV video, IEC
61834 and SMPTE 314M.  See http://libdv.sourceforge.net/ for more.

This is the libraries, include files and other resources you can use
to incorporate libdv into applications.

%package -n	%{staticname}
Group:		Development/C
Summary:	Static library of %{name}
Requires:	%{develname} = %{version}-%{release}

%description -n	%{staticname}
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
%makeinstall_std

%files apps
%doc ChangeLog COPYING README AUTHORS NEWS INSTALL TODO COPYRIGHT
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc ChangeLog COPYING README AUTHORS NEWS INSTALL TODO COPYRIGHT
%{_includedir}/libdv
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdv.pc

%files -n %{staticname}
%{_libdir}/*.a

%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9mdv2011.0
+ Revision: 662364
- mass rebuild

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 1.0.0-8
+ Revision: 636027
- rebuild
- tighten BR

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdv2011.0
+ Revision: 602538
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6mdv2010.1
+ Revision: 520765
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.0-5mdv2010.0
+ Revision: 425532
- rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1.0.0-4mdv2009.1
+ Revision: 365972
- drop old distro
- rediff mmx patch

* Tue Jul 15 2008 Götz Waschk <waschk@mandriva.org> 1.0.0-4mdv2009.0
+ Revision: 235758
- new devel package naming
- fix license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2009.0
+ Revision: 222536
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-2mdv2008.1
+ Revision: 150553
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Sep 25 2006 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2007.0
- drop patches 2,1,3,6,7,8,9
- New version 1.0.0

* Wed Jul 26 2006 Austin Acton <austin@mandriva.org> 0.104-5mdv2007.0
- disable gtk1.2

* Wed Jun 07 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.104-4mdv2007.0
- fix buildrequires
- sync with debian patches
- %%mkrel
- wipe out buildroot in %%install, not %%prep
- cleanups

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.104-3mdk
- Rebuild

* Mon Feb 14 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.104-2mdk
- PIC fixes to x86_64 code (libdv CVS)

* Tue Nov 30 2004 Götz Waschk <waschk@linux-mandrake.com> 0.104-1mdk
- New release 0.104

* Thu Jul 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.103-1mdk
- reenable libtoolize for cooker
- add source URL
- New release 0.103

* Fri Apr 02 2004 Götz Waschk <waschk@linux-mandrake.com> 0.102-1mdk
- major 4
- new version

* Sat Jan 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.101-1mdk
- don't run libtoolize
- drop merged patch1
- mdkversion macro
- new version

