Summary:	Xprobe2 is a fuzzy remote OS fingerprinting tool
Summary(pl):	Xprobe2 - narzêdzie do "rozmytej" identyfikacji zdalnych systemów
Name:		xprobe2
Version:	0.3
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://www.sys-security.com/archive/tools/xprobe2/%{name}-%{version}.tar.gz
# Source0-md5:	3ebb89ed9380038d368327816e34ec54
Patch0:		%{name}-paths.patch
URL:		http://www.sys-security.com/html/projects/X.html
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

%description -l pl
Xprobe2 to narzêdzie do "rozmytej" identyfikacji zdalnych systemów
operacyjnych. Funkcjonalno¶æ Xprobe2 bazuje g³ównie na Xprobe, ale
u¿ywa innych technik identyfikacji i opiera siê na bazie sygnatur,
które s± dopasowywane w sposób rozmyty. Xprobe2 zosta³o napisane od
zera w C++.

%prep
%setup -q
%patch0	-p1

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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -D etc/xprobe2.conf $RPM_BUILD_ROOT%{_sysconfdir}/xprobe2.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG docs/modules_howto.txt
%attr(755,root,root) %{_bindir}/xprobe2
%{_mandir}/man1/*
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xprobe2.conf
