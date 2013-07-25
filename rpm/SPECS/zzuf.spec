Name:           zzuf
Version:        0.13
Release:        %mkrel 1
Summary:        Transparent application input fuzzer

Group:          Development/Tools
License:        WTFPL
URL:            http://sam.zoy.org/zzuf/
Source0:        http://ftp.debian.org/debian/pool/main/z/zzuf/zzuf_0.13.svn20100215.orig.tar.gz

%description
zzuf is a transparent application input fuzzer.  It works by
intercepting file operations and changing random bits in the program's
input.  zzuf's behavior is deterministic, making it easy to reproduce
bugs.


%prep
%setup -q


%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/zzuf/*.la


%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/zzuf
%{_bindir}/zzat
%dir %{_libdir}/zzuf/
%{_libdir}/zzuf/libzzuf.so
%{_mandir}/man1/zzuf.1*
%{_mandir}/man1/zzat.1*
%{_mandir}/man3/libzzuf.3*


%changelog
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6.20100215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5.20100215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Jon Ciesla <limburgher@gmail.com> - 0.13-4.20100215
- Update to svn snapshot to fix BZ 641024, zzcat is now zzat.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 01 2010 Jon Ciesla <limb@jcomserv.net> - 0.13-1
- 0.13.
- Updated optflags patch, dropped open patch.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 14 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.12-1
- 0.12.

* Thu May 22 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.11-1
- 0.11.

* Tue Feb 12 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.10-2
- Rebuild.

* Sat Nov  3 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.10-1
- 0.10.

* Sun Aug 19 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.9-2
- Fix build with glibc >= 2.6.90 and -D_FORTIFY_SOURCE=2, thanks to
  Jan Kratochvil.

* Tue Jul 10 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.9-1
- 0.9.

* Sat Apr  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.8.1-1
- First Fedora build.

* Thu Apr  5 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.8.1-0.1
- First build.
