Name:           milkytracker
Version:        0.90.85
Release:        %mkrel 1
Summary:        Module tracker software for creating music

Group:          Sound/Utilities
License:        GPLv3+
URL:            http://www.milkytracker.org/
Source0:        http://milkytracker.org/files/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         milkytracker-0.90.85-use-system-library.patch
Patch1:         milkytracker-0.90.85-use-system-library-pregenerated.patch
Patch2:         milkytracker-0.90.85-integer-types.patch
Patch3:         milkytracker-0.90.85-gzfile-type.patch

BuildRequires:  libSDL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(zziplib)
BuildRequires:  pkgconfig(jack)


%description
MilkyTracker is an application for creating music in the .MOD and .XM formats.
Its goal is to be free replacement for the popular Fasttracker II software.

%prep
%setup -q
#find . -regex '.*\.\(cpp\|h\|inl\)' -print0 | xargs -0 chmod 644

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Explicitly remove source files
rm -rf src/compression/zlib/
rm -rf src/compression/zziplib/generic/

# timestamp: touch files to remove autotool call
#touch -r configure aclocal.m4 Makefile.in config.h.in

%build
%configure2_5x --enable-jack
%make


%install
rm -rf %{buildroot}
%makeinstall_std

# copy the icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p resources/pictures/carton.png %{buildroot}%{_datadir}/pixmaps/milkytracker.png

# copy the desktop file
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE1}


%files
%doc AUTHORS COPYING NEWS README
%doc docs/FAQ.html
%doc docs/MilkyTracker.html
%doc docs/ChangeLog.html
%doc docs/readme_unix
%{_bindir}/milkytracker
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/milkytracker.png

%changelog
* Mon Aug 5 2013 Florent Monnier (@ Mageia)
- Added documentations
- Fixed homepage link

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.90.85-6
- Remove the --vendor flag from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.85-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 Joonas Sarajärvi <muep@iki.fi> - 0.90.85-4
- Fix build error from invalid C++ type conversions

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 07 2011 Joonas Sarajärvi <muepsj@gmail.com> - 0.90.85-1
- Update to upstream version 0.90.85
- Redo the build system tweaks to avoid using bundled zziplib
- Fix integer type errors

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.80-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.80-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 30 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.90.80-3
- Use system-wide zziplib (zlib is not used directly)

* Mon May 26 2008 Joonas Sarajärvi <muepsj@gmail.com> - 0.90.80-2
- Set Source0 to use macros for easier updating.
- Removed the --without-jack configuration option.
- Added -p to the cp command to preserve the timestamp.
- Replaced /usr/share with a macro.
- Added a line to prep to set correct permissions for source files extracted from the tarball.
- Modified a Makefile.am to not compile the included static zlib library.

* Sat May  3 2008 Joonas Sarajärvi <muepsj@gmail.com> - 0.90.80-1
- Initial RPM release.

