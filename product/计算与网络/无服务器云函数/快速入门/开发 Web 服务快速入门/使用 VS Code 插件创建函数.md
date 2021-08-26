## 操作场景
Tencent Serverless Toolkit for VS Code 是腾讯云 Serverless 产品的 VS Code（Visual Studio Code）IDE 的插件。该插件可以让您更好地在本地进行 Serverless 项目开发和代码调试，并且轻松将项目部署到云端。
本文介绍如何通过腾讯云云函数（Serverless Cloud Function，SCF）及 VS Code 插件开发简单的 Hello World Web 服务。

通过该 VS Code 插件，您可以：
- 拉取云端的云函数列表，并触发云函数在云端运行。
- 在本地快速创建云函数项目。
- 在本地开发、调试及测试您的云函数代码。
- 使用模拟的 COS、CMQ、CKafka、API 网关等触发器事件来触发函数运行。
- 上传函数代码到云端，更新函数配置。

## 前提条件
- Tencent Serverless 可在 Windows， MacOS 中安装。在安装 Tencent Serverless 之前，需要确保系统中已有以下组件/信息：
	- 已注册腾讯云帐户。若未注册腾讯云账户，可 [点此](https://cloud.tencent.com/register) 进入注册页面。
	- VS Code ：在 [VS Code下载页面](https://code.visualstudio.com/) 下载对应的 IDE 并安装，其**版本要求为 v1.33.0 +**。
- 请确保您当前使用的腾讯云账户已完成了以下授权操作：
 1. 参考 [角色与授权](https://cloud.tencent.com/document/product/583/32389) 完成 SCF 默认角色配置。
 2. 新建角色 `QCS_SCFExcuteRole` ，并参考 [用户与权限](https://cloud.tencent.com/document/product/583/40142) 完成预设策略关联。


## 操作步骤
### 安装插件
可通过以下两种方式安装 SCF VS Code 插件：  

**a. 通过插件市场直接安装**
进入 [插件市场](https://marketplace.visualstudio.com/items?itemName=tencentcloud.tencent-cloud-vscode-toolkit) 单击**install**进行安装。

**b. 通过 VS Code IDE 安装**
1. 运行 VS Code IDE。
2. 打开 VS Code 插件市场。
3. 在搜索框中输入 “Tencent Serverless”，单击搜索框下方列表中的 Tencent Serverless 插件查看详情并选择**install**。如下图所示：      
![](https://main.qcloudimg.com/raw/aad8aa8235fcf68713072d6270ce9e83.png)    
    安装完成后，左侧栏中会展示已安装完毕的 Tencent Serverless 插件。


### 配置插件
>?如果您已经在 SCF CLI 中配置了账户信息，无需再次配置，请跳过此步骤。
>
1. 单击左侧导航栏的<img src="https://main.qcloudimg.com/raw/0916687440e89c5b9a397537fe35ae42.png" style="margin:-3px 0;">，打开已安装好的 Tencent Serverless 插件。
2. 单击创建一个腾讯云用户凭证。如下图所示：  
![Alt text](https://main.qcloudimg.com/raw/f657198718f1ebc03257718785246477.png)
3. 根据提示依次输入账号的 APPID，SecretId 及 SecretKey 信息，作为插件调用云 API 时的认证信息。并在认证成功后，选择您希望部署函数的地域。配置信息获取途径请参见 [配置 SCF CLI](https://cloud.tencent.com/document/product/583/33449#.E9.85.8D.E7.BD.AE.E8.B4.A6.E5.8F.B7.E4.BF.A1.E6.81.AF)。
已配置的账号信息将写入本地 `~/.tcli_config.ini` 文件，您也可以直接修改该文件中的账号信息，修改完成后需要重启 VS Code 配置才可生效。
4. 为提升函数上传效率，您可以在 VS Code 中 [设置开启 COS 上传](#openCOS)。



### 创建函数
1. 单击已配置账户函数列表上方的<img src="https://main.qcloudimg.com/raw/306642573f06897732e6af65e5ddf0df.png" style="margin:-3px 0;">，在本地初始化新的函数项目。
2. 根据提示依次选择函数运行时 runtime，并输入函数名。
3. 函数信息录入成功后，将开始创建。
4. 函数创建成功后，会跳转到工作区打开函数的入口文件。
5. 将 `index.py` 中的代码替换为如下内容：   
```
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
           "headers": {"Content-Type": "text",    "Access-Control-Allow-Origin": "*"},
           "body": body
       }
       return response
```

### 本地测试
进入 Tencent Serverless 插件，单击本地函数列表目标函数右侧的<img src="https://main.qcloudimg.com/raw/394808de581cf1aaaec4337cf201ee55.png" style="margin:-3px 0;">，即可对函数进行本地测试。如下图所示：
>?
>- 当前仅支持 Python 及 Node.js 函数的本地调试能力。
>- 如果您有安装多个 Python 版本，可根据当前要调试的 runtime 在 VS Code 里 [设置 Python path](#pythonpath)。
>
![](https://main.qcloudimg.com/raw/2c18e88f39bdefda438a5d8d0396a2b1.png)



### 断点调试

#### 设置断点
针对 Python 函数，可以在 VS Code 插件进行本地调试。
>?本地调试目前支持 Python 和 Node.js ，调试 Python 项目需要先安装 [Python 插件](https://marketplace.visualstudio.com/items?itemName=ms-Python.Python)。如果您有安装多个 Python 版本，可根据当前要调试的 runtime 在 VS Code 里 [设置 Python path](#pythonpath)。
>
单击左侧导航栏中的<img src="https://main.qcloudimg.com/raw/5c3bec3934e5d5a2dbdbf53ec105d6bd.png" style="margin:-3px 0;">，进入本地编辑页面，给函数设置断点。如下图所示：  
![](https://main.qcloudimg.com/raw/a112a7af7dd57e7f7a4e1de20f7c4db3.png)

#### 设置调试模版
1. 单击左侧导航栏顶部的<img src="https://main.qcloudimg.com/raw/f51801927eb766c828e721b193539e9e.png" style="margin:-3px 0;">，进入调试页面（或 `Ctrl+Shift+D`）。
2. 选择**create a launch.json file**，新建调试配置文件。
3. 选择 SCF Debugger For Python 调试模板（Node 项目请选择 SCF Debugger For Node）。如下图所示：
>!不同的 runtime 须选择对应的调试模板，可根据您当前的调试文件类型，区分选择 Python 和 Node.js。     
>
![](https://main.qcloudimg.com/raw/ab797f48bd2f835c24a99e18aa958b64.png) 


#### 开始调试
单击<img src="https://main.qcloudimg.com/raw/11ae4fcabe25adf8840bbcc25816ebec.png" style="margin:-3px 0;">，即可看到调试信息。如下图所示：  
>?目前插件是对当前工作区打开的函数文件进行调试，为保障调试正常进行，您需要确保目标函数文件已经当前窗口打开。
>
![](https://main.qcloudimg.com/raw/ffe1e3d2f7e8ce9dee89717ba3cc058c.png)

### 部署函数（含配置触发器）

1. 修改模板文件，配置触发器。
由于我们的函数是基于 API 网关触发，所以需要在模板文件里 `template.yaml` 添加 API 网关触发事件。完整 `template.yaml` 如下：
```yaml
    Resources:
     default:
       Type: TencentCloud::Serverless::Namespace
       helloworld:
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
2. 进入 Tencent Serverless 插件，单击本地函数列表目标函数右侧的<img src="https://main.qcloudimg.com/raw/940dfe3754caddd4613b5cdbff0fa558.png" style="margin:-3px 0;">。如下图所示：
>!
>- 如果您的函数有使用第三方依赖，则需要将依赖包放至函数目录下然后执行上传。Python 依赖安装方法可 [参考此处](<https://cloud.tencent.com/developer/article/1443081>)。
>- 如果在部署时提示 Role 不存在，请前往 SCF 控制台并参考 [角色与授权](https://cloud.tencent.com/document/product/583/32389) 添加 Role。
>
![](https://main.qcloudimg.com/raw/84d3caba3f22743e2ba76dfef2d4ac7b.png)         
3. 函数上传完毕，单击云端函数右侧的<img src="https://main.qcloudimg.com/raw/7d8ff7082e8db0a3c8548b36b4b15a7d.png" style="margin:-3px 0;">进行刷新，即可查看已上传的函数。（查看区域需切换到上传时选择的区域）如下图所示：   
![](https://main.qcloudimg.com/raw/cd7fe796ea7b986e4bdb1bc3a9f38f70.png)
上传成功之后，可在 VS Code 查看部署详情。如下图所示：  
![](https://main.qcloudimg.com/raw/4710afe79d4c816f73fbb86f45a43435.png)  
`template.yaml` 文件中 ServiceId 为空时，SCF 将会为您重新创建该函数的 API 网管触发器。您可以将已获取的 ServiceId 复制到配置文件 `template.yaml` 中，之后部署就不会再创建新的 API 网关。如何获取 ServiceId 请参见 [查看 API 网关触发器](#api)。
4. 完成部署后，可使用浏览器访问 VS Code 输出的访问路径，显示结果如下：  
![](https://main.qcloudimg.com/raw/2a14a48452c33341a0c82b46203a7656.png)  
您也可以登录 [SCF 控制台](https://console.cloud.tencent.com/scf)，到相应地域查看已成功部署的函数。
>?
>- 使用 COS 部署函数最高能提升80%的速率，大大提高了工作效率。但在部署频次、部署包很大时，可能会产生 COS 计费。
>- 现 SCF 与 COS 联合发布限时活动，开启 COS 部署即可领取代金券，请前往 [SCF 控制台](https://console.cloud.tencent.com/scf/index?rid=1?from=fromdoc) 查看活动。
>- 您可以在 VS Code 中 [设置开启 COS 上传](#openCOS)。

### 忽略上传
实际项目中，可以自定义不想上传的文件内容，SCF 插件将会忽略这些内容进行打包上传。
1. 在代码路径下，新建 `ignore` 文件夹。
2. 进入 `ignore` 文件夹，新建忽略配置文件 `FUNCTIONNAME.ignore`，并在该文件下描述忽略的内容。
>?路径规范：以 template.yaml 里的 CodeUri 路径为基准 ，定义想要忽略的内容所在位置。
>
如下所示，template.yaml 里定义函数名为 hello，CodeUri 为`./`。
```yaml
Resources:
  default:
    Type: TencentCloud::Serverless::Namespace
    helloworld:
      Type: TencentCloud::Serverless::Function
      Properties:
        CodeUri: ./
        Type: Event
        Description: This is a template function
        Handler: index.main_handler
        MemorySize: 128
        Runtime: Python3.6
        Timeout: 3
```
则目录层级及 `HELLOWORLD.ignore` 如下图所示：
![](https://main.qcloudimg.com/raw/c9ca3143d69671814083d29f9b1eb4d7.png)
完成配置后，最终上传会**忽略 testmodule 目录**和**当前路径下所有 md 文件**。




### 云端测试
单击左侧列表右侧的<img src="https://main.qcloudimg.com/raw/394808de581cf1aaaec4337cf201ee55.png" style="margin:-3px 0;">，即可在页面中查看到函数在云端运行的相关信息。如下图所示：    
![](https://main.qcloudimg.com/raw/35fd3a013d82ffe9d179c2aaeef20e9c.png)



### 更多功能

#### 查看日志

云端调用的日志会输出到 VS Code。如下图所示：  
![](https://main.qcloudimg.com/raw/3b5672e8d181021b4ed7b57c93a563bc.png)  
您也可以前往控制台打开函数页面选择**运行日志**，查看所有历史日志，详情请参见 [函数日志](https://cloud.tencent.com/document/product/583/36143)。

#### 下载函数

如果您已经在 [云函数控制台](https://console.cloud.tencent.com/scf/list) 创建了函数，则可以在 VS Code 插件里直接将云端函数下载到本地。  
1. 单击目标云端函数右侧的<img src="https://main.qcloudimg.com/raw/3c72bf2180157adcd5bc66072e1d063f.png" style="margin:-3px 0;">，将函数导入到本地。如下图所示：   
![](https://main.qcloudimg.com/raw/48225ecf3d903c41d67c6cdbf071d09b.png)
2. 选择函数下载的目标目录，下载完成后您可以选择在本窗口打开函数或者新建窗口打开。



#### 测试模板

本地调用时，可根据函数功能选择不同的测试模板，也可以自定义模板。如下图所示：  
![](https://main.qcloudimg.com/raw/c2b7c5ed4cebcc1f488fdd2e2a4bb905.png)
更多测试模版相关内容，详情请参见 [触发器](https://cloud.tencent.com/document/product/583/9705)。



#### 查看监控

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/list)，单击左侧导航栏**函数服务**。
2. 在“函数服务”页面上方选择已创建函数地域，并单击函数 ID。
3. 在已创建函数的详情页面，选择**监控信息**，即可查看函数调用次数/运行时间等情况。如下图所示：
>?监控统计的粒度最小为1分钟。您需要等待1分钟后，才可查看当次的监控记录。
>
![](https://main.qcloudimg.com/raw/acc4d768c7a23e424fd65e065b1c043f.png)
更多关于监控信息请参见 [监控指标说明](https://cloud.tencent.com/document/product/583/32686)。

#### 配置告警

在已创建函数的详情页面，单击**前往新增告警**为云函数配置告警策略，对函数运行状态进行监控。如下图所示：  
![](https://main.qcloudimg.com/raw/6850e40bca71bfe7ca976004388294c8.png)
更多关于配置告警请参见 [告警配置说明](https://cloud.tencent.com/document/product/583/30133)。  

#### 切换账号
如果您有多个账号，可按照以下步骤在 SCF 插件页中添加新账号并切换使用：
1. 选择云端函数右侧的<img src="https://main.qcloudimg.com/raw/ae8b96f8ee48b4dc003cf8b5173e5b12.png" > > **切换账号**。如下图所示：
![](https://main.qcloudimg.com/raw/f2a93ff675883768ed326f7bd44353ee.png)
2. 在弹出的菜单中选择**登录新用户**，输入对应信息完成配置，即可使用多用户。


## 常见问题  

安装或使用过程中有遇到问题，可参考 [SCF 工具类常见问题](https://cloud.tencent.com/document/product/583/33456) 解决，您也可以通过 [欢迎交流](#welcome) 与我们联系。    

## 相关操作

[](id:openCOS)
### 设置开启 COS 上传
1. 选择左下角的<img src="https://main.qcloudimg.com/raw/20fd46098cf037eb003dc41f1f913313.png" style="margin:-3px 0px;"/> >**Settings**。如下图所示：
![](https://main.qcloudimg.com/raw/e9e1f63819d29d86d8f9cae9cbb9e31a.png)
2. 在“Settings”页面，选择**Extensions** > **Tencent-SCF**并勾选**Enable deployed by COS**。如下图所示：
![](https://main.qcloudimg.com/raw/438d40222bd6fcc481c890c052bb6865.png)


[](id:pythonpath)
### 设置 Python path
如果您有安装多个 Python 版本，可根据当前要调试的 runtime 将 Python 2 或 Python 3 的对应路径填入 Tencent-SCF 设置即可。如下图所示：
![](https://main.qcloudimg.com/raw/69e0a4b6652799c1c5069b977346b551.png)

### 查看 API 网关触发器[](id:api)
如果您已为函数创建 API 网管触发器，可通过以下方式获取触发器的 serviceId：
1. 登录 [SCF 控制台](https://console.cloud.tencent.com/scf/list)，在页面上方选择函数所在地域及命名空间。
2. 在“函数服务”列表页面中，选择需查看信息的函数名。
3. 进入“函数配置”页面，选择**触发方式**页签，即可在 “API网关触发器” 中查看 `serviceId`。如下图所示：
![](https://main.qcloudimg.com/raw/d90649aac12e8011979148d26e9b7bcc.png)



## 欢迎交流[](id:welcome)
如果您对 Tencent Serverless 感兴趣，您可以加入QQ群（537539545）与我们交流。    
![Alt text](https://main.qcloudimg.com/raw/bc881547d1cd2043ecf1b286c70f7319.png)
