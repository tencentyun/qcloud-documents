登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus)，创建 JAR 作业后，在【作业管理】中单击要进行开发的作业名称，然后单击【分析开发】即可在作业草稿中进行作业开发。

## 开发并使用 JAR 包

开发 JAR 作业需要先在本地开发并编译好 JAR 包，以程序包的形式上传后方可在控制台配置 JAR 作业（JAR 包上传请参考 [程序包管理-创建程序包](https://cloud.tencent.com/document/product/849/48295#.E5.88.9B.E5.BB.BA.E7.A8.8B.E5.BA.8F.E5.8C.85)）。在【配置信息】中选择主程序包及其版本，并输入主类和主类入参，完成参数设置，单击【保存】即可保存作业配置和参数信息。

目前流计算 Oceanus 支持运行基于开源 Flink V1.11 开发的 JAR 包，业务代码开发指南请参见 Flink 社区官方文档：[Flink DataStream API 开发指南 ](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/dev/datastream_api.html) 和 [Flink Table API & SQL 开发指南](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/dev/table/)。
![](https://main.qcloudimg.com/raw/f9c9d6646668242eb51f082910ecc61f.png)

## 参数说明

### 内置 Connector

由系统提供可让用户选择的 Connector，例如在 JAR 包中使用了来自 Ckafka 的数据流，则必须要在此处选择 Ckafka 相应的 connector。关于内置 Connector 的使用说明请参考 [上下游开发指南](https://cloud.tencent.com/document/product/849/48263)。

### 引用程序包

若用户有自定义函数的需求，可以自行开发 JAR 包并在【程序包管理】中上传后，方可在此添加引用程序包，并选择版本。

若前述的内置 Connector 无法满足需求，用户也可以自行开发自定义 Connector，以同样的方式上传并在此添加引用。自定义 Connector 的开发请参考 [自定义 Connector](https://cloud.tencent.com/document/product/849/48330)。

程序包的上传和版本管理方式请参考 [程序包管理](https://cloud.tencent.com/document/product/849/48295)。

### 算子默认并行度

当没有在 JAR 包中通过代码显式定义算子并行度时，作业将采用用户指定的算子默认并行度。1个并行度将占用1 CU 计算资源。

### 日志状态

显示当前地域的运行日志的开启状态，若要进行调整则需要到【诊断日志】>【运行日志】>【日志投递设置】中进行操作。详情可参考 [查看作业日志信息](https://cloud.tencent.com/document/product/849/48288) 中的开启运行日志。

