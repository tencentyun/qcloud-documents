常见示例中包含了 Node.js 环境下可以试用的相关代码片段，您可以根据需要选择尝试。示例均基于 Node.js 12.16 环境提供。

您可从 github 项目 [scf-nodejs-code-snippet](https://github.com/awesome-scf/scf-nodejs-code-snippet) 中获取相关代码片段并直接部署。

## 环境变量读取

本示例提供了获取全部环境变量列表，或单一环境变量值的方法。

```js
'use strict';
exports.main_handler = async (event, context) => {
		console.log(process.env)
    console.log(process.env.SCF_RUNTIME)
    return "Hello world"
};
```

## 本地时间格式化输出

本示例使用了 moment 库获取本地时间，并提供了时间格式化输出方法，按指定格式进行日期和时间输出。

SCF 环境默认是 UTC 时间，如果期望按北京时间输出，可以为函数添加 `TZ=Asia/Shanghai` 环境变量。

```js
'use strict';
const moment = require('moment')
exports.main_handler = async (event, context) => {
    let currentTime = moment(Date.now()).format('YYYY-MM-DD HH:mm:ss')
    console.log(currentTime)
    return "hello world"
};
```

## 函数内发起网络连接

本示例使用了 requests 库在函数内发起网络连接，获取页面信息。可以通过在项目目录下执行 npm install requests` 命令完成依赖库安装。

```js
'use strict';
var request = require('request');
exports.main_handler = async (event, context) => {
    request('https://cloud.tencent.com/', function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body) // 请求成功的处理逻辑
        }
    })
    return "success"
};
```

