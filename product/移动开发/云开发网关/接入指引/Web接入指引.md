<dx-alert infotype="explain" title="">
此项能力内测中，如需接入请请 [联系我们](https://cloud.tencent.com/online-service) 或 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行开通。
</dx-alert>


首先引入 SDK：
<dx-codeblock>
:::  js
https://web-9gikcbug35bad3a8-1304825656.tcloudbaseapp.com/sdk/1.3.0/cloud.js
:::
</dx-codeblock>


示例代码：
<dx-codeblock>
:::  js
var c1 = new cloud.Cloud({
  identityless: true,
  resourceAppid: '<微信服务商AppId>',   //微信服务商AppId，或者环境共享下资源方微信小程序账号
  resourceEnv: '<云开发环境ID>',        //云开发环境ID
});
await c1.init()
const result =  await c1.callContainer({
  // 去除域名后的接口路径，中文需要转译
  path: `/?word=${encodeURIComponent('微信网关访问')}`,
  header: {
    // 网关所在地域，不填默认是上海。北京 ap-beijing , 广州 ap-guangzhou
    'X-WX-REGION': '<网关所在地域>',
    // 微信网关ID
    'X-WX-GATEWAY-ID': '<填入网关ID>', 
    // 网关路由
    'HOST': '<填入域名>', 
  },
  method: 'GET',
  // 其余参数遵从 wx.request
})
console.log(result)
:::
</dx-codeblock>
