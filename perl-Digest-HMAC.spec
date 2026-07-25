%define	modname	Digest-HMAC
%define modver	1.05

Summary:	Keyed-Hashing for Message Authentication
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/arodland/Digest-HMAC
Source0:	https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/Digest-HMAC-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Digest::SHA1)
Requires:	perl(Digest::SHA1)
Provides:	perl-HMAC

%description
Digest-HMAC module for perl.

%prep
%setup -qn %{modname}-%{modver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Digest
%{_mandir}/man3/*

