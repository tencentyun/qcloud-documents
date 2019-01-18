腾讯云DNSPod域名解析支持 IPv6-only 网络环境，并且在境内外均验证解析成功。

### 背景
自2016年6月1日起，苹果要求所有提交 App Store 的 iOS 应用必须支持 IPv6-only 环境，背景也是众所周知的，IPv4 地址已基本分配完毕，同时 IPv6 比 IPv4 也更加高效，向 IPv6 过渡是大势所趋。
然而在对 IPv6 进行兼容适配过程中，很多开发者在本地环境测试通过，却在 App Store 审核时被拒，这种情况下可以首先排查是否由 DNS 解析失败引起，那么如何验证 DNS 服务器是否正确响应了 IPv6 地址的解析请求呢？搭建好 DNS64 环境后，可以通过以下命令查询：
```
$ dig dnspod.cn aaaa
```

验证 DNS 解析的原因是：App 访问网络的第一步就是进行 DNS 解析，App Store 审核时会先访问 DNS 服务器，获得 iOS 应用服务器的IPv6地址，再进行访问，如果这时 DNS 服务器无法成功解析到 IPv6 地址，即使在本地搭建的 IPv6-only 环境中测试成功，仍然会出现在提交 App Store 审核时被拒的情况。所以选择一个稳定性、兼容性俱佳的域名解析服务至关重要！

经过全面的测试和灰度发布，腾讯云DNSPod域名解析已全面支持App Store IPv6-only 网络环境，已有成功通过审核案例，并且在境内外均验证解析成功。

### iOS 应用支持 IPv6-only 环境说明

#### 1. 应用中的所有域名接入 DNSPod
腾讯云的业务底层 DNS 解析和 DNSPod 域名解析均支持 IPv6-only，能保证业务在 IPv6-only 的环境中成功解析。
iOS 应用服务器不需要支持 IPv6，IPv6-only 环境下 DNS64/NAT64 可以将 IPv4 地址转化为 IPv6 地址。

#### 2. 改造客户端
例如使用 IP 直接访问的问题、SDK接口等升级兼容 IPv6。

#### 3. 搭建环境验证
参考 [苹果官网文档](https://developer.apple.com/library/ios/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/UnderstandingandPreparingfortheIPv6Transition/UnderstandingandPreparingfortheIPv6Transition.html#//apple_ref/doc/uid/TP40010220-CH213-SW1) 搭建 IPv6-only 的热点，用 IPhone 连接热点测试。

#### 4. 其他建议
如果确认自建 DNS64 环境测试完全正常，但提交 APP Store 审核依然无法访问的话，排除 DNS 支持问题和访问服务器的接口问题，还有一个很重要的原因就是跨国网络质量的原因。
DNS 一般是通过 IP 地址库来实现 GEO 分地区解析的，而 IPv6 没有地址库，所有 IPv6 的解析都是解析到默认线路的地址的。如果默认线路是设置的电信或者 BGP（CAP，默认走电信）的 IP ，因为电信的跨国质量问题，会有很大概率在国外无法连接，也就无法通过。所以建议：
1. 将审核所必须功能的域名的默认 IP 修改为联通或移动。
2. 审核所必须功能接入动态加速服务，可以对跨国访问进行加速。
