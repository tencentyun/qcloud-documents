# koa 入门案例

基于 [koa](https://github.com/koajs/koa) 框架的 `hello world` 示例。

## 前置条件

* 安装 node.js 和 npm
* git

## 获取机器的 IP 和密码

购买主机后，到腾讯云 `云主机控制台` 获取机器的 `IP` 并且到 `消息中心` 获取主机的密码。

![消息中心](https://main.qcloudimg.com/raw/bbcd54b3d0501881b37cd3ffa62121e6.png)

## 初始化项目

```shell
git clone https://github.com/lcxfs1991/pai-template.git

## 进入 koa demo 目录
cd koa

## 安装依赖
npm install
```

## 开发

```shell
## 启动本地服务
npm start
```

## 部署

安装 [@cloudbase/cli](https://github.com/TencentCloudBase/cloud-base-cli)。

```shell
## 安装命令行工具
npm i -g @cloudbase/cli
```

然后基于 `tcb.example.json` 创建 `tcb.json` 配置文件，然后填入机器的 `IP` 和 `SSH` 登陆密码。然后运行以下命令进行部署。

```shell
tcb deploy --start
```

如果是进行重启，则运行以下命令：

```shell
tcb deploy
```

## 验证

访问购买机器后分配好的域名，就能看到带有 `Hello World!` 字样的页面。

![](https://main.qcloudimg.com/raw/d35b36607d5f02ee4b47b36a3401b0a9.png)