#!/bin/bash

comandos=(
 "hdfs dfs -mkdir /user"
 "hdfs dfs -mkdir /user/hduser"
 "hdfs dfs -mkdir input"
 "sudo chown -R hduser ."
 "cd proyecto/"
 "python api.py"
 "hdfs dfs -put */*.txt input"
 "hdfs dfs -ls input"
 "mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output hduser/outhadoop/ -mapper ./mapper.py -reducer ./reducer.py"
 "hdfs dfs -get /user/hduser/hduser/outhadoop/ /home/hduser/proyecto"
 "python buscador.py"
)

for comando in "${comandos[@]}"; do
    echo "Ejecutando comando: $comando"
    $comando
    echo "=================================================="
done
