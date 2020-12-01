Apache Zeppelin 是一个可以进行大数据可视化分析的交互式开发系统，可以承担数据接入、数据发现、数据分析、数据可视化、数据协作等任务。其前端提供丰富的可视化图形库，不限于 SparkSQL；后端以插件扩展的方式支持 HBase、Flink 等大数据系统。在 Zeppelin 中还可以完成机器学习的数据预处理、算法开发和调试、算法作业调度的工作。

### 使用 spark 功能完成 wordcount
1. 单击页面左侧【Create new note】，在弹出页面中创建 notebook。
 ![](https://main.qcloudimg.com/raw/c31d7b714f22b1170d9c6799572227a3.png)
2. 配置 spark 对接 EMR 的集群（spark on yarn），修改并保存配置。
 ![](https://main.qcloudimg.com/raw/d617cf01e1175200596da85de252a7f2.png)
3. 进入自己的 notebook。
 ![](https://main.qcloudimg.com/raw/d56fe984a78c0f8f59498d2c24ee5b73.png)
4. 编写 wordcount 程序，并运行如下命令：
```
val data = sc.textFile("cosn://huanan/zeppelin-spark-randomint-test")
case class WordCount(word: String, count: Integer)
val result = data.flatMap(x => x.split(" ")).map(x => (x, 1)).reduceByKey(_ + _).map(x => WordCount(x._1, x._2))
result.toDF().registerTempTable("result")
%sql select * from result
```
![](https://main.qcloudimg.com/raw/8d70fcea7197c81e2d0235cab6d77843.png)
