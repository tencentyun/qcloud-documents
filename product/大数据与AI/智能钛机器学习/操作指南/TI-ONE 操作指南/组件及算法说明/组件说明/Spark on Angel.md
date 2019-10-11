凭借 Angel 强大的 PS Service 能力，Spark on Angel 扩展了 Spark 的参数更新能力，使 Spark 也具备高速训练大模型的能力而不用再顾虑 Spark Driver 的单点性能问题。
Spark on Angel 组件一般用来运行用户自己实现的算法，如果需要运行 Spark on Angel 自带算法，建议使用各个算法对应的算法组件。

## 操作步骤
#### 添加组件
从左侧菜单栏中，选择【框架】>【机器学习】列表下的  Spark on Angel 节点，并将其拖拽至画布中。
![](https://main.qcloudimg.com/raw/b725cc0f37253fccb2d772332c56dd94.png)

#### 配置参数
 - 作业 Jar 包：通过该配置框上传您的 Spark on Angel 应用程序 Jar 包，必填项。
 - 主类名：指定您的 Spark on Angel 应用程序的入口类，即 main 函数所在的类，必填项。
 - 程序参数：您的 Spark on Angel 应用程序所需的参数，即传给 main 函数的参数，可选项。
 - 配置文件：指定您的 Spark on Angel 应用程序用到的配置文件，可选项。
 ![](https://main.qcloudimg.com/raw/cdf170de016b90d0244e9db963666d07.png)

#### 配置资源
 - Spark 资源参数
 - num-executors：指定分配的 Spark Executor 个数。
 - driver-memory：指定 Spark Driver 需要的内存大小，单位为 GB。
 - executor-cores：指定每个 Spark Executor 上需要的 CPU Core 数。
 - executor-memory：指定每个 Spark Executor 上需要的内存大小，单位为 GB。
 - spark-conf：指定 Spark 和 Angel 的属性参数，换行分割，例如 spark.default.parallelism = 200。
![](https://main.qcloudimg.com/raw/f5b649e6ff1c8119790592beb881b65a.png)
 - Angel 资源参数
 - spark.ps.instances：angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 ps 个数越多。
 - spark.ps.cores：每个 angel ps 需要的核数。
 - spark.ps.memory(g)：每个 angel ps 需要的内存，单位为 GB。
![](https://main.qcloudimg.com/raw/6949d4aa3a6dfe00534a2a659e147ce8.png)

#### 运行
单击【保存】并运行工作流。
![](https://main.qcloudimg.com/raw/64e526a96e6f3eb962a0259502ffcd00.png)

#### 查看 Spark 控制台和日志
在 Spark on Angel 节点上单击右键菜单，可查看任务状态和详细日志。
![](https://main.qcloudimg.com/raw/28a44e8ff8f2a05edf35b9e81fda9a60.png) 
