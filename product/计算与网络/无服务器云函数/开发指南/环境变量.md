在创建或编辑云函数时，您可以通过修改配置中的环境变量，为云函数的运行环境增加、删除或修改环境变量。

在配置环境变量后，环境变量将在函数运行时配置到所在的操作系统环境中。函数代码可以使用读取系统环境变量的方式来获取到设置的具体值并在代码中使用。

## 新增环境变量
### 使用控制台新增环境变量
1. 登录云函数控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在创建函数的过程中，或针对已创建的函数进行编辑时，可在“环境变量”中，增加环境变量。
环境变量通常以 `key-value` 对的形式出现，请在环境变量的输入框中，前一输入框输入所需的环境变量 key，后一输入框输入所需的环境变量 value。

### 本地新增环境变量
本地开发时，可以直接在 `serverless.yml` 中的函数下配置环境变量 Environment ，然后执行 `sls deploy` 命令部署到云端。如下所示：
```yaml
component: scf # (必选) 组件名称，在该实例中为scf
name: scfdemo # (必选) 组件实例名称。

#组件参数配置
inputs:
  name: scfdemo # 云函数名称，默认为 ${name}-${stage}-${app}
  namespace: default
  # 1. 默认写法，新建特定命名的 cos bucket 并上传
  src: ./src
  type: event # 函数类型，默认为 event(事件类型)，web(web类型)
  handler: index.main_handler #入口（函数类型为事件类型时生效）
  runtime: Nodejs10.15 # 运行环境 默认 Nodejs10.15
  region: ap-guangzhou # 函数所在区域
  description: This is a function in ${app} application.
  memorySize: 128 # 内存大小，单位MB
  timeout: 20 # 函数执行超时时间，单位秒
  initTimeout: 3 # 初始化超时时间，单位秒
  environment: #  环境变量
    variables: #  环境变量对象
      TEST1: value1
      TEST2: value2
```

## 查看环境变量

在配置好云函数的环境变量后，可通过查看云函数的函数配置，查询到具体已配置的环境变量，环境变量以 `key=value` 的形式显示。


## 使用环境变量

已配置的环境变量，会在函数运行时配置到函数所在的运行环境中，可通过代码读取系统环境变量的方式来获取到具体值并在代码中使用。需要注意的是，**环境变量无法在本地进行读取**。
假设针对云函数，配置的环境变量的 key 为 `key`，以下为各运行环境读取并打印此环境变量值的示例代码。
- 在 Python 运行环境中，读取环境变量的方法为：
```
import os
value = os.environ.get('key')
print(value)
```
- 在 Node.js 运行环境中，读取环境变量的方法为：
```
var value = process.env.key
console.log(value)
```
- 在 Java 运行环境中，读取环境变量的方法分为临时授权字段和其他字段两种情况：
 - 临时授权字段包括：`TENCENTCLOUD_SESSIONTOKEN`、`TENCENTCLOUD_SECRETID`、`TENCENTCLOUD_SECRETKEY`，读取环境变量的方法为：
```
System.out.println("value: "+ System.getProperty("key"));
```
 - 其他字段，读取环境变量的方法为：
```
System.out.println("value: "+ System.getenv("key"));
```
- 在 Golang 运行环境中，读取环境变量的方法为：
```
import "os"
var value string
value = os.Getenv("key")
```
- 在 PHP 运行环境中，读取环境变量的方法为：
```
$value = getenv('key');
```








## 使用场景

- **可变值提取**：针对业务中有可能会变动的值，提取至环境变量中，可避免需要根据业务变更而修改代码。
- **加密信息外置**：认证、加密相关的 key，从代码中提取至环境变量，可避免相关 key 硬编码在代码中而引起的安全风险。
- **环境区分**：针对不同开发阶段所要进行的配置和数据库信息，可提取到环境变量中。针对开发和发布的不同阶段，仅需要修改环境变量的值，分别执行开发环境数据库和发布环境数据库即可。

## 使用限制

