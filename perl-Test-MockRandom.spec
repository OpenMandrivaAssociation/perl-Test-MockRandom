
%define realname   Test-MockRandom
%define version    1.00
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Override randoms with non-random behavior
Source:     http://www.cpan.org/modules/by-module/Test/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description
This perhaps ridiculous-seeming module was created to test routines that
manipulate random numbers by providing a known output from 'rand'. Given a
list of seeds with 'srand', it will return each in turn. After seeded
random numbers are exhausted, it will always return 0. Seed numbers must be
of a form that meets the expected output from 'rand' as called with no
arguments -- i.e. they must be between 0 (inclusive) and 1 (exclusive). In
order to facilitate generating and testing a nearly-one number, this module
exports the function 'oneish', which returns a number just fractionally
less than one. 

Depending on how this module is called with 'use', it will export 'rand' to
a specified package (e.g. a class being tested) effectively overriding and
intercepting calls in that package to the built-in 'rand'. It can also
override 'rand' in the current package or even globally. In all of these
cases, it also exports 'srand' and 'oneish' to the current package in order
to control the output of 'rand'. See the /USAGE manpage for details.

Alternatively, this module can be used to generate objects, with each
object maintaining its own distinct seed array.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.00-3mdv2011.0
+ Revision: 658888
- rebuild for updated spec-helper

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.00-2mdv2010.0
+ Revision: 440697
- rebuild

* Fri Feb 20 2009 Jérôme Quelin <jquelin@mandriva.org> 1.00-1mdv2009.1
+ Revision: 343333
- import perl-Test-MockRandom


* Fri Feb 20 2009 cpan2dist 1.00-1mdv
- initial mdv release, generated with cpan2dist

