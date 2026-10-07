#!/bin/bash
# rpmlint every spec in packages/
set -euo pipefail
cd "$(dirname "$0")/.."
fail=0
for s in packages/*/*.spec; do
	echo "== $s =="
	rpmlint "$s" || fail=1
done
exit $fail
