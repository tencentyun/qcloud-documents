Spark组件是面向使用Scala/Java的Spark用户，用户编写Spark应用程序，编译打包成jar后，通过Spark组件完成部署。

使用阶段

1. 添加组件

从左边栏中，组件>机器学习 列表下拖拽出 Spark 节点至画布中。
![](https://main.qcloudimg.com/raw/bb66d7c90816da1ecc7010920ded2371.png)
 



2.参数配置

- 作业Jar包：
  通过该配置框上传你的Spark应用程序Jar包，必填项
- 主类名：
  指定你的Spark应用程序的入口类，即main函数所在的类，必填项
- 程序参数：
  指定你的Spark应用程序所需的参数，即传给main函数的参数，可选项
- 配置文件：
  指定你的Spark应用程序用到的配置文件，可选项
![](https://main.qcloudimg.com/raw/fd3b44eb42711ee6270cc4765d67d8a8.png)


3. 资源配置

  在 资源参数 列表配置任务的资源参数。

- num-executors：指定分配的Executor个数
- driver-memory：指定Driver需要的内存大小，单位为GB
- executor-cores：指定每个Executor上需要的cpu core数
- executor-memory：指定每个Executor上需要的内存大小，单位为GB
- spark-conf：指定Spark的属性参数，换行分割，例如 spark.default.parallelism=200
![](https://main.qcloudimg.com/raw/ee08ffcc7bc7c94e3db4bdc75ccf4790.png)


4. 运行

单击【保存】并运行工作流。



5. 查看 Spark 控制台和日志

在 Spark 节点上单击右键菜单可查看任务状态和详细日志。

     ![](https://main.qcloudimg.com/raw/956d37b9eb7634a1104db2be2d996244.png)

 




