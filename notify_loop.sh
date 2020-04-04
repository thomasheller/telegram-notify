#!/bin/bash
while read line
do
	echo "$line" | sed 's/§/\n/g' | notify.py
done
