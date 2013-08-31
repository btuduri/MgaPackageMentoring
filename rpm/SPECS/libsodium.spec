#exemple :
#lib3ds
#libcaca
#libarchive
#libass
#libassuan

%define name    libsodium
%define version 0.4.2
%define rel     1
%define api     0.4
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname -d %{name}

Name:           %{name}
Version:        %{version}
Release:        %mkrel %{rel}
Group:          System/Libraries
License:        ISC
URL:            http://github.org/jedisct1/libsodium
Source0:        http://download.libsodium.org/libsodium/releases/libsodium-0.4.2.tar.gz

Summary:        Sodium is a portable, cross-compatible, installable, packageable fork of NaCI.

%description
llalalaa

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}


%build
%configure2_5x --disable-static
%make


%check
%make check


%install
%makeinstall_std
rm -fr %{buildroot}%{_libdir}/*.la


%files
%doc AUTHORS NEWS THANKS
%{_libdir}/*.so.*

%files devel
%doc AUTHORS NEWS THANKS
%{_includedir}/*
%{_libdir}/*.so
