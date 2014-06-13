%define	_class	XML
%define	_subclass	Parser
%define	modname	%{_class}_%{_subclass}

Summary:	XML parsing class based on PHP's bundled expat
Name:		php-pear-%{modname}
Version:	1.3.4
Release:	8
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/%{modname}
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This is an XML parser based on PHPs built-in xml extension.  It supports two
basic modes of operation:	"func" and "event".  In "func" mode, it will look for
a function named after each element (xmltag_ELEMENT for start tags and
xmltag_ELEMENT_ for end tags), and in "event" mode it uses a set of generic
callbacks.

Since version 1.2.0 there's a new XML_Parser_Simple class that makes parsing of
most XML documents easier, by automatically providing a stack for the elements.
Furthermore its now possible to split the parser from the handler object, so
you do not have to extend XML_Parser anymore in order to parse a document with
it.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

