%if 0%{?fedora}
%global dist_version %{fedora}
%else
%global dist_version 44
%endif

Name:       urukos-release-notes
Version:    %{dist_version}
Release:    0.1
Summary:    UrukOS release notes
License:    LicenseRef-Not-Copyrightable
BuildArch:  noarch

Provides:   system-release-notes = %{version}-%{release}
Conflicts:  fedora-release-notes

%description
UrukOS release notes package. Placeholder content; real notes are
published with each tagged UrukOS release.

%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/%{name}
cat > %{buildroot}%{_docdir}/%{name}/README.UrukOS-Release-Notes << EOF
UrukOS %{version} (Gilgamesh)
============================

UrukOS is an independent project based on Fedora Linux. It is not
affiliated with or endorsed by the Fedora Project or Red Hat.

See https://github.com/j0yb0y-m/UrukOS-distro/releases for release notes.
EOF

%files
%doc %{_docdir}/%{name}/README.UrukOS-Release-Notes

%changelog
* Wed Oct 07 2026 Mahdi (J0yB0y) <jb.mahdi@outlook.com> - 44-0.1
- Initial package
