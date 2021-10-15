#!/bin/bash

set -e

wget https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
tar -xvf spark-3.1.2-bin-hadoop3.2.tgz

git clone https://github.com/zjffdu/zeppelin_plugin.git
mkdir plugins
cp -r zeppelin_plugin/hooks plugins/
cp -r zeppelin_plugin/operators plugins/
