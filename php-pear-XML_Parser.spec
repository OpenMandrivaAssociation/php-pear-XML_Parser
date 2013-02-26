%define		_class		XML
%define		_subclass	Parser
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.3.4
Release:	%mkrel 2
Summary:	XML parsing class based on PHP's bundled expat
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is an XML parser based on PHPs built-in xml extension.  It supports two
basic modes of operation: "func" and "event".  In "func" mode, it will look for
a function named after each element (xmltag_ELEMENT for start tags and
xmltag_ELEMENT_ for end tags), and in "event" mode it uses a set of generic
callbacks.

Since version 1.2.0 there's a new XML_Parser_Simple class that makes parsing of
most XML documents easier, by automatically providing a stack for the elements.
Furthermore its now possible to split the parser from the handler object, so
you do not have to extend XML_Parser anymore in order to parse a document with
it.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-2mdv2011.0
+ Revision: 667680
- mass rebuild

* Thu Oct 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.4-1mdv2011.0
+ Revision: 589700
- new version

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.2-3mdv2010.1
+ Revision: 466339
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Oct 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.2-2mdv2010.0
+ Revision: 452033
- fix %%postun

* Mon Sep 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.2-1mdv2010.0
+ Revision: 450708
- import php-pear-XML_Parser


* Fri Sep 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.2-1mdv2010.0
- split out from php-pear package
