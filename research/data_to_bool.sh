#!/bin/bash
find ./ -type f -name "data.csv" | xargs sed -i -e 's/0/false/g'
find ./ -type f -name "data.csv" | xargs sed -i -e 's/truei/true/g'
