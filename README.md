# UrukOS-repo

RPM packaging for UrukOS: one spec per package, COPR integration, lint CI.

## How it fits

Part of the UrukOS project:

- [UrukOS-assets](https://github.com/j0yb0y-m/UrukOS-assets) — branding source, consumed here as tagged release tarballs
- [UrukOS-repo](https://github.com/j0yb0y-m/UrukOS-repo) — this repo
- [UrukOS-distro](https://github.com/j0yb0y-m/UrukOS-distro) — KIWI build files that install these packages into the ISO

## Quick start

```bash
scripts/new-package.sh <name>   # scaffold packages/<name>/<name>.spec
scripts/lint-specs.sh           # rpmlint all specs
```

COPR builds RPMs via the `make_srpm` method using `.copr/Makefile`.

## Directory map

```
packages/<name>/<name>.spec   one folder per package (+ sources/patches only if small)
.copr/Makefile                COPR "make srpm" entry
scripts/                      new-package.sh, lint-specs.sh
docs/                         STATUS.md, PACKAGING.md, tools.md
.github/workflows/lint.yml    rpmlint on specs, shellcheck, ruff
```

## Contributing

See the UrukOS agent guide in the parent folder. Conventional Commits, English docs. Package names use the `urukos-` prefix. Verify package names with `dnf5 repoquery` before adding them.

## License

MIT. Copyright (c) 2026 Mahdi (J0yB0y). See [LICENSE](LICENSE).

UrukOS is an independent project based on Fedora Linux. It is not affiliated with or endorsed by the Fedora Project or Red Hat. Fedora and the Infinity design logo are trademarks of Red Hat, Inc.
