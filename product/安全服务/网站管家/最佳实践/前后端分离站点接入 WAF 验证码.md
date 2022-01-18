在前后端分离或 App 站点中接入 WAF 验证码，可以实现在前端端分离站点或 App 站点动态下发验证码。

前后端分离站点接入 WAF 验证码流程，适用于利用 WAF 进行 前后端分离站点动态进行人机验证的场景（如命中自定义规则、CC攻击、BOT行为管理等），App（iOS 和 Android） 皆使用 Web 前端 H5 方式进行接入。


## 前提条件
 已购买 [Web 应用防火墙](https://cloud.tencent.com/document/product/627/11730)（高级版及以上），并完成 [接入 WAF](https://cloud.tencent.com/document/product/627/18635)。 
 

## 检出原理
通过动态识别服务端返回包中是否包含 WAF下 发的验证码的相关字段，如果包含 WAF 下发的验证码的相关信息时，在顶部浮层渲染验证码，实现前后端分离站点或 App 进行 WAF 站点验证码接入。

## 操作步骤
以下代码为接入WAF 验证码示例代码（以 axios 为例），根据应用场景，以此作为参考完成前后端分离站点的接入WAF 验证码。
1.  Axios Response 增加 interceptors。
```
 	//WAF 验证码seqid相关正则
const sig_data = /seqid\s=\s"(\w+)"/g
const waf_id_data = /TencentCaptcha\((\'\d+\')/g

const service = axios.create({ 
    baseURL: '/api',
    timeout: 10000, 
    withCredentials: true
});

service.interceptors.response.use((response)=>{
    const res = response.data;
    if(res.code === 0){
      return res;
    }else{
      //捕捉错误及渲染验证码
      const matches = sig_data.exec(res);
      if(matches){
        //展示验证码
        let seqid = matches[1];      
	      const wid_matches = waf_id_data.exec(res);
        let wid = wid_matches[1]
        var captcha = new TencentCaptcha(wid, function(res){
          var captchaResult = []
          captchaResult.push(res.ret)
          if(res.ret === 0){
              captchaResult.push(res.ticket)
              captchaResult.push(res.randstr)
              captchaResult.push(seqid)
          }
          var content = captchaResult.join('\n')
          axios.post(
            "/WafCaptcha",content
          ).then().catch();
        });
        captcha.show()
      }else{
        return res;
      }   
    }
},()=>{});
export default service;


Vue.prototype.$axios = service;
```
2.	调用 API 时使用增加 interceptors 的 axios。
```
 	getTopic:function(){
  this.$axios.get("/api.php").then(res => {
	  this.topic = res
  });
  }
```
3.	全局引入验证码脚本 ，即在 public/index.html 引入 `<script src="https://ssl.captcha.qq.com/TCaptcha.js"></script>`。
```
src="https://ssl.captcha.qq.com/TCaptcha.js"></script>
 	<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <title><%= htmlWebpackPlugin.options.title %></title>
  </head>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <script src="https://ssl.captcha.qq.com/TCaptcha.js"></script>
    <div id="app"></div>
    <!-- built files will be auto injected -->
  </body>
</html>
```
4. 输入上述代码后，编译并部署至服务器上即可。
5. 在 WAF 配置自定义规则，通过异步请求，查看当前页面是否展示验证码弹窗。
![](https://qcloudimg.tencent-cloud.cn/raw/5f2a85eaee0f53bebe2eb43f658f7ddd.png)
