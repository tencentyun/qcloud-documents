使用博睿APM

## 准备工作

在接入[博睿 Server](https://server.bonree.com/) 之前，需要先注册博睿 Server 的账号。

>? 1. 博睿探针目前支持了多数主流框架，具体请参参照 博睿探针支持列表。只有使用这些支持的框架，博睿 smartAgent 才能自动捕获。
>
>2. 云函数需开启公网访问才可以上报至博睿。


## 使用云函数控制台接入

使用云函数控制台接入博睿包括三个步骤：探针的绑定、探针的引入以及新增环境变量。

### 绑定博睿探针

您需要下载博睿探针，将该探针上传到层并绑定在函数上。

1. 下载博睿的探针

   您可以在这里[下载博睿Serverless版探针](https://apm-1253665819.cos.ap-guangzhou.myqcloud.com/bonree-python-nodejs-agent.zip)。

2. 上传层

   在层管理页面，新建层，将下载下来的探针压缩文件上传。根据您的需要选择运行环境，目前支持Python和Node.js。

   ![image-20210120173713989](https://main.qcloudimg.com/raw/6e1ae0440abd37824d6055843d1c1691/image-20210120173713989.png)

3. 绑定层

   在函数管理，层管理中绑定刚才创建的层。

   ![image-20210120173903239](https://main.qcloudimg.com/raw/217329d4adc780e34fb4f9c4dbeeec5c/image-20210120173903239.png)


### 引入探针

绑定层以后，探针并不会自动启动，需要在代码的入口引入探针。探针的运行会占用少量内存，但不会对您的业务运行带来影响。如业务代码本身占用了大量内存，探针将触发熔断机制以保障业务运行。

#### Node.js的引入

在云函数的入口函数所在的文件`require`博睿的探针。例如您可以在 `sl_handler.js`文件中加入引入的代码。

```js
require("/opt/bonree/apm/agent/nodejs/4.0.0-Beta1/Bonree/index.js");
```

![image-20210120172640118](https://main.qcloudimg.com/raw/e955797d305de2cf3abdbf424e787a66/image-20210120172640118.png)

#### Python的引入

在云函数的入口函数所在的文件`import`博睿探针。以Flask框架为例，您可以在`sl_handler.py`文件中添加如下代码。

```Python
import sys

sys.path.insert(0, "/opt/bonree/apm/agent/python/4.1.2-Beta1")
try:
    from Bonree.autoinject import sitecustomize
except ImportError:
    pass
```

![image-20210120175012815](https://main.qcloudimg.com/raw/2fc0a90a6f1c2b600e7d5669f13d3c90/image-20210120175012815.png)


### 增加云函数的环境变量

您需要在每个绑定了博睿探针的云函数中增加环境变量，探针将根据环境变量中的账户信息上报。需要新增

| 环境变量 Key               | Value                                                      |
| -------------------------- | ---------------------------------------------------------- |
| BONREE_SMARTAGENT_SDK_PATH | /opt/bonree/apm/agent/c/2.3.2/lib/libagentsdk-x64-linux.so |
| BONREE_APM_ACCOUNT_GUID    | 博睿账户GUID                                               |

您可以在博睿 Server 产品的右上角找到GUID信息。
![image-20210120171353393](https://main.qcloudimg.com/raw/9baf607b889311465b239dc1abd5b818/image-20210120171353393.png)



## 使用Serverless Framework 接入

 您可以下载博睿探针，然后使用Serverless Framework的layer component上传。
 这里以Flask框架为例，展示如何绑定和使用博睿探针。

### 1. 下载并解压探针

   您可以在这里[下载博睿Serverless版探针](https://apm-1253665819.cos.ap-guangzhou.myqcloud.com/bonree-python-nodejs-agent.zip)。

   下载探针后，将其放在layer目录下，并解压缩。

### 2. 创建层并绑定至函数

在layer目录下解压出bonree文件夹，然后新建`serverless.yml`文件。在src目录下创建了Flask的`serverless.yml`文件。具体目录结构如下：

```
.
├── layer
│   ├── bonree
│   ├── bonree-python-nodejs-agent.zip
│   └── serverless.yml
└── src
    └── serverless.yml
```

`layer`目录下`serverless.yml`文件：

```
component: layer
name: bonree_agent
org: tencent
app: tencent
stage: dev

inputs:
  name: bonree_agent
  region: ap-beijing
  src: ./bonree
  runtimes:
    - Nodejs10.15
    - Python3.6
  description: bonree server layer
```

只使用 layer component 便可以完成层的创建。在函数中配置 layers 参数可以完成绑定的操作，您也可以选择在云函数控制台手动绑定层。
`src`目录下的`serverless.yml`文件：

```
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
        BONREE_SMARTAGENT_SDK_PATH: /opt/bonree/apm/agent/c/2.3.2/lib/libagentsdk-x64-linux.so

```

在根目录下执行`sls deploy`进行应用的部署。

### 3. 引入探针

登录[云函数](https://console.cloud.tencent.com/scf/)的控制台，进入该函数，在`sl_handler.py`文件中加入`import`探针的代码。详细内容可参考上文引入探针。

![image-20210120175012815](https://main.qcloudimg.com/raw/2fc0a90a6f1c2b600e7d5669f13d3c90/image-20210120175012815.png)

## 使用博睿 Server 

登录[博睿 Server 控制台](https://server.bonree.com/)，待数据上报至博睿，在博睿 Server 部署管理 - 部署状态 中即可查看已进行数据上报的函数。

![image-20210120210504905](https://main.qcloudimg.com/raw/3eb34d55e17d050066a17b0d69145519/image-20210120210504905.png)

将该函数关联一个应用，即可在查看应用运行的情况。详细介绍可参照：博睿Server文档

![image-20210120210813786](https://main.qcloudimg.com/raw/016e28ad12eaa979ec8d0776ad005fe5/image-20210120210813786.png)

您可以将多个函数上报后关联至同一个应用，便可以查看调用链路的情况。

![image-20210120212212888](https://main.qcloudimg.com/raw/af72b23295b1a9baed10e41f4f90fad1/image-20210120212212888.png)

## 博睿探针支持列表

Python 支持的框架及库如下：

| 框架                   | 版本                |
| ---------------------- | ------------------- |
| Flask                  | 0.10及以上/1.1.2    |
| Django                 | 1.5及以上/3.1       |
| Tornado                | 3.0及以上/6.1       |
| Web.py                 | 0.33及以上/0.6.2    |
| Pyramid                | 1.3及以上/1.10.5    |
| Bottle                 | 0.12及以上/0.12.19  |
| Cherrypy               | 10.0及以上/18.6.0   |
| Sanic                  | 0.5.0及以上/20.9.1  |
| Odoo                   | 8.0及其以上/14.0    |
| fastapi                | 0.23.0及以0.63.0    |
| quart                  | 0.11.0及以0.14.1    |
| starlette              | 0.12.0及以上0.14.1  |
| Pymysql                | 0.7.1及以上/0.10.1  |
| mysqlclient            | 1.3.0及以上/2.0.1   |
| mysql-connector-python | 8.0.5及以上/8.0.22  |
| psycopg2               | 2.6.2及以上/2.8.6   |
| Cx-Oracle              | 6.0及以上/8.0.1     |
| pyhive                 | 0.1.6及以上/0.6.3   |
| Pymongo                | 3.3.0及以上/3.11.1  |
| python-memcached       | 1.57及以上/1.5.9    |
| pyssdb                 | 0.4.0及以上/0.4.2   |
| redis                  | 2.10.0及以上/3.5.3  |
| redis-py-cluster       | 0.1.0及以上/2.1.0   |
| urllib3                | 1.18及以上/1.26.2   |
| requests               | 2.12.0及以上/2.25.0 |
| httplib/http           | 标准库              |
| tornado_httpclient     | 3.1及以上6.1        |
| elasticsearch          | 5.2.0及以上/7.10.0  |
| grpcio                 | 1.0.0及以上/1.33.2  |
| xmlrpclib              | python 2.6/2.7      |
| xmlrpc                 | python3.4+          |
| thrift                 | 0.10.0及以上/0.13.0 |
| aiohttp                | 3.0.0及以上/3.7.3   |
| kafka-python           | 1.3.0及以上/2.0.2   |
| stomp.py               | 4.1.20及以上/6.1.0  |
| kombu                  | 3.0.30及以上/5.0.2  |
| librabbitmq            | 1.6.0及以上2.0.0    |
| Logging：              | 标准库              |
| logbook                | 1.3.0及以上/1.5.3   |
| Eliot                  | 0.8.0及以上/1.12.0  |
| celery                 | 3.1.0及以上/5.0.2   |

Node.js 支持的框架及库如下：

| 框架       | 版本    |
| ---------- | ------- |
| Express    | 3.4.8+  |
| Koa        | 2.2.0+  |
| Hapi       | 17.0.0+ |
| Promise    | 8.0.1+  |
| Bluebird   | 3.5.1+  |
| when       | 3.7.8+  |
| Async      | 2.6.0+  |
| q          | 1.5.1+  |
| request    | 2.18.0  |
| superagent | 3.6.0+  |
| mysql      | 2.13.0+ |
| pg         | 6.2.4+  |
| ioredis    | 2.5.0+  |
| redis      | 2.8.0+  |
| hiredis    | 0.5.0+  |
| mongodb    | 2.2.31+ |
| mongoose   | 5.0.10+ |
| rabbit.js  | 0.4.4+  |
| amqplib    | 0.5.2+  |
