## 1.接口调用流程 ##
![](http://7xrn7f.com1.z0.glb.clouddn.com/16-10-24/52183098.jpg)
1）后台通过调用天御的CaptchIframeQuery接口获取验证码的js地址。 <br> 2）把获取到的js地址回传给网页客户端。<br> 3）客户端依据获取到的回传的js地址加载和校验验证码。<br> 4）用户验证完成后提交天御返回的票据到后台。<br> 5）后台调用天御的CaptchaCheck接口来验证票据是否通过验证。
## 2.后台获取验证码js地址接口 ##
天御获取验证码的CaptchIframeQuery接口
## 3.客户端加载验证码和获取票据接口 ##
IOS客户端-API
<br> 安卓客户端-API
## 4.获取验证码票据
用户依据第3步获取的用户验证票据，提交到后台。<p> function cbfn(retJson){<p> 　　if(retJson.ret==0)<p> 　　{<p> 　　　//用户验证成功<p> 　　　retJson.ticket://用户票据<p> 
　　}<p> 　　else<p> 　　｛<p> 　　　//用户关闭验证码页面，没有验证<p> 　　｝<p> ｝
## 5.后台校验验证码票据
后台依据第三步获取的用户票据，提交天御验证
<br> 天御校验验证码票据（CaptchaCheck）API