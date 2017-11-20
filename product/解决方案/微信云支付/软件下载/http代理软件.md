## 代理网络下使用云支付收银终端
### 代理网络结构
- 公司为了安全考虑，员工的电脑都处在局域网环境办公。为了给局域网的电脑访问外网的权限，公司会在局域网和外网之间加一个代理服务器（代理服务器本身可以访问外网），然后局域网的电脑可以通过这个代理服务器访问外网。网络结构如下图：
![](https://mc.qcloudimg.com/static/img/33a637b9071ab4df9ba083a698725450/image.png)   
### 收银终端访问外网
- 代理服务器安装代理软件WProxy（这里只是举例，也可安装其他代理软件）
√ 在代理服务器上安装WProxy软件，一款免费的代理软件，官网有详细的配置说明；
√ WProxy官网下载地址http://www.imfirewall.com/WProxy.htm
√ WProxy配置说明见官网的演示图片。
- 收银终端访问外网（免用户名和密码）
√ 服务商在配置收银终端时，可以点击设置代理，然后填写代理URL，格式为:http://proxy_server_ip:proxy_server_port，然后点击保存即可。
![](https://mc.qcloudimg.com/static/img/0445fbe86f69c8859d89d9848abc92c5/image.png)   
- 收银终端访问外网（需要用户名和密码）
√ 代理服务器安装WFilter 
 - 公司可能会给局域网的员工分配代理账户和密码，只有账户的员工才有访问外网的权限；
 - 在代理服务器上安装WProxy后，再安装WFilter（超级嗅探狗），使用WFilter分配账户，然后设置WFilter监控局域网内的机器。在局域网访问外网时，就会提示对需要使用代理上网的机器进行账号验证；
 - 注：WFilter是需要交费的，有30天的免费试用期；
 - 官方下载地址：http://www.imfirewall.com/WFilter.htm ；
 - 账户的详细配置方式：http://www.imfirewall.com/support/WFilter_4_1/Doc/WFilter_Local_Account.htm 。
√ 收银终端访问外网
 - 服务商在配置收银终端时，可以点击设置代理，然后填写代理URL，格式为:http://proxy_server_ip:proxy_server_port、 代理用户名、密码，然后点击保存即可 。
 ![](https://mc.qcloudimg.com/static/img/7d33d87ca0a44b8c2a624cace5f182f9/image.png)   
 ## 代理网络下使用订单查询终端
### 代理网络结构
- 公司为了安全考虑，员工的电脑都处在局域网环境办公。为了给局域网的电脑访问外网的权限，公司会在局域网和外网之间加一个代理服务器（代理服务器本身可以访问外网），然后局域网的电脑可以通过这个代理服务器访问外网。网络结构如下图。
![](https://mc.qcloudimg.com/static/img/33a637b9071ab4df9ba083a698725450/image.png)   
### 订单查询终端访问外网
- 代理服务器安装代理软件WProxy
 - 在代理服务器上安装WProxy软件，一款免费的代理软件，官网有详细的配置说明。
 - WProxy官网下载地址http://www.imfirewall.com/WProxy.htm
 - WProxy配置说明见官网的演示图片。
- 订单查询终端访问外网（免用户名和密码）
 - 服务商在配置订单查询终端时，可以点击设置代理，然后填写代理URL，格式为:http://proxy_server_ip:proxy_server_port，然后点击保存即可。
 ![](https://mc.qcloudimg.com/static/img/74848ab56b089654e3be7ddf6b61d0c3/image.png)   
- 订单查询终端访问外网（需要用户名和密码）
 - 代理服务器安装WFilter 
 - 公司可能会给局域网的员工分配代理账户和密码，只有账户的员工才有访问外网的权限。
 - 在代理服务器上安装WProxy后，再安装WFilter（超级嗅探狗），使用WFilter分配账户，然后设置WFilter监控局域网内的机器。在局域网访问外网时，就会提示对需要使用代理上网的机器进行账号验证。 
 - 注：WFilter是需要交费的，有30天的免费试用期。
 - 官方下载地址：http://www.imfirewall.com/WFilter.htm
 - 账户的详细配置方式：
http://www.imfirewall.com/support/WFilter_4_1/Doc/WFilter_Local_Account.htm
- 订单查询终端访问外网
 - 服务商在配置订单查询终端时，可以点击设置代理，然后填写代理URL，格式为:http://proxy_server_ip:proxy_server_port、代理用户名、密码，然后点击保存即可。
![](https://mc.qcloudimg.com/static/img/338c9aff68a894f416aa3730366fcb87/image.png)
