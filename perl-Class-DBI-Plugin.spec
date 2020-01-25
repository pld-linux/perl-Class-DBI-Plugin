#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Class
%define	pnam	DBI-Plugin
Summary:	Class::DBI::Plugin - Abstract base class for Class::DBI plugins
Name:		perl-Class-DBI-Plugin
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b020611a93fe51cbcdfd78f2cbf872cb
URL:		http://search.cpan.org/dist/Class-DBI-Plugin/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::DBI) >= 0.9
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::DBI::Plugin is an abstract base class for Class::DBI plugins.
Its purpose is to make writing plugins easier. Writers of plugins
should be able to concentrate on the functionality their module
provides, instead of having to deal with the symbol table hackery
involved when writing a plugin module.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/DBI/*.pm
%{_mandir}/man3/*
