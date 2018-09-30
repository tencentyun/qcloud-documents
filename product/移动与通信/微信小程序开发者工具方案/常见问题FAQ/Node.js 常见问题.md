如果您要开通腾讯云微信小程序开发者工具解决方案，可以阅读[《开通指引》](/document/product/619/11447)；

您还可以查看[《开发环境和生产环境》](/document/product/619/11446)了解开发环境和生产环境的区别；

如果本文还不能解决您的问题，您可以到腾讯云[问答](https://cloud.tencent.com/developer/ask)提问，我们将尽快跟进解答。

## 如何部署代码到开发环境

通过已经绑定腾讯云账号的微信号扫码登录微信开发者工具，接着创建一个小程序项目：

![上传代码](https://mc.qcloudimg.com/static/img/4fd45bb5c74eed92b031fbebf8600bd2/1.png)

项目目录可以选择 `wafer2-startup` 提供的 Demo 代码，也可以自行开发。

创建好项目之后会打开微信开发者工具页面，点击右上角腾讯云，选择“上传测试代码”，即可将本地的服务端代码部署到腾讯云免费分配的开发环境中。

>  **注意：**
>
>  服务器端的代码上传逻辑为合并，即如果有重名的文件，后面上传的代码会覆盖前一次上传的，如果不重名，则两者保留。文件夹一律为合并，即文件夹内文件保持前面所说的合并逻辑，不会完全替换整个文件夹。另外目前暂不支持删除线上文件、文件夹功能，您可以使用恢复开发环境来清空代码目录重新上传。

## 如何重启服务器

在微信开发者工具页面点击右上角“腾讯云”，在下拉菜单中选中“重启服务”，即可重启开发环境中的 Node.js 进程。

## 如何恢复初始化环境

在微信开发者工具页面点击右上角“腾讯云”，在下拉菜单中选中“恢复开发环境”，即可将代码环境恢复到分配开发环境时的状态。

> **注意：**
>
> 本操作不会删除开发环境中的 MySQL 数据库，仅会对代码目录进行恢复。

## 如何远程调试后台代码

腾讯云微信小程序解决方案 2.0 是基于 Node.js 开发的，提供远程调试功能，在微信开发者工具页面点击右上角“腾讯云”，在下拉菜单中选中“启动单步调试”，系统会自动重启远程服务，并使用 [inspect-brk 模式](https://nodejs.org/en/docs/inspector/)启动 Node.js App，接着开发者工具会打开调试窗口。

![Debug窗口](https://mc.qcloudimg.com/static/img/abd646218599ff3c0056ce99ee6fdbd7/1.png)

此时，App 进入暂停状态，这个时候您可以在 `app.js` 或者其他启动程序就会载入的包中下断点，点击代码左边的行号即可下断点，接着点击右上角蓝色的三角形按钮，启动 App，可以看到，程序会在断点处暂停下来。

![给程序下断点并启动](https://mc.qcloudimg.com/static/img/1731adeff8e3be435a4ba2213fef2ec9/2.png)

更多关于 Node.js 远程调试的文档说明，可以查看 [Chrome 开发者工具官方文档](https://developers.google.cn/web/tools/chrome-devtools/?hl=zh-cn)。

## 如何查看后台日志

进入[腾讯云小程序控制台](https://console.cloud.tencent.com/lav2)，点击“日志下载”即可下载 Node.js 输出的日志。

## 如何修改数据库密码

进入[腾讯云小程序控制台](https://console.cloud.tencent.com/lav2)，点击“重置密码”，输入原密码（默认密码为小程序的 AppID）和新密码，点击确定即可修改 MySQL 数据库密码。

## 如何新建和修改数据库的库表

进入[腾讯云小程序控制台](https://console.cloud.tencent.com/lav2)，点击“phpMyAdmin”按钮打开 phpMyAdmin 登录界面，输入用户名（默认为 `root`）和密码（默认密码为小程序的 AppID）点击登录即可登录进图形化数据库操作界面。

![phpMyAdmin](https://mc.qcloudimg.com/static/img/0b17ef0178c71463d65b3f883a3f1f2b/3.png)

点击右边列表的“新建”，即可新建数据库。点击任一一个数据库可以进行新建表等操作。phpMyAdmin 具体操作说明可以查看 [phpMyAdmin文档](https://docs.phpmyadmin.net/zh_CN/latest/)。

> **注意：**
>
> 如果您使用了腾讯云一站式微信小程序解决方案的 SDK，请不要删除 `cAuth` 数据库，该数据库存储登录相关的信息。

## 如何上传图片

腾讯云一站式微信小程序解决方案 SDK 还提供了一个直接上传图片到 COS 上的接口，具体配置项在 `server/config.js` 的 `cos` 中，不过无需配置，直接点击 Demo 中的上传图片，SDK 会自动创建 Bucket （若 Bucket 不存在）并将图片上传到 Bucket 中，并返回访问地址。

## 如何部署 Demo 到自己的服务器

###### *这步适合对运维有相关基础的开发者操作

除了使用腾讯云分配的开发环境和生产环境，您还可以部署 Demo 到自己的服务器上，只需要修改 `server/config.js` 的配置，并修改相应的 `client/config.js` 中 `host` 到您的服务器上即可。

`server/config.js` 具体配置可以参考 [服务端SDK 文档](/document/product/619/11448)。

## 如何快速新建路由

服务端 Demo 采用 Koa.js 框架编写，腾讯云基于 Koa 对上层进行一个简单的封装，方便您快速的添加新建路由。

只需要在 `controllers` 目录下新建一个文件，例如为 `demo.js`，写入如下代码：

```javascript
module.exports = function (ctx, next) {
    ctx.state.data = { msg: 'Hello World' }
}
```

保存之后，接着在 `routes/index.js` 的 `module.exports = router` 之前添加如下路由并保存：

```javascript
router.get('/demo', controllers.demo)
```

接着点击右上角的“腾讯云”按钮，选择“上传代码”，勾选“node_modules之外的代码”，点击确定即可上传代码，接着再次点击右上角的“腾讯云”按钮，选择“部署开发环境”，等到提示开发环境部署成功了之后，打开浏览器，访问 `https://腾讯云分配的域名/weapp/demo`，即可看到刚刚编写的返回，是一个 JSON 字符串：

```json
{"code":0,"data":{"msg":"Hello World"}}
```

## 微信后台如何配置客服消息推送接口

在 Demo 中 `server/config.js` 的 `CONF` 里添加一项 `wxMessageToken`，为任意值：

![修改配置](https://mc.qcloudimg.com/static/img/d6ac75415137fcc01166227b5c8c000f/4.png)

点击开发者工具右上角的“腾讯云”按钮，点击“上传代码”，代码上传完成之后点击“部署开发环境”，部署开发环境完成之后登录微信公众平台，依次进入“设置”-“开发设置”-“消息推送”，点击启用，按如下指引填写并点击【提交】即可。：

![配置消息推送](https://mc.qcloudimg.com/static/img/445e323417d279c8e40ad50e96f89bcc/5.png)

## 如何使用服务端 SDK 连接和操作数据库

服务端 SDK 还暴露出了内部使用的 MySQL 连接，由于 SDK 内部使用 [Knex.js](http://knexjs.org/) 连接数据库，SDK 暴露的 MySQL 实例就是 Knex.js 连接实例，具体使用方法可以查看 [Knex.js 文档](http://knexjs.org/)：

```javascript
const { mysql } = qcloud

mysql('db_name').select('*').where({ id: 1 }) // => { id:1, name: 'leo', age: 20 }
```

## 快速添加 CGI 指引

1. 打开 `server/routes/index.js` 文件，添加如下语句：

   ```javascript
   router.get('/demo', controllers.demo)
   ```

2. 在 `server/controllers` 下新建一个 `demo.js` 文件，写入如下代码：

   ```javascript
   module.exports = ctx => {
       ctx.state.data = {
           msg: 'Hello World'
       }
   }
   ```

3. 点击开发者工具右上角“腾讯云” - “上传代码”，上传完成再点击“部署开发环境”。

4. 点击测试 CGI 按钮，即可看到结果。

## 本地如何搭建开发环境

**本步骤适合对开发有相关基础的开发者操作**

**本地不能测试信道和客服相关接口**

如果您不想每次都上传到开发环境来测试代码，通过以下配置您可以在本地运行服务端进行测试。

**配置 config.js**

将 Demo 代码 clone 到本地，用编辑器打开 `server/config.js` **添加**以下配置：

```javascript
const CONF = {
  	// 其他配置 ...
    serverHost: 'localhost',
    tunnelServerUrl: '',
    tunnelSignatureKey: '27fb7d1c161b7ca52d73cce0f1d833f9f5b5ec89',
  	// 腾讯云相关配置可以查看云 API 密钥控制台：https://console.cloud.tencent.com/capi
    qcloudAppId: '您的腾讯云 AppID',
    qcloudSecretId: '您的腾讯云 SecretId',
    qcloudSecretKey: '您的腾讯云 SecretKey',
    wxMessageToken: 'weixinmsgtoken',
    networkTimeout: 30000
}
```

并修改 MySQL 相关的配置为您本地的 MySQL 数据库。

> **注意：**
>
> 您不能使用开发环境、生产环境分配的数据库，为了安全，我们通过安全组拦截了 3306 端口的入站访问。

修改 `client/config.js` 的 `host` 为 `localhost:5757`，并把链接改为 `http` 开头（本地调试无法使用 HTTPS 访问）

**初始化环境**

配置好 `config.js` 之后，就要开始初始化环境，初始化环境分为两步：

- 安装依赖 - 打开 CMD 输入如下命令：

  ```bash
  # 切换到服务端代码目录
  cd server

  # 安装依赖
  npm install

  # 安装全局依赖
  npm install -g nodemon
  ```

- 初始化数据库 - 打开 CMD 输入如下命令：

  ```bash
  node tools/initdb.js
  ```

**本地启动调试环境**

Demo 里已经内置了调试的脚本，在 CMD 中输入如下命令即可启动 Debug 模式：

```bash
npm run dev
```

启动之后，会输出 SDK 和其他 npm 包的 debug 信息，您也可以自己开发的时候直接输出。

![本地开发环境下启动](https://mc.qcloudimg.com/static/img/283a9f3250a97f826d4f0d25c04ab2c2/6.png)

## Error: 未找到 project.config.json 中的 svr 字段。错误：10080

如果您想使用腾讯云微信小程序一站式解决方案，并使用微信开发者工具一键部署，微信开发者工具打开的目录必须包含 `project.config.json` 文件，文件必须是个 JSON 字符串并包含 `client` 和 `svr` 两个 `key`。实例文件如下：

```json
{
  "client": "./client",
  "svr": "./server"
}
```

文件中的 `client` 表示小程序端代码，`svr` 表示服务器端代码。点击腾讯云相关操作（如上传测试代码）的时候，只会把 `svr` 指向的目录下的代码上传到开发（或生产）环境。

## (-1) 服务内部错误，请稍后重试或联系客服人员解决。

点击“登录”提示“{"code":-1,"error":"ERR_GET_SESSION_KEY\n{"code":5100,"message":"(-1) 服务内部错误，请稍后重试或联系客服人员解决。","codeDesc":"ResourceOpFailed"}"}”的错误，可以按照如下方式排查问题：

1. 检查是否将 client/config.js 里的 host 修改为分配的开发环境域名
2. 重新点击“编译”小程序，点击登录重试
3. 点击“腾讯云”-“重启服务”，重启成功之后点击登录重试
4. 如果您有一定的开发能力，可以启动单步调试，在 controller/login.js 里打一下断点，看看具体原因。

## 上传测试代码出错

上传测试代码错误，提示：

```json
{"code":-1,"reason":"module.js:487\n throw err;\n ^\n\nError: Cannot find module'wafer-node-sdk'\n at Function.Module._resolveFilename (module.js:485:15)\n at Function.Module._load (module.js:437:25)\n at Module."}
```

是因为代码里的依赖没有安装，请点击开发者工具右上角“腾讯云”里的“安装依赖”，依赖安装完成之后，点击“重启服务”即可正常启动 Node.js 程序。

建议上传测试代码的时候，点击勾选”部署后自动安装依赖“

<img alt="点击勾选部署后自动安装依赖" src="https://mc.qcloudimg.com/static/img/7dcb9f30aba7fbdfa4a9f415bc8b75a1/7.jpg" width="420px">

## 如何连接上服务器

新版小程序解决方案目前**暂无**计划支持开发服务器连接能力，您只能通过微信开发者工具上传、部署、调试代码。

## 真机预览的时候提示网络出错

<img src="https://mc.qcloudimg.com/static/img/049a1f8b5a477ebda6f088828f290e3c/8.png" width="240px" alt="真机预览的时候提示网络出错">

这种问题是因为开发域名不在安全域名列表里，可以点击界面右上角的三个小点，选择开启调试，就会绕过域名的验证

<img src="https://mc.qcloudimg.com/static/img/b192942b7593bcc344dfe89bd7fa2d3e/9.jpg" width="240px" alt="真机预览打开调试">
