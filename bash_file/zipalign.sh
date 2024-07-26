#!/bin/bash
sudo apt update
sudo apt --purge remove zipalign -y
wget http://ftp.de.debian.org/debian/pool/main/a/android-platform-build/zipalign_8.1.0+r23-2_amd64.deb
chmod +x zipalign_8.1.0+r23-2_amd64.deb
sudo apt install ./zipalign_*_amd64.deb -y
