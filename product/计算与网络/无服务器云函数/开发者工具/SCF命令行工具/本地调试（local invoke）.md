通过本地调试能力，我们可以在本地的模拟环境中运行代码，发送模拟测试事件，并获取到函数代码的运行日志及耗时、内存占用等信息。

## 依赖组件
在运行本地调试前，需确保本地环境中已经安装并启动 Docker。Docker 的安装及配置过程可以参考 [安装与配置](https://cloud.tencent.com/document/product/583/33449)。

## 调试命令
SCF CLI 通过 `local invoke` 子命令完成本地触发运行。SCF 命令行工具将依据指定的函数模板配置文件，启动容器实例，将代码目录挂载到容器实例的指定目录中，并通过指定的触发事件，运行代码，实现在本地的云函数模拟运行。

### 参数说明
`scf local invoke` 命令支持的参数如下：

| 参数                  | 必填 | 描述                                                         | 示例                           |
| --------------------- | ---- | ------------------------------------------------------------ | ------------------------------ |
| event                 | 否   | 模拟测试事件的文件来源，文件内容必须为 JSON 格式。             | event.json                     |
| template              | 否   | 项目描述配置文件的路径或文件名，默认为 template.yaml。         | template.yaml                  |
| env-vars              | 否   | 函数运行时的环境变量配置，需要指定环境变量配置文件，内容必须为 JSON 格式。 | env.json                       |
| debug-port            | 否   | 函数运行时暴露的端口。在指定端口后，容器运行时将以 debug 模式启动并暴露指定端口。 | 3366                           |
| debugger-path         | 否   | 本机中的调试器路径。在指定路径后，容器运行时将会把调试器挂载到容器中。 | /root/debugger/pydev           |
| debug-args            | 否   | 本机中的调试器启动参数。在指定参数后，调试器启动时将传递指定参数。 |   无                             |
| docker-volume-basedir | 否   | 指定挂载到容器中的路径。                                       | /User/xxx/code/project         |
| docker-network        | 否   | 指定容器使用的网络，默认使用 bridge 模式。                     | bridge                         |
| log-file              | 否   | 指定输出日志到文件。                                           | /User/xxx/code/project/log.txt |
| skip-pull-image       | 否   | 跳过检查和拉取新的容器镜像。                                   |   无                             |

支持选项 FUNCTION_IDENTIFIER 说明如下：

| 参数                | 必填 | 描述                                                         | 示例        |
| ------------------- | ---- | ------------------------------------------------------------ | ----------- |
| FUNCTION_IDENTIFIER | 否   | 指明函数的标识、名称；在项目描述配置文件中如果有多个函数描述，可以通过此参数指定需要调试的函数。 | hello_world |


### 测试模拟事件
用于在本地触发云函数的模拟事件，可以通过 Linux 的命令管道传递，也可以通过文件传递。
- **通过命令管道传递：** `scf local invoke` 命令支持从命令行管道中接收事件。
 - 可通过执行 `scf local generate-event` 命令生成事件并传递，形成例如 `scf local generate-event cos post | scf local invoke` 的调试命令。
 - 也可以自行构造输出 JSON 格式内容并传递给 `scf local invoke` 命令，形成例如 `echo '{"test":"value"}' | scf local invoke` 的调试命令。
- **通过文件传递：**通过使用 `scf local invoke` 命令的 `--event` 参数，指定包含有测试模拟事件内容的文件。文件内容必须为 JSON 数据结构，形成例如 `scf local invoke --event event.json` 的调试命令。 

### 使用示例
在通过 `scf init` 初始化得到的示例项目中，均带有已准备好的代码文件及模板配置文件。以该示例项目为例，假定在环境为 Python 2.7 下，`/Users/xxx/code/scf` 目录中创建了一个 testproject 项目。
我们通过命令管道传递 cos post 文件的模拟事件，触发函数运行。函数代码内容仅为打印 event 并返回 “hello world”。函数代码 `/Users/xxx/code/scf/testproject/hello_world/main.py` 示例如下：
```python
# -*- coding: utf8 -*-
def main_handler(event, context):
    print(event)
    return "hello world"

```
1. 执行 `scf local generate-event cos post | scf local invoke` 命令，启动函数在本地运行。
```bash
$ scf local generate-event cos post | scf local invoke 
read event from stdin
pull image ccr.ccs.tencentyun.com/scfrepo/scfcli:python3.6......
START RequestId: 766e10b0-fd41-42ed-acd4-c161833e3bd2
{'Records': [{'cos': {'cosSchemaVersion': '1.0', 'cosObject': {'url': 'http://testpic-1253970026.cos.ap-guangzhou.myqcloud.com/testfile', 'meta': {'Content-Type': '', 'x-cos-request-id': 'NWMxOWY4MGFfMjViMjU4NjRfMTUyMV8yNzhhZjM='}, 'key': '/1253970026/testpic/testfile', 'vid': '', 'size': 1029}, 'cosBucket': {'region': 'gz', 'name': 'testpic', 'appid': '1253970026'}, 'cosNotificationId': 'unkown'}, 'event': {'eventVersion': '1.0', 'eventTime': 1545205770, 'requestParameters': {'requestSourceIP': '59.37.125.38', 'requestHeaders': {'Authorization': 'q-sign-algorithm=sha1&q-ak=AKIDQm6iUh2NJ6jL41tVUis9KpY5Rgv49zyC&q-sign-time=1545205709;1545215769&q-key-time=1545205709;1545215769&q-header-list=host;x-cos-storage-class&q-url-param-list=&q-signature=098ac7dfe9cf21116f946c4b4c29001c2b449b14'}}, 'eventName': 'cos:ObjectCreated:Post', 'reqid': 179398952, 'eventSource': 'qcs::cos', 'eventQueue': 'qcs:0:lambda:cd:appid/1253970026:default.printevent.$LATEST', 'reservedInfo': ''}}]}
END RequestId: 766e10b0-fd41-42ed-acd4-c161833e3bd2
REPORT RequestId: 766e10b0-fd41-42ed-acd4-c161833e3bd2 Duration: 0 ms Billed Duration: 100 ms Memory Size: 128 MB Max Memory Used: 15 MB
"hello world"
```
通过输出内容可以看到，函数运行完成后，输出了函数的打印日志、及函数返回内容。
2. 生成如下的 event.json 测试事件文件。
```json
{
"key1":"value1",
"key2":"value2"
}
```
3. 执行 `scf local invoke --event event.json` 命令，启动函数在本地运行，并通过文件输出测试事件。
```bash
$ scf local invoke --event event.json 
pull image ccr.ccs.tencentyun.com/scfrepo/scfcli:python3.6......
START RequestId: 4a06d73d-e716-4e58-bc5f-ecfc955d77bd
{'key1': 'value1', 'key2': 'value2'}
END RequestId: 4a06d73d-e716-4e58-bc5f-ecfc955d77bd
REPORT RequestId: 4a06d73d-e716-4e58-bc5f-ecfc955d77bd Duration: 0 ms Billed Duration: 100 ms Memory Size: 128 MB Max Memory Used: 15 MB
"hello world"
```
通过输出内容可以看到，函数代码打印了测试事件，并返回了指定内容。
