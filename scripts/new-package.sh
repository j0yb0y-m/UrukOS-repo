#!/bin/bash
# Scaffold a new package: scripts/new-package.sh <name>
set -euo pipefail
name="${1:?usage: new-package.sh <name>}"
dir="packages/${name}"
if [ -e "$dir" ]; then
	echo "exists: $dir" >&2
	exit 1
fi
mkdir -p "${dir}/files"
cat >"${dir}/${name}.spec" <<EOF
%global assets_version 0.1.0

Name:       ${name}
Version:    %{assets_version}
Release:    1%{?dist}
Summary:    TODO(verify): one-line summary
URL:        https://github.com/j0yb0y-m/UrukOS-repo
License:    MIT
BuildArch:  noarch

%description
TODO(verify): describe ${name}.

%prep

%build

%install
rm -rf %{buildroot}

%files

%changelog
* $(date '+%a %b %d %Y') Mahdi (J0yB0y) <jb.mahdi@outlook.com> - %{version}-1
- Initial package
EOF
echo "created ${dir}/${name}.spec"
