## HTTP 代理简介

### 代理网络结构
公司为了安全考虑，员工的电脑都处在局域网环境办公。为了给局域网的电脑访问外网的权限，公司会在局域网和外网之间加一个代理服务器（代理服务器本身可以访问外网），然后局域网的电脑可以通过这个代理服务器访问外网。网络结构如下图：
![](https://mc.qcloudimg.com/static/img/33a637b9071ab4df9ba083a698725450/image.png)   

### 安装代理软件 WProxy（仅为示例，也可安装其他代理软件）
- 免用户名和密码代理模式
在代理服务器上安装 WProxy 软件，一款免费的代理软件，下载 WProxy 参见 [官网地址](http://www.imfirewall.com/WProxy.htm)，WProxy 配置说明见官网的演示图片。
- 需要用户名和密码模式
 - 公司可能会给局域网的员工分配代理账户和密码，仅有账户的员工才有访问外网的权限。
 - 在代理服务器上安装 WProxy 后，再安装 WFilter（超级嗅探狗），使用 WFilter 分配账户，然后设置 WFilter 监控局域网内的机器。在局域网访问外网时，就会提示对需要使用代理上网的机器进行账号验证。
>!WFilter 是需要交费的，有30天的免费试用期，[官方下载地址](http://www.imfirewall.com/WFilter.htm)，[账户的详细配置方式](http://www.imfirewall.com/support/WFilter_4_1/Doc/WFilter_Local_Account.htm)。   

## 收银台访问外网
服务商在配置收银台时，可以单击**设置网络代理**，然后填写代理服务器的 IP、端口、用户名和密码（如果用户名和密码没有则不用填写），然后单击**保存**即可。
![](https://main.qcloudimg.com/raw/ad6201299509d886390449c99c215ed3.png) 

## 订单查询终端访问外网
服务商在配置订单查询终端时，可以单击**设置代理**，填写代理 URL（格式为：`http://proxy_server_ip:proxy_server_port`）、用户名和密码（如没有则不用填写），然后单击**设置**保存即可。
 ![](https://mc.qcloudimg.com/static/img/74848ab56b089654e3be7ddf6b61d0c3/image.png)   
