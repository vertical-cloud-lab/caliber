#!/usr/bin/env bash
# Headless install of NIST DTSA-II Polaris plus the programmatic quant demo.
# Requires a Java 24+ JDK (GitHub Actions runners ship /usr/lib/jvm/temurin-25-jdk-amd64).
# Usage: scripts/dtsa2_headless_setup.sh [spectrum.msa]
set -euo pipefail

JAVA="${JAVA:-/usr/lib/jvm/temurin-25-jdk-amd64/bin/java}"
DTSA2_HOME="${DTSA2_HOME:-$HOME/dtsa2}"
INSTALLER=/tmp/dtsa2_Polaris.jar

[ -f "$INSTALLER" ] || curl -sS -o "$INSTALLER" https://www.cstl.nist.gov/div837/837.02/epq/dtsa2/dtsa2_Polaris.jar

# IzPack 5 console-mode answers, in prompt order: continue, accept licence,
# install path, OK to create dir, continue, include 'NIST DTSA-II Application',
# skip 'NIST Relocation Application', continue, no auto-install script, finish.
[ -d "$DTSA2_HOME" ] || printf '1\n1\n%s\nO\n1\nY\nN\n1\nN\n1\n' "$DTSA2_HOME" | "$JAVA" -jar "$INSTALLER" -console

exec "$JAVA" -Djava.awt.headless=true --enable-native-access=ALL-UNNAMED \
  -Dpython.cachedir.skip=false -Dpython.cachedir=/tmp/jython-cache \
  -cp "$DTSA2_HOME/*" org.python.util.jython \
  "$(dirname "$0")/dtsa2_headless_demo.py" "$@"
