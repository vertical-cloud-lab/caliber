#!/usr/bin/env bash
# Run a DTSA-II Jython script without a display: NIST DTSA-II "Polaris" (2026-09-10, epq 15.1.57)
# started with --script under Xvfb. Installs DTSA-II and a Linux Java 26 runtime on first use.
# Usage: ./run_dtsa2.sh <script.py>   (scripts read NAB_DATA and NAB_OUT from the environment)
set -euo pipefail
DTSA2_HOME="${DTSA2_HOME:-/tmp/dtsa2}"
JAVA26="${JAVA26:-/tmp/jre26/jdk-26.0.2.1+1-jre/bin/java}"
if [ ! -x "$JAVA26" ]; then
  mkdir -p /tmp/jre26
  curl -sSL "https://api.adoptium.net/v3/binary/latest/26/ga/linux/x64/jre/hotspot/normal/eclipse" | tar xz -C /tmp/jre26
  JAVA26=$(ls -d /tmp/jre26/*/bin/java | head -1)
fi
if [ ! -f "$DTSA2_HOME"/dtsa2-*.jar ]; then
  mkdir -p /tmp/dtsa2dl
  curl -sSL -o /tmp/dtsa2dl/dtsa2_polaris.jar "https://cstl.nist.gov/div837/837.02/epq/dtsa2/dtsa2_polaris.jar"
  printf 'INSTALL_PATH=%s\n' "$DTSA2_HOME" > /tmp/dtsa2dl/opts.properties
  java -Djava.awt.headless=true -jar /tmp/dtsa2dl/dtsa2_polaris.jar -options /tmp/dtsa2dl/opts.properties
fi
# DTSA-II asks for a report folder on first start; pre-set it so no dialog blocks the script.
prefs="$HOME/.java/.userPrefs/gov/nist/microanalysis/dtsa2/prefs.xml"
if ! grep -q 'key="Base Path"' "$prefs" 2>/dev/null; then
  mkdir -p "$(dirname "$prefs")" /tmp/dtsa2reports
  printf '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<!DOCTYPE map SYSTEM "http://java.sun.com/dtd/preferences.dtd">\n<map MAP_XML_VERSION="1.0">\n  <entry key="Base Path" value="/tmp/dtsa2reports"/>\n</map>\n' > "$prefs"
fi
xvfb-run -a -s "-screen 0 1600x1200x24" "$JAVA26" --enable-preview --enable-native-access=ALL-UNNAMED -Dderby.stream.error.file=/tmp/derby.log \
  -jar "$DTSA2_HOME"/dtsa2-*.jar --script "$(readlink -f "$1")"
