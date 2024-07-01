#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v4
# autospec commit: da8b975
#
Name     : perl-Crypt-URandom
Version  : 0.40
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/D/DD/DDICK/Crypt-URandom-0.40.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DD/DDICK/Crypt-URandom-0.40.tar.gz
Summary  : 'Provide non blocking randomness'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Crypt-URandom-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Pod)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Crypt::URandom - Provide non blocking randomness
VERSION
This document describes Crypt::URandom version 0.40

%package dev
Summary: dev components for the perl-Crypt-URandom package.
Group: Development
Provides: perl-Crypt-URandom-devel = %{version}-%{release}
Requires: perl-Crypt-URandom = %{version}-%{release}

%description dev
dev components for the perl-Crypt-URandom package.


%package perl
Summary: perl components for the perl-Crypt-URandom package.
Group: Default
Requires: perl-Crypt-URandom = %{version}-%{release}

%description perl
perl components for the perl-Crypt-URandom package.


%prep
%setup -q -n Crypt-URandom-0.40
cd %{_builddir}/Crypt-URandom-0.40
pushd ..
cp -a Crypt-URandom-0.40 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Crypt::URandom.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