针对云函数的环境变量，有如下使用限制： 
- key 必须以字母  **[a-zA-Z]** 开头，只能包含字母数字字符和下划线（ **[a-zA-Z0-9\_]**）。
- 预留的环境变量 key 无法配置。预留的 key 包括：
 - SCF\_ 开头的 key，例如 SCF\_RUNTIME。
 - QCLOUD\_ 开头的 key，例如 QCLOUD\_APPID。
 - TECENTCLOUD\_ 开头的 key，例如 TENCENTCLOUD\_SECRETID。


## 已内置环境变量

目前运行环境中已内置的环境变量的 Key 及 Value 见下表：


<table>
<thead>
<tr>
<th nowrap="nowrap">环境变量 Key</th>
<th>具体值或值来源</th>
</tr>
</thead>
<tbody><tr>
<td nowrap="nowrap"><code>TENCENTCLOUD_SESSIONTOKEN</code></td>
<td>{临时 SESSION TOKEN}</td>
</tr>
<tr>
<td><code>TENCENTCLOUD_SECRETID</code></td>
<td>{临时 SECRET ID}</td>
</tr>
<tr>
<td><code>TENCENTCLOUD_SECRETKEY</code></td>
<td>{临时 SECRET KEY}</td>
</tr>
<tr>
<td><code>_SCF_SERVER_PORT</code></td>
<td>28902</td>
</tr>
<tr>
<td><code>TENCENTCLOUD_RUNENV</code></td>
<td>SCF</td>
</tr>
<tr>
<td><code>USER_CODE_ROOT</code></td>
<td>/var/user/</td>
</tr>
<tr>
<td><code>TRIGGER_SRC</code></td>
<td>timer（使用定时触发器时）</td>
</tr>
<tr>
<td><code>PYTHONDONTWRITEBYTECODE</code></td>
<td>x</td>
</tr>
<tr>
<td><code>PYTHONPATH</code></td>
<td>/var/user:/opt</td>
</tr>
<tr>
<td><code>CLASSPATH</code></td>
<td>/var/runtime/java8:/var/runtime/java8/lib/*:/opt</td>
</tr>
<tr>
<td><code>NODE_PATH</code></td>
<td>/var/user:/var/user/node_modules:/var/lang/node6/lib/node_modules:/opt:/opt/node_modules</td>
</tr>
<tr>
<td><code>_</code></td>
<td>/var/lang/python3/bin/python3</td>
</tr>
<tr>
<td><code>PWD</code></td>
<td>/var/user</td>
</tr>
<tr>
<td><code>LOGNAME</code></td>
<td>qcloud</td>
</tr>
<tr>
<td><code>LANG</code></td>
<td>en_US.UTF8</td>
</tr>
<tr>
<td><code>LC_ALL</code></td>
<td>en_US.UTF8</td>
</tr>
<tr>
<td><code>USER</code></td>
<td>qcloud</td>
</tr>
<tr>
<td><code>HOME</code></td>
<td>/home/qcloud</td>
</tr>
<tr>
<td><code>PATH</code></td>
<td>/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin</td>
</tr>
<tr>
<td><code>SHELL</code></td>
<td>/bin/bash</td>
</tr>
<tr>
<td><code>SHLVL</code></td>
<td>3</td>
</tr>
<tr>
<td><code>LD_LIBRARY_PATH</code></td>
<td>/var/runtime/java8:/var/user:/opt</td>
</tr>
<tr>
<td><code>HOSTNAME</code></td>
<td>{host id}</td>
</tr>
<tr>
<td><code>SCF_RUNTIME</code></td>
<td>函数运行时</td>
</tr>
<tr>
<td><code>SCF_FUNCTIONNAME</code></td>
<td>函数名</td>
</tr>
<tr>
<td><code>SCF_FUNCTIONVERSION</code></td>
<td>函数版本</td>
</tr>
<tr>
<td><code>TENCENTCLOUD_REGION</code></td>
<td>区域</td>
</tr>
<tr>
<td><code>TENCENTCLOUD_APPID</code></td>
<td>账号APPID</td>
</tr>
<tr>
<td><code>TENCENTCLOUD_UIN</code></td>
<td>账号UIN</td>
</tr>
<tr>
<td><code>TENCENTCLOUD_TZ</code></td>
<td>时区，当前为UTC</td>
</tr>
</tbody></table>
