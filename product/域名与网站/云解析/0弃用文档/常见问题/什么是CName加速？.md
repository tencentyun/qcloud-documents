### 1. 功能介绍

CNAME 加速功能是腾讯云 DNSPod 自主研发，旨在解决用户在设置多跳 CNAME 解析记录时，递归服务器需要多次请求授权服务器，导致解析耗时增加的问题。

假设 a.com, b.com, c.com 都是在 DNSPod 解析的域名：
www.a.com 设置 CNAME 记录，记录值为 www.b.com
www.b.com 设置 CNAME 记录，记录值为 www.c.com
www.c.com 设置 A 记录，记录值为 1.2.3.4

一般情况下，递归需要到授权服务器请求三次才能得到 www.a.com 的 IP 地址，如下图所示：
![加速-1](https://mc.qcloudimg.com/static/img/57938b0d24aa1a136c852c0cf0d1abc3/123.png)

启用 CNAME 加速功能，授权服务器会把 CNAME 记录和最终的 A 记录一次返回给递归，递归服务器由请求三次授权服务器，减小到请求一次，如下图所示：
![加速-2](https://mc.qcloudimg.com/static/img/a8b35c14692209372897e985990be3a6/123.png)

这样就极大地减少了请求和应答中网络通信消耗的时间，让解析变得更快，特别是在设置多跳 CNAME 解析记录的情况下，加速效果更明显。

### 2. 加速效果
开启 CNAME 加速前，query-time 1021 msec：
![](https://mc.qcloudimg.com/static/img/a3b44b2e056e921ca1adac9e5dfb77d3/speedup_off.png)

开启 CNAME 加速后，query-time 410 msec:
![](https://mc.qcloudimg.com/static/img/f71dfc679621faff5a93889f56c9ac48/speedup_on.jpg)

解析耗时减小 59.84%，提升幅度相当明显。

注：该测试是清空缓存之后的，并且修改设置需要等待 TTL 过期。

### 3. 注意事项

3.1 开启 CNAME 加速的相关域名必须都使用腾讯云 云解析 或者 DNSPod平台 的解析服务，否则无法开启该功能或者加速失败，严重的甚至会造成解析错误；

3.2 对于已经开启 CNAME 加速的域名，当系统检测到域名没有使用腾讯云解析服务的时候(比如域名注册到期、域名更换到其他 DNS 解析服务提供商等等)，会自动关闭该 CNAME 加速功能，当检测到域名又重新使用 DNSPod 解析服务的时候，会自动再开启 CNAME 加速；

3.3 同一域名下的不同子域名无需再单独开启 CNAME 加速，系统会自动加速；

3.4 域名转出之前应该关闭 CNAME 加速功能。如果已经转出，而系统还没有扫描到该域名当前的状态时，用户可以亲自或联系技术支持去关闭 CNAME加速功能。
