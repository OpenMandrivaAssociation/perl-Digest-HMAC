%define	modname	Digest-HMAC
%define modver	1.03

Summary:	Keyed-Hashing for Message Authentication
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	15
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/release/Digest-HMAC
Source0:	http://www.cpan.org/authors/id/GAAS/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
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

