# Packaging

## Layout

```
packages/<name>/<name>.spec   spec file
packages/<name>/files/        local sources (scripts, configs, LICENSE)
.copr/Makefile                COPR make_srpm entry
scripts/new-package.sh        scaffold a new package
scripts/lint-specs.sh         rpmlint all specs
```

## Adding a package

```bash
./scripts/new-package.sh <name>
rpmlint packages/<name>/<name>.spec      # 0 errors expected
rpmbuild -bs --define "_sourcedir <dir-with-sources>" packages/<name>/<name>.spec
```

Rules (from AGENT_README.md):
- Use `urukos-` prefix. Verify any external package name with `dnf5 repoquery`.
- Reference the assets tarball as `Source0: https://github.com/j0yb0y-m/UrukOS-assets/archive/refs/tags/v%{assets_version}.tar.gz` — no git submodules.
- `FEDORA_RELEASE=44` comes from the `%fedora` macro; never hardcode "44".

## Building srpms for COPR

`.copr/Makefile` implements the `make_srpm` method. COPR invokes roughly:

```bash
make srpm outdir=<out> spec=<spec> sources=<srcdir>
```

It stages `packages/<name>/files/` plus any local sources and runs `spectool -g` for remote URLs, then `rpmbuild -bs`.

## Local verification

```bash
./scripts/lint-specs.sh                      # rpmlint
for s in packages/*/*.spec; do rpmbuild -bs ... "$s"; done   # build srpms
```

## Current packages

| Package | Source | Verified |
|---|---|---|
| urukos-release | generic-release 44-0.2 structure (dnf download --source) | rpmlint 0 errors, rpmbuild -bs + -bb OK |
| urukos-logos | assets v0.1.0 tarball | rpmlint 0 errors, -bs + -bb OK |
| urukos-release-notes | standalone (based on generic-release notes) | rpmlint 0 errors, -bs + -bb OK |
| urukos-skel | assets v0.1.0 tarball | rpmlint 0 errors, -bs + -bb OK |
| urukos-branding-kde | assets v0.1.0 tarball | rpmlint 0 errors, -bs + -bb OK |
| anu | local Python CLI | ruff clean + smoke test, -bs + -bb OK |

## TODO(verify)

- Exact COPR `make_srpm` variable names (`outdir`/`spec`/`sources`) — verify against COPR docs before wiring the webhook.
- LazyVim starter files for `/etc/skel/.config/nvim` (planned M5).
