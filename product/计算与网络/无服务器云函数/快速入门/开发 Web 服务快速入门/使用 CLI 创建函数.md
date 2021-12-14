## 操作场景
本文介绍如何通过腾讯云云函数（Serverless Cloud Function，SCF）产品的命令行工具 SCF CLI 开发简单的 Hello World Web 服务，您可通过此案例试用 SCF 的基础功能。


## 前提条件
- 已注册腾讯云账户。若未注册腾讯云账户，可 [点此](https://cloud.tencent.com/register) 进入注册页面。
- 已安装对应的开发语言（如 Node 开发，需要安装 Node.js 等）。
- (可选) 安装并启动 Docker（使用  [本地调用云函数 local invoke](https://cloud.tencent.com/document/product/583/35401) 时需要）。
-  请确保您当前使用的账户已完成了以下授权操作：
 1. 参考 [角色与授权](https://cloud.tencent.com/document/product/583/32389) 完成 SCF 默认角色配置。
 2. 新建角色 `QCS_SCFExcuteRole` ，并参考 [用户与权限](https://cloud.tencent.com/document/product/583/40142) 完成预设策略关联。



## 操作步骤

### 安装 CLI （Windows）

#### 方式1
1. 安装 Python 2.7 或 3.6+ 版本，您可以参考[ Python 安装教程](https://cloud.tencent.com/document/product/583/33449#.E5.AE.89.E8.A3.85-python) 进行安装。
2. 执行 `pip install scf` 命令，安装 CLI。
3. 升级 CLI 可直接执行 `pip install -U scf` 命令。

#### 方式2
1. 前往 [CLI 下载](https://cloud.tencent.com/document/product/583/37940)，获取 SCF CLI 安装包。
>?选择此方式，升级 CLI 需获取最新安装包并重新进行安装。
>
2. 对已下载的 “scfcli.exe” 文件单击右键，选择**以管理员身份运行**进行安装。
3. 执行以下命令，验证 CLI 是否安装成功。
```
scf --version
```
返回类似如下信息，则表示安装成功。
```bash
scf CLI, version 0.0.1
```




### 安装 CLI （Mac / Linux）
1. 执行以下命令，检查 Python 版本。
```
Python --version
```
Python 版本须为 2.7 或 3.6 + ，如果 Python 版本不符，您可以参考[ Python 安装教程](https://cloud.tencent.com/document/product/583/33449#.E5.AE.89.E8.A3.85-python) 进行安装。
2. 执行以下命令，安装 SCF CLI。
```bash
pip install scf
```
3. 执行以下命令，验证 SCF CLI 是否安装成功。
```bash
scf --version
```
返回类似如下信息，则表示安装成功。
```
scf CLI, version 0.0.1
```




### 配置 SCF CLI
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com)。
2. 获取账号的 APPID，SecretId，SecretKey 以及产品期望所属的地域，配置信息获取途径请参见 [配置账号信息](https://cloud.tencent.com/document/product/583/33449#.E9.85.8D.E7.BD.AE.E8.B4.A6.E5.8F.B7.E4.BF.A1.E6.81.AF)。
3. 执行以下命令，并按照提示，将 APPID，SecretId，SecretKey 以及产品期望所属的地域配置到 SCF 中。
例如，您希望在**广州**地区使用云函数，并获取到账号 ID 为1253970223，SecretId 和 SecretKey 分别为 AKIxxxxxxxxxx，uxxlxxxxxxxx。
您可以通过执行 `scf configure set` 命令，按照提示输入对应信息，完成 SCF CLI 的配置：
```shell
$ scf configure set
TencentCloud appid(None): 1253970223
TencentCloud region(None): ap-guangzhou
TencentCloud secret-id(********************************): AKIxxxxxxxxxx
TencentCloud secret-key(****************************): uxxlxxxxxxxx
Show the command information without color(cur:False). (y/n):n
Deploy SCF function by COS, it will be faster(cur:False).  (y/n): y
```
>?using-cos 是指在部署时是否通过 COS 部署。使用 COS 部署函数最高能提升80%的速率，大大提高了工作效率。但在部署频次、部署包很大时，可能会产生 COS 计费。现 SCF 与 COS 联合发布限时活动，开启 COS 部署即可领取代金券，请前往 [SCF 控制台](https://console.cloud.tencent.com/scf/index?rid=1?from=fromdoc) 查看活动信息。

### 编写函数
1. 在命令行中选择并进入到存放项目代码的目录。
2. 执行以下命令，创建函数。
```
scf init
```
>?此命令会在当前目录下创建 hello_world 函数。
>
返回信息如下所示，则函数创建成功：
```bash
[+] Initializing project...
Template: /usr/local/lib/Python3.7/site-packages/tcfcli/cmds/init/templates/tcf-demo-Python
Output-Dir: .
Project-Name: hello_world
Type: Event
Runtime: python3.6
[*] Project initialization is complete
[*] You could 'cd hello_world', and start this project.
```
此时默认创建了名称为 hello_world，runtime 为 Python 3.6 的函数。
了解更多关于初始化命令，详情请参见 [初始化示例项目](https://cloud.tencent.com/document/product/583/33450)。
3. 将本地 hello_wolrd 函数目录中的 `index.py` 文件替换为如下内容：
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
通过本地调用，您可以在本地使用模拟事件触发函数执行，实时调试函数代码。当前 `native invoke` 仅支持 Node.js 及 Python 语言，结合 Docker  进行本地调试请参考 [本地调试（local invoke）](https://cloud.tencent.com/document/product/583/35401)。
1. 进入项目所在目录 `hello_world`。
2. 执行以下命令，启动函数在本地运行。
```
$ cd hello_world 
$ scf native invoke --no-event
```
输出结果如下：
```
Run Python3.6's cmd: Python
START RequestId: 2f258903-95d0-4992-9321-0d720867a383
Loading function
start main handler
{}
END RequestId: 2f258903-95d0-4992-9321-0d720867a383
REPORT RequestId: 2f258903-95d0-4992-9321-0d720867a383 Duration: 0 ms Billed Duration: 100 ms Memory Size: 128 MB Max Memory Used: 8 MB
{"body": "API GW Test Success", "headers": {"Access-Control-Allow-Origin": "*", "Content-Type": "text"}, "isBase64": false, "statusCode": 200}
```
通过输出内容可以看到，函数在本地运行完成后，输出了函数的打印日志、及函数返回内容。
本地调用命令详情及了解更多命令参数信息，请参见 [本地调试（native invoke）](https://cloud.tencent.com/document/product/583/35402)。


### 部署函数（含配置触发器）
1. 修改模板文件，配置触发器。
    由于已创建的函数是基于 API 网关触发，所以需要在模板文件里（文件路径：hello_world / template.yaml）添加 API 网关触发事件。完整 `template.yaml` 内容如下：
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
               hello_world_apigw:  # ${FunctionName} + '_apigw'
                   Type: APIGW
                   Properties:
                       StageName: release
                       ServiceId: 
                       HttpMethod: ANY
```
更多模板文件规范请参阅 [腾讯云无服务器应用模型](https://cloud.tencent.com/document/product/583/36198)。
2. 在项目目录下执行命令`scf deploy`，将本地代码包及函数配置部署到云端。
```bash
$ scf deploy 
Package name: default-hello_world-latest.zip, package size: 4.097 kb
...
[o] Deploy function 'hello_world' success
[o] Deploy trigger 'api' success
[+] Function Base Information: 
     Name: hello_world
     ...
[+] Trigger Information: 
    > APIGW - hello_world_apigw:
       ModTime: 2019-08-16 12:01:13
       Type: apigw
      ...
         service:
           serviceId: service-qnwxxxxxx
           serviceName: SCF_API_SERVICE
           subDomain: https://service-qnw3irqg-xxxxxxxxxxx.gz.apigw.tencentcs.com/release/hello_world
       ...
[o] Deploy success
```
部署完成后，您可以在终端输出信息中查看函数信息和网关信息，您可以将 serviceId 复制到 template.yaml，之后部署就不会再创建新的 API 网关。
3. 完成部署后，您可以登录 [云函数控制台](https://console.cloud.tencent.com/scf)，到相应地域下查看已成功部署的函数。
    部署命令详情及了解更多命令参数信息，请参见 [打包部署](https://cloud.tencent.com/document/product/583/33451)。

### 云端测试
完成云函数部署后，复制终端输出的访问路径，使用浏览器访问该路径进行测试。
显示如下，即为成功部署函数。
![](https://main.qcloudimg.com/raw/bcaffcaa34e2e75988c01a7d8df923c0.png)

### 查看日志
您可以执行 `scf logs -n hello_world` 命令获取 hello_world 函数日志，输出结果如下：
```bash
$scf logs -n hello_world
[>] Log startTime: 2019-08-16 12:06:26
START RequestId: 37fe28ff-bfdb-11e9-acc7-5254008a4f10
Event RequestId: 37fe28ff-bfdb-11e9-acc7-5254008a4f10
Loading function
start main handler
{'headers': {'connection': 'keep-alive', 'accept-language': 'zh-cn', 'accept-encoding': 'br, gzip, deflate', 'x-anonymous-consumer': 'true', 'x-qualifier': '$LATEST', 'host': 'service-qnw3irqg-1255721742.gz.apigw.tencentcs.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'}, 'headerParameters': {}, 'requestContext': {'httpMethod': 'ANY', 'serviceId': 'service-qnw3irqg', 'path': '/hello_world', 'sourceIp': '59.37.124.125', 'identity': {}, 'stage': 'release'}, 'queryStringParameters': {}, 'httpMethod': 'GET', 'path': '/hello_world', 'pathParameters': {}, 'queryString': {}}
END RequestId: 37fe28ff-bfdb-11e9-acc7-5254008a4f10
Report RequestId: 37fe28ff-bfdb-11e9-acc7-5254008a4f10 Duration:0ms Memory:128MB MaxMemoryUsed:0.679688MB
```
更多关于使用 CLI 查看日志，请参见 [日志查看](https://cloud.tencent.com/document/product/583/36352)。


### 查看监控
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/list)，单击左侧导航栏**函数服务**。
2. 在“函数服务”页面上方选择已创建函数地域，并单击函数 ID。
3. 在已创建函数的详情页面，选择**监控信息**，即可查看函数调用次数/运行时间等情况。如下图所示：
>!监控统计的粒度最小为1分钟。您需要等待1分钟后，才可查看当次的监控记录。
>
![](https://main.qcloudimg.com/raw/acc4d768c7a23e424fd65e065b1c043f.png)
更多关于监控信息请参见 [监控指标说明](https://cloud.tencent.com/document/product/583/32686)。


### 配置告警
在已创建函数的详情页面，单击**前往新增告警**为云函数配置告警策略，对函数运行状态进行监控。如下图所示：
![](https://main.qcloudimg.com/raw/6850e40bca71bfe7ca976004388294c8.png)
更多关于配置告警请参见 [告警配置说明](https://cloud.tencent.com/document/product/583/30133)。



## 常见问题

工具安装或使用常见问题参考 [SCF 工具类常见问题](https://cloud.tencent.com/document/product/583/33456)。
