%define BINNAME date
Summary: date
Name: date
Version: 1.0.0
Release: 1
License: MIT
Group: Development/Tools
URL: https://github.com/fmidev/date
Source0: %{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
Provides: cpr

%description
A date and time library based on the C++11/14/17 <chrono> header

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{BINNAME}
 
%build
cmake -DUSE_SYSTEM_TZ_DB=ON -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=/usr .
cmake --build .

%install
mkdir -m 0755 -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -m 0755 -p $RPM_BUILD_ROOT/%{_includedir}/date
install -m 644 libtz.so $RPM_BUILD_ROOT/%{_libdir}/
install -m 644 include/date/*.h $RPM_BUILD_ROOT/%{_includedir}/date/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0664,root,root,-)
%{_libdir}/*.so
%{_includedir}/date/*.h

%changelog
* Tue Sep 11 2018 Mika Heiskanen <mika.heiskanen@fmi.fi> - 1.0.0-1
- Initial RPM package


