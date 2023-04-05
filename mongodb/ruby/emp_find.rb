#!/usr/bin/ruby

require 'rbygem'
require 'mongo'

$client = Mongo::Client.new(['0.0.0.0:27017'], :database => 'ruby')
Mongo::Logger.logger.level = ::Logger::ERROR
$emp = $client[:emp]
puts 'connected!'

cursor = $emp.find()
cursor.each do | doc |
    puts doc
end