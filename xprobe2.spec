Summary:	Xprobe2 is a fuzzy remote OS fingerprinting tool
Summary(pl.UTF-8):	Xprobe2 - narzędzie do "rozmytej" identyfikacji zdalnych systemów
Name:		xprobe2
Version:	0.3
Release:	0.2
License:	GPL
Group:		Networking
Source0:	http://dl.sourceforge.net/xprobe/%{name}-%{version}.tar.gz
# Source0-md5:	3ebb89ed9380038d368327816e34ec54
Patch0:		%{name}-paths.patch
Patch1:		gcc4.3.patch
URL:		http://www.sys-security.com/index.php?page=xprobe
BuildRequires:	autoconf
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description
Xprobe2 is a fuzzy remote OS fingerprinting tool. Xprobe2
functionality is heavily based on Xprobe, but also uses other OS
fingerprinting techniques and is based on a signature base, which is
matched in fuzzy manner. Xprobe2 has been completely rewritten from
the scratch in C++.

%description -l pl.UTF-8
Xprobe2 to narzędzie do "rozmytej" identyfikacji zdalnych systemów
operacyjnych. Funkcjonalność Xprobe2 bazuje głównie na Xprobe, ale
używa innych technik identyfikacji i opiera się na bazie sygnatur,
które są dopasowywane w sposób rozmyty. Xprobe2 zostało napisane od
zera w C++.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
cp -f /usr/share/automake/config.sub cfg-scripts/config.sub
cp -f /usr/share/automake/config.sub libs-external/USI++/src/cfgaux/config.sub
%{__autoconf}
cd libs-external/USI++/src
%{__autoconf}
cd ../../../
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D etc/xprobe2.conf $RPM_BUILD_ROOT%{_sysconfdir}/xprobe2.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG docs/modules_howto.txt
%attr(755,root,root) %{_bindir}/xprobe2
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xprobe2.conf
%{_mandir}/man1/*
