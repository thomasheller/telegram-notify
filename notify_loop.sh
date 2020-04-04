#!/bin/bash
while read line
do
	echo "$line" | tr '§' '\n' | notify.py
done
