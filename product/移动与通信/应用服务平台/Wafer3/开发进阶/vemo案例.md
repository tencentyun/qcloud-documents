# vemo 案例

基于 [vemo](https://github.com/vemoteam/vemo) 框架的 `hello world` 示例。

## 前置条件

* 安装 node.js 和 npm
* git

## 获取机器的 IP 和密码

购买主机后，到腾讯云 `云主机控制台` 获取机器的 IP 并且到 `消息中心` 获取主机的密码。

![消息中心](https://main.qcloudimg.com/raw/bbcd54b3d0501881b37cd3ffa62121e6.png)

## 获取腾讯云 SecretId 和 SecretKey

获取 `secretId` 和 `secretKey`。通过此[链接](https://www.qcloud.com/login/mp?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fcam%2Fcapi)登录小程序对应的腾讯云帐号(需要小程序管理员或拥有者权限)，然后在[云API密钥](https://console.cloud.tencent.com/cam/capi) 里获取。

![](https://main.qcloudimg.com/raw/63512b321eee6c8779d6cb5b20f641cf.png)

## 初始化项目

```shell
// 在你自己的开发电脑而不是刚买的主机上操作
git clone https://github.com/TencentCloudBase/wafer-template

## 进入 vemo demo 目录
cd wafer-template/vemo

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

## 登陆并填入腾讯云云主机 IP， SSH 登陆密码，secretId 和 secretKey
tcb login
```

然后在 `wafer-template/vemo` 目录下，然后新建 `tcb.json` 文件，将 `tcb.example.json` 的内容拷贝过来并保存。

```js
{
    "deploys": [
        {
            "name": "vemo",
            "path": "./",
            "type": "node"
        }
    ]
}
```

再运行以下命令进行部署。

```shell
tcb deploy
```

如果成功，则会有以下的显示：

![](https://main.qcloudimg.com/raw/26f34ae33be47ce38b5a8ead67a20013.png)

## 验证

访问购买机器后分配好的域名，就能看到带有 `Hello World!` 字样的页面。

![](https://main.qcloudimg.com/raw/d35b36607d5f02ee4b47b36a3401b0a9.png)