## 操作场景
本文介绍通过腾讯云云函数（Serverless Cloud Function，SCF）、SCF VS Code 插件开发简单的 Hello World Web 服务。

## 前提条件
- 已注册腾讯云帐户。单击 [这里](https://cloud.tencent.com/register) 进入注册页面，注册指引请参见 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985)。
- VS Code ：在 [VS Code下载页面](https://code.visualstudio.com/) 下载对应的 IDE 并安装，其**版本要求为 v1.33.0 +**。
- 已安装 Python 2.7+ 或 Python 3.6+，以及对应版本 pip。

## 操作步骤
### 安装插件
可通过以下两种方式安装 SCF VS Code 插件。
**通过插件市场直接安装**
进入 [插件市场](https://marketplace.visualstudio.com/items?itemName=tencentcloud.tencent-cloud-vscode-toolkit) 单击【install】进行安装。

**通过 VS Code IDE 安装**
1. 运行 VS Code IDE。
2. 打开 VS Code 插件市场。
3. 在搜索框中输入 “Tencent Serverless”，单击搜索框下方列表中的 Tencent Serverless 插件查看详情并选择【install】。如下图所示：    
![](https://main.qcloudimg.com/raw/4d629d80bb03d4957213af44a4fb524c.png)    
安装完成后，左侧栏中会展示已安装完毕的 Tencent Serverless 插件。

### 配置插件
>?如果您已经在 SCF CLI 中配置了账户信息，无需再次配置，请跳过此步骤。
>
1. 单击左侧导航栏的<img src="https://main.qcloudimg.com/raw/4395057dfb3a8f4a92c90ba7dff9b1c1.png" style="margin:-3px 0;">，打开已安装好的 Tencent Serverless 插件。
2. 单击创建一个腾讯云用户凭证。如下图所示：  
![Alt text](https://main.qcloudimg.com/raw/fca11ef6e54287f2ad400d34123872c9.png)
3. 根据提示依次输入账号的 APPID，SecretId 及 SecretKey 信息，作为插件调用云 API 时的认证信息。并在认证成功后，选择您希望部署函数的地域。配置信息获取途径请参见 [配置 SCF CLI](https://cloud.tencent.com/document/product/583/33449#.E9.85.8D.E7.BD.AE-scf-cli)。


### 编写函数
1. 在配置账户对应地域下的云端函数列表中，单击【创建一个函数】，在本地初始化新的函数项目。如下图所示：
>!**暂不支持不同的命名空间（无论是否在同一区域）下创建同名的本地函数**。
>
![](https://main.qcloudimg.com/raw/2bfe26b670ba259477c607da98c216b8.png)  
2. 根据提示依次选择函数所在的命名空间，运行时 runtime，输入函数名。
3. 函数信息录入成功后，将开始创建。创建成功后，列表页中会展示新建的本地函数（以 `vsCode` 函数为例）。如下图所示：  
![](https://main.qcloudimg.com/raw/62a0f773ab07b9a1feaf8fb4d7afd232.png)
4. 将 `vsCode` 中的 `index.py` 文件代码替换为如下内容：
```python
# -*- coding: utf-8 -*-
import sys
import logging
print('Loading function')
logger = logging.getLogger()
def main_handler(event, context):
    logger.info("start main handler")
    print(event)
    body = 'API GW Test Success'
    response = {
        "isBase64": False,
        "statusCode": 200,
        "headers": {"Content-Type": "text", "Access-Control-Allow-Origin": "*"},
        "body": body
    }
    return response
```

### 本地测试
单击左侧列表中的本地函数，选择【本地调用】，即可对函数进行本地测试。如下图所示：
>?当前仅支持 Python 及 Node.js 函数的本地触发能力。  
>
![](https://main.qcloudimg.com/raw/0f245ea0d4c53a7b1b3f00670f0d448b.jpg)

### 部署函数（含配置触发器）
1. 修改模板文件，配置触发器。
由于我们的函数是基于 API 网关触发，所以需要在模板文件里（文件路径：hello_world / template.yaml）添加 API 网关触发事件。完整 template.yaml 如下：
```yaml
Resources:
  default:
    Type: TencentCloud::Serverless::Namespace
    hello_world:
      Type: TencentCloud::Serverless::Function
      Properties:
        CodeUri: ./
        Type: Event
        Description: This is a template function
        Environment:
          Variables:
            ENV_FIRST: env1
            ENV_SECOND: env2
        Handler: index.main_handler
        MemorySize: 128
        Runtime: Python2.7
        Timeout: 3
        Events:
              hello_world_apigw:   #${FunctionName} + '_apigw'
                   Type: APIGW
                   Properties:
                          StageName: release
                          ServiceId:
                          HttpMethod: ANY
```
更多模板文件规范请参见 [腾讯云无服务器应用模型](https://cloud.tencent.com/document/product/583/36198)。
2. 单击左侧列表中的函数名称，进入该函数基本信息页面。
3. 单击【上传函数】，等待函数上传完毕，即可在 [函数服务]() 列表页中查看到函数的相关信息。如下图所示：    
![](https://main.qcloudimg.com/raw/7b6b3cdbec4af3167612e1611791155f.jpg)
上传成功之后，可在 VS Code 查看部署详情。如下图所示：
![](https://main.qcloudimg.com/raw/b2ee7c648a68157d3a5e31c119916ea6.png)
您可以将 serviceId 复制到配置文件 template.yaml 中，之后部署就不会再创建新的 API 网关。
4. 完成部署后，您可以登录 [云函数控制台](https://console.cloud.tencent.com/scf)，到相应地域查看已成功部署的函数。

### 云端测试
单击左侧列表中的云函数名称，在右侧页面中单击【云端调用】，即可在页面中查看到函数在云端运行的相关信息。如下图所示：  
![](https://main.qcloudimg.com/raw/34732ab4a7f7b2ea34ee32618f560f35.jpg)

### 查看日志
云端调用的日志会输出到 VS Code。如下图所示：
![](https://main.qcloudimg.com/raw/83c56ff1d4e808488cffafea2867f4de.png)
您也可以前往控制台打开函数页面选择【运行日志】，查看所有历史日志，详情请参见 [函数日志](https://cloud.tencent.com/document/product/583/36143)。

### 查看监控
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/list)，单击左侧导航栏【函数服务】。
2. 在“函数服务”页面上方选择已创建函数地域，并单击函数 ID。
3. 在已创建函数的详情页面，选择【监控信息】，即可查看函数调用次数/运行时间等情况。如下图所示：
>!监控统计的粒度最小为1分钟。您需要等待1分钟后，才可查看当次的监控记录。
>
![](https://main.qcloudimg.com/raw/acc4d768c7a23e424fd65e065b1c043f.png)
更多关于监控信息请参见 [监控指标说明](https://cloud.tencent.com/document/product/583/32686) 


### 配置告警
在已创建函数的详情页面，单击【前往新增告警】为云函数配置告警策略，对函数运行状态进行监控。如下图所示：
![](https://main.qcloudimg.com/raw/6850e40bca71bfe7ca976004388294c8.png)
更多关于配置告警请参见 [告警配置说明](https://cloud.tencent.com/document/product/583/30133) 。



