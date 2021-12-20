本文档将指导您如何修改 DNS 的解析记录，使公网用户访问网站的流量经过 Web 应用防火墙的防护。

## 操作步骤
为了使公网用户访问网站的流量经过 Web 应用防火墙的防护，需要修改 DNS 的解析记录。下面以在腾讯云 DNS 解析 DNSPod 上修改测试站点 `waf.qcloudwaf.com` 的 DNS 解析为例，说明配置步骤。

1. 登录 [DNS 解析 DNSPod 控制台](https://console.cloud.tencent.com/cns)，在左侧导航栏中，单击**域名解析列表**，找到需要接入 Web 应用防火墙的域名`.technicalsupport.cn`，单击**解析**进入解析配置界面。
![](https://qcloudimg.tencent-cloud.cn/raw/b87453ac773ebcf238663a09df446db8.png)
2. 单击**添加记录**。
	 ![](https://main.qcloudimg.com/raw/2f7380ecb4a2a2d6a12878b5eef4e4f9.png)
3. 在当前配置页面中填写相应信息。
	- 主机记录填写对应网站的主机记录，本例中需要防护的是`saas.technicalsupport.cn`，即填写 saas 。
![](https://qcloudimg.tencent-cloud.cn/raw/2eed8406e86ce877ff636484f67ac4e0.png)
	- 记录类型选择 CNAME。
   ![3](https://main.qcloudimg.com/raw/fb4d9604279ad05a8d2db97eb7858422.png)
	- 记录值填写 Web 应用防火墙分配的 CNAME 域名，分配的 CNAME 域名样式为：`xxxx.qcloudcjgj.com`。
  ![](https://qcloudimg.tencent-cloud.cn/raw/f12b77af90d46bb985b8a4a127e7c3e1.png)
	- 填写完毕后， 单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/6c9faae0974e4ddade0df0ffa2bc83e4.png)

5. 修改完成之后，待 DNS 记录生效，Web 应用防火墙即可对访问网站的流量进行防护了。同时，Web 应用防火墙检测到被防护域名解析正常之后，[Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-domain) 上将提示 “正常防护”。
>?DNS 记录生效需要10分钟左右时间。
>
![](https://qcloudimg.tencent-cloud.cn/raw/92a6da061f60c99a8d835325303e3ccf.png)

## 后续步骤
当您修改完成 DNS 的解析记录后，可执行 [步骤 4：设置安全组](https://cloud.tencent.com/document/product/627/18634)。
