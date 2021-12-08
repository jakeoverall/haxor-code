#!/bin/bash

# Reset
Color_Off='\033[0m'       # Text Reset

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

printLabel(){
  printf "$Cyan[+]  $*  $Color_Off \n"
}
printData(){
  printf "$Green    [~] $* $Color_Off \n"
}

printSysInfo(){

  printf "$Yellow [+] Evaluating this computer $Color_Off\n"
  printf "$Yellow ___________________________________________ $Color_Off\n"
  printLabel "Computer Name: $Purple $(lshw | grep "" -m1)" 
  printLabel "CPU:"
  printData $(lshw | grep "*-cpu" -A 5)
  printLabel "RAM:"
  printData $(lshw | grep "*-memory" -A 3)
  printLabel "Network Adapter:"
  printf "$Red $(lshw | grep "*-network")"
  printf "\n\n$Yellow[+] Evaluation complete.$Color_Off\n\n"
}

printSysInfo