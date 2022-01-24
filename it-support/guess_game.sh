#! /usr/bin/bash
# TODO fix stupid bash
num = "10"

function play(){
  echo "Can you guess my number"
  guess = read

  if [[ $guess -eq $num ]] then 
    echo "Great Job"
    exit
  elif [[ $guess -gt $num ]] then 
    echo "Nope to high"
  else 
    echo "Nope to Low"
  play()
}

play()