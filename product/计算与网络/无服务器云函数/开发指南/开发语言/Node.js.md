目前支持的 Node.js 开发语言包括如下版本：

* Node.js 6.10
* Node.js 8.9

## 函数形态

Node.js 函数形态一般如下所示：

```
exports.main_handler = (event, context, callback) => {
    console.log("Hello World")
    console.log(event)
    console.log(context)
    callback(null, event); 
};
```

## 执行方法

在创建 SCF 云函数时，均需要指定执行方法。使用 Node.js 开发语言时，执行方法类似 `index.main_handler`，此处 `index`表示执行的入口文件为 `index.js` ，`main_handler`表示执行的入口函数为 `main_handler` 函数。在使用 本地 zip 文件上传、COS 上传等方法提交代码 zip 包时，请确认 zip 包的根目录下包含有指定的入口文件，文件内有定义指定的入口函数，文件名和函数名和执行方法处填写的能够对应，避免因为无法查找到入口文件和入口函数导致的执行失败。

## 入参

Node.js 环境下的入参包括 event 、context 和 callback，其中 callback为可选参数。

* event：使用此参数传递触发事件数据。
* context：使用此参数向您的处理程序传递运行时信息。
* callback：使用此参数用于将您所希望的信息返回给调用方。如果没有此参数值，返回值为null。

## 返回和异常

您的处理程序需要使用 `callback` 入参来返回信息。`callback` 的语法为：

```
callback(Error error, Object result);
```

其中：

* error：可选参数，在函数执行内部失败时使用此参数返回错误内容。成功情况下可设置为null。
* result：可选参数，使用此参数返回函数成功的执行结果信息。参数需兼容 JSON.stringify 以便序列化为 JSON 格式。

如果在代码中未调用 callback，云函数后台将会隐式调用，并且返回 null。

根据调用函数时的调用类型不同，返回值会有不同的处理方式。同步调用的返回值将会序列化为 JSON 格式后返回给调用方，异步调用的返回值将会被抛弃。同时，无论同步调用还是异步调用，返回值均会在函数日志中 `ret_msg` 位置显示。

## Node.js 事件循环

由于 Node.js 大量采用了异步事件循环的方式处理回调，在云函数中运行 Node.js 代码时，同样支持异步事件。在入口函数中调用 callback 后，云函数后台会等待事件队列为空后才返回。

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


### 关闭事件循环等待

由于部分外部引入的库的原因，可能会导致事件循环持续不为空。这种情况将会导致函数无法返回，直到超时。为了避免外部库的影响，我们可以通过关闭事件循环等待，来自行控制函数的返回时机。通过如下两种方式，我们可以修改默认的回调行为，避免等待事件循环为空。

* 设置 context.callbackWaitsForEmptyEventLoop 为 false
* 使用 context.done 回调

通过在 callback 回调执行前设置 `context.callbackWaitsForEmptyEventLoop = false;` ，可以使得云函数后台在 callback 回调被调用后立刻冻结进程，不再等待事件循环内的事件，而在同步命令完成后立刻返回。

同样也可以通过使用 context.done 回调替换掉 callback 回调。context.done 回调的入参与 callback 回调入参相同。context.done 回调在被执行后同样会冻结事件循环监听的进程，在同步命令执行完成后立刻返回。

## 日志

您可以在程序中使用如下语句来完成日志输出：

* console.log()
* console.error()
* console.warn()
* console.info()

输出内容您可以在函数日志中的 `log` 位置查看。

## 已包含的库及使用方法

### COS SDK

云函数的运行环境内已包含 [COS 的 Node.js SDK](https://cloud.tencent.com/document/product/436/8629)，具体版本为 `cos-nodejs-sdk-v5`。

可在代码内通过如下方式引入 COS SDK 并使用：


```
var COS = require('cos-nodejs-sdk-v5');
```

更详细的 COS SDK 使用说明见[COS Node.js SDK](https://cloud.tencent.com/document/product/436/8629)。
