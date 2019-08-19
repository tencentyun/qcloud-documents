## 操作场景
Spark 组件是面向使用 Scala/Java 的 Spark 用户，用户编写 Spark 应用程序并编译打包成 jar 后，可通过 Spark 组件完成部署。

## 操作步骤
1. **添加组件**
从左侧菜单栏中，选择【组件】>【机器学习】列表下的 Spark 节点，并将其拖拽至画布中。
2. **配置参数**
 - 作业 Jar 包：通过该配置框上传您的 Spark 应用程序 Jar 包，必填项。
 - 主类名：指定您的 Spark 应用程序的入口类，即 main 函数所在的类，必填项。
 - 程序参数：您的 Spark 应用程序所需的参数，即传给 main 函数的参数，可选项。
 - 配置文件：指定您的 Spark 应用程序用到的配置文件，可选项。
![](https://main.qcloudimg.com/raw/fd3b44eb42711ee6270cc4765d67d8a8.png)
3. **配置资源**
  在资源参数列表配置任务的资源参数。
 - num-executors：指定分配的 Executor 个数。
 - driver-memory：指定 Driver 需要的内存大小，单位为 GB。
 - executor-cores：指定每个 Executor 上需要的 CPU Core 数。
 - executor-memory：指定每个 Executor 上需要的内存大小，单位为GB。
 - spark-conf：指定 Spark 的属性参数，换行分割，例如 spark.default.parallelism=200。
![](https://main.qcloudimg.com/raw/ee08ffcc7bc7c94e3db4bdc75ccf4790.png)
4. **运行**
单击【保存】并运行工作流。
5. **查看 Spark 控制台和日志**
在 Spark 节点上单击右键菜单，可查看任务状态和详细日志。
