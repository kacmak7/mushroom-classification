#!/bin/bash

path=data_bool.csv

cp data.csv $path
find ./ -type f -name $path | xargs sed -i -e 's/0/false/g'
find ./ -type f -name $path | xargs sed -i -e 's/1/true/g'

