#!/bin/bash

mongod --config /shard/mongodConfig.conf &
mongos --config /shard/mongodRouter.conf &
sleep 3s

mongod --config /shard/mongodShard1.conf &
mongod --config /shard/mongodShard2.conf &
sleep 2s

ps -ef | grep mongo
sleep 3s
netstat -ntlp
