
添加完成加速域名后，CDN 会为您分配一个 CNAME 域名。您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受 CDN 加速服务。如下将为您提供配置示例，更多详细操作请查看 [配置 CNAME](https://cloud.tencent.com/document/product/228/3121)。
- 若您的域名解析服务商为腾讯云：
![](https://qcloudimg.tencent-cloud.cn/raw/d938b5198158c689b800c3741ad52bd5.png)
- 若您的域名解析服务商为阿里云：
![](https://qcloudimg.tencent-cloud.cn/raw/3bb332e784bde31f80ce1eb26c1ad1db.png)
配置完成后您可通过 nslookup 或 dig 命令验证是否生效。若生效，会显示“加速服务正常运行中”。
测试命令：`nslookup www.qcdntest.cn或dig www.qcdntest.cn`，若有返回 CNAME 域名，说明域名解析已指向腾讯云。
![](https://qcloudimg.tencent-cloud.cn/raw/efb293deae93f16e96d22c91ac29050f.png)
<img src="https://qcloudimg.tencent-cloud.cn/raw/8e65d17fd785696b21cad2b091da6c1c.png" width="70%">
