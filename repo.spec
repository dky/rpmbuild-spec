Name:           examplerepo
Version:        0.0.1
Release:        1%{?dist}
Summary:        Example Internal RHEL7 repo

License:        GPLv3
URL:            http://repo.example.com/repo/rhel7-x86_64
Source0:    	 http://repo.example.com/repo/rhel7-x86_64/examplerepo-0.0.1.tar.gz

%description
Populates /etc/yum.repos.d with internal repo

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
cp -p examplerepo.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/etc/yum.repos.d/examplerepo.repo

%changelog
* Sun Nov 16 2014 Don Ky <dkynyc@gmail.com> 0.0.1
- Custom RPM for internal repo

