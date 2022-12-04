#!/bin/bash
#Creator E-manuel Manzanarez Mora 1948116

os=$(awk -F= '/^NAME/{print $2}' /etc/os-release)

if [ "$os" == '"CentOS Linux"' ]
then
    echo $os
    sudo yum -y update
    #sudo yum -y install clamav
    rpm=$(sudo rpm -q clamav)
    if [ "$rpm" == "package clamav is not installed" ]
    then
      sudo yum -y install clamav
    fi
    if [ "$rpm" != "package clamav is not installed" ]
    then
      echo "removing clamav"
      sudo systemctl stop clamav-freshclam
      sudo yum -y remove clamav
      sudo yum -y install clamav
      echo "clamav installed"
      fi
fi

if [ "$os" == '"Ubuntu"' ]
then
    echo $os
    sudo apt-get upgrade -y

    wi=$(sudo whereis clamav)
    if [ "$wi" != "clamav: /etc/clamav" ]
    then
      echo Installing clamav...
      sudo apt-get install clamav clamav-daemon
      echo Clamav instaled
    fi
    if [ "$wi" == "clamav: /etc/clamav" ]
    then
      echo "Removing clamav..."
      sudo systemctl stop clamav-freshclam -y
      sudo apt-get autoremove clamav clamav-daemon -y
      sudo apt-get install clamav clamav-daemon -y
      echo "FINISHED. Clamav installed"
      fi

fi
