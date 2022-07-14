## 前提条件
准备接入 SDK  使用之前，需要确保您已创建 Web License，具体请参见[ License 申请与购买](https://cloud.tencent.com/document/product/616/71368)。

## 获取前置信息
### 获取 License Key
进入**音视频终端 SDK 控制台** > **License 管理** > **[Web License管理](https://console.cloud.tencent.com/vcube/web)**，查看您已创建的 Web License 并复制其 License Key。
![](https://qcloudimg.tencent-cloud.cn/raw/52655108c03334640d80f31dd959b565.png)

- Domain 是您可以使用 SDK  的 Web 站点域名（如请求 Referer 有非80、443端口号，也必须匹配，如：`localhost:3000`）。
- 小程序 APPID 是您可以使用  SDK  的微信小程序。
- 不论是测试 License 还是正式 License 只要结束时间没有过期，都可以激活当前项目。

### 获取 Token
进入**音视频终端 SDK 控制台** > **License 管理** > **[Web License管理](https://console.cloud.tencent.com/vcube/web)**，单击**显示**并复制 Token。
![](https://qcloudimg.tencent-cloud.cn/raw/b739714517046ea377f774d8b5a01f56.png)
>!此 Token 是您身份的唯一标识，不能泄露，不能放在前端页面，否则您的资源会泄露盗用。

### 获取 APPID

您可以登录腾讯云控制台，进入**账号信息** > **[基本信息](https://console.cloud.tencent.com/developer)** 查看 APPID。
![](https://qcloudimg.tencent-cloud.cn/raw/a237e4493e425219550b557254cf0fdf.png)

##  SDK 接入前置准备
>!  要接入  SDK  除了需要 License Key 授权 SDK 外，还需要使用 Token 对 SDK 中调用腾讯服务的接口进行签名。

### 签名方法
**鉴权流程**
![](https://qcloudimg.tencent-cloud.cn/raw/da5ccf517e599d892d68322d3a8792e5.png)

- **Token**：用于 SDK 接口签名，是您身份的唯一标识。
- **appid**：即腾讯云控制台 **账号信息** > **[基本信息](https://console.cloud.tencent.com/developer)** 展示的 APPID。
- **timestamp**：当前时间戳，精确到秒（10位数字）。 
- **signature**：签名（签名有时效性，目前5分钟过期）。

由于 signature 有时效性，且需要防止 Token 泄露，您需要部署一个生成签名的服务。
>! 
>- **如果 Token 泄露您的身份会被盗用，您的资源会泄露。**
>- 生成签名的方法放在前端会导致 Token 泄露，为了避免利益受损，建议您**不要将生成签名的方法放在前端**。

```js
// 以express后台为例
// 签名方法： sha256(timestamp+token+appid+timestamp)

const { createHash } = require('crypto');
const config = {
  appid: '您的腾讯云APPID',
  token: '您的Token',
}
const sha256 = function(str) {
  return createHash('sha256')
    .update(str)
    .digest('hex');
}

const genSignature = function() {
  const timestamp = Math.round(new Date().getTime() / 1000);
  const signature = sha256(timestamp + config.token + config.appid + timestamp).toUpperCase(); // 使用上面获取到的token和appid合成加密串返回
  return { signature, timestamp };
}

app.get("/get-ar-sign", (req, res) => {
  const sign = genSignature();
  res.setHeader('Access-Control-Allow-Origin','*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');  
  res.send(sign);
})
```

### 前端调用
获取签名的服务部署完成后，在您的 Web 页面或小程序中，添加一个获取签名的方法供 SDK 接入调用。
<dx-tabs>
::: 小程序
```js
async function getSignature() {
  return new Promise((resolve,reject)=>{
      wx.request({
        url: '您的域名/get-ar-sign',
        method: 'GET',
        success(res) {
          console.log('getSignature ok', res)
          resolve(res.data);
        },
        fail(e){
          console.log('getSignature error', e)
        }
      })
    })
}
```
:::
::: Web 端
```js
async function getSignature() {
  const res = await fetch('您的域名/get-ar-sign')
  const authdata = await res.json()
  console.log('authdata',authdata)
  return authdata
}
```
:::
</dx-tabs>

后续流程，请参见 [SDK 接入指南](https://cloud.tencent.com/document/product/616/71364)。





