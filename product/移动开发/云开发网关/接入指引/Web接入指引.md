## 开通允许未登录访问
在网关配置页面，开启“允许未登录访问”。


## 调用示例
首先引入 SDK：`https://web-9gikcbug35bad3a8-1304825656.tcloudbaseapp.com/sdk/1.3.0/cloud.js`。
示例代码：
```js
<script src="https://web-9gikcbug35bad3a8-1304825656.tcloudbaseapp.com/sdk/1.3.0/cloud.js"></script>
<script>
  var c1 = new cloud.Cloud({
    identityless: true,
    resourceAppid: '<wx-appid>',  //微信服务商APPID，或者环境共享下资源方微信小程序账号
    resourceEnv: '<env-id>',      //环境ID
  });
  await c1.init()
  const result =  await c1.callContainer({
    // 去除域名后的接口路径，中文需要转译
    path: `/?word=${encodeURIComponent('云开发网关访问')}`,
    header: {
      // 网关所在地域，不填默认是上海。北京 ap-beijing , 广州 ap-guangzhou
      'X-WX-REGION': 'ap-shanghai',
      // 网关ID
      'X-WX-GATEWAY-ID': '<gateway-id>', 
      // 网关路由
      'HOST': 's.cloudbase.net', 
    },
    method: 'GET',
    // 其余参数遵从 wx.request
  })
  console.log(result)
</script>


```
