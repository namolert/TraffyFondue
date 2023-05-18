## Pyspark
• Linux and mac:
  https://medium.com/@GalarnykMichael/install-spark-on-ubuntu-pyspark-231c45677de0
  
• Windows:
  https://medium.com/@GalarnykMichael/install-spark-on-windows-pyspark-4498a5d8d66c
  
• Using pip (Linux, mac, and windows):
  http://sigdelta.com/blog/how-to-install-pyspark-locally/
  
## If you run in Colab, run this code first
```
try:
  import google.colab
  IN_COLAB = True
except:
  IN_COLAB = False
  
if IN_COLAB:
    !apt-get install openjdk-8-jdk-headless -qq > /dev/null
    !wget -q https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz
    !tar xf spark-3.3.2-bin-hadoop3.tgz
    !mv spark-3.3.2-bin-hadoop3 spark
    !pip install -q findspark
    import os
    os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
    os.environ["SPARK_HOME"] = "/content/spark"
```

## If you want to save spark model with mlflow, you should set HADOOP_HOME
### for hadoop configuration, modify XML file in pathtohadoop\etc\hadoop
core-site.xml
```
<configuration>
 <property>
  <name>fs.default.name</name>
  <value>hdfs://localhost:9000</value>
 </property>
</configuration>
```
yarn-site.xml
```
<configuration>
 <property>
  <name>yarn.nodemanager.aux-services</name>
  <value>mapreduce_shuffle</value>
 </property>
 <property>
  <name>yarn.nodemanager.auxservices.mapreduce.shuffle.class</name>
  <value>org.apache.hadoop.mapred.ShuffleHandler</value>
 </property>
</configuration>
```
hdfs-site.xml
```
<configuration>
 <property>
  <name>dfs.replication</name>
  <value>1</value>
 </property>
 <property>
  <name>dfs.namenode.name.dir</name>
  <value>file:///C:/hadoop-3.3.5/data/namenode</value>
 </property>
 <property>
  <name>dfs.datanode.data.dir</name>
  <value>file:///C:/hadoop-3.3.5/data/datanode</value>
 </property>
</configuration>
```
mapred-site.xml
```
<configuration>
 <property>
  <name>mapreduse.framework.name</name>
  <value>yarn</value>
 </property>
</configuration>
```
hadoop-env.cmd
```
<!-- set to your own java path -->
set JAVA_HOME=C:\Java\jdk-20
```


## Note
25/04/2023: The bangkok_traffy.csv now use in local, we will update later. You can download raw data from 

https://publicapi.traffy.in.th/dump-csv-chadchart/bangkok_traffy.csv
