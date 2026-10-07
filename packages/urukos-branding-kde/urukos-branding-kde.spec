%global assets_version 0.1.0

Name:       urukos-branding-kde
Version:    %{assets_version}
Release:    1%{?dist}
Summary:    UrukOS KDE Plasma color scheme, look-and-feel and avatar
URL:        https://github.com/j0yb0y-m/UrukOS-assets
Source0:    https://github.com/j0yb0y-m/UrukOS-assets/archive/refs/tags/v%{assets_version}.tar.gz
License:    MIT
BuildArch:  noarch

%description
Installs the UrukOS KDE color scheme, look-and-feel package and user
avatar.

%prep
%setup -q -n UrukOS-assets-%{assets_version}

%build

%install
rm -rf %{buildroot}

install -Dm644 kde/colors/UrukOS.colors %{buildroot}%{_datadir}/color-schemes/UrukOS.colors
mkdir -p %{buildroot}%{_datadir}/plasma/look-and-feel
cp -r kde/look-and-feel/org.urukos.desktop %{buildroot}%{_datadir}/plasma/look-and-feel/
install -Dm644 kde/avatar/urukos-avatar.png %{buildroot}%{_datadir}/plasma/avatars/urukos.png

%files
%license LICENSE
%{_datadir}/color-schemes/UrukOS.colors
%{_datadir}/plasma/look-and-feel/org.urukos.desktop
%{_datadir}/plasma/avatars/urukos.png

%changelog
* Wed Oct 07 2026 Mahdi (J0yB0y) <jb.mahdi@outlook.com> - 0.1.0-1
- Initial package
