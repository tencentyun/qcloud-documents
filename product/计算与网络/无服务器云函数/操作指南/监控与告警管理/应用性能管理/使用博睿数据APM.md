本文将为您介绍云函数如何接入和使用博睿数据 APM。


## 前提条件

- 已注册 [博睿 Server](https://server.bonree.com/) 账号。
- 已 [创建云函数](https://cloud.tencent.com/document/product/583/19806#.E5.88.9B.E5.BB.BA.E5.87.BD.E6.95.B0) 并开启公网访问。

>?博睿探针目前支持 Python 和 Node.js 的多数主流框架，且仅在使用支持的框架时，博睿 smartAgent 才可自动捕获。详情请参见 [博睿探针支持列表](#list)。



## 操作步骤


### 使用云函数控制台接入

您可以使用云函数控制台接入博睿，详细步骤如下：


#### 绑定探针[](id:bindagent)

您需要下载博睿探针，将该探针上传到层并绑定在函数上。

1. 下载 [博睿 Serverless 版探针](https://scf.bonree.com/download/last/bonree-serverless-agent.zip)。
2. 登录云函数控制台，选择左侧菜单栏中的 **[层](https://console.cloud.tencent.com/scf/layer)**。
3. 在“层”管理页面，单击**新建**。
4. 在“新建层”页面，根据提示信息进行配置。如下图所示：
   ![](https://main.qcloudimg.com/raw/19b29b36a09d6adaf8ce55f7dfc9a599.jpg)
 - **层名称**：输入层名称。只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2 - 60个字符。
 - **提交方法**：选择**本地上传zip包**。
 - **层代码**：选择步骤1下载的探针文件。
 - **运行环境**：根据实际运行环境进行选择。目前支持 Python 和 Node.js。
5. 单击**确定**即可创建层。
6. 选择左侧菜单栏中的**函数服务**，进入函数服务页面。
7. 单击需要绑定层的函数名称，进入函数管理页面。
8. 选择**层管理** > **绑定**，在绑定层窗口按照提示绑定上述步骤创建的层。如下图所示：
   ![](https://main.qcloudimg.com/raw/635f496e58943f4cfa7fd5330d00b2bf.jpg)
9. 单击**确定**即可完成探针的绑定。



#### 引入探针[](id:inputagent)

绑定层后，探针并不会自动启动，需要在代码入口引入探针。探针运行会占用少量内存，但不会影响您的业务运行。如业务代码本身占用了大量内存，探针将触发熔断机制以保障业务运行。目前提供 Nods.js 和 Python 引入：

<dx-tabs>
::: Node.js\s的引入
在云函数的入口函数所在的文件 `require` 博睿探针。例如您可以在 `sl_handler.js` 文件中加入如下引入的代码：
<dx-codeblock>
:::  js
require("/opt/bonree/apm/agent/nodejs/serverless/Bonree/index.js");
:::
</dx-codeblock>
:::
:::  Python\s的引入
在云函数的入口函数所在的文件 `import` 博睿探针。以 Flask 框架为例，您可以在 `sl_handler.py` 文件中添加如下代码：
<dx-codeblock>
:::  python
import sys

sys.path.insert(0, "/opt/bonree/apm/agent/python/serverless")
try:
   from Bonree.autoinject import sitecustomize
except ImportError:
   pass
:::
</dx-codeblock>
如下图所示：
![](https://main.qcloudimg.com/raw/775d6e13f4112e166ba49c2ffa0862ad.png)
:::
</dx-tabs>



#### 增加云函数环境变量

您需要在每个绑定博睿探针的云函数中增加环境变量，探针将根据环境变量中的账户信息上报。需新增以下变量：

| 环境变量 Key               | Value                                                        |
| -------------------------- | ------------------------------------------------------------ |
| BONREE_SMARTAGENT_SDK_PATH | /opt/bonree/apm/agent/c/serverless/lib/libagentsdk-x64-linux.so |
| BONREE_APM_ACCOUNT_GUID    | 博睿账户 GUID                                                |

>?您可以在博睿 Server 产品的右上角找到 GUID 信息。如下图所示：
>![](https://main.qcloudimg.com/raw/f54e2fcd2c4fec46c27f4814c11bb0f3.png)



### 使用 Serverless Framework 接入


您还可以使用 Serverless Framework 的 bonree component 上传博睿探针。本文以 Flask 框架为例，介绍如何使用bonree component来绑定和使用博睿探针。您也可以单独使用 bonree component 上传层，再进行 [层绑定](#bindagent)。


#### 创建层并绑定至函数

1. 在 apm 目录下新建 `serverless.yml` 文件，`serverless.yml` 文件内容如下：
<dx-codeblock>
:::  yaml
component: bonree
name: bonree_agent
org: tencent
app: tencent
stage: dev
inputs: 
  name: bonree_agent
  region: ap-beijing
  runtimes: 
    - Nodejs10.15
    - Python3.6

:::
</dx-codeblock>

2. 同样在 src 目录下创建 Flask 的 `serverless.yml` 文件，在`layers`参数填写 bonree component 的信息，在环境变量中填写博睿账号的GUID和SDK路径参数。`serverless.yml` 文件内容如下：
<dx-codeblock>
:::  yaml
component: flask
name: bonree_flask
org: tencent
app: tencent
stage: dev
inputs: 
  region: ap-beijing
  runtime: Python3.6
  layers: 
    - name: ${output:${stage}:${app}:bonree_agent.name}
      version: ${output:${stage}:${app}:bonree_agent.version}
  functionConf: 
    memorySize: 128
    environment: 
      variables: 
        BONREE_APM_ACCOUNT_GUID: your_bonree_GUID
        BONREE_SMARTAGENT_SDK_PATH: /opt/bonree/apm/agent/c/serverless/lib/libagentsdk-x64-linux.so
:::
</dx-codeblock>
3. 查看目录结构，具体目录结构如下所示：
<dx-codeblock>
:::  bash
   .
   ├── apm
   │   └── serverless.yml
   └── src
       └── serverless.yml
:::
</dx-codeblock>
4. 只使用 bonree component 便可以完成层的创建。在云函数中配置 layers 参数可以完成绑定操作，您也可以选择在云函数控制台手动绑定层。
5. 在根目录下执行以下命令，进行应用部署。
```bash
sls deploy
```





#### 引入探针

1. 登录云函数控制台，选择左侧菜单栏中的 **[函数服务](https://console.cloud.tencent.com/scf/)**。
2. 在函数服务页面，单击对应的函数名称，进入函数管理页面。
3. 单击**函数代码**页签，在 `sl_handler.py` 文件中加入引入探针的代码，详细内容可参考上文 [引入探针](#inputagent)。



### 使用博睿 Server 

1. 登录 [博睿 Server 控制台](https://server.bonree.com/)，待数据上报至博睿。
2. 在博睿 Server 控制台右上角中选择**<img src="https://main.qcloudimg.com/raw/3475d18df76f95b36d1cc5f3708494ac.jpg" width="2.5%">** > **部署状态**，进入部署状态页面查看已进行数据上报的函数。如下图所示：
   ![](https://main.qcloudimg.com/raw/8ab20877d29235519da69df08861a95a.png)
3. 将该函数关联一个应用，即可查看应用运行的情况。如下图所示：
   ![](https://main.qcloudimg.com/raw/d4e13fba93cd83a752270817adfe18dc.png)
4. 您可以将多个函数上报后关联至同一个应用，便可查看调用链路情况。如下图所示：
   ![image-20210120212212888](https://main.qcloudimg.com/raw/af72b23295b1a9baed10e41f4f90fad1/image-20210120212212888.png)

更多操作指导可以查看 [博睿 Server 产品文档](https://docs.qq.com/doc/DZkFPZURGU0xPR2VF)。





## 博睿探针支持列表[](id:list)


博睿探针目前支持以下主流框架和库：

<dx-tabs>
::: Python
Python 支持的框架及库如下：

<table>
<thead>
<tr>
<th style="width: 50%;">框架</th>
<th>版本</th>
</tr>
</thead>
<tbody><tr>
<td>Flask</td>
<td>0.10及以上/1.1.2</td>
</tr>
<tr>
<td>Django</td>
<td>1.5及以上/3.1</td>
</tr>
<tr>
<td>Tornado</td>
<td>3.0及以上/6.1</td>
</tr>
<tr>
<td>Web.py</td>
<td>0.33及以上/0.6.2</td>
</tr>
<tr>
<td>Pyramid</td>
<td>1.3及以上/1.10.5</td>
</tr>
<tr>
<td>Bottle</td>
<td>0.12及以上/0.12.19</td>
</tr>
<tr>
<td>Cherrypy</td>
<td>10.0及以上/18.6.0</td>
</tr>
<tr>
<td>Sanic</td>
<td>0.5.0及以上/20.9.1</td>
</tr>
<tr>
<td>Odoo</td>
<td>8.0及其以上/14.0</td>
</tr>
<tr>
<td>fastapi</td>
<td>0.23.0及以0.63.0</td>
</tr>
<tr>
<td>quart</td>
<td>0.11.0及以0.14.1</td>
</tr>
<tr>
<td>starlette</td>
<td>0.12.0及以上0.14.1</td>
</tr>
<tr>
<td>Pymysql</td>
<td>0.7.1及以上/0.10.1</td>
</tr>
<tr>
<td>mysqlclient</td>
<td>1.3.0及以上/2.0.1</td>
</tr>
<tr>
<td>mysql-connector-python</td>
<td>8.0.5及以上/8.0.22</td>
</tr>
<tr>
<td>psycopg2</td>
<td>2.6.2及以上/2.8.6</td>
</tr>
<tr>
<td>Cx-Oracle</td>
<td>6.0及以上/8.0.1</td>
</tr>
<tr>
<td>pyhive</td>
<td>0.1.6及以上/0.6.3</td>
</tr>
<tr>
<td>Pymongo</td>
<td>3.3.0及以上/3.11.1</td>
</tr>
<tr>
<td>python-memcached</td>
<td>1.57及以上/1.5.9</td>
</tr>
<tr>
<td>pyssdb</td>
<td>0.4.0及以上/0.4.2</td>
</tr>
<tr>
<td>redis</td>
<td>2.10.0及以上/3.5.3</td>
</tr>
<tr>
<td>redis-py-cluster</td>
<td>0.1.0及以上/2.1.0</td>
</tr>
<tr>
<td>urllib3</td>
<td>1.18及以上/1.26.2</td>
</tr>
<tr>
<td>requests</td>
<td>2.12.0及以上/2.25.0</td>
</tr>
<tr>
<td>httplib/http</td>
<td>标准库</td>
</tr>
<tr>
<td>tornado_httpclient</td>
<td>3.1及以上6.1</td>
</tr>
<tr>
<td>elasticsearch</td>
<td>5.2.0及以上/7.10.0</td>
</tr>
<tr>
<td>grpcio</td>
<td>1.0.0及以上/1.33.2</td>
</tr>
<tr>
<td>xmlrpclib</td>
<td>python 2.6/2.7</td>
</tr>
<tr>
<td>xmlrpc</td>
<td>python3.4+</td>
</tr>
<tr>
<td>thrift</td>
<td>0.10.0及以上/0.13.0</td>
</tr>
<tr>
<td>aiohttp</td>
<td>3.0.0及以上/3.7.3</td>
</tr>
<tr>
<td>kafka-python</td>
<td>1.3.0及以上/2.0.2</td>
</tr>
<tr>
<td>stomp.py</td>
<td>4.1.20及以上/6.1.0</td>
</tr>
<tr>
<td>kombu</td>
<td>3.0.30及以上/5.0.2</td>
</tr>
<tr>
<td>librabbitmq</td>
<td>1.6.0及以上2.0.0</td>
</tr>
<tr>
<td>Logging：</td>
<td>标准库</td>
</tr>
<tr>
<td>logbook</td>
<td>1.3.0及以上/1.5.3</td>
</tr>
<tr>
<td>Eliot</td>
<td>0.8.0及以上/1.12.0</td>
</tr>
<tr>
<td>celery</td>
<td>3.1.0及以上/5.0.2</td>
</tr>
</tbody></table>

:::
::: Node.js
Node.js 支持的框架及库如下：

<table>
<thead>
<tr>
<th style="width: 50%;">框架</th>
<th>版本</th>
</tr>
</thead>
<tbody><tr>
<td>Express</td>
<td>3.4.8及以上</td>
</tr>
<tr>
<td>Koa</td>
<td>2.2.0及以上</td>
</tr>
<tr>
<td>Hapi</td>
<td>17.0.0及以上</td>
</tr>
<tr>
<td>Promise</td>
<td>8.0.1及以上</td>
</tr>
<tr>
<td>Bluebird</td>
<td>3.5.1及以上</td>
</tr>
<tr>
<td>when</td>
<td>3.7.8及以上</td>
</tr>
<tr>
<td>Async</td>
<td>2.6.0及以上</td>
</tr>
<tr>
<td>q</td>
<td>1.5.1及以上</td>
</tr>
<tr>
<td>request</td>
<td>2.18.0</td>
</tr>
<tr>
<td>superagent</td>
<td>3.6.0及以上</td>
</tr>
<tr>
<td>mysql</td>
<td>2.13.0及以上</td>
</tr>
<tr>
<td>pg</td>
<td>6.2.4及以上</td>
</tr>
<tr>
<td>ioredis</td>
<td>2.5.0及以上</td>
</tr>
<tr>
<td>redis</td>
<td>2.8.0及以上</td>
</tr>
<tr>
<td>hiredis</td>
<td>0.5.0及以上</td>
</tr>
<tr>
<td>mongodb</td>
<td>2.2.31及以上</td>
</tr>
<tr>
<td>mongoose</td>
<td>5.0.10及以上</td>
</tr>
<tr>
<td>rabbit.js</td>
<td>0.4.4及以上</td>
</tr>
<tr>
<td>amqplib</td>
<td>0.5.2及以上</td>
</tr>
</tbody></table>

:::
</dx-tabs>

