#!/bin/bash
sudo apt update
curl https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool > apktool
wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.9.3.jar
mv apktool_2.9.3.jar apktool.jar
chmod +x apktool apktool.jar
sudo apt purge apktool -y
sudo mv apktool apktool.jar /usr/local/bin
