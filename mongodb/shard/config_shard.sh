#!/bin/bash

# default mongodb daemon stop.
systemctl stop mongod

# remove data directory
if [ -d data ]; then
    rm -rf ./data
fi

# config Server
mkdir -pv /shard/data/configdb
mkdir -pv /shard/data/logs
touch /shard/data/logs/configsvr.log

mongod --config /shard/mongodConfig.conf &
sleep 3s

mongo 192.168.1.51:27019 < mongo_rs
sleep 3s

# router Server
touch /shard/data/logs/mongorouter.log

mongos --config /shard/mongodRouter.conf &
sleep 3s

# shard1 Server
mkdir -pv /shard/data/shard1db
touch /shard/data/logs/shard1.log

mongod --config /shard/mongodShard1.conf &
sleep 1s

# shard2 Server
mkdir -pv /shard/data/shard2db
touch /shard/data/logs/shard2.log

mongod --config /shard/mongodShard2.conf &
sleep 1s

# process status
ps -ef | grep mongo
sleep 2s

#netstatus
netstat -ntlp