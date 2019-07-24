您的域名接入 CDN 后，系统会为您自动分配一个以 `.cdn.dnsv1.com` 为后缀的 CNAME 域名，可在 CDN 控制台 [域名管理页](https://console.cloud.tencent.com/cdn/access) 查看。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受 CDN 加速服务。
![](https://main.qcloudimg.com/raw/78d17f30169609610fd7a2eda4ceaf1d.png)

## 腾讯云设置方法
若您的 DNS 服务商为腾讯云，您可通过如下步骤添加 CNAME 记录。
1. 登录 [域名服务](https://console.cloud.tencent.com/domain) 控制台，在列表中，找到需要添加 CNAME 记录的域名所在行，单击操作栏的【解析】。
![CNAME配置](https://main.qcloudimg.com/raw/12eba66e1d073aade459318d6e9c53ef.png)
2. 在跳转到的页面中，单击【添加记录】。
 ![](https://main.qcloudimg.com/raw/88a0cda619aeaf1a88120ad5294250fa.png)
3. 在 **主机记录** 处填写域名前缀（如：www），将 **记录类型** 设置为 CNAME，在 **记录值** 处填写 CNAME 域名，单击【保存】，即可添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/24ee35e7bba9d181abbdaf65fe7fc3cb.png)

## DNSPod 设置方法
若您的 DNS 服务商为 DNSPod，您可通过如下步骤添加 CNAME 记录。
![](https://mccdn.qcloud.com/static/img/5104d2605864556a130cac06b87e8187/image.png)

## 万网设置方法
若您的 DNS 服务商为万网，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/40807fb309311697a542e556a4d33710.png)
![](https://main.qcloudimg.com/raw/a92777ba4b09168e187103d18a1ff152.png)

## 新网设置方法
若您的 DNS 服务商为新网，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/cb654e02602b6dd277978c185799b307.png)

## 验证 CNAME 是否生效
不同的 DNS 服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您也可以通过命令行中的 PING 命令来查询 CNAME 是否生效，如果 PING 到后缀为 `.sp.spcdntip.com` 的域名表示域名 CNAME 已生效。
