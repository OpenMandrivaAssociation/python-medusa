%define oname	medusa

Name: 	 	python-%{oname}
Summary: 	Framework for Python-based server
Version: 	0.5.4
Release: 	8
Source0:	http://www.amk.ca/files/python/%{oname}-%{version}.tar.bz2
URL:		http://www.amk.ca/python/code/medusa.html
License:	BSD
Group:		System/Servers
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
python setup.py install --root=%{buildroot} --compile --optimize=2

%files
%doc *.txt demo docs test
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}-py%{py_ver}.egg-info



%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0.5.4-7mdv2011.0
+ Revision: 594075
- rebuild

* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0.5.4-6mdv2011.0
+ Revision: 593932
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.5.4-5mdv2010.0
+ Revision: 442312
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.5.4-4mdv2009.1
+ Revision: 323788
- rebuild

* Fri Sep 12 2008 Adam Williamson <awilliamson@mandriva.org> 0.5.4-3mdv2009.0
+ Revision: 284047
- clean file list
- generate pyc and pyo files
- s,$RPM_BUILD_ROOT,%%{buildroot}
- clean python requires
- source location
- define and work off oname
- drop unnecessary defines

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.5.4-2mdk
- Rebuild for new python

* Sun Feb 22 2004 Austin Acton <austin@mandrake.org> 0.5.4-1mdk
- 0.5.4
- noarch

* Sat Aug 09 2003 Austin Acton <aacton@yorku.ca> 0.5.3-2mdk
- python 2.3

* Mon Mar 31 2003 Austin Acton <aacton@yorku.ca> 0.5.3-1mdk
- initial package

