## 1.接口调用流程 ##
![](https://mc.qcloudimg.com/static/img/3cabdc2a3af7369cd05eca73ce5517bb/image.png)
1）后台通过调用天御的CaptchIframeQuery接口获取验证码的js地址。 <br> 2）把获取到的js地址回传给网页客户端。<br> 3）客户端依据获取到的回传的js地址加载和校验验证码。<br> 4）用户验证完成后提交天御返回的票据到后台。<br> 5）后台调用天御的CaptchaCheck接口来验证票据是否通过验证。
## 2.后台获取验证码js地址接口 ##
<a href="/doc/product/295/6620"target="blank">后台获取验证码API</a>

## 3.客户端加载验证码和获取票据接口 ##
<a href="/doc/product/295/6618"target="blank">PC页面API</a>
## 4.获取验证码票据
用户依据第3步获取的用户验证票据，提交到后台。<br> function cbfn(retJson){<br> 　　if(retJson.ret==0)<r> 　　{<br> 　　　//用户验证成功<br> 　　　retJson.ticket://用户票据<br> 
　　}<r> 　　else<br> 　　｛<br> 　　　//用户关闭验证码页面，没有验证<br> 　　｝<br> ｝
## 5.后台校验验证码票据
后台依据第三步获取的用户票据，提交天御验证
<br> <a href="/doc/product/295/6619"target="blank">后台验证票据API</a>
## 6.使用注意
1）请不要使用iframe页面嵌入验证码。验证码弹出的iframe框大小会变化，如果业务使用iframe会导致验证码iframe页面显示不全。<br> 2）PC预留给验证码展示的地方尺寸不能小于300px（宽）*310px（高），否则会导致验证码显示异常而影响用户使用。<br> 3）PC页面必须设置验证码显示页面初始宽高。<br> 4）手机验证码页面要全屏显示，否则验证码页面会显示异常，影响用户使用。