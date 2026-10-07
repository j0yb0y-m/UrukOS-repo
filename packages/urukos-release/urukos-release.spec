%global release_name Gilgamesh
# If you're not building this on Fedora, you're going to have a bad day.... but whatever.
%if 0%{?fedora}
%global dist_version %{fedora}
%else
%global dist_version 44
%endif

Summary:	UrukOS release files
Name:		urukos-release
Version:	%{dist_version}
Release:	0.1
License:	MIT
BuildArch: noarch

Provides: urukos-release = %{version}-%{release}
Provides: urukos-release-variant = %{version}-%{release}
Provides: urukos-release-identity = %{version}-%{release}

Conflicts: system-release
Provides: system-release
Provides: system-release(%{version})
Provides: system-release(releasever) = %{dist_version}
Conflicts:	fedora-release
Conflicts:	fedora-release-identity
Requires: urukos-release-common = %{version}-%{release}

%description
UrukOS release files such as os-release, issue files and macros that
define the release. Replacement for the Fedora trademarked release
packages. UrukOS is an independent project based on Fedora Linux.


%package common
Summary: UrukOS release files

Requires:   urukos-release-variant = %{version}-%{release}
Requires:   fedora-repos(%{version})

Conflicts: fedora-release-common

%description common
Release files for UrukOS


%prep

%build

%install
install -d %{buildroot}%{_prefix}/lib
echo "UrukOS release %{version} (%{release_name})" > %{buildroot}%{_prefix}/lib/urukos-release
echo "cpe:/o:urukos:urukos:%{version}" > %{buildroot}%{_prefix}/lib/system-release-cpe

# Symlink the -release files
install -d %{buildroot}%{_sysconfdir}
ln -s ../usr/lib/urukos-release %{buildroot}%{_sysconfdir}/urukos-release
ln -s ../usr/lib/system-release-cpe %{buildroot}%{_sysconfdir}/system-release-cpe
ln -s urukos-release %{buildroot}%{_sysconfdir}/redhat-release
ln -s urukos-release %{buildroot}%{_sysconfdir}/system-release

# Create the common os-release file
install -d $RPM_BUILD_ROOT/usr/lib/os.release.d/
cat << EOF >>%{buildroot}%{_prefix}/lib/os-release
NAME="UrukOS"
VERSION="%{dist_version} (%{release_name})"
ID=urukos
ID_LIKE="fedora"
VERSION_ID=%{dist_version}
PRETTY_NAME="UrukOS %{dist_version} (%{release_name})"
ANSI_COLOR="0;33"
LOGO=urukos-logo-icon
CPE_NAME="cpe:/o:urukos:urukos:%{dist_version}"
HOME_URL="https://github.com/j0yb0y-m/UrukOS-distro"
DOCUMENTATION_URL="https://github.com/j0yb0y-m/UrukOS-distro/tree/main/docs"
SUPPORT_URL="https://github.com/j0yb0y-m/UrukOS-distro/discussions"
BUG_REPORT_URL="https://github.com/j0yb0y-m/UrukOS-distro/issues"
IMAGE_VERSION="0.1"
EOF

# Create the common /etc/issue
echo "\\S" > %{buildroot}%{_prefix}/lib/issue
echo "Kernel \\r on an \\m (\\l)" >> %{buildroot}%{_prefix}/lib/issue
echo >> %{buildroot}%{_prefix}/lib/issue
ln -s ../usr/lib/issue %{buildroot}%{_sysconfdir}/issue

# Create /etc/issue.net
echo "\\S" > %{buildroot}%{_prefix}/lib/issue.net
echo "Kernel \\r on an \\m (\\l)" >> %{buildroot}%{_prefix}/lib/issue.net
ln -s ../usr/lib/issue.net %{buildroot}%{_sysconfdir}/issue.net

# Create the symlink for /etc/os-release
ln -s ../usr/lib/os-release $RPM_BUILD_ROOT/etc/os-release

# Set up the dist tag macros
install -d -m 755 $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d
cat >> $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.

%%fedora                %{dist_version}
%%dist                %%{?distprefix}.fc%{dist_version}%%{?with_bootstrap:~bootstrap}
%%fc%{dist_version}                1
EOF

%files common
%{_prefix}/lib/urukos-release
%{_prefix}/lib/system-release-cpe
%{_sysconfdir}/os-release
%{_sysconfdir}/urukos-release
%{_sysconfdir}/redhat-release
%{_sysconfdir}/system-release
%{_sysconfdir}/system-release-cpe
%attr(0644,root,root) %{_prefix}/lib/issue
%config(noreplace) %{_sysconfdir}/issue
%attr(0644,root,root) %{_prefix}/lib/issue.net
%config(noreplace) %{_sysconfdir}/issue.net
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist


%files
%{_prefix}/lib/os-release


%changelog
* Wed Oct 07 2026 Mahdi (J0yB0y) <jb.mahdi@outlook.com> - 44-0.1
- Initial UrukOS release package
