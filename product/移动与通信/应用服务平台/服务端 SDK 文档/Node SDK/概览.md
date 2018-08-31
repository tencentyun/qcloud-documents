## 介绍
TCB 提供开发应用所需服务和基础设施。tcb admin Node.js SDK 让你可以在服务端（如腾讯云云函数或 CVM 等）使用 Node.js 服务访问 TCB 的的服务。

需要 Node.js v8.9 及以上版本。

## 安装
tcb admin Node.js SDK 可以通过 [tcb-admin-node](https://github.com/TencentCloudBase/tcb-admin-node) 来访问：
```bash
npm install --save tcb-admin-node@latest
```

要在你的模块式使用模块可以
```js
const app = require("tcb-admin-node");
```
或
```js
import * as app from "tcb-admin-node";
```
