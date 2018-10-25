您的域名接入 CDN 后，系统会为您自动分配一个 CNAME 域名（以 ```.cdn.dnsv1.com``` 为后缀)。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受 CDN 加速服务。
![](https://mc.qcloudimg.com/static/img/1ad97c3a92340219c728f25290ca1f78/CNAME.png)
## 腾讯云设置方法
若您的 DNS 服务商为腾讯云，您可通过如下步骤添加 CNAME 记录。
1. 登录 [域名管理](https://console.cloud.tencent.com/domain) 控制台，单击要添加 CNAME 记录的域名右侧的【解析】。
![](https://mc.qcloudimg.com/static/img/d736722a9a2f0788f55c3ea10320baab/mydomain.png)
2. 跳转到指定域名的 **记录管理** 页面，单击【添加记录】。
![](https://mc.qcloudimg.com/static/img/280a9f09e37eeb5938a8b10b7e671b9c/add_record.png)
3. 在弹出的窗口中，将 **记录类型** 设置为 CNAME，在 **主机记录** 处填写域名前缀（如：www），在 **记录值** 处填写 CNAME 域名，单击【确定】，即可添加 CNAME 记录。
![](https://mc.qcloudimg.com/static/img/398f272e255e7645c7a170c483a29f68/record_info.png)

## DNSPod设置方法
若您的 DNS 服务商为DNSPod，您可通过如下步骤添加 CNAME 记录。
![](https://mccdn.qcloud.com/static/img/5104d2605864556a130cac06b87e8187/image.png)

## 万网设置方法
若您的 DNS 服务商为万网，您可通过如下步骤添加 CNAME 记录。
![](https://mccdn.qcloud.com/static/img/f0eff3c6e223575b91322a49c1138ddf/image.png)
![](https://mccdn.qcloud.com/static/img/93e3eeef133d305dcc80433a168ee75a/image.png)

## 新网设置方法
若您的 DNS 服务商为新网，您可通过如下步骤添加 CNAME 记录。
![](https://mccdn.qcloud.com/static/img/301f06bf3f6f107fec5295f69f8c0ad3/image.png)

## 验证 CNAME 是否生效
不同的 DNS 服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您也可以通过命令行中的 PING 命令来查询 CNAME 是否生效，如果 PING 到后缀为 ```.sp.spcdntip.com``` 的域名表示域名 CNAME 已生效。