# This is where the package will be installed.  Change this next line as necessary.
%define _prefix         /usr
%define name            php-krb5
%define version         1.0.0
%define release         2%{?dist}

Summary: Kerberos authentication and management
Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.gz
Vendor: Moritz Bechler <mbechler@eenterphace.org>
URL: http://mbechler.eenterphace.org/blog/index.php?/archives/12-php_krb5-releases.html
License: MIT
Group: Development/Languages
BuildRoot: %{_builddir}/%{name}-root
BuildRequires: gcc, make, krb5-libs, php-devel, php-pear

Prefix: %{_prefix}

%description
Provides credential cache mangement, GSSAPI bindungs and KADM5 admistrative interface for kerberos

%prep
# Extract the source tar file
%setup -q

%build
%{_bindir}/phpize
# --enable-shared
#   build shared libraries [default=yes]
# --disable-static
#   don't build static libraries
CFLAGS="$RPM_OPT_FLAGS -O2" ./configure --prefix=%{_prefix} --enable-shared --disable-static
make

%install
# Cleanup from previous builds
rm -rf %{buildroot}

# Installs the files in BuildRoot when building the RPM
# phpize uses "INSTALL_ROOT" instead of "DESTDIR"
make INSTALL_ROOT=%{buildroot} install

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/krb5.ini << 'EOF'
; Enable krb5 extension module
extension = krb5.so
EOF

%clean
rm -rf %{buildroot}

%files
# Sets the owner and group of all files to root
%defattr(-,root,root)
# Labels certain files as documents to be put in /usr/share/doc
%doc CREDITS README
%config(noreplace) %{_sysconfdir}/php.d/krb5.ini
# Files to include in the RPM
%{_prefix}

%changelog
* Fri March 14 2014 Don Ky <don.d.ky@gmail.com> 1.0.0 
- Rebuilding for CentOS 6
- Removed changelog and manual.pdf from %files

* Fri May 10 2013 Bryan Maupin <bmaupincode@gmail.com> 20121214-2
- Add krb5.ini

* Thu May  9 2013 Bryan Maupin <bmaupincode@gmail.com> 20121214-1
- Initial package

