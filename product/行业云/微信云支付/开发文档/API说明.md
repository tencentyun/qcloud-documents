## windows环境
&nbsp;&nbsp;&nbsp;云支付提供了两种初始化函数，一种是普通初始化，一种是安全初始化，如服务商自己没有对商户敏感信息（如支付密钥）做保护，则建议采用安全初始化模式。  
 
- **普通初始化**   
&radic;&nbsp;&nbsp;&nbsp;使用云支付类接口时需要在进程启动时调用初始化函数，函数定义如下：
![](https://mc.qcloudimg.com/static/img/0c11f96209c282e4c55702087849c418/image.png)
&radic;&nbsp;&nbsp;&nbsp;初始参数打包例子，有些参数可以不用设置。如果不设置，则会使用系统的默认值。建议使用默认值：
![](https://mc.qcloudimg.com/static/img/c1111bbddaeb87bc93991aa48306c823/image.png)
![](https://mc.qcloudimg.com/static/img/bcc9f934b47858c12bce00c6a3f6bc40/image.png)
- **安全初始化**   
&radic;&nbsp;&nbsp;&nbsp;初始化函数
![](https://mc.qcloudimg.com/static/img/813872c61f79d6cc7d780229b85c6eb6/init.png)
&radic;&nbsp;&nbsp;&nbsp;安全登入接口
![](https://mc.qcloudimg.com/static/img/521f4c55b460eaa71f03ed20693bc201/login.png)
&radic;&nbsp;&nbsp;&nbsp;安全登入查询
![](https://mc.qcloudimg.com/static/img/283437e5e3833bd4258e40de562abfc4/login_check.png)
- **支付类接口**  
&radic;&nbsp;&nbsp;&nbsp;刷卡支付，接口定义如下，返回0表示受理支付成功，-1表示受理失败。   需要注意的是，支付受理成功并不代表支付成功，需要通过查单接口去查询是否支付成功。
![](https://mc.qcloudimg.com/static/img/9dda0e7a882f0edb8828a76b75022d32/image.png)    
&radic;&nbsp;&nbsp;&nbsp;构造刷卡支付请求参数的例子：
![](https://mc.qcloudimg.com/static/img/444dedddf935fbc4d2b7c1c5704f6b91/image.png)    
&radic;&nbsp;&nbsp;&nbsp;调用 SDK 刷卡支付接口的例子：
![](https://mc.qcloudimg.com/static/img/b422837b1b5f809ae7e8176a87347f61/image.png)    
&radic;&nbsp;&nbsp;&nbsp;查询订单，可以查询一个订单的支付结果，支付成功则返回具体的订单信息，接口定义如下：
![](https://mc.qcloudimg.com/static/img/ba6032f3c843d5c1e0da7bf3fbc44556/image.png)    
&radic;&nbsp;&nbsp;&nbsp;构造查询订单请求参数的例子：
![](https://mc.qcloudimg.com/static/img/4b178e73fe2b6e56ca49b6812448c36f/image.png)     
&radic;&nbsp;&nbsp;&nbsp;刷卡支付调用SDK查单接口例子：
![](https://mc.qcloudimg.com/static/img/586b2a47a70695538cb90c4333ac2491/image.png)   
&radic;&nbsp;&nbsp;&nbsp;如果支付成功，订单信息保存在 order 中，为 json 格式，需要按照 `cloud_pay_sdk.proto` 中 `OrderSdk` 的结构去解析具体的订单信息。
&radic;&nbsp;&nbsp;&nbsp;取消订单，商户可以主动调用取消订单接口，取消订单接口为同步调用云支付的撤单（对应刷卡支付）或关单接口（对应扫码支付）。
![](https://mc.qcloudimg.com/static/img/db06c77ab6a495f11869d7c5b9adc10b/image.png)    
&radic;&nbsp;&nbsp;&nbsp;刷卡支付下构造取消订单请求参数的例子：    
![](https://mc.qcloudimg.com/static/img/62fb392de50bd80eb18e983b626aff3a/image.png)   
&radic;&nbsp;&nbsp;&nbsp;刷卡支付下调用SDK取消订单接口例子：    
![](https://mc.qcloudimg.com/static/img/aab8ed77b94e2a109e025ff6f855831c/image.png)
&radic;&nbsp;&nbsp;&nbsp;扫码支付，返回0表示受理支付成功，-1表示受理失败。支付受理成功并不代表预下单成功，需要通过查单接口去查询是否预下单成功。    
![](https://mc.qcloudimg.com/static/img/84c9ade2542f961c4a20bb4360dedf6f/image.png)     
&radic;&nbsp;&nbsp;&nbsp;扫码支付下构造扫码支付请求参数的例子：
![](https://mc.qcloudimg.com/static/img/ab4001e6bf1cb8d39e0d2227ff446eeb/image.png)     
&radic;&nbsp;&nbsp;&nbsp;扫码支付下调用SDK扫码支付接口例子：
![](https://mc.qcloudimg.com/static/img/ea268d59867960ef04b994cb5e5938c1/image.png)
&radic;&nbsp;&nbsp;&nbsp;申请退款，支付成功的订单，可以申请退款。申请退款接口为：
![](https://mc.qcloudimg.com/static/img/801f3d5b1b0b4049cfec73c7ff725118/image.png)     
&radic;&nbsp;&nbsp;&nbsp;构造申请退款请求参数为例子：
![](https://mc.qcloudimg.com/static/img/6fdf88d048d075ec9d6c0bb11857126c/image.png)    
&radic;&nbsp;&nbsp;&nbsp;调用申请退款请求的接口例子：
![](https://mc.qcloudimg.com/static/img/51247510ff1accc2731d744e7c22ef7f/image.png)    
&radic;&nbsp;&nbsp;&nbsp;查询退款，申请退款成功后，可以查询退款的进展：
![](https://mc.qcloudimg.com/static/img/b1410f5855e07e7adf79f782d6c9a605/image.png)    
&radic;&nbsp;&nbsp;&nbsp;构造查询退款请求参数的例子：
![](https://mc.qcloudimg.com/static/img/af1331d4ca219d8d3c7dd5f2fba99d57/image.png)      
&radic;&nbsp;&nbsp;&nbsp;调用查询退款请求的例子： 
![](https://mc.qcloudimg.com/static/img/2cf4655acfbfb2e96e10c12144c3da95/image.png)
- 门店类      
&radic;&nbsp;&nbsp;&nbsp;设置门店信息，接口定义如下：      
![](https://mc.qcloudimg.com/static/img/9f89cdd93c3ba64f9a04c702f95c42e0/image.png)    
&radic;&nbsp;&nbsp;&nbsp;构造门店请求的参数的例子：    
![](https://mc.qcloudimg.com/static/img/26abe441c73affc7794c6f667d2b5002/image.png)   
&radic;&nbsp;&nbsp;&nbsp;调用设置门店接口的例子：     
![](https://mc.qcloudimg.com/static/img/834800a1bceeca22a609b958f68b7ede/image.png)      
&radic;&nbsp;&nbsp;&nbsp;查询门店信息，接口定义如下：   
![](https://mc.qcloudimg.com/static/img/d5857289db182db67bcf882d6b8611be/image.png)     
&radic;&nbsp;&nbsp;&nbsp;查询门店接口参数打包的例子：      
![](https://mc.qcloudimg.com/static/img/70fe8fd183c2fcdfe4a3a59b3e73ceec/image.png)       
&radic;&nbsp;&nbsp;&nbsp;调用查询门店接口的例子：
![](https://mc.qcloudimg.com/static/img/ac464c1d700788e404813440b7eba188/image.png)    
- 结束函数   
&radic;&nbsp;&nbsp;&nbsp;使用云支付类接口时需要在进程退出时调用结束函数，函数定义如下：
![](https://mc.qcloudimg.com/static/img/025565506110172861aada26e31e56f5/image.png)