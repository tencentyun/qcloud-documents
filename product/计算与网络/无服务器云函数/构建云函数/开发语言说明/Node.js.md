目前支持的 Node.js 开发语言包括如下版本：
* Node.js 6.10

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

您的处理程序需要使用 `callback` 入参来返回信息，函数的`return`将会被忽略。`callback` 的语法为：
```
callback(Error error, Object result);
```
其中：
* error：可选参数，在函数执行内部失败时使用此参数返回错误内容。成功情况下可设置为null。
* result：可行参数，使用此参数返回函数成功的执行结果信息。参数需兼容 JSON.stringify 以便序列化为 JSON 格式。


根据调用函数时的调用类型不同，返回值会有不同的处理方式。同步调用的返回值将会序列化为 JSON 格式后返回给调用方，异步调用的返回值将会被抛弃。同时，无论同步调用还是异步调用，返回值均会在函数日志中 `ret_msg` 位置显示。


## 日志
您可以在程序中使用如下语句来完成日志输出：
* console.log()
* console.error()
* console.warn()
* console.info()

输出内容您可以在函数日志中的 `log` 位置查看。
