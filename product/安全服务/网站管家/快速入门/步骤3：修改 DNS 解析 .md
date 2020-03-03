为了使公网用户访问网站的流量经过 Web 应用防火墙的防护，需要修改 DNS 的解析记录。下面以在腾讯云云解析上修改测试站点`waf.qcloudwaf.com`的 DNS 解析为例，说明配置步骤。

1. 登录 [云解析控制台](https://console.cloud.tencent.com/cns)，在左侧导航栏中，单击【域名解析列表】，找到需要接入 Web 应用防火墙的域名`qcloudwaf.com`，单击【解析】进入解析配置界面。
	 ![](https://main.qcloudimg.com/raw/b41c71dec079758fa5b2c2fccadb1681.png)
2. 单击【添加记录】。
	 ![](https://main.qcloudimg.com/raw/2f7380ecb4a2a2d6a12878b5eef4e4f9.png)
3. 在当前配置页面中填写相应信息。
	- 主机记录填写对应网站的主机记录，本例中需要防护的是`waf.qcloudwaf.com`，即填写 waf 。
   ![4](https://main.qcloudimg.com/raw/881fa62631473226eec39fe97cc032d1.png)
	- 记录类型选择 CNAME。
   ![3](https://main.qcloudimg.com/raw/fb4d9604279ad05a8d2db97eb7858422.png)
	- 记录值填写 Web 应用防火墙分配的 CNAME 域名，分配的 CNAME 域名样式为：`xxxx.qcloudcjgj.com`。
   ![5](https://main.qcloudimg.com/raw/660137182993991acb43fde45d53053d.png)
	- 填写完毕后， 单击【保存】。
 ![6](https://main.qcloudimg.com/raw/181fd99ac73c145d359805a975540305.png)

5. 修改完成之后，待 DNS 记录生效，Web 应用防火墙即可对访问网站的流量进行防护了。同时，Web 应用防火墙检测到被防护域名解析正常之后，[Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/config) 上将提示 “正常防护”。
![](https://main.qcloudimg.com/raw/c3dfeae5cf9442df882946bb0bbec902.png)
