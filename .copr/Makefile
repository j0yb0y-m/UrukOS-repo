# COPR "make_srpm" entry point (method: make_srpm).
# COPR invokes: make srpm outdir=<dir> spec=<path> sources=<dir> opts=...
# Builds one package when `spec` is set, otherwise every packages/*/*.spec.

SPEC ?= $(shell ls packages/*/*.spec 2>/dev/null)

.PHONY: srpm spec

spec:
	@echo "Specs are static: see packages/<name>/<name>.spec"

srpm:
	mkdir -p $(outdir)
	@set -e; for s in $(SPEC); do \
		dir=$$(dirname $$s); \
		stage=$$(mktemp -d); \
		[ -d $$dir/files ] && cp -a $$dir/files/. $$stage/; \
		if [ -n "$(sources)" ]; then cp -a $(sources)/. $$stage/; fi; \
		if command -v spectool >/dev/null; then spectool -g -R $$s --define "_sourcedir $$stage" || true; fi; \
		rpmbuild -bs --define "_sourcedir $$stage" --define "_srcrpmdir $(outdir)" --define "_specdir $(outdir)" $$s; \
		rm -rf $$stage; \
	done
