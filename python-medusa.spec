%define name	python-medusa
%define version 0.5.4
%define release 2mdk

Name: 	 	%{name}
Summary: 	Framework for python-based server
Version: 	%{version}
Release: 	%{release}

Source:		medusa-%{version}.tar.bz2
URL:		http://www.amk.ca/python/code/medusa.html
License:	BSD
Group:		System/Servers
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel

%description
Medusa is an architecture for very-high-performance TCP/IP servers
(like HTTP, FTP, and NNTP).  Medusa is different from most other
servers because it runs as a single process, multiplexing I/O with its
various client and server connections within a single process/thread.
 
It is capable of smoother and higher performance than most other
servers, while placing a dramatically reduced load on the server
machine.  The single-process, single-thread model simplifies design
and enables some new persistence capabilities that are otherwise
difficult or impossible to implement.

%prep
%setup -q -n medusa-%version

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *.txt demo docs test
%_libdir/python2*/site-packages/medusa

