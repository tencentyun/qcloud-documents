目前支持的 Node.js 开发语言包括如下版本：
* Node.js 6.10
* Node.js 8.9
* Node.js 10.15
* Node.js 12.16

## 函数形态

Node.js 函数形态一般如下所示：
- Node.js 10.15 及 12.16
```
module.exports = (event,context,callback)=>{
	console.log(event);
	callback(null, {code:0});
}
```
或
```
module.exports = async (event,context)=>{
    console.log(event);
	return { code:0 };
}
```
- Node.js 8.9 及 6.10
```
exports.main_handler = (event, context, callback) => {
    console.log("Hello World");
    console.log(event);
    console.log(context);
    callback(null, event); 
};
```

## 执行方法

在创建云函数 SCF 时，均需要指定执行方法。在使用 Node.js 开发语言时，执行方法类似 `index.main_handler`，此处 `index` 表示执行的入口文件为 `index.js` ，`main_handler` 表示执行的入口函数为 `main_handler` 函数。在使用本地 zip 文件上传、COS 上传等方法提交代码 zip 包时，请确认 zip 包的根目录下包含有指定的入口文件，文件内有定义指定的入口函数，文件名和函数名和执行方法处填写的能够对应，避免因为无法查找到入口文件和入口函数导致的执行失败。

## 入参

Node.js 环境下的入参包括 event、context 和 callback，其中 callback 为可选参数。
* **event**：使用此参数传递触发事件数据。
* **context**：使用此参数向您的处理程序传递运行时信息。
* **callback（可选）**：使用此参数用于将您所希望的信息返回给调用方。在 Node.js 8.9 和 6.10 版本中，均可以使用 callback 来返回。在 Node.js 10.15 及 12.16 中，使用 async 描述的入口函数，需要使用 return 关键字返回，非 async 模式的入口函数，需要使用 callback 入参返回。

## 返回和异常

您的处理程序可以使用 `callback` 入参，或代码中的 `return` 关键字来返回信息。使用 callback 或 return 进行返回的支持情况如下：

<table>
<thead>
<tr>
<th>Node.js 版本</th>
<th>callback 支持</th>
<th>return 支持</th>
</tr>
</thead>
<tbody><tr>
<td>6.10</td>
<td>支持</td>
<td>不支持</td>
</tr>
<tr>
<td>8.9</td>
<td>支持</td>
<td>支持</td>
</tr>
<tr>
<td>10.15</td>
<td rowspan=2>非 async 入口函数</td>
<td rowspan=2>async 入口函数</td>
</tr>
<tr>
<td>12.16</td>
</tr>
</tbody></table>

- 如果使用 `callback` 进行返回，语法为：
```
callback(Error error, Object result);
```
	- **error**：可选参数，在函数执行内部失败时使用此参数返回错误内容。成功情况下可设置为 null。
	- **result**：可选参数，使用此参数返回函数成功的执行结果信息。参数需兼容 JSON.stringify 以便序列化为 JSON 格式。
- 如果使用 `return` 关键字进行返回，可直接使用 `return object` 来返回一个对象或值。
- 如果在代码中未调用 `callback` 或 `return`，云函数后台将会隐式调用，并且返回 null。

根据调用函数时的调用类型不同，返回值会有不同的处理方式。同步调用的返回值将会序列化为 JSON 格式后返回给调用方，异步调用的返回值将会被抛弃。同时，无论同步调用还是异步调用，返回值均会在函数日志中 `ret_msg` 位置显示。


## Node.js 10.15 及 12.16 的异步特性

在 Node.js 10.15 及 12.16 的 runtime 中，我们支持了将函数的同步执行返回和异步事件处理分开进行的能力：
* 入口函数的同步执行过程完成及返回后，云函数的调用将立刻返回，并将代码的返回信息返回给函数调用方。
* 同步流程处理并返回后，代码中的异步逻辑可以继续执行和处理，直到异步事件执行完成后，云函数的实际执行过程才完成和退出。

