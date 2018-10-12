# INF0617_Tarefa3

copy map_votes.py to your /data folder
copy reduce_votes.py to your /data folder

$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
    -D stream.reduce.output.field.separator=" " \
    -D stream.num.reduce.output.key.fields=2 \
    -D reduce.output.key.field.separator=" " \
    -D mapreduce.partition.keycomparator.options=-k2,2nr \
    -input /tmp/data/votes \
    -output /tmp/data/votes_out \
    -mapper "python map_votes.py" \
    -reducer "python reduce_votes.py"
    
$HADOOP_HOME/bin/hdfs dfs -cat /tmp/data/votes_out/part-00000 | sort -k2nr


# resultado da eleições

https://pt.wikipedia.org/wiki/Elei%C3%A7%C3%B5es_estaduais_em_S%C3%A3o_Paulo_em_2014

http://www.tse.jus.br/eleicoes/estatisticas/eleicoes/eleicoes-anteriores/estatisticas-candidaturas-2014/estatisticas-eleitorais-2014-resultados
