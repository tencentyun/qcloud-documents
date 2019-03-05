
Spark组件是面向使用Scala/Java的Spark用户，用户编写Spark应用程序，编译打包成jar后，通过Spark组件完成部署。

1.从左侧组件列表里拖拽出一个Spark节点


![](https://main.qcloudimg.com/raw/2061d016fdeaeb0131476fe357763387.png) 

2.单击任务节点，会从右侧弹出配置框


![](https://main.qcloudimg.com/raw/8ffb25a474b1d4382917bfc6451c12c8.png)

> * 作业Jar包：通过该配置框上传你的Spark应用程序Jar包，必填项
> * 主类名：指定你的Spark应用程序的入口类，即main函数所在的类，必填项
> * 程序参数：指定你的Spark应用程序所需的参数，即传给main函数的参数，可选项
> * 配置文件：指定你的Spark应用程序用到的配置文件，可选项
> * num-executors：指定分配的Executor个数
> * driver-memory：指定Driver需要的内存大小，单位为GB
> * executor-cores：指定每个Executor上需要的cpu core数
> * executor-memory：指定每个Executor上需要的内存大小，单位为GB
> * spark-conf：指定Spark的属性参数，换行分割，例如 spark.default.parallelism=200

3.配置完毕后，即可右键启动运行

![](https://main.qcloudimg.com/raw/05070bd6a76c7a0e9183457a992b85e3.png) 


4.运行过程中可以通过"右键->Spark控制台" 查看日志（日志查看具体的方法见日志章节）。

 ![](https://main.qcloudimg.com/raw/ed78a8edd3ee61c9f199e1e9804a04af.png) 

 Spark控制台与日志
 ![](https://main.qcloudimg.com/raw/680a3e2096c3f133ecfab0060ae3bdbe.png)

