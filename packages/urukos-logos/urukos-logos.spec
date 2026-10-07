%global assets_version 0.1.0

Name:       urukos-logos
Version:    %{assets_version}
Release:    1%{?dist}
Summary:    UrukOS icons and pictures

URL:        https://github.com/j0yb0y-m/UrukOS-assets
Source0:    https://github.com/j0yb0y-m/UrukOS-assets/archive/refs/tags/v%{assets_version}.tar.gz
License:    MIT
BuildArch:  noarch

Obsoletes:  redhat-logos
Obsoletes:  urukos-logos < 17.0.0-5
Provides:   system-logos = %{version}-%{release}

Conflicts:  fedora-logos
Requires(post): coreutils

%description
The urukos-logos package contains the UrukOS logo and pictures used by
the bootloader, anaconda, and other tools. It replaces the trademarked
fedora-logos package.

%prep
%setup -q -n UrukOS-assets-%{assets_version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 brand/logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/urukos-logo.svg
ln -s urukos-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/urukos-logo-icon.svg

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 brand/logo.svg %{buildroot}%{_datadir}/pixmaps/urukos-logo.svg
ln -s urukos-logo.svg %{buildroot}%{_datadir}/pixmaps/system-logo.svg

%files
%license LICENSE
%{_datadir}/icons/hicolor/scalable/apps/urukos-logo.svg
%{_datadir}/icons/hicolor/scalable/apps/urukos-logo-icon.svg
%{_datadir}/pixmaps/urukos-logo.svg
%{_datadir}/pixmaps/system-logo.svg

%changelog
* Wed Oct 07 2026 Mahdi (J0yB0y) <jb.mahdi@outlook.com> - 0.1.0-1
- Initial package
