Summary:	Xprobe2 is a fuzzy remote OS fingerprinting tool.
Name:		xprobe2
Version:	0.1rc1
Release:	0.5
License:	GPL
Group:		Networking
Source0:	http://www.sys-security.com/archive/tools/xprobe2/%{name}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
URL:		http://www.sys-security.com/html/projects/X.html
BuildRequires:	glibc-devel
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description
Xprobe2 is a fuzzy remote OS fingerprinting tool. Xprobe2 functionality is
heavily based  on Xprobe, but also uses other OS fingerprinting techniques
and is based on a signature base, which is matched in fuzzy manner.
Xprobe2 has been completely rewritten from the scratch in C++.

%prep
%setup -q -n %{name}
%patch0	-p1

%build
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