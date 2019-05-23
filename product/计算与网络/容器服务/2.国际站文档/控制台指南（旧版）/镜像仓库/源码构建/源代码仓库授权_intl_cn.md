如果用户需要从 Git 代码仓库来构建容器镜像，首先必须进行源代码授权。目前我们支持 Github 仓库和 Gitlab 仓库授权。
 
## 操作步骤
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的 【镜像仓库】，在下拉列表中单击【我的镜像】，进入 **我的镜像库** 页面，单击【源代码授权】。
 ![](//mc.qcloudimg.com/static/img/4019d743e8a653a333b984d68f4ce3f5/image.png)
3. 进入代码源授权选择页面。
![](https://mc.qcloudimg.com/static/img/47dc0339b4a602a07ba2f92dda6290ff/image.png)

## Github 授权
如果您的代码仓库位于 Github，那么请单击【授权同步 Github 代码源】。
跳转至 Github 网站，Github 会提示 APP 需要访问用户的代码仓库、个人信息等数据，单击【authorize】完成 Github 代码仓库的授权。
![](//mc.qcloudimg.com/static/img/80b89840adbfcb9dac1f27b1e5a83e10/image.png)

## Gitlab 授权
如果您的代码仓库位于自建的 Gitlab 服务器，或者官方的 Gitlab 托管服务器，那么请单击【授权同步 Gitlab 代码源】。
跳转至 **Gitlab 代码源授权** 页面。
![](https://mc.qcloudimg.com/static/img/68d44d7dd5d621f288e56efdc8bad7f3/image.png)
- **服务地址**：Gitlab 服务器地址。必须包含 http 或者 https 协议，并且公网必须能够访问该地址。
- **用户名**：您在 Gitlab 上注册的用户名。在 Gitlab 页面的 Profile -> Name 可以查看您的用户名。
- **私有Token**：必须是 Access Token，如果您没有 Access Token，在 Gitlab 上可以创建一个 Access Token：
![](//mc.qcloudimg.com/static/img/993e48f457b7e9db35bd8402da6f6291/image.png)

>**注意：**
>每个用户可以同时授权 Github 和 Gitlab 帐号，但是 Github 和 Gitlab 帐号分别只能授权一个帐号，如果需要更改 Github 或者 Gitlab 帐号，则需要先注册原来的帐号。
  
