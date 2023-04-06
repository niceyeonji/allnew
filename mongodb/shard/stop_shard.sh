#!/bin/bash

config=$(ps -ef | grep 'mongodConfig')
router=$(ps -ef | grep 'mongodRouter')
shard1=$(ps -ef | grep 'mongodShard1')
shard2=$(ps -ef | grep 'mongodShard2')

second1=$(echo ${config} | cut -d " " -f2)
second2=$(echo ${router} | cut -d " " -f2)
second3=$(echo ${shard1} | cut -d " " -f2)
second4=$(echo ${shard2} | cut -d " " -f2)

for var in $second1 $second2 $second3 $second4
do
	echo $var
	if [ -n ${var} ]; then
		result=$(kill -9 ${var})
		echo process is killed.
	else
		echo running process not found.
	fi
done
