#!/bin/bash

a=1

while [ $a != "0" ]; do
	echo -n "input : "
	read a

	if [ $a != "0" ]; then
		for k in 1 2 3 4 5 6 7 8 9
		do
			echo " $a * $k = `expr $a \* $k `"
		done
	fi
done
echo Exit
