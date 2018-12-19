>  CDN 为您提供回源跟随 302 配置功能。当节点回源请求返回 302 状态码时，CDN 节点会直接向跳转地址请求资源而不返回 302 给用户。

## 配置指引
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】：
![](https://mc.qcloudimg.com/static/img/1f2cb594cd614b62b589cb20a20ed362/basic-config-1.png)
单击【回源配置】，您可以看到 **回源跟随 302 配置** 模块：
![](https://mc.qcloudimg.com/static/img/91e36432a50b741b58b73c28db60b1ef/302-config-1.png)

默认情况下，回源跟随 302 配置为关闭状态。

## 配置案例

域名 ```www.test.com``` 302 配置如下：![](https://mc.qcloudimg.com/static/img/91e36432a50b741b58b73c28db60b1ef/302-config-1.png)

用户A请求资源： ```http://www.test.com/1.jpg```，在节点未命中缓存，则节点会请求源站获取所需资源，若源站返回的 HTTP Response 状态码为 302，跳转指向地址为 ```http://www.abc.com/1.jpg```，则：
1. 节点将该 HTTP Response 直接返回给用户；
2. 用户向 ```http://www.abc.com/1.jpg``` 发起请求，若该域名未接入 CDN，则不会有加速效果；
3. 若此时用户B也向 ```http://www.test.com/1.jpg```  发起请求，则会重复上述流程。

域名 ```www.test.com``` 302 配置如下：![](https://mc.qcloudimg.com/static/img/efb7f294d8d8a55b55166df011dce492/302-config-2.png)

用户A请求资源： ```http://www.test.com/1.jpg```，在节点未命中缓存，则节点会请求源站获取所需资源，若源站返回的 HTTP Response 状态码为 302，跳转指向地址为 ```http://www.abc.com/1.jpg```，则：

1. 开启回源跟随 302 配置后，节点收到状态码为 302 的 HTTP Response 后，会直接向跳转指向的地址发起请求；
2. 获取到所需资源后，缓存至节点，并返回给用户；
3. 此时用户B也向 ```http://www.test.com/1.jpg``` 发起请求，则会在节点直接命中并返回给用户；
4. 开启回源跟随 302 配置后，最多仅跟随 3 次跳转，超出限制则会直接返回 302 给客户。
