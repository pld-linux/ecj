Summary:	Eclipse Compiler for Java
Name:		ecj
Version:	0.298
Release:	0.1
License:	CPL v1.0
Group:		Development/Languages/Java
Source0:	ftp://sources.redhat.com/pub/rhug/ecj/rhug-%{name}-%{version}.tar.gz
# Source0-md5:	8e617bf2845a45b04c451694751d7408
URL:		http://www.eclipse.org/
BuildRequires:	gcc-java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ECJ is a Java bytecode compiler extracted from the Eclipse IDE.

%prep
%setup -q -n rhug-ecj-%{version}

%build
%configure \
	--disable-static

%{__make} -r

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%ldconfig_post

%postun
%ldconfig_postun

%files
%defattr(644,root,root,755)
%doc upstream/about.html ChangeLog
%attr(755,root,root) %{_bindir}/ecj
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
