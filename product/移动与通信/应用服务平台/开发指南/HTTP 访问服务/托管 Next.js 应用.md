[Next.js](https://nextjs.org/) 是一款 React 框架，支持服务端渲染（SSR），本文将介绍如何将 Next.js 应用托管至云开发。

## 步骤1：初始化项目

1. 使用 CLI 工具初始化一个云开发项目。
<dx-codeblock>
:::  sh
cloudbase init
:::
</dx-codeblock>

2. 语言选择 `Node`，模板选择 `Hello World`。
<dx-codeblock>
:::  sh
? 选择关联环境 xxx - [xxx-xxx]
? 请输入项目名称 cloudbase-next
? 选择模板语言 Node
? 选择云开发模板 Hello World
✔ 创建项目 cloudbase-next 成功！
:::
</dx-codeblock>

3. 进入项目根目录：
<dx-codeblock>
:::  sh
cd cloudbase-next
:::
</dx-codeblock>

4. 然后创建一个 next 应用到 `functions/next` 内：
<dx-codeblock>
:::  sh
npm init next-app functions/next
:::
</dx-codeblock>


## 步骤2：配置项目

我们接下来对 next 项目进行一些改造，让它满足云函数内部署的要求。
1. 进入 next 根目录
```sh
cd functions/next
```
2. 安装 `serverless-http`
```sh
npm install --save serverless-http
```
3. 然后把以下文件添加至 `functions/next/index.js`
```js
// index.js
const next = require("next");
const serverless = require("serverless-http");

const app = next({ dev: false });
const handle = app.getRequestHandler();

exports.main = async function (...args) {
  await app.prepare();
  return serverless((req, res) => {
    handle(req, res);
  })(...args);
};
```
4. 以下文件添加至 `functions/next/next.config.js`：
```js
// next.config.js
module.exports = {
  assetPrefix: "/next"
};
```

## 步骤3：构建与发布

1. 我们在 `functions/next` 目录下，运行
```sh
npm run build
```
2. 然后回到**项目根目录**，运行
```sh
cloudbase functions:deploy next
```
3. 发布时，使用默认配置即可
```
cloudbase functions:deploy next
? 未找到函数发布配置，使用默认配置？ Yes
✔ [next] 函数部署成功！
```
4. 然后我们建立一条 HTTP 服务路由：
```sh
cloudbase service:create -f next -p /next
```
5. 随后我们便可以通过 URL 访问 Next.js 应用。
```sh
cloudbase service:create -f next -p /next
✔ 云函数 HTTP service 创建成功！
https://${env-id}.service.tcloudbase.com/next
```
