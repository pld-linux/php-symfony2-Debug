%define		package	Debug
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Debug Component
Name:		php-symfony2-Debug
Version:	2.7.7
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	7e7563dff4779f9e186696c1ddf6d068
URL:		http://symfony.com/doc/2.7/components/debug/index.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(spl)
Requires:	php-pear >= 4:1.3.10
Requires:	php-psr-Log >= 1.0
Suggests:	php(symfony_debug)
Suggests:	php-symfony2-HttpKernel >= 2.6.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Debug Component provides tools to ease debugging PHP code.

%prep
%setup -q -n debug-%{version}

# native extension. to be built from separate .spec
rm -r Resources/ext

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/Debug
%{php_pear_dir}/Symfony/Component/Debug/*.php
%{php_pear_dir}/Symfony/Component/Debug/Exception
%{php_pear_dir}/Symfony/Component/Debug/FatalErrorHandler
