### 腾讯云解析是否支持 IPv6-only 环境？  
腾讯云 DNSPod 域名解析支持 IPv6-only 网络环境，并且在境内外均验证解析成功。
### 提交 App Store 的 iOS 在本地环境测试通过，却在 App Store 审核时被拒是什么原因？  
* **排查是否由 DNS 解析失败引起**  
那么如何验证 DNS 服务器是否正确响应了 IPv6 地址的解析请求呢？搭建好 DNS64 环境后，可以通过以下命令查询：
```
$ dig dnspod.cn aaaa
```
验证 DNS 解析的原因是：App 访问网络的第一步就是进行 DNS 解析，App Store 审核时会先访问 DNS 服务器，获得 iOS 应用服务器的 IPv6 地址，再进行访问，如果这时 DNS 服务器无法成功解析到 IPv6 地址，即使在本地搭建的 IPv6-only 环境中测试成功，仍然会出现在提交 App Store 审核时被拒的情况，所以选择一个稳定性、兼容性俱佳的域名解析服务至关重要。
* **可能跨国网络质量的原因**  
DNS 一般是通过 IP 地址库来实现 GEO 分地区解析的，而 IPv6 没有地址库，所有 IPv6 的解析都是解析到默认线路的地址的。如果默认线路是设置的电信或者 BGP（CAP，默认走电信）的 IP ，因为电信的跨国质量问题，会有很大概率在国外无法连接，也就无法通过，所以建议：  
 1. 将审核所必须功能的域名的默认 IP 修改为联通或移动。
 2. 审核所必须功能接入动态加速服务，可以对跨国访问进行加速。  
### 如何使 iOS 应用支持 IPv6-only 环境？  
目前使 iOS 应用支持 IPv6-only 环境有三种方式可以尝试，如下所示：    
* 应用中的所有域名接入 DNSPod  
腾讯云的业务底层 DNS 解析和 DNSPod 域名解析均支持 IPv6-only，能保证业务在 IPv6-only 的环境中成功解析。iOS 应用服务器不需要支持 IPv6，IPv6-only 环境下 DNS64/NAT64 可以将 IPv4 地址转化为 IPv6 地址。
* 改造客户端  
例如使用 IP 直接访问的问题、SDK 接口等升级兼容 IPv6。
* 搭建环境验证  
参考 [苹果官网文档](https://developer.apple.com/library/ios/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/UnderstandingandPreparingfortheIPv6Transition/UnderstandingandPreparingfortheIPv6Transition.html#//apple_ref/doc/uid/TP40010220-CH213-SW1) 搭建 IPv6-only 的热点，用 iPhone 连接热点测试。

