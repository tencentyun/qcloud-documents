## 功能介绍
CNAME 加速功能是腾讯云 DNSPod 自主研发，旨在解决用户在设置多条 CNAME 解析记录时，递归服务器需要多次请求授权服务器，导致解析耗时增加的问题。
假设 `a.com`，`b.com`，`c.com` 都是在 DNSPod 解析的域名：

| 域名| 记录类型 | 记录值 |
|---------|---------|---------|
| www.a.com | CNAME | www.b.com |
| www.b.com | CNAME | www.c.com |
| www.c.com |  A | 1.2.3.4 |

一般情况下，递归需要到授权服务器请求三次才能得到 `www.a.com` 的 IP 地址，如下图所示：
![加速-1](https://mc.qcloudimg.com/static/img/57938b0d24aa1a136c852c0cf0d1abc3/123.png)
启用 CNAME 加速功能，授权服务器会把 CNAME 记录和最终的 A 记录一次返回给递归，递归服务器由请求三次授权服务器，减小到请求一次，如下图所示：
![加速-2](https://mc.qcloudimg.com/static/img/a8b35c14692209372897e985990be3a6/123.png)
这样就极大地减少了请求和应答中网络通信消耗的时间，让解析变得更快，特别是在设置多条 CNAME 解析记录的情况下，加速效果更明显。

## 功能开启
1. 登录腾讯云 [DNS 解析控制台](https://console.cloud.tencent.com/cns)，进入 “域名解析列表” 管理页面。
2. 选择您需要开启 CNAME 加速功能的域名行，进入该域名的管理页面。
3. 单击**域名设置**页签，选择**功能设置 > CNAME 加速**，并单击<span><img src="https://main.qcloudimg.com/raw/340e01340ee9908b99b80b2f3fb95c79.png" style="margin-bottom:-5px"></span>开启 CNAME 加速功能。如下图所示：
![](https://main.qcloudimg.com/raw/449adbec2fa4a51cc3dfd0697f69c553.png)

## 加速效果
>!该测试是清空缓存之后的，并且修改设置需要等待 TTL 过期。
>
- 开启 CNAME 加速前 query-time 1021 msec：
![1](https://mc.qcloudimg.com/static/img/a3b44b2e056e921ca1adac9e5dfb77d3/speedup_off.png)
- 开启 CNAME 加速后 query-time 410 msec：
![2](https://mc.qcloudimg.com/static/img/f71dfc679621faff5a93889f56c9ac48/speedup_on.jpg)
解析耗时减小59.84%，提升幅度相当明显。


## 注意事项
- 开启 CNAME 加速的相关域名必须使用腾讯云 DNS 解析或者 DNSPod 平台的解析服务，否则无法开启该功能或者加速失败，严重的甚至会造成解析错误。
- 对于已经开启 CNAME 加速的域名，当系统检测到域名没有使用腾讯云 DNS 解析服务时（例如域名注册到期、域名更换到其他 DNS 解析服务提供商等），会自动关闭该 CNAME 加速功能，当检测到域名又重新使用 DNSPod 解析服务时，会自动再开启 CNAME 加速。
- 同一域名下的不同子域名无需再单独开启 CNAME 加速，系统会自动加速。
- 域名转出之前应该关闭 CNAME 加速功能。如果已经转出，而系统还没有扫描到该域名当前的状态时，您可以亲自或 [联系技术](https://cloud.tencent.com/document/product/302/33949) 支持去关闭 CNAME 加速功能。



