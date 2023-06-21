本指引用于协助指导如何调整 Web、H5 应用，使得应用的网络请求经过网关进行转发。


## 开通允许未登录访问
Web、H5 应用由于默认没有微信相关认证信息，因此接入前，在网关配置页面，需开启**允许未登录访问**。


## 接入调整

1. 通过在前端页面中引入 SDK，提供前端发起网络请求的方法，SDK 引入地址为：`https://web-9gikcbug35bad3a8-1304825656.tcloudbaseapp.com/sdk/1.3.0/cloud.js`，可以通过下载本地后与前端应用一同打包部署，或者通过直接引用地址的方式引入页面使用。
2. 按如下示例代码接入页面并发送后端请求。
 - 其中所使用的参数如下：
      - resourceAppid：微信开发者 APPID，或者环境共享下资源方微信小程序账号。
      - resourceEnv：网关环境 ID。
 - 在请求中需附上的 header 参数说明如下：
    - X-WX-REGION：可选填写，网关环境所在地域，默认值 ap-shanghai，当网关实例地域非上海时，需要填写此参数，包括：ap-guangzhou、ap-beijing。
    - X-WX-GATEWAY-ID： 必填，网关实例 ID。
    - HOST：业务自定义 HOST 名，需要和网关的路由配置中的域名对应，用于网关路由转发匹配。
 
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