>!
>- 在这个过程中，由于云函数的日志是在整个执行过程完成后才进行收集和处理，因此在同步执行过程完成并返回时，云函数的返回信息中暂时无法提供日志、运行信息包括耗时、内存消耗等内容。具体信息可以在函数实际执行过程完成后，通过 Request Id 在日志中查询。
>- 云函数的运行时长，将按照异步事件执行完成后进行计算。如果异步事件队列一直无法清空或执行完成，将会导致函数超时。这种情况下，调用方可能已经获得了函数的正确响应结果，但是云函数的运行状态将标注为由于超时而失败，同时运行时长按超时时间统计。

Node.js 10.15 及 12.16 的同步和异步运行特性、返回时间及运行时长示例如下图所示：
![node10.15feature](https://main.qcloudimg.com/raw/ae2aaa71e19d73e6f782abf715e1ec18.png)

### Node.js 10.15 及 12.16 函数内异步特性示例

使用如下示例代码创建函数，其中使用 setTimeout 方法设置了一个2秒后执行的函数：
```
'use strict';
exports.main_handler = (event, context, callback) => {
    console.log("Hello World")
    console.log(event)
    setTimeout(timeoutfunc, 2000, 'data');
    callback(null, event); 
};

function timeoutfunc(arg) {
    console.log(`arg => ${arg}`);
}
```
在保存代码后，通过控制台测试或者通过云 API 的 Invoke 接口调用此函数，可以看到此函数在很短时间内即返回，响应时间小于1秒。
而查看函数的执行日志时，可以看到相关统计信息类似如下：
```
START RequestId: 1d71ddf8-5022-4461-84b7-e3a152403ffc
Event RequestId: 1d71ddf8-5022-4461-84b7-e3a152403ffc
2020-03-18T09:16:13.440Z	1d71ddf8-5022-4461-84b7-e3a152403ffc	Hello World
2020-03-18T09:16:13.440Z	1d71ddf8-5022-4461-84b7-e3a152403ffc	{ key1: 'test value 1', key2: 'test value 2' }
2020-03-18T09:16:15.443Z	1d71ddf8-5022-4461-84b7-e3a152403ffc	arg => data 
END RequestId: 1d71ddf8-5022-4461-84b7-e3a152403ffc
Report RequestId: 1d71ddf8-5022-4461-84b7-e3a152403ffc Duration:2005ms Memory:128MB MemUsage:13.425781MB
```
在日志中统计了2005ms的执行时间，同时日志中可以看到在2秒后输出了 `arg => data` 的内容，即相关异步操作在当前调用中执行且是在同步过程执行完成后执行的，而函数调用在异步任务执行完成后才结束。

## Node.js 8.9 及 6.10 异步事件支持
在 Node.js 8.9 及 6.10 中同样支持异步事件，但目前未支持同步处理完成后立刻返回。在入口函数中调用 callback 后，云函数后台会等待异步事件处理完成，且事件队列为空后才会完成函数的调用返回以及结束此次调用。

因此，如下代码：
```
'use strict';

exports.callback_handler = function(event, context, callback) {
    console.log("event = " + event);
    console.log("before callback");
    setTimeout(
        function(){
            console.log(new Date);
            console.log("timeout before callback");
        }, 
        500
    );
    callback(null, "success callback");
    console.log("after callback");
};
```
实际日志输出结果为：
```
2018-06-14T08:07:16.545Z	f3cb1ef4-6fa9-11e8-aa8a-525400c7c826	event = [object Object]
2018-06-14T08:07:16.546Z	f3cb1ef4-6fa9-11e8-aa8a-525400c7c826	before callback
2018-06-14T08:07:16.546Z	f3cb1ef4-6fa9-11e8-aa8a-525400c7c826	after callback
2018-06-14T08:07:17.047Z	f3cb1ef4-6fa9-11e8-aa8a-525400c7c826	2018-06-14T08:07:17.047Z
2018-06-14T08:07:17.048Z	f3cb1ef4-6fa9-11e8-aa8a-525400c7c826	timeout before callback
```

可以看到，setTimeout 设置的异步任务在 callback 执行后执行，函数在异步任务完成后才实际返回。


## 关闭事件循环等待

由于部分外部引入的库的原因，可能会导致事件循环持续不为空。这种情况将会在某些条件下导致函数无法返回直至超时。为了避免外部库的影响，可以通过关闭事件循环等待来自行控制函数的返回时机。通过如下方式，可以修改默认的回调行为，避免等待事件循环为空。
* 设置 `context.callbackWaitsForEmptyEventLoop` 为 false。
通过在 callback 回调执行前设置 `context.callbackWaitsForEmptyEventLoop = false;` ，可以使云函数后台在 callback 回调被调用后立刻冻结进程，不再等待事件循环内的事件，而在同步过程完成后立刻返回。

## 日志

您可以在程序中使用如下语句来完成日志输出：

- console.log()
- console._stdout.write()
- process.stdout.write()


例如，执行以下代码，可以在函数日志中查询输出内容。
``` node.js
'use strict';
exports.main_handler = async (event, context) => {
    console.log("Hello World")
    console._stdout.write("Hello World")
    process.stdout.write("Hello World")
    return event
};
```

## 如何安装依赖

请参考 [依赖安装](https://cloud.tencent.com/document/product/583/39780) 及 [在线依赖安装](https://cloud.tencent.com/document/product/583/37920)。

## 已包含的库及使用方法

### COS SDK

云函数的运行环境内已包含 [COS 的 Node.js SDK](https://cloud.tencent.com/document/product/436/8629)，具体版本为 `cos-nodejs-sdk-v5`。

可在代码内通过如下方式引入 COS SDK 并使用：
```
var COS = require('cos-nodejs-sdk-v5');
```
更详细的 COS SDK 使用说明请参见 [COS Node.js SDK](https://cloud.tencent.com/document/product/436/8629)。

### 环境内的内置库

- Node.js 12.16 运行时内已支持的库如下表：
<table><thead>
<tr><th width="60%">库名称</th><th width="40%">版本</th></tr>
</thead>
<tbody><tr>
<td align="left">cos-nodejs-sdk-v5</td>
<td align="left">2.5.20</td>
</tr>
<tr>
<td align="left">base64-js</td>
<td align="left">1.3.1</td>
</tr>
<tr>
<td align="left">buffer</td>
<td align="left">5.5.0</td>
</tr>
<tr>
<td align="left">crypto-browserify</td>
<td align="left">3.12.0</td>
</tr>
<tr>
<td align="left">ieee754</td>
<td align="left">1.1.13</td>
</tr>
<tr>
<td align="left">imagemagick</td>
<td align="left">0.1.3</td>
</tr>
<tr>
<td align="left">isarray</td>
<td align="left">2.0.5</td>
</tr>
<tr>
<td align="left">jmespath</td>
<td align="left">0.15.0</td>
</tr>
<tr>
<td align="left">lodash</td>
<td align="left">4.17.15</td>
</tr>
<tr>
<td align="left">microtime</td>
<td align="left">3.0.0</td>
</tr>
<tr>
<td align="left">npm</td>
<td align="left">6.13.4</td>
</tr>
<tr>
<td align="left">punycode</td>
<td align="left">2.1.1</td>
</tr>
<tr>
<td align="left">puppeteer</td>
<td align="left">2.1.1</td>
</tr>
<tr>
<td align="left">qcloudapi-sdk</td>
<td align="left">0.2.1</td>
</tr>
<tr>
<td align="left">querystring</td>
<td align="left">0.2.0</td>
</tr>
<tr>
<td align="left">request</td>
<td align="left">2.88.2</td>
</tr>
<tr>
<td align="left">sax</td>
<td align="left">1.2.4</td>
</tr>
<tr>
<td align="left">scf-nodejs-serverlessdb-sdk</td>
<td align="left">1.1.0</td>
</tr>
<tr>
<td align="left">tencentcloud-sdk-nodejs</td>
<td align="left">3.0.147</td>
</tr>
<tr>
<td align="left">url</td>
<td align="left">0.11.0</td>
</tr>
<tr>
<td align="left">uuid</td>
<td align="left">7.0.3</td>
</tr>
<tr>
<td align="left">xml2js</td>
<td align="left">0.4.23</td>
</tr>
<tr>
<td align="left">xmlbuilder</td>
<td align="left">15.1.0</td>
</tr>
</tbody></table>

- Node.js 10.15 运行时内已支持的库如下表：
<table>
<thead>
<tr><th width="60%">库名称</th><th width="40%">版本</th></tr>
</thead>
<tbody><tr>
<td align="left">cos-nodejs-sdk-v5</td>
<td align="left">2.5.14</td>
</tr>
<tr>
<td align="left">base64-js</td>
<td align="left">1.3.1</td>
</tr>
<tr>
<td align="left">buffer</td>
<td align="left">5.4.3</td>
</tr>
<tr>
<td align="left">crypto-browserify</td>
<td align="left">3.12.0</td>
</tr>
<tr>
<td align="left">ieee754</td>
<td align="left">1.1.13</td>
</tr>
<tr>
<td align="left">imagemagick</td>
<td align="left">0.1.3</td>
</tr>
<tr>
<td align="left">isarray</td>
<td align="left">2.0.5</td>
</tr>
<tr>
<td align="left">jmespath</td>
<td align="left">0.15.0</td>
</tr>
<tr>
<td align="left">lodash</td>
<td align="left">4.17.15</td>
</tr>
<tr>
<td align="left">microtime</td>
<td align="left">3.0.0</td>
</tr>
<tr>
<td align="left">npm</td>
<td align="left">6.4.1</td>
</tr>
<tr>
<td align="left">punycode</td>
<td align="left">2.1.1</td>
</tr>
<tr>
<td align="left">puppeteer</td>
<td align="left">2.0.0</td>
</tr>
<tr>
<td align="left">qcloudapi-sdk</td>
<td align="left">0.2.1</td>
</tr>
<tr>
<td align="left">querystring</td>
<td align="left">0.2.0</td>
</tr>
<tr>
<td align="left">request</td>
<td align="left">2.88.0</td>
</tr>
<tr>
<td align="left">sax</td>
<td align="left">1.2.4</td>
</tr>
<tr>
<td align="left">scf-nodejs-serverlessdb-sdk</td>
<td align="left">1.0.1</td>
</tr>
<tr>
<td align="left">tencentcloud-sdk-nodejs</td>
<td align="left">3.0.104</td>
</tr>
<tr>
<td align="left">url</td>
<td align="left">0.11.0</td>
</tr>
<tr>
<td align="left">uuid</td>
<td align="left">3.3.3</td>
</tr>
<tr>
<td align="left">xml2js</td>
<td align="left">0.4.22</td>
</tr>
<tr>
<td align="left">xmlbuilder</td>
<td align="left">13.0.2</td>
</tr>
</tbody></table>

- Node.js 8.9 运行时内已支持的库如下表：
<table>
<thead>
<tr><th width="60%">库名称</th><th width="40%">版本</th></tr>
</thead>
<tbody><tr>
<td align="left">cos-nodejs-sdk-v5</td>
<td align="left">2.5.8</td>
</tr>
<tr>
<td align="left">base64-js</td>
<td align="left">1.2.1</td>
</tr>
<tr>
<td align="left">buffer</td>
<td align="left">5.0.7</td>
</tr>
<tr>
<td align="left">crypto-browserify</td>
<td align="left">3.11.1</td>
</tr>
<tr>
<td align="left">ieee754</td>
<td align="left">1.1.8</td>
</tr>
<tr>
<td align="left">imagemagick</td>
<td align="left">0.1.3</td>
</tr>
<tr>
<td align="left">isarray</td>
<td align="left">2.0.2</td>
</tr>
<tr>
<td align="left">jmespath</td>
<td align="left">0.15.0</td>
</tr>
<tr>
<td align="left">lodash</td>
<td align="left">4.17.4</td>
</tr>
<tr>
<td align="left">npm</td>
<td align="left">5.6.0</td>
</tr>
<tr>
<td align="left">punycode</td>
<td align="left">2.1.0</td>
</tr>
<tr>
<td align="left">puppeteer</td>
<td align="left">1.14.0</td>
</tr>
<tr>
<td align="left">qcloudapi-sdk</td>
<td align="left">0.1.5</td>
</tr>
<tr>
<td align="left">querystring</td>
<td align="left">0.2.0</td>
</tr>
<tr>
<td align="left">request</td>
<td align="left">2.87.0</td>
</tr>
<tr>
<td align="left">sax</td>
<td align="left">1.2.4</td>
</tr>
<tr>
<td align="left">tencentcloud-sdk-nodejs</td>
<td align="left">3.0.56</td>
</tr>
<tr>
<td align="left">url</td>
<td align="left">0.11.0</td>
</tr>
<tr>
<td align="left">uuid</td>
<td align="left">3.1.0</td>
</tr>
<tr>
<td align="left">xml2js</td>
<td align="left">0.4.17</td>
</tr>
<tr>
<td align="left">xmlbuilder</td>
<td align="left">9.0.1</td>
</tr>
</tbody></table>




- Node.js 6.10 运行时内已支持的库如下表：
<table>
<thead>
<tr><th width="60%">库名称</th><th width="40%">版本</th></tr>
</thead>
<tbody><tr>
<td align="left">base64-js</td>
<td align="left">1.2.1</td>
</tr>
<tr>
<td align="left">buffer</td>
<td align="left">5.0.7</td>
</tr>
<tr>
<td align="left">cos-nodejs-sdk-v5</td>
<td align="left">2.0.7</td>
</tr>
<tr>
<td align="left">crypto-browserify</td>
<td align="left">3.11.1</td>
</tr>
<tr>
<td align="left">ieee754</td>
<td align="left">1.1.8</td>
</tr>
<tr>
<td align="left">imagemagick</td>
<td align="left">0.1.3</td>
</tr>
<tr>
<td align="left">isarray</td>
<td align="left">2.0.2</td>
</tr>
<tr>
<td align="left">jmespath</td>
<td align="left">0.15.0</td>
</tr>
<tr>
<td align="left">lodash</td>
<td align="left">4.17.4</td>
</tr>
<tr>
<td align="left">npm</td>
<td align="left">3.10.10</td>
</tr>
<tr>
<td align="left">punycode</td>
<td align="left">2.1.0</td>
</tr>
<tr>
<td align="left">qcloudapi-sdk</td>
<td align="left">0.1.5</td>
</tr>
<tr>
<td align="left">querystring</td>
<td align="left">0.2.0</td>
</tr>
<tr>
<td align="left">request</td>
<td align="left">2.87.0</td>
</tr>
<tr>
<td align="left">sax</td>
<td align="left">1.2.4</td>
</tr>
<tr>
<td align="left">tencentcloud-sdk-nodejs</td>
<td align="left">3.0.10</td>
</tr>
<tr>
<td align="left">url</td>
<td align="left">0.11.0</td>
</tr>
<tr>
<td align="left">uuid</td>
<td align="left">3.1.0</td>
</tr>
<tr>
<td align="left">xml2js</td>
<td align="left">0.4.17</td>
</tr>
<tr>
<td align="left">xmlbuilder</td>
<td align="left">9.0.1</td>
</tr>
</tbody></table>




## 相关操作
您可参考以下文档，使用相关功能：
- [使用 SCF 连接数据库](https://cloud.tencent.com/document/product/583/38012)
- [网络配置管理](https://cloud.tencent.com/document/product/583/38202)
- [角色与授权](https://cloud.tencent.com/document/product/583/32389)
