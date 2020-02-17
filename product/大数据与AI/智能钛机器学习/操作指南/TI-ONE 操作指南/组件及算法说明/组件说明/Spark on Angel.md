凭借 Angel 强大的 PS Service 能力，Spark on Angel 扩展了 Spark 的参数更新能力，使 Spark 也具备高速训练大模型的能力而不用再顾虑 Spark Driver 的单点性能问题。
Spark on Angel 组件一般用来运行用户自己实现的算法，如果需要运行 Spark on Angel 自带算法，建议您使用各个算法对应的算法组件。

## 操作步骤
1. **添加组件**
从左侧菜单栏中，选择【框架】>【机器学习】列表下的【Spark on Angel 】节点，并将其拖拽至画布中。
2. **配置参数**
 - 作业 Jar 包：通过该配置框上传您的 Spark on Angel 应用程序 Jar 包，必填项。
 - 主类名：指定您的 Spark on Angel 应用程序的入口类，即 main 函数所在的类，必填项。
 - 程序参数：您的 Spark on Angel 应用程序所需的参数，即传给 main 函数的参数，可选项。
 - 配置文件：指定您的 Spark on Angel 应用程序用到的配置文件，可选项。
3. **配置资源**
 - Spark 资源参数
    - num-executors：指定分配的计算节点数目。
    - driver-memory：指定主节点内存大小，上限为14GB。
    - executor-cores：指定每个子节点分配的 CPU Core 数，推荐 2 - 3。
    - executor-memory：指定每个子节点分配的内存大小，上限为55GB，推荐单个 core 分配2 - 3GB。
    - spark-conf：指定 Spark 常用参数配置，如压缩、序列化、网络等。例如 spark.cores.max=1000。 
 - Angel 资源参数
    - spark.ps.instances：angel ps 个数，可根据模型大小来配置，一般模型越大，需要的 ps 个数越多。
    - spark.ps.cores：每个 angel ps 需要的核数。
    - spark.ps.memory(g)：每个 angel ps 需要的内存，单位为 GB。
4. **运行**
单击【保存】并运行工作流。
5. **查看 Spark 控制台和日志**
在 Spark on Angel 节点上单击右键菜单，可查看任务状态和详细日志。 
