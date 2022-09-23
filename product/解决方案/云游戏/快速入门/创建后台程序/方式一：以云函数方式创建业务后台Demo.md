通过本文档指引，开发者可快速创建云游戏业务 server 示例，以尝试云游能力接入。

[](id:step1)
## 步骤1：导入云函数
1. 访问 [函数服务控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)，单击**新建**进入函数创建页。
2. 选择创建方式为“**自定义创建**”，函数类型为“**Web函数**”，部署方式为“**代码部署**”，运行环境为“**Nodejs12.16**”。
3. 在**函数代码**中选择提交方法为“**本地上传zip包**”，单击**上传**，上传云游戏提供的 [ZIP 文件](https://demo-1304469412.cos.ap-guangzhou.myqcloud.com/express_demo-1630920466.zip)，单击**完成**即可完成导入函数操作。
![](https://qcloudimg.tencent-cloud.cn/raw/95d2010dbf05e20d384e1546de9820dd.png)
4. 在**函数管理 > 函数代码** 中打开 `app.js` 文件。`app.js` 文件里定义了2个客户业务后台接口，分别为启动云端游戏（StartCloudGame）和退出云端游戏（StopCloudGame），并通过调用 [云渲染后端 API](https://cloud.tencent.com/document/product/1162/40729) 实现业务逻辑。
>! 需将 `app.js` 文件中的 secretId 和 secretKey 替换为您购买腾讯云游戏的账号的 [API 密钥](https://console.cloud.tencent.com/cam/capi)。
![](https://qcloudimg.tencent-cloud.cn/raw/485873e133b63e2e32b4784e4e0fa1c9.png)  

[](id:step2)
## 步骤2：部署和测试
1. 代码修改之后，打开**自动安装依赖**，单击**部署**。部署运行云函数后，可以在云函数页面上查看云函数的“访问路径”，构造“测试模版”，进行接口测试。
![](https://qcloudimg.tencent-cloud.cn/raw/d931b6caf5c912a1f8c963fb5af4a92a.png)
6. 记录下后台接口的 server，在构建客户端程序的时候会要用到。
>? server 地址示例：`service-test-xxxxxxxxxx.gz.apigw.tencentcs.com/release`。


[](id:step3)
## 步骤3：解决跨域问题
如果从 [JS 入门 Demo](https://github.com/tencentyun/cloudgame-js-sdk/tree/master/demo) 里访问 Server，会遇到跨域问题，则需将云函数服务配置为允许跨域访问：
1. 在您刚刚创建函数中，选择触发管理，并单击 API 服务名。
![](https://qcloudimg.tencent-cloud.cn/raw/225b4784266c9d00b1aa1f02d41de8c8.png)   
2. 在新打开的 API 网关页面中选择对应的通用 API，单击 API 的 ID 进入详情页。
![](https://qcloudimg.tencent-cloud.cn/raw/f0e3adad64a0363a71f6d2eca857d06c.png)    
3. 在**基础配置**页下，开启**跨域访问控制**。
![](https://qcloudimg.tencent-cloud.cn/raw/0345206299521e0fd34133f24ac08ab5.png)
