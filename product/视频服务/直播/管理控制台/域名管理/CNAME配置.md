您的域名接入腾讯云直播后，系统会为您自动分配一个 CNAME 域名（以 .liveplay.myqcloud.com 为后缀)。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受腾讯云直播服务。播放域名和推流域名均需完成 CNAME 解析。

## 腾讯云设置方法
若您的 DNS 服务商为腾讯云，您可通过如下步骤添加 CNAME 记录：
1. 登录 [域名服务控制台](https://console.cloud.tencent.com/domain)，单击要添加 CNAME 记录的域名右侧的【解析】。
![](https://main.qcloudimg.com/raw/67dda19da4a1995507648eedd85af37b.png)

2. 跳转到指定域名的域名解析页面，单击【添加记录】。
![](https://main.qcloudimg.com/raw/edc2202d3906cae23163e1ca62e89dfe.png)
3. 在【主机记录】处选填写域名前缀（如：www），将【记录类型】设置为 CNAME，在【记录值】处填写 CNAME 域名，单击【保存】，即可添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/8a4a3fc6179c1b09fef2d69b1a673356.png)

## DNSPod 设置方法
若您的 DNS 服务商为 DNSPod，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/c78f494c6b550562ddb49a255f1caf0d.png)

## 万网设置方法
若您的 DNS 服务商为万网，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/2d5e7afc347f2dd549c2e83c5e2c3f46.png)
![](https://main.qcloudimg.com/raw/0640d16350ad8d8e54ff5d8cf2230c8b.png)



## 新网设置方法
若您的 DNS 服务商为新网，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/caaa0fb6c0af5d58cc8012e9d090b5b9.png)


## 验证 CNAME 是否生效
不同的 DNS 服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您也可以通过命令行中的 PING 命令来查询 CNAME 是否生效，如果 PING 到后缀为 .myqcloud.com 的域名表示域名 CNAME 已生效。
