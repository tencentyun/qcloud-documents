
## 应用场景

用户的个性化业务需求若需要将产品下所有设备上报的数据传输至用户自有的服务器上进行处理，平台提供了 HTTP 转发服务，将设备上报数据实时 POST 到用户的 HTTP 服务器的能力。
![](https://main.qcloudimg.com/raw/d95cb3da410f42661d48e1af67e12724.png)

客户在此场景下，需要一个HTTP的服务器去接收控制台传过来的设备信息。HTTP服务器需要具备的功能如下：

- 通过 token 验证签名
- 接收控制台同步的设备信息

本文将向用户介绍，如何通过云函数快速实现对物联网开发平台数据同步 HTTP 转发的设备消息数据和上下线数据的同步接收。开发者使用云函数将无需购买 CVM ，即可快速入手搭建实现 HttpServer，后续也无需运维关注，同时享受弹性扩容、毫秒级冷启动等基础特性。

## 操作步骤

1. 登录 [物联网开发平台](https://console.cloud.tencent.com/iotexplorer) ，选择**公共实例**或您购买的**标准企业实例**。
2. 进入项目列表页面，单击**项目 ID** 进入项目详情页。
3. 单击左侧菜单**数据同步**进入数据同步配置页面，数据同步在未设置时，默认生效状态都为关闭，HTTP 服务地址为空。
![](https://main.qcloudimg.com/raw/bdbb79b1804f420aaf2acf7b758268c1.png)
4. 随后进入 [云函数](https://console.cloud.tencent.com/scf/list?rid=16&ns=default) 产品控制台创建模板函数。
![](https://main.qcloudimg.com/raw/6908d242862fabac3058c9ab62e66d98.png)
5. 单击**新建**按钮，创建方式选择**模板创建**，在下方模糊搜索栏搜索 `IoT Explorer`。
![](https://main.qcloudimg.com/raw/738bacf6c26feb3109343b81c909eced.png)
选择“IoT Explorer数据同步转发”模板后，单击**下一步**按钮
6. 无需更改相关配置信息，单击**完成**按钮后进入函数管理页面。
![](https://main.qcloudimg.com/raw/9e16f86259efc77220e6c3e80fc47d18.png)
7. 在“函数管理”页面选择“函数代码”功能栏，下滑单击**部署按钮**。
![](https://main.qcloudimg.com/raw/82d4743fab35d396f2706ac667bec3cc.png)
8. 部署成功后，复制“访问路径” url（该访问路径即为数据同步转发功能内，接收设备消息数据的 url）。
9. 回到物联网开发平台-数据同步页面，选择需要设置数据同步的产品，单击**设置按钮**，选择需要推送的消息类型，填写接收服务端地址，同时增加鉴权 token（默认为 test，若需自定义可查看下方的提示）。
![](https://main.qcloudimg.com/raw/d6f8098e42eb9364b0e3f117af1fbb16.png)
![](https://main.qcloudimg.com/raw/e791156ac39a80818bec3ee3fa0b57a5.png)
> !鉴权 token 如何自定义设置，可在函数部署阶段在代码中自定义配置。默认为`test`。
> ![](https://main.qcloudimg.com/raw/51bcb353a227fffc04c05ef259a2e5ae.png)
> 
10. 配置完成后，单击**保存**按钮，跳转到列表页，可开启该产品的**生效状态**，完成该产品的数据同步配置。
![](https://main.qcloudimg.com/raw/16aadaea76e1a51def49cf68aacfe467.png)
11. 重新返回云函数界面，进入“日志查询”功能页面，可查看服务端接收到的由物联网开发平台同步的设备数据、上下线消息日志：
![](https://main.qcloudimg.com/raw/ab886e6fcf46a2b90b4b2d9de20578d9.png)
![](https://main.qcloudimg.com/raw/ebe85e02b3f5201b539c7ffff39cd1ce.png)
