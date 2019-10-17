Summary:	Multi-purpose finite-state toolkit
Summary(pl.UTF-8):	Toolkit do tworzenia automatów skończonych różnego zastosowania
Name:		foma
Version:	0.9.17
Release:	3
License:	GPL v2
Group:		Development/Tools
#Source0Download: https://github.com/mhulden/foma
Source0:	https://foma.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	17c40eb005d3c823231c24c77a8ec99d
URL:		http://fomafst.github.io/
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Foma is a multi-purpose finite-state toolkit designed for applications
ranging from natural language processing and research in automata
theory. It should be upwardly compatible with Xerox xfst and lexc,
with the exception of binary file reading and writing.

%description -l pl.UTF-8
Foma to toolkit do tworzenia automatów skończonych o różnych
zastosowaniu, począwszy od aplikacji przetwarzających języki naturalne
do badań w dziedzinie teorii automatów. Powinien być kompatybilny w
górę z narzędziami Xeroksa xfst i lexc, z wyjątkiem odczytu i zapisu
plików binarnych.

%package devel
Summary:	Header files for Foma library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Foma
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Foma library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Foma.

%package static
Summary:	Static Foma library
Summary(pl.UTF-8):	Statyczna biblioteka Foma
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Foma library.

%description static -l pl.UTF-8
Statyczna biblioteka Foma.

%prep
%setup -q

%build
%{__make} libfoma \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_GNU_SOURCE -std=c99 -fvisibility=hidden -fPIC" \
	LDFLAGS="%{rpmldflags} -lreadline -lz"

# workaround to avoid rebuilding library on install
touch libfoma

%{__make} foma flookup cgflookup \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_GNU_SOURCE -std=c99 -fvisibility=hidden" \
	LDFLAGS="%{rpmldflags} -lreadline -lz"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	libdir=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG README*
%attr(755,root,root) %{_bindir}/cgflookup
%attr(755,root,root) %{_bindir}/flookup
%attr(755,root,root) %{_bindir}/foma
%attr(755,root,root) %{_libdir}/libfoma.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfoma.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfoma.so
%{_includedir}/fomalib*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libfoma.a
