#!/usr/bin/env bash
var="$(wc -l BLACKBOX_INPUT/input.txt | cut -d " " -f1)"
var="$(echo "scale=0 ; $var / 2500" | bc)"
#echo $var
bin/mgfsm  -i BLACKBOX_INPUT/ -o OUTPUT/ -s $var -g 0 -l 70 -m s
