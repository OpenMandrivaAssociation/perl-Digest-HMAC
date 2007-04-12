%define	name	perl-Digest-HMAC
%define	real_name Digest-HMAC
%define	version	1.01
%define	release	%mkrel 13

Summary:	Keyed-Hashing for Message Authentication
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.cpan.org/authors/id/GAAS/%{real_name}-%{version}.tar.bz2
URL:		http://www.cpan.org
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
Provides:	perl-HMAC
Requires:	perl perl-Digest-SHA1

%description
Digest-HMAC module for perl.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/Digest


