#!/usr/bin/env bash

$OS = "${uname}"

if [["$OS" == "Linux"]]; then
  ifconfig
else
  ipconfig
fi

read -p "All done"
