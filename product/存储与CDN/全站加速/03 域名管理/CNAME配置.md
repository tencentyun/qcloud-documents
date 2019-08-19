您的域名接入 ECDN 后，系统会为您自动分配一个 CNAME 域名（以`.dsa.dnsv1.com`为后缀)。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受 ECDN 加速服务。
![](https://main.qcloudimg.com/raw/2a1ebdce1a0978ee162ccb3d534eabaf.png)

## 腾讯云设置方法
若您的 DNS 服务商为腾讯云，您可通过如下步骤添加 CNAME 记录。
1. 登录 [域名管理](https://console.cloud.tencent.com/domain) 控制台，在“我的域名”列表中，找到需要添加 CNAME 记录的域名，单击操作类中的【解析】。
![](https://main.qcloudimg.com/raw/66826f1e9105e359279b6290a3dcd5d4.png)
2. 跳转到指定域名的 **记录管理** 页面，单击【添加记录】。
![](https://main.qcloudimg.com/raw/53b07e045bddf3d8b8a11ec8d8dced4b.png)
3. 在弹出框中，将 **记录类型** 设置为 CNAME，在 **主机记录** 处填写域名前缀（如：www），在 **记录值** 处填写 CNAME 域名，单击【确定】，即可添加 CNAME 记录。
![](https://mc.qcloudimg.com/static/img/1374c7877eca588d8a14779a60b13a1e/add_cname.png)

## DNSPod 设置方法
若您的 DNS 服务商为 DNSPod，您可通过如下步骤添加 CNAME 记录。
![](https://mc.qcloudimg.com/static/img/419c169fdcb37b8ec6d3fae687851bfa/dnspod.png)

## 万网设置方法
若您的 DNS 服务商为万网，您可通过如下步骤添加 CNAME 记录。
![](https://mc.qcloudimg.com/static/img/fb60c59705d37b0d132a8f62e32f7ccc/wang.png)

## 新网设置方法
若您的 DNS 服务商为新网，您可通过如下步骤添加 CNAME 记录。
![](https://mccdn.qcloud.com/static/img/301f06bf3f6f107fec5295f69f8c0ad3/image.png)

## 验证 CNAME 是否生效
不同的 DNS 服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您也可以通过命令行中的 PING 命令来查询 CNAME 是否生效，如果 PING 到后缀为`.ecdn.sp.spcdntip.com`或`.ecdn.p23.tc.cdntip.com`的域名，表示域名 CNAME 已生效。
![](https://mc.qcloudimg.com/static/img/3e45aca57e30b993541c16d83d07d154/image.png)
![](https://mc.qcloudimg.com/static/img/c3deeb94c05f02ae934d2f7bb7673f28/image.png)
