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

## Note
25/04/2023: The bangkok_traffy.csv now use in local, we will update later. You can download raw data from 

https://publicapi.traffy.in.th/dump-csv-chadchart/bangkok_traffy.csv
