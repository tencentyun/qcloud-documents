## 前提条件
流计算作业需运行于流计算独享集群，若还没有集群，请参考 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。

## 创建作业
在 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus) 中选择**作业管理 > 新建作业**，在弹窗中选择作业类型、作业名称和运行集群，单击**确定**，即可在作业列表中看到新建的作业。
![-w548](https://mweb-1306209138.cos.ap-guangzhou.myqcloud.com/2022/03/02/16462223928030.jpg)
创建 Python 作业后，在**作业管理**中单击要进行开发的作业名称，然后单击**开发调试**，即可在草稿状态下进行作业开发。

## 开发 Python 作业
Python 作业的开发页面如下所示：
![-w670](https://mweb-1306209138.cos.ap-guangzhou.myqcloud.com/2022/03/02/16462233233114.jpg)
开发 Python 作业需要先在本地编写好 Python 文件或者打包好 Zip 程序包，以 Python 程序包的形式上传后方可在控制台配置 Python 作业（Python 程序包上传可参考 [依赖管理](https://cloud.tencent.com/document/product/849/48295)）。

![-w797](https://mweb-1306209138.cos.ap-guangzhou.myqcloud.com/2022/03/02/16462230999136.jpg)

在**开发调试**页面，选择主程序包及其版本，并输入入口类和入口类参数，选择好平台提供的 Python 环境，单击**作业参数**并在侧边弹出的参数界面中设置参数值，然后单击**保存**，保存作业配置和参数信息。
主程序包可以是单独的 Python 文件或者是 zip 程序包。如果主程序包为 Python 文件，则入口类不需要填写；主程序包为 Zip，则需要指定其入口类，如下图所示：
![-w712](https://mweb-1306209138.cos.ap-guangzhou.myqcloud.com/2022/03/02/16462229073302.jpg)
数据文件会被解压到 Python worker 进程的工作目录下。如果数据文件所在的压缩包名称为 archive.zip，则在 Python 自定义函数中可以编写以下代码来访问 archive.zip 数据文件。
```
def my_udf():  
        with open("archive.zip/mydata/data.txt") as f: 
        ...
```
	 
### 使用限制
目前流计算 Oceanus 支持运行基于开源 Flink V1.13 开发的 Python 作业，且预装了 Python 3.7 版本的环境。业务代码开发指南请参见 Flink 社区官方文档：[Flink Python API 开发指南](https://nightlies.apache.org/flink/flink-docs-master/zh/docs/dev/python/overview/)。

## 作业参数
作业参数可以在**开发调试**页面中单击**作业参数**，并在侧边弹出的参数界面中设置参数值，然后单击**确定**，保存作业参数信息。下文会有各参数的详细介绍说明，以帮助您更好地配置各作业参数。
![](https://main.qcloudimg.com/raw/e66238a9e09f37a19558240f469de5b1.png)

### 内置 Connector
由系统提供可让用户选择的 Connector。例如，在 Python 作业中需要使用来自 Ckafka 的数据流，则必须要在此处选择 Ckafka 相应的 connector。内置 Connector 的使用说明可参考 [上下游开发指南](https://cloud.tencent.com/document/product/849/48263)。

### 运行日志采集
显示当前作业的运行日志的开启状态，默认为开启。作业的运行日志将自动采集到作业所在的集群绑定的日志集和日志主题，可在**日志**页面中查看。关闭或重新打开都需重启作业才能生效。

### 高级参数
支持部分 Flink 高级参数自定义，需按照 YML 语法，并以“key: value”的形式进行配置，详情可参考 [作业高级参数](https://cloud.tencent.com/document/product/849/53391)。 

### 规格配置
可以按需配置 JobManager 和 TaskManager 的规格大小，灵活运用资源，详情可参考 [作业资源配置](https://cloud.tencent.com/document/product/849/57772)。

### 算子默认并行度

当没有在 JAR 包中通过代码显式定义算子并行度时，作业将采用用户指定的算子默认并行度。并行度与 TaskManager 规格大小决定作业所占用的计算资源。1 个并行度将占用 1 个 TaskManager 规格大小的CU 计算资源（当 TaskManager 规格大小为 1 时，1 个并行度将占用 1 CU 计算资源。当 TaskManager 规格大小为 0.5时，1个并行度将占用 0.5 CU 计算资源）。
