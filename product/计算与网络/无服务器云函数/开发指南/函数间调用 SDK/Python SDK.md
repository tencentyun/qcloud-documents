## Tencentserverless SDK 简介

Tencentserverless 是腾讯云云函数 SDK，集成云函数业务流接口，简化云函数的调用方法。在使用该 SDK 的情况下，用户可以方便的从本地、云服务器（CVM）、容器、以及云端函数里快速调用某一个云函数，无需再进行公有云 API 的接口封装。

## 功能特性

Tencentserverless SDK 的功能特性可分为以下几点：

* 高性能，低时延的进行函数调用。
* 填写必须的参数后，即可快速进行函数间的调用（SDK 会默认获取环境变量中的参数，例如 region，SecretId 等）。
* 支持内网域名的访问。
* 支持 keepalive 能力。
* 支持跨地域函数调用。
* 支持 Python 原生调用方式。

## 快速开始

### 云端函数互调

#### 示例

>!
>
>- 不同地域下的函数互调，须指定地域，命名规则参见 [地域列表](https://cloud.tencent.com/document/api/583/17238#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
>- 如果不指定地域，默认为同地域下函数互调。
>- 命名空间不指定，默认为 default。

1. 在云端创建一个被调用的 Python 云函数，地域为**广州**，命名为 “FuncInvoked”。函数内容如下：
``` python
# -*- coding: utf8 -*-

def main_handler(event, context):
	if 'key1' in event.keys():
		print("value1 = " + event['key1'])
	if 'key2' in event.keys():
		print("value2 = " + event['key2'])
	return "Hello World from the function being invoked"  #return

```

2. 在云端创建调用的 Python 云函数，地域为**成都**，命名为 “PythonInvokeTest”。可通过以下两种方式，结合您的实际情况编辑 PythonInvokeTest 函数。

 - 方式 1：如果您不需要频繁的调用函数，可使用如下示例代码：
<dx-codeblock>
:::  python
from tencentserverless import scf 
from tencentserverless.scf import Client
from tencentserverless.exception import TencentServerlessSDKException
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

def main_handler(event, context):
	print("prepare to invoke a function!")
	try:
		data = scf.invoke('FuncInvoked',region="ap-guangzhou",data={"a": "b"})
		print (data)
	except TencentServerlessSDKException as e:
    	print (e)
	except TencentCloudSDKException as e:
    	print (e)
	except Exception as e:
    	print (e)
	return "Already invoked a function!" # return

:::
</dx-codeblock>
输出结果如下：
```shell
"Already invoked a function!"
```

 - 方式 2：如果您需要频繁调用函数，可选择通过 Client 的方式连接并触发。可使用如下示例代码：
<dx-codeblock>
:::  python
# -*- coding: utf8 -*-

from tencentserverless import scf 
from tencentserverless.scf import Client
from tencentserverless.exception import TencentServerlessSDKException
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

def main_handler(event, context):
	#scf = Client(region="ap-guangzhou") # 使用该方法进行 Client 连接，请在函数配置中启用“运行角色”功能，并选择具有调用函数权限的运行角色。
	scf = Client(secret_id="AKIxxxxxxxxxxxxxxxxxxxxxxggB4Sa",secret_key="3vZzxxxxxxxxxxxaeTC",region="ap-guangzhou",token=" ")# 使用该方法进行 Client 连接，请将 secret_id 和 secret_key 替换为您的 secret_id 和 secret_key，该组密钥需要包含调用函数的权限。
	print("prepare to invoke a function!")
	try:
    	data = scf.invoke('FuncInvoked',data={"a": "b"})
    	# data = scf.FuncInvoked(data={"a": "b"}) #使用Python原生调用方式，需要首先通过Client进行初始化
    	print (data)
	except TencentServerlessSDKException as e:
    	print (e)
	except TencentCloudSDKException as e:
    	print (e)
	except Exception as e:
    	print (e)
	return "Already invoked a function!" # return
:::
</dx-codeblock>
输出结果如下：
```shell
"Already invoked a function!"
```
>! secret_id 及 secret_key：指云 API 的密钥 ID 和密钥 Key。您可以通过登录 **[访问管理控制台](https://console.cloud.tencent.com/cam/overview)**，选择**云 API 密钥** >  **[API 密钥管理](https://console.cloud.tencent.com/cam/capi)**，获取相关密钥或创建相关密钥。


### 本地调用云端函数

#### 开发准备

- 开发环境
  已安装 Python2.7 或者 Python3.6。
- 运行环境
  已安装 tencentserverless SDK，支持 Windows、Linux 和 Mac 操作系统。

>? 本地调用云端函数须进行以上开发准备，推荐函数在本地开发完成后上传到云端，使用云端函数互调进行调试。



#### 通过 pip 安装（推荐）

执行以下命令，安装 tencentserverless Python SDK。

```shell
pip install tencentserverless
```




#### 通过源码包安装

前往 [Github 代码托管地址](https://github.com/tencentyun/tencent-serverless-python)下载最新源码包，待源码包解压后依次执行以下命令进行安装。

```shell
cd tencent-serverless-python
python setup.py install
```



#### 配置 tencentserverless Python SDK

执行以下命令，升级 tencentserverless Python SDK。

```shell
pip install tencentserverless -U
```

执行以下命令，查看 tencentserverless Python SDK 信息。

```shell
pip show tencentserverless
```

#### 示例

1. 在云端创建一个被调用的 Python 云函数，地域为**广州**，命名为 “FuncInvoked”。函数内容如下：
``` python
# -*- coding: utf8 -*-

def main_handler(event, context):
	if 'key1' in event.keys():
		print("value1 = " + event['key1'])
	if 'key2' in event.keys():
		print("value2 = " + event['key2'])
	return "Hello World from the function being invoked"  #return
```

2. 创建完毕后，在本地创建一个名为 PythonInvokeTest.py 的文件。内容如下：
``` python
# -*- coding: utf8 -*-

from tencentserverless import scf 
from tencentserverless.scf import Client
from tencentserverless.exception import TencentServerlessSDKException
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

def main_handler(event, context):
	print("prepare to invoke a function!")
	scf = Client(secret_id="AKIxxxxxxxxxxxxxxxxxxxxxxggB4Sa",secret_key="3vZzxxxxxxxxxxxaeTC",region="ap-guangzhou",token=" ")# 替换为您的 secret_id 和 secret_key
	try:
		data = scf.invoke('FuncInvoked',data={"a":"b"}) 
		# data = scf.FuncInvoked(data={"a":"b"}) 
		print (data)
	except TencentServerlessSDKException as e:
		print (e)
	except TencentCloudSDKException as e:
		print (e)
	except Exception as e:
		print (e)
	return "Already invoked a function!" # return

main_handler("","")


```

进入 PythonInvokeTest.py 所在文件目录，执行以下命令，查看结果。
```python
python PythonInvokeTest.py
```

输出结果如下：
```shell
prepare to invoke a function!"Hello World form the function being invoked"
```

   

## 接口列表

### API Reference

- [Client](#client)（类）
- [invoke](#invoke) （方法）
- [TencentserverlessSDKException](#TencentserverlessSDKException) （类）

#### Client

**方法：**

- **\_\_init__** 

 **参数信息：**

 <table>
	<tr>
	<th>参数名</th> <th>是否必填</th> <th>类型</th> <th>描述</th>
	</tr>
	<tr>
	<td>region </td> 	<td>否</td> 	<td><code>String</code></td>
		<td>地域信息，默认与调用接口的函数所属地域相同，本地调用默认是广州。</td>
	</tr>
	<tr>
	<td>secret_id</td> 	<td>否</td> 	<td><code>String</code></td>
		<td>用户 SecretId， 默认是从云函数环境变量中获取，<b>本地调试必填</b>。</td>
	</tr>
	<tr>
	<td>secret_key</td> 	<td>否</td> 	<td><code>String</code></td>
		<td>用户 SecretKey， 默认是从云函数环境变量中获取，<b>本地调试必填</b>。</td>
	</tr>
	<tr>
		<td>token</td> 	<td>否</td> 	<td><code>String</code></td>
		<td>用户 token，默认是从云函数环境变量中获取</td>
	</tr>
</table>




- **invoke**

 **参数信息：**

 <table>
	<tr>
	<th>参数名</th> <th>是否必填</th> <th>类型</th> <th>描述</th>
	</tr>
	<tr>
		<td>function_name</td> <td>是</td> <td><code>String</code></td> 
		<td>函数名称。</td>
	</tr>
	<tr>
		<td>qualifier</td> <td>否</td> <td><code>String</code></td>
		<td>函数版本，默认为 $LATEST。</td>
	</tr>
	<tr>
		<td>data</td> <td>否</td> <td><code>Object</code></td>
		<td>函数运行入参，必须可以被 json.dumps 的对象。</td>
	</tr>
	<tr>
		<td>namespace</td> <td>否</td> <td><code>String</code></td>
		<td>命名空间，默认为 default。</td>
	</tr>
</table>




#### invoke

调用函数，暂时只支持同步调用。

**参数信息：**

| 参数名        | 是否必填 | 类型     | 描述                                                         |
| ------------- | -------- | -------- | ------------------------------------------------------------ |
| region        | 否       | `String` | 地域信息，默认与调用接口的函数所属地域相同，本地调用默认是广州。 |
| secret_id     | 否       | `String` | 用户 SecretId， 默认是从云函数环境变量中获取，**本地调试必填**。 |
| secret_key    | 否       | `String` | 用户 SecretKey， 默认是从云函数环境变量中获取，**本地调试必填**。 |
| token         | 否       | `String` | 用户 token，默认从云函数环境变量中获取。                     |
| function_name | 是       | `String` | 函数名称。                                                   |
| qualifier     | 否       | `String` | 函数版本，默认为 $LATEST。                                   |
| data          | 否       | `String` | 函数运行入参，必须可以被 json.dumps 的对象。                 |
| namespace     | 否       | `String` | 命名空间，默认为 default。                                   |

[](id:TencentserverlessSDKException)

#### TencentserverlessSDKException

**属性：**

- [**code**]
- [**message**]
- [**request_id**]
- [**response**]
- [**stack_trace**]

**方法及描述：**

| 方法名          | 描述                  |
| --------------- | --------------------- |
| get_code        | 返回错误码信息        |
| get_message     | 返回错误信息          |
| get_request_id  | 返回 RequestId 信息   |
| get_response    | 返回 response 信息    |
| get_stack_trace | 返回 stack_trace 信息 |
