## 1.接口调用流程 ##
![](https://mc.qcloudimg.com/static/img/2db4947e1315ffb60e25183050fa55ba/image.jpg)
1）后台通过调用天御的CaptchIframeQuery接口获取验证码的js地址。 <br> 2）把获取到的js地址回传给网页客户端。<br> 3）客户端依据获取到的回传的js地址加载和校验验证码。<br> 4）用户验证完成后提交天御返回的票据到后台。<br> 5）后台调用天御的CaptchaCheck接口来验证票据是否通过验证。

## 2.后台获取验证码js地址接口 ##
[后台获取验证码API](https://www.qcloud.com/document/product/295/6620)

## 3.客户端加载验证码和获取票据接口 ##
[IOS客户端API](https://www.qcloud.com/document/product/295/6617)
<br>[Android客户端API](https://www.qcloud.com/document/product/295/6615)

## 4.获取验证码票据
用户依据第3步获取的用户验证票据，提交到后台。

## 5.后台校验验证码票据
后台依据第三步获取的用户票据，提交天御验证
<br>[后台验证票据API](https://www.qcloud.com/document/product/295/6619)

## 6.使用注意
手机验证码页面要全屏显示，否则验证码页面会显示异常影响用户使用。