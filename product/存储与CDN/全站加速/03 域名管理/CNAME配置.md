您的域名接入 ECDN 后，系统会为您自动分配一个 CNAME 域名（以`.dsa.dnsv1.com`为后缀)。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受 ECDN 加速服务。
![](https://main.qcloudimg.com/raw/69802e106ed7b373195179d6b9773438.png)

## 腾讯云设置方法
若您的 DNS 服务商为腾讯云，您可通过如下步骤添加 CNAME 记录。
1. 登录 [域名管理](https://console.cloud.tencent.com/domain) 控制台，在“我的域名”列表中，找到需要添加 CNAME 记录的域名，单击操作类中的【解析】。
![](https://main.qcloudimg.com/raw/5687364cbdec038240c9b37373524d39.png)
2. 跳转到指定域名的 **记录管理** 页面，单击【添加记录】。
![](https://main.qcloudimg.com/raw/7c91ba3dffd64c7829e2cb1667e3c86b.png)
3. 在弹出框中，将 **记录类型** 设置为 CNAME，在 **主机记录** 处填写域名前缀（如：www），在 **记录值** 处填写 CNAME 域名，单击【确定】，即可添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/62a4fa35db0aafebae75c151cfc9f449.png)

## DNSPod 设置方法
若您的 DNS 服务商为 DNSPod，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/49f2b661f302dd50368718e415a371f8/dnspod.png)

## 万网设置方法
若您的 DNS 服务商为万网，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/c311f1b82a99ff34eae7d9bfb859debc/wang.png)

## 新网设置方法
若您的 DNS 服务商为新网，您可通过如下步骤添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/d0338015f16a091ea6fe1dd2ed70593c.png)

## 验证 CNAME 是否生效
不同的 DNS 服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您也可以通过命令行中的 PING 命令来查询 CNAME 是否生效，如果 PING 到后缀为`.dsa.sp.spcdntip.com`或`.dsa.p23.tc.cdntip.com`的域名，表示域名 CNAME 已生效。
![](https://main.qcloudimg.com/raw/e089136ab0e4d4acd12064af7c8c7a1f.png)
![](https://main.qcloudimg.com/raw/635eb4d1b85602323d19c22629c12013.png)
