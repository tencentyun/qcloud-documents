在 Spark 安装目录下通过如下命令提交任务

<pre>
./bin/spark-submit examples/demo/wordcount.py cosn://bucketname/example/source/people.txt
</pre>

任务运行结果会直接打印到控制台

```
Justin,: 1
Michael,: 1
19: 1
30: 1
29: 1
Andy,: 1
```

任务结束后，可以通过如下命令看到 Spark 运行日志（注意替换您的任务 ID）

``` 
/usr/localrvice/hadoop/bin/yarn logs -applicationId application_1489458311206_10547
```
