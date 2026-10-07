# Status
Last updated: 2026-10-07
Milestone: M3

## Done
- Specs created under `packages/`: urukos-release, urukos-logos, urukos-release-notes, urukos-skel, urukos-branding-kde, anu
- Structure mirrored from upstream `generic-release`/`generic-logos` (dnf download --source, extracted to /tmp/opencode/urukos-m3)
- All specs pass rpmlint with 0 errors (warnings only: unversioned-provides/obsoletes mirroring upstream, no-%check-section, heredoc whitespace)
- All 6 packages build: `rpmbuild -bs` OK for all, `rpmbuild -bb` OK for all; os-release verified from built rpm (NAME=UrukOS, ID=urukos, ID_LIKE=fedora, VERSION 44 (Gilgamesh))
- `anu` skeleton: argparse CLI (setup/install/update/doctor/fw/tpm), --dry-run, /var/log/anu.log best-effort, ruff clean, smoke-tested
- `.copr/Makefile` (make_srpm method), scripts/new-package.sh, scripts/lint-specs.sh (shellcheck clean), docs/PACKAGING.md, .github/workflows/lint.yml
- Provided `system-release(releasever) = %{fedora}` per AGENT_README 3; dnf5 on this host already resolves releasever=44 from fedora-release, confirming the mechanism matches

## In progress
- <none>

## Blocked
- <none>

## Needs human
- Create the COPR project + webhook and enable fedora-44-x86_64 chroot (needs FAS login)
- Create/store GPG signing key

## TODO(verify)
- Exact COPR make_srpm variable names (outdir/spec/sources)
- LazyVim starter vendoring for /etc/skel/.config/nvim (planned M5)
