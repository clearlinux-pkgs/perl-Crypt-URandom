#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Crypt-URandom
Version  : 0.36
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/D/DD/DDICK/Crypt-URandom-0.36.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DD/DDICK/Crypt-URandom-0.36.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libcrypt-urandom-perl/libcrypt-urandom-perl_0.36-1.debian.tar.xz
Summary  : 'Provide non blocking randomness'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Crypt-URandom-license = %{version}-%{release}
Requires: perl-Crypt-URandom-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Crypt-URandom version 0.0.27
This Module is intended to provide an interface to the strongest
available source of non-blocking randomness on the current platform.
Platforms currently supported are anything supporting /dev/urandom
and versions of Windows greater than or equal to Windows 2000.

%package dev
Summary: dev components for the perl-Crypt-URandom package.
Group: Development
Provides: perl-Crypt-URandom-devel = %{version}-%{release}
Requires: perl-Crypt-URandom = %{version}-%{release}

%description dev
dev components for the perl-Crypt-URandom package.


%package license
Summary: license components for the perl-Crypt-URandom package.
Group: Default

%description license
license components for the perl-Crypt-URandom package.


%package perl
Summary: perl components for the perl-Crypt-URandom package.
Group: Default
Requires: perl-Crypt-URandom = %{version}-%{release}

%description perl
perl components for the perl-Crypt-URandom package.


%prep
%setup -q -n Crypt-URandom-0.36
cd %{_builddir}
tar xf %{_sourcedir}/libcrypt-urandom-perl_0.36-1.debian.tar.xz
cd %{_builddir}/Crypt-URandom-0.36
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Crypt-URandom-0.36/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Crypt-URandom
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Crypt-URandom/d3ce19637abaf0ec89a77868c508ea1d5169dd92
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Crypt::URandom.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Crypt-URandom/d3ce19637abaf0ec89a77868c508ea1d5169dd92

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Crypt/URandom.pm
