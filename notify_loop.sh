#!/bin/bash
while read line
do
	echo "$line" | notify.py
done
