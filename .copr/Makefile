# COPR "make srpm" entry point (SCM source method, SRPM build method: make srpm).
# COPR invokes:  make -f .copr/Makefile srpm outdir="<outdir>" spec="<spec_path>"
# Runs in the cloned repo (or Subdirectory) inside a Fedora mock chroot.

SRCDIR := $(dir $(spec))files

srpm:
	mkdir -p $(outdir)
	which rpmbuild || dnf -y install rpm-build
	which spectool || dnf -y install rpmdevtools
	stage=$$(mktemp -d); \
	cp -a $(SRCDIR)/. $$stage/ 2>/dev/null || true; \
	spectool -g -R "$(spec)" --define "_sourcedir $$stage"; \
	rpmbuild -bs --define "_sourcedir $$stage" --define "_srcrpmdir $(outdir)" "$(spec)"; \
	rm -rf $$stage
