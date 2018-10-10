#./bin/spark-submit Tarefa03.py

from pyspark import SparkContext, SparkConf
import csv

conf = SparkConf().setAppName('Tarefa03')
sc = SparkContext(conf=conf)

vote_file = sc.textFile("/tmp/data/votacao_secao_2014_SP.txt")

votes = vote_file.mapPartitions(lambda row: csv.reader(row, delimiter=';')) \
            .filter(lambda line : "3" in line[11]) \
            .map(lambda line : (line[13], int(line[14]))) \
            .reduceByKey(lambda a, b: a+b) \
            .sortBy(lambda d: d[1],ascending=False) \
            .collect()

for v in votes:
    print (v)
