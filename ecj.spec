Summary:	Eclipse Compiler for Java
Summary(pl.UTF-8):   Kompilator Eclipse dla Javy
Name:		ecj
Version:	0.298
Release:	2
License:	CPL v1.0
Group:		Development/Languages/Java
Source0:	ftp://sources.redhat.com/pub/rhug/ecj/rhug-%{name}-%{version}.tar.gz
# Source0-md5:	8e617bf2845a45b04c451694751d7408
URL:		http://www.eclipse.org/
BuildRequires:	automake
BuildRequires:	gcc-java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ECJ is a Java bytecode compiler extracted from the Eclipse IDE.

%description -l pl.UTF-8
ECJ to kompilator bajtkodu Javy wyodrębiony ze środowiska
programistycznego (IDE) Eclipse.

%prep
%setup -q -n rhug-ecj-%{version}

%build
cp -f /usr/share/automake/config.sub .

%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc upstream/about.html ChangeLog
%attr(755,root,root) %{_bindir}/ecj
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
