Name:       anu
Version:    0.1.0
Release:    1%{?dist}
Summary:    UrukOS post-install helper
URL:        https://github.com/j0yb0y-m/UrukOS-repo
Source0:    anu
Source1:    LICENSE
License:    MIT
BuildArch:  noarch

Requires:   python3
Requires:   python3-rich

%description
anu helps with post-install setup (codecs, RPM Fusion, Flatpak remotes),
app installs, firewall helpers, TPM2 enrollment and doctor checks.

%install
rm -rf %{buildroot}
install -Dm755 %{SOURCE0} %{buildroot}%{_bindir}/anu
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/anu/LICENSE

%files
%license %{_datadir}/licenses/anu/LICENSE
%{_bindir}/anu

%changelog
* Wed Oct 07 2026 Mahdi (J0yB0y) <jb.mahdi@outlook.com> - 0.1.0-1
- Initial skeleton
