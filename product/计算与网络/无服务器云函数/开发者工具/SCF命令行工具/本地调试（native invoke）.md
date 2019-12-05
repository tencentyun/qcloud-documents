通过本地调试能力，SCF CLI 可以在本地的模拟环境中运行代码，发送模拟测试事件，并获取到函数代码的运行日志及耗时、内存占用等信息。

## 依赖组件
本地调试 native 不需要依赖 Docker，需确保系统中已经安装好 Node.js 环境。当前 native 命令仅支持 Node.js 和 Python runtime。为保证部署云端和本地运行的结果一致，建议本地安装的 runtime 版本和云端版本保持一致。例如，如在云端使用 Node.js 6.10，则本机建议也安装 Node.js 6.x 版本。

## 调试命令
SCF CLI 通过 `native invoke` 子命令完成本地触发运行。SCF 命令行工具将依据指定的函数模板配置文件，在本机的指定目录中运行相应代码，并通过指定的触发事件，实现在本地的云函数模拟运行。

### 参数说明
`scf native invoke` 命令支持的参数如下：

| 参数       | 必填 | 描述                                                         | 示例          |
| ---------- | ---- | ------------------------------------------------------------ | ------------- |
| event      | 否   | 模拟测试事件的文件来源，文件内容必须为 JSON 格式。            | event.json    |
| template   | 否   | 项目描述配置文件的路径或文件名，默认为 template.yaml。         | template.yaml |
| env-vars   | 否   | 函数运行时的环境变量配置，需要指定环境变量配置文件，内容必须为 JSON 格式。 | env.json      |
| debug-port | 否   | 函数运行时暴露的端口。在指定端口后，本地运行时将以 debug 模式启动并暴露指定端口。 | 3366          |
| debug-args | 否   | 本机中的调试器启动参数。在指定参数后，调试器启动时将传递指定参数。 |   无            |

支持选项 FUNCTION_IDENTIFIER 说明如下：

| 参数                | 必填 | 描述                                                         | 示例        |
| ------------------- | ---- | ------------------------------------------------------------ | ----------- |
| FUNCTION_IDENTIFIER | 否   | 指明函数的标识、名称；在项目描述配置文件中如果有多个函数描述，可以通过此参数指定需要调试的函数。 | hello_world |

### 测试模拟事件
用于在本地触发云函数的模拟事件，可以通过 Linux 的命令管道传递，也可以通过文件传递。
- **通过命令管道传递：** `scf native invoke` 命令支持从命令行管道中接收事件。
 - 可通过执行 `scf native generate-event` 命令生成事件并传递，形成例如 `scf native generate-event cos post | scf native invoke ` 的调试命令。
 - 也可以自行构造输出 JSON 格式内容并传递给 `scf native invoke` 命令，形成例如 `echo '{"test":"value"}' | scf native invoke  ` 的调试命令。
- **通过文件传递：**通过使用 `scf native invoke` 命令的 `--event` 参数，指定包含有测试模拟事件内容的文件。文件内容必须为 JSON 数据结构，形成例如 `scf native invoke --event event.json ` 的调试命令。 

### 使用示例
在通过 `scf init` 初始化得到的示例项目中，均含有已准备好的代码文件及模板配置文件。以该示例项目为例，假定在环境为 Node.js 8.9下，`/Users/xxx/code/scf` 目录中创建了一个 hello_world 项目。
我们通过命令管道传递 cos post 文件的模拟事件，触发函数运行。函数代码内容仅为打印 event 并返回 “hello world”。函数代码 `/Users/xxx/code/scf/testproject/hello_world/main.js` 示例如下：
```
'use strict';
exports.main_handler = async (event, context, callback) => {
    console.log("%j", event);
    return "hello world"
};
```
1. 执行 `scf native generate-event cos post | scf native invoke` 命令，启动函数在本地运行。
```bash
Enter a event: [0m
START RequestId: 3e3e71c9-dc56-1967-c0a3-3a454e2ce634
{"Records":[{"cos":{"cosSchemaVersion":"1.0","cosObject":{"url":"http://testpic-1253970026.cos.ap-guangzhou.myqcloud.com/testfile","meta":{"x-cos-request-id":"NWMxOWY4MGFfMjViMjU4NjRfMTUyMV8yNzhhZjM=","Content-Type":""},"vid":"","key":"/1253970026/testpic/testfile","size":1029},"cosBucket":{"region":"gz","name":"testpic","appid":"1253970026"},"cosNotificationId":"unkown"},"event":{"eventName":"cos:ObjectCreated:Post","eventVersion":"1.0","eventTime":1545205770,"eventSource":"qcs::cos","requestParameters":{"requestSourceIP":"xx.xx.xx.xxx","requestHeaders":{"Authorization":"q-sign-algorithm=sha1&q-ak=AKIDQm6iUh2NJ6jL41tVUis9KpY5Rgv49zyC&q-sign-time=1545205709;1545215769&q-key-time=1545205709;1545215769&q-header-list=host;x-cos-storage-class&q-url-param-list=&q-signature=098ac7dfe9cf21116f946c4b4c29001c2b449b14"}},"eventQueue":"qcs:0:lambda:cd:appid/1253970026:default.printevent.$LATEST","reservedInfo":"","reqid":179398952}}]}
END RequestId: 3e3e71c9-dc56-1967-c0a3-3a454e2ce634
REPORT RequestId: 3e3e71c9-dc56-1967-c0a3-3a454e2ce634  Duration: 1.91 ms
Billed Duration: 100 ms Memory Size: 128 MB     Max Memory Used: 20 MB
"hello world"
```
通过输出内容可以看到，函数在本地运行完成后，输出了函数的打印日志、及函数返回内容。
2. 生成如下的 event.json 测试事件文件：
```json
{
"key1":"value1",
"key2":"value2"
}
```
3. 执行 `scf native invoke  --event event.json` 命令，启动函数在本地运行，并通过文件输出测试事件。
```bash
Enter a event: [0m
START RequestId: 6d06b0cf-4cc9-1f76-5f92-1f5871ff110a
{"key1":"value1","key2":"value2"}
END RequestId: 6d06b0cf-4cc9-1f76-5f92-1f5871ff110a
REPORT RequestId: 6d06b0cf-4cc9-1f76-5f92-1f5871ff110a  Duration: 1.72 ms
Billed Duration: 100 ms Memory Size: 128 MB     Max Memory Used: 20 MB
"hello world"
```
通过输出内容可以看到，函数代码打印了测试事件，并返回了指定内容。
