#!/usr/bin/env bash
var="$(wc -l BLACKBOX_INPUT/input.txt | cut -d " " -f1)"
var="$(echo "scale=0 ; $var / 10" | bc)"
#echo $var
bin/mgfsm  -i BLACKBOX_INPUT/ -o SAMPLE_OUTPUT/ -s $var -g 0 -l 15 -m s
