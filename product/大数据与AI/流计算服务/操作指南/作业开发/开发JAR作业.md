## 前提条件
流计算作业需运行于流计算独享集群，若还没有集群，请参考 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。

## 创建作业
在 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus)【作业管理】中单击【新建作业】，在弹窗中选择作业类型、作业名称和运行集群，单击【确定】后即可在作业列表中看到新建的作业。
![](https://main.qcloudimg.com/raw/8e352c21f7457587d35f6b7c2c592312.png)

创建 JAR 作业后，在【作业管理】中单击要进行开发的作业名称，然后单击【开发调试】，即可在草稿状态下进行作业开发。【版本管理（草稿）】后的“（草稿）”，即表示当前正处于可编辑的草稿状态下。

## 开发并使用 JAR 包
开发 JAR 作业需要先在本地开发并编译好 JAR 包，以程序包的形式上传后方可在控制台配置 JAR 作业（JAR 包上传可参考 [程序包管理-创建程序包](https://cloud.tencent.com/document/product/849/48295#.E5.88.9B.E5.BB.BA.E7.A8.8B.E5.BA.8F.E5.8C.85)）。在【开发调试】页面中选择主程序包及其版本，并输入主类和主类入参，单击【作业参数】并在侧边弹出的参数界面中设置参数值，然后单击【保存】保存作业配置和参数信息。

目前流计算 Oceanus 支持运行基于开源 Flink V1.11 开发的 JAR 包，业务代码开发指南请参见 Flink 社区官方文档：[Flink DataStream API 开发指南 ](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/dev/datastream_api.html)和 [Flink Table API & SQL 开发指南](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/dev/table/)。

![](https://main.qcloudimg.com/raw/98f8206dc6b069d2c41ee6caf789ca53.png)

## 作业参数
作业参数可以在【开发调试】页面中点击【作业参数】并在侧边弹出的参数界面中设置参数值，然后单击【确定】保存作业参数信息。下文会有各参数的详细介绍说明，以帮助您更好地配置各作业参数。
![](https://main.qcloudimg.com/raw/e66238a9e09f37a19558240f469de5b1.png)

### 引用程序包
若用户有自定义函数的需求，可以自行开发 JAR 包并在【程序包管理】中上传后，方可在此添加引用程序包，并选择版本。

若内置 Connector 无法满足需求，可自行开发自定义 Connector，以同样的方式上传并在此添加引用。自定义 Connector 的开发可参考 [自定义 Connector](https://cloud.tencent.com/document/product/849/48330)。

程序包的上传和版本管理方式请参考 [程序包管理](https://cloud.tencent.com/document/product/849/48295)。

### 内置 Connector
由系统提供可让用户选择的 Connector。例如，在 JAR 包中使用了来自 Ckafka 的数据流，则必须要在此处选择 Ckafka 相应的 connector。内置 Connector 的使用说明可参考 [上下游开发指南](https://cloud.tencent.com/document/product/849/48263)。

### 运行日志采集
显示当前作业的运行日志的开启状态，默认为开启。作业的运行日志将自动采集到作业所在的集群绑定的日志集和日志主题，可在【日志】页面中查看。关闭或重新打开都需重启作业才能生效。

### 高级参数
支持部分 Flink 高级参数自定义，需按照 YML 语法，并以“key: value”的形式进行配置，详情可参考 [作业高级参数](https://cloud.tencent.com/document/product/849/53391)。 

### 规格配置
可以按需配置 JobManager 和 TaskManager 的规格大小，灵活运用资源，详情可参考 [作业资源配置](https://cloud.tencent.com/document/product/849/57772)。

### 算子默认并行度

当没有在 JAR 包中通过代码显式定义算子并行度时，作业将采用用户指定的算子默认并行度。并行度与TaskManager 规格大小决定作业所占用的计算资源。1个并行度将占用1 个 TaskManager  规格大小的CU 计算资源（当 TaskManager 规格大小为1时，1个并行度将占用1 CU 计算资源。当 TaskManager 规格大小为0.5时，1个并行度将占用0.5 CU 计算资源）。

