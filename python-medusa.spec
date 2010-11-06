%define oname	medusa

Name: 	 	python-%{oname}
Summary: 	Framework for Python-based server
Version: 	0.5.4
Release: 	%mkrel 6
Source0:	http://www.amk.ca/files/python/%{oname}-%{version}.tar.bz2
URL:		http://www.amk.ca/python/code/medusa.html
License:	BSD
Group:		System/Servers
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
%{py_requires}
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
%setup -q -n %{oname}-%{version}

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt demo docs test
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}-py%{pyver}.egg-info

