#!/bin/bash

a=1

while [ $a != "0" ]; do
	echo -n "input : "
	read a
		
	if [ $a -eq 0 ]; then
		break;
	elif [ $a -eq 1 ]; then
		echo "The number of inputs must be between 2 and 9."
	elif [ $a -gt 9 ]; then
		echo "The number of inputs must be between 2 and 9."
	else
		for ((k=1; k<=9; k++)) do
			echo "$a * $k = `expr $a \* $k `"
		done
	fi
done
echo Exit
