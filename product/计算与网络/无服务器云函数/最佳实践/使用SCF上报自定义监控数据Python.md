## 操作背景
云函数（SCF）可帮助您在无需购买和管理服务器的情况下运行代码。SCF 的配套监控功能已覆盖自身的指标监控，例如函数被调用次数、错误次数、消耗内存等。
自定义监控可以帮助您监控业务逻辑，例如某个逻辑错误的次数、红包活动中用户发送红包的数量、领取红包的数量等。您可以直接在代码内打点上报业务指标，自动汇聚后实时生成监控图表，也可以针对上报指标配置告警，查看指标趋势变化。

本文介绍了如何使用 SCF 上报数据至自定义监控、查看指标及配置告警。

## 示例逻辑
每次请求判断是否存在 `key1` 字符传入：
 - 是，则成功次数 (suc_counts)+1。
 - 否，则失败次数 (fail_counts)+1。


##  前提条件
- 了解 [云函数](https://cloud.tencent.com/document/product/583)，或直接参考示例代码。
- 已具备一台设备用于构建项目及打包代码，且该设备已安装 Python 2.7。您可参考 [安装 Python 及 pip](https://cloud.tencent.com/document/product/583/33449#.E5.AE.89.E8.A3.85-python-.E5.8F.8A-pip) 安装所需环境。
本文以操作系统为 CentOS 的 [腾讯云服务器](https://cloud.tencent.com/product/cvm) 为例。



##  操作步骤
### 步骤1：新建本地项目
1. [登录云服务器](https://cloud.tencent.com/document/product/213/5436)，执行以下命令进入 `/data` 目录。
```
cd /data
```
2. 执行以下命令，新建项目 `MyProject`。
```
mkdir MyProject
```

### 步骤2：编写业务逻辑
进入 `MyProject` 目录，新建 `index.py` 文件并写入以下内容：
```
# -*- coding: utf8 -*-
import time
import urllib2
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.monitor.v20180724 import monitor_client, models
#自定义监控初始化函数，指定region和secrecId、secretKey
def MONITOR(secretId,secretKey):
    try:
        # 获取region地区，这里填写云函数所在的地域
        region = "ap-guangzhou"

        cred = credential.Credential(secretId,secretKey )

        client = monitor_client.MonitorClient(cred, region)
    except TencentCloudSDKException as err:
        print(err)
    return client
#自定义监控上报函数，传入函数名称，指标名称，指标值
def API(client,instanceName,MetricName,Value):
    req = models.PutMonitorDataRequest() 
    req.AnnounceInstance = instanceName
    req.AnnounceTimestamp = int(time.time())
    req.Metrics = [
      {"MetricName": MetricName,"Value": Value}
    ]
    resp = client.PutMonitorData(req)
    return resp.to_json_string()

def main_handler(event, context):
    client = MONITOR("yourSecretId", "yourSecretKey")
    if 'key1' in event.keys():
        #scf的名称需要包含namespace和函数名称，中间用"|"分割
        print(API(client,"default|scf_monitor_Test","scf_suc_count",1))
    else:
    	print(API(client,"default|scf_monitor_Test","scf_fail_count",1))
    return "hello from scf"  #return
```
>?请将示例代码中的 `yourSecretId`、`yourSecretKey` 分别替换为您实际使用账户的 SecretId 及 SecretKey，可前往 **[API密钥管理](https://console.cloud.tencent.com/cam/capi)** 获取。
>


### 步骤3：安装自定义监控 SDK
1. 在 `MyProject` 目录下，执行以下命令，将自定义监控的 SDK 以及相关依赖安装到项目目录中。
```
pip install tencentcloud-sdk-python -t .
```
2. 安装完成后，可在项目根目录执行以下命令查看文件。
```
ll
```
成功安装，则返回结果如下图所示：
![](https://main.qcloudimg.com/raw/2f9415b582b31c9c56a0456b900da187.png)


### 步骤4：打包项目文件[](id:Step4)
1. 执行以下命令，将整个项目目录打包成 zip 文件。
```
zip project.zip * -r
```
2. 将打包好的 `project.zip` 下载文件到本地，便于后续将项目上传至云函数。

### 步骤5：上传项目压缩包至云函数
1. 登录 SCF 控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在“函数服务”页面上方，选择需上传函数的**地域**及**命名空间**，并单击**新建**。
3. 在“新建函数”页面的“基础信息”步骤中，根据以下信息创建函数，并单击**下一步**。如下图所示：
 - **函数名称**：输入自定义函数名，本文以 `scf_monitor_Test` 为例。
 - **运行环境**：选择**Python 2.7**。
 - **创建方式**：选择**模板函数**，并选择 helloworld 模板。
![](https://main.qcloudimg.com/raw/6b510988be5a4025b6b29c6e7eb712dc.png)
4. 在“函数配置”步骤中，保持默认设置并单击**完成**即可开始创建。
5. 在函数管理页面，选择**函数代码**页签，按照以下步骤上传代码。如下图所示：
![](https://main.qcloudimg.com/raw/fa7c3bd1931e05b988c326c6053c2cdc.png)
  1. 在**提交方法**中，选择**本地上传zip包**。
  2. 单击**上传**，并在弹出的目录中选择 [步骤4](#Step4) 中已准备好的 `project.zip` 文件。  
  3. 单击**保存**即可上传代码。
  上传成功后，界面自动展示 `index.py` 文件的代码内容。如下图所示：
![](https://main.qcloudimg.com/raw/aedb8b14a9fdecebd5debc8d2fba46d5.png)
 4. 再次单击**保存**，完成项目代码上传。 


### 步骤6：触发调试
1. 在**函数代码**页签中，选择界面下方“当前测试模板”中的**新建模板**。
2. 在弹出的“配置测试模板”窗口中，进行以下配置并单击**提交**。如下图所示：
![](https://main.qcloudimg.com/raw/7b0fba328e46a6e5e0d2d389c81e8d2e.png)
 - **测试事件模板**：输入自定义测试模板名称，本文以 `scf_monitor_test` 为例。
 - **引用模板代码**：选择**Hello World事件模板**。并在代码框中输入以下测试内容：
```
{
  "key1": "test value 1",
  "key2": "test value 2"
}
```
3. 模板创建成功后，在**函数代码**页签中选择该模板，并单击**测试**。
返回结果如下，则表示监控数据上报成功：
![](https://main.qcloudimg.com/raw/1eb3a7947b3615ff4e5a2839dc3e1b51.png)


### 步骤7：查看监控视图
进入 [自定义监控](https://console.cloud.tencent.com/monitor/indicator-view) 查看已触发上报的指标视图。如下图所示：
![](https://main.qcloudimg.com/raw/a87ba4b124d5f38a1a0636dbb237f13f.png)

### 步骤8：配置告警
您可参考 [配置告警策略](https://cloud.tencent.com/document/product/397/40223) 为函数配置告警。



