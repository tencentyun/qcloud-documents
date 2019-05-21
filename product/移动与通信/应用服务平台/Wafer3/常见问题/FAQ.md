# 常见问题

## 如何获取腾讯云永久密钥

取 `secretId` 和 `secretKey`。通过此[链接](https://www.qcloud.com/login/mp?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fcam%2Fcapi)登录小程序对应的腾讯云帐号(需要小程序管理员或拥有者权限)，然后在[云API密钥](https://console.cloud.tencent.com/cam/capi) 里获取。

## 如何获取云主机 IP 和 SSH 登录密码

购买主机后，到腾讯云 `云主机控制台` 获取机器的 `IP` 并且到 `消息中心` 获取主机的密码。

![消息中心](https://main.qcloudimg.com/raw/bbcd54b3d0501881b37cd3ffa62121e6.png)

## 命令行工具 @cloudbase/cli 使用 `tcb login` 的时候验证失败怎么办

有可能是以的问题：

1. 提供的腾讯云密钥或者云主机的 IP 和密码不正确

2. 网络连接不通畅

3. 本地的网络代理需要正确设置，需要设置 `Node.js` 的 `HTTP_PROXY` 和 `HTTPS_PROXY` 环境变量