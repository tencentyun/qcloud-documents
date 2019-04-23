# 聊天室进阶案例

基于 [vemo](https://github.com/vemoteam/vemo) 运行框架的小程序聊天室 `demo`。

## 前置条件
* [注册小程序](https://developers.weixin.qq.com/miniprogram/introduction/#%E6%B3%A8%E5%86%8C%E5%B0%8F%E7%A8%8B%E5%BA%8F%E5%B8%90%E5%8F%B7)
* [开通云开发](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/basis/getting-started.html#%E5%BC%80%E9%80%9A%E4%BA%91%E5%BC%80%E5%8F%91)
* 安装 Node.js, Npm 和微信开发者工具

## 获取机器的 IP 和密码

购买主机后，到腾讯云 `云主机控制台` 获取机器的 IP 并且到 `消息中心` 获取主机的密码。

![消息中心](https://main.qcloudimg.com/raw/bbcd54b3d0501881b37cd3ffa62121e6.png)

## 获取腾讯云 SecretId 和 SecretKey

获取 `secretId` 和 `secretKey`。通过此[链接](https://www.qcloud.com/login/mp?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fcam%2Fcapi)登录小程序对应的腾讯云帐号(需要小程序管理员或拥有者权限)，然后在[云API密钥](https://console.cloud.tencent.com/cam/capi) 里获取。

![](https://main.qcloudimg.com/raw/63512b321eee6c8779d6cb5b20f641cf.png)

## 初始化项目

```shell
git clone https://github.com/lcxfs1991/pai-template.git

## 进入 chatroom demo 的服务器端代码目录
cd chatroom/server

## 安装依赖
npm install

## 安装命令行工具
npm i -g @cloudbase/cli

## 登陆并填入腾讯云的 secretId 和 secretKey
tcb login
```

初始化后，请用微信开发者工具，导入该项目。

## 开发

在微信开发者工具中，右键选中云函数 `cloud/functions/tcb-auth`，并上传。

![上传云函数](https://main.qcloudimg.com/raw/8687b443edec893f51811a30c4589778.png)

然后运行以下命令：

```shell
npm start
```

## 部署

* 更改 `client/config/index.js` 中的链接，将其改成生产环境的地址。

* 基于 `tcb.example.json` 创建 `tcb.json` 配置文件，然后填入机器的 `IP` 和 `SSH` 登陆密码。

* 运行以下命令，将服务部署到云主机

```shell
tcb deploy --start
```

* 如果是进行重启，则运行以下命令：

```shell
tcb deploy
```

## 验证

在微信开发者工具的左侧模拟器中，可以进行聊天室的试用，如下图：

![](https://main.qcloudimg.com/raw/baaa2997b69242329479edb4de49517a.png)

如果访问分配好的域名，你能够体验到 `H5` 的版本。但体验前，要将在 `server/src/static/config` 目录下，基于 `example.js` 新建 `index.js` 配置文件，然后将用户的 `tcb-token` 放到刚才的 `index.js` 文件里：

![](https://main.qcloudimg.com/raw/2557bf06c9c543a95890879f3c7e6f5a.png)

配置好后即可体验 `H5` 的版本，如下图：

![](https://main.qcloudimg.com/raw/6363b4e711d6c2de0f23230c5474500d.png)