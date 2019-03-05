为了使公网用户访问网站的流量经过 Web 应用防火墙（网站管家）的防护，需要修改 DNS 的解析记录。下面以在腾讯云【云解析】上修改测试站点 waf.qcloudwaf.com 的 DNS 解析为例，说明配置步骤。

1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，选择【云产品】>【域名与网站】>【云解析】，在 “我的域名” 列表中，选择需要接入 Web 应用防火墙（网站管家）的域名 qcloudwaf.com ，单击【解析】进入解析配置界面。
   ![1](https://main.qcloudimg.com/raw/ac20238557922e232e31bf3fb6048a9e.png)
2. 单击【添加记录】。
   ![2](https://main.qcloudimg.com/raw/b6973835503ae256070a9c4f279fdddb.png)
    在当前配置页面中：
3. 主机记录填写对应网站的主机记录，本例中需要防护的是 waf.qcloudwaf.com，即填写 waf 。
   ![4](https://main.qcloudimg.com/raw/881fa62631473226eec39fe97cc032d1.png)
4. 记录类型选择 CNAME。
   ![3](https://main.qcloudimg.com/raw/fb4d9604279ad05a8d2db97eb7858422.png)
5. 记录值填写 Web 应用防火墙（网站管家）分配的 CNAME 域名 ```***************bd4e69fd3c8a187.qcloudcjgj.com ```。
   ![5](https://main.qcloudimg.com/raw/660137182993991acb43fde45d53053d.png)

 填写完毕后，单击【保存】。
 ![6](https://main.qcloudimg.com/raw/181fd99ac73c145d359805a975540305.png)

1. 修改完成之后，待 DNS 记录生效，Web 应用防火墙（网站管家）即可对访问网站的流量进行防护了。同时，Web 应用防火墙（网站管家）检测到被防护域名解析正常之后，控制台上将提示 “正常防护”。
   ![7](https://main.qcloudimg.com/raw/3d77a5ec02b9d684f3e52494ac2549be.png)
