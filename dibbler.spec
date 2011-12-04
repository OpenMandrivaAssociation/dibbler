Summary: Dibbler - a portable DHCPv6
Name: dibbler
Version: 0.8.0
Release: 1
URL: http://klub.com.pl/dhcpv6/dibbler
License: GPL
Group: System/Servers
Source: %{name}-%{version}-src.tar.gz 
Source1: dibbler-client
Source2: dibbler-server
BuildRequires:  tetex-latex

%description
It supports both stateful (i.e. IPv6 address granting) and stateless 
(i.e. options granting) autoconfiguration modes of DHCPv6 protocol. 
There are ports available for Linux 2.4/2.6 systems as well as MS 
Windows XP,2003 (experimental support for NT4 and 2000). 
They are freely available under GNU GPL v2 or later license. 

Install Dibbler if you'd like to have IPv6 hosts automatically 
configured in your network. All infrastructure elements are
provided: server, client and relay.

%prep
%setup -q

%build
%make client server relay doc

%install
mkdir -p %{buildroot}/%{_sbindir}
install -m 755 dibbler-server %{buildroot}/%{_sbindir}
install -m 755 dibbler-client %{buildroot}/%{_sbindir}
install -m 755 dibbler-relay  %{buildroot}/%{_sbindir}

mkdir -p %{buildroot}/%{_datadir}/man/man8
install -m 644 doc/man/dibbler-client.8 %{buildroot}/%{_datadir}/man/man8
install -m 644 doc/man/dibbler-server.8 %{buildroot}/%{_datadir}/man/man8
install -m 644 doc/man/dibbler-relay.8  %{buildroot}/%{_datadir}/man/man8
mkdir -p %{buildroot}/%{_sysconfdir}/dibbler
mkdir -p %{buildroot}/var/lib/dibbler/
mkdir -p %{buildroot}/%{_sysconfdir}/init.d/

install -m 644 client.conf %{buildroot}/%{_sysconfdir}/dibbler
install -m 644 client-stateless.conf %{buildroot}/%{_sysconfdir}/dibbler
install -m 644 server.conf %{buildroot}/%{_sysconfdir}/dibbler
install -m 644 server-stateless.conf %{buildroot}/%{_sysconfdir}/dibbler
install -m 644 relay.conf %{buildroot}/%{_sysconfdir}/dibbler
install -m 700 %{SOURCE1} %{buildroot}/etc/init.d/
install -m 700 %{SOURCE2} %{buildroot}/etc/init.d/

%files
%defattr(-,root,root)
%doc CHANGELOG LICENSE RELNOTES doc/dibbler-user.pdf doc/dibbler-devel.pdf
%{_sbindir}/dibbler-server
%{_sbindir}/dibbler-client
%{_sbindir}/dibbler-relay
%{_datadir}/man/man8/*
/var/lib/dibbler/
%{_sysconfdir}/dibbler/client.conf
%{_sysconfdir}/dibbler/client-stateless.conf
%{_sysconfdir}/dibbler/server.conf
%{_sysconfdir}/dibbler/server-stateless.conf
%{_sysconfdir}/dibbler/relay.conf
%{_sysconfdir}/init.d/*
