## 前提条件
流计算作业 Python 作业需运行于流计算独享集群，若还没有集群，请参考 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。目前流计算 Oceanus 支持运行基于开源 Flink V1.13 开发的 Python 作业，且预装了 Python 3.7 版本的环境。

## 步骤1：Python 作业开发
创建 Python 作业需要上传已开发好的 Python 文件。

## 步骤2：上传 Python 文件
登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus)，选择**依赖管理 > 新建依赖**。在新建程序包中选择地域，该地域需与独享集群所在地域一致，默认使用本地上传的方式。单击**选择依赖**将打开本地文件选择窗口，选择步骤1中下载的 Python 文件并上传。填写程序包名称、程序包描述、版本说明后，单击**确定**完成新建程序包。完成新建后程序包列表将出现刚新建的程序包。
![](https://qcloudimg.tencent-cloud.cn/raw/e220757594242bf881c2bb84cda50c1a.png)

## 步骤3：创建 Python 作业
登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus)，进入某一工作空间后，单击左侧导航**作业管理**，进入作业管理页面，单击**新建作业**，作业类型选中 Python 作业，输入作业名称，并选择一个运行中的集群，新建的 Python 作业将运行于此集群，单击**确定**后即成功创建作业。
![](https://qcloudimg.tencent-cloud.cn/raw/def1ac6554ddea4681d76445b589aa1c.png)

## 步骤4：流计算服务委托授权
选择**作业管理**中刚新建的作业，单击**开发调试**。在未授权时，弹出访问授权对话框如下，单击**前往授权**，授权流计算作业访问您的 CKafka、TencentDB 等资源。此授权的详细说明参见 [流计算服务委托授权](https://cloud.tencent.com/document/product/849/38290)。
![](https://main.qcloudimg.com/raw/b92ca7251fa1cf4d4a617c07db7d3104.png)

## 步骤5：配置 Python 作业
在**开发调试**中，在**主程序包**的下拉框中选择刚才新建的程序包名称，在**入口类**输入对应的参数，如果入口类中有参数可以在**入口参数**中加上，目前 Oceanus 中内置了 Python 3.7 版本的环境，可以在 **Python 环境**中选择。您可以在**作业参数**设置中调整作业的算子默认并行度、添加外部依赖。
![](https://qcloudimg.tencent-cloud.cn/raw/394cecf93923886d2556e580bccbe96f.png)

## 步骤6：发布运行 Python 作业
单击**发布草稿**，将进行作业运行检查，检查通过后将进入发布确认。发布将生成新的作业版本，版本号由系统自动生成。
![](https://qcloudimg.tencent-cloud.cn/raw/1161e91b84df6e3dad88a770f8b61bba.png)
发布草稿后，单击**版本管理**，可以查看并切换当前作业的不同版本。
![](https://qcloudimg.tencent-cloud.cn/raw/88792bf7138682bc5dad52509afcdfb8.png)
切换到期望运行的作业版本后，单击**运行版本**，再单击**确认**即可启动作业。
![](https://qcloudimg.tencent-cloud.cn/raw/dcd4739f49c6385e5f7cbb65f29dd4fa.png)

## 步骤7：查看作业运行情况
作业发布并启动运行后，将变为操作中的状态，成功启动后将变为运行中的状态。作业运行中时，可以通过监控、日志、Flink UI 等功能查看作业运行的情况。·
