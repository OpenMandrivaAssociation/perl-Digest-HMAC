%define	upstream_name    Digest-HMAC
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:	Keyed-Hashing for Message Authentication
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	http://www.cpan.org/authors/id/GAAS/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  perl-devel
BuildRequires:  perl(Digest::SHA1)
Requires:	perl(Digest::SHA1)
Provides:	perl-HMAC

%description
Digest-HMAC module for perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/Digest


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-5mdv2012.0
+ Revision: 765186
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-4
+ Revision: 763702
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-3
+ Revision: 763057
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-2
+ Revision: 667120
- mass rebuild

* Mon Jan 11 2010 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.1
+ Revision: 489514
- update to 1.02

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 406986
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.01-16mdv2009.1
+ Revision: 351715
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.01-15mdv2009.0
+ Revision: 223658
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.01-14mdv2008.1
+ Revision: 180392
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.01-13mdv2007.0
+ Revision: 108541
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Digest-HMAC

* Tue Jan 18 2005 Abel Cheung <deaddog@mandrake.org> 1.01-12mdk
- rebuild

