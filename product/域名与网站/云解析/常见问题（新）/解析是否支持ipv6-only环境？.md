### 腾讯云 DNS 解析是否支持 IPv6-only 环境？  
腾讯云 DNSPod 域名解析支持 IPv6-only 网络环境，并且在境内外均验证解析成功。

### 提交 App Store 的 iOS 在本地环境测试通过，却在 App Store 审核时被拒是什么原因？  
- **排查是否由 DNS 解析失败引起**  
那么如何验证 DNS 服务器是否正确响应了 IPv6 地址的解析请求呢？搭建好 DNS64 环境后，可以通过执行以下命令查询：
```
$ dig dnspod.cn aaaa
```
验证 DNS 解析的原因是：App 访问网络的第一步就是进行 DNS 解析，App Store 审核时会先访问 DNS 服务器，获得 iOS 应用服务器的 IPv6 地址，再进行访问，如果这时 DNS 服务器无法成功解析到 IPv6 地址，即使在本地搭建的 IPv6-only 环境中测试成功，仍然会出现在提交 App Store 审核时被拒的情况，所以选择一个稳定性、兼容性俱佳的域名解析服务至关重要。
- **可能跨国网络质量的原因**  
DNS 一般是通过 IP 地址库来实现 GEO 分地区解析，而 IPv6 没有地址库，所有 IPv6 的解析都是解析到默认线路的地址。如果默认线路是设置的电信或者 BGP（CAP，默认走电信）的 IP ，因为电信的跨国质量问题，会有很大概率在国外无法连接，也就无法通过。所以建议如下内容：    
 - 将审核所必须功能的域名的默认 IP 修改为联通或移动。
 - 将审核所必须功能接入动态加速服务，可以对跨国访问进行加速。

### 如何使 iOS 应用支持 IPv6-only 环境？  
目前使 iOS 应用支持 IPv6-only 环境有如下三种方式可以尝试：    
- 应用中的所有域名接入 DNSPod  
腾讯云的业务底层 DNS 解析和 DNSPod 域名解析均支持 IPv6-only，能保证业务在 IPv6-only 的环境中成功解析。iOS 应用服务器不需要支持 IPv6，IPv6-only 环境下 DNS64/NAT64 可以将 IPv4 地址转化为 IPv6 地址。
- 改造客户端  
例如，使用 IP 直接访问的问题、SDK 接口等升级兼容 IPv6。
- 搭建环境验证  
参考 [苹果官网文档](https://developer.apple.com/library/ios/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/UnderstandingandPreparingfortheIPv6Transition/UnderstandingandPreparingfortheIPv6Transition.html#//apple_ref/doc/uid/TP40010220-CH213-SW1) 搭建 IPv6-only 的热点，使用 iPhone 连接热点测试。

### 腾讯云 DNSPod 能够隐藏 IP 解析吗？
域名解析不能 IP 隐藏，域名解析是将域名映射为 IP。  

### 一个域名分别指定了电信、联通的 IP，但有时候电信或联通中有一个 IP 会不通，能否设置自动暂停不通 IP 的解析？
使用 D 监控功能可以实现。
具体请参考：[D 监控的使用教程](https://support.dnspod.cn/d-monitor/)。

### 删除或暂停记录后，为什么执行 ping 命令连接域名还能得到 IP 呢？
原因是地方 ISP 提供商的服务器（递归服务器）缓存导致的，请耐心等待地方缓存失效，缓存失效时间理论上为之前记录设置的 TTL 时间。

### 域名的解析结果和解析 IP 不一致是什么原因？
建议使用 DNSPod 官方网站的 [DNS.TECH 域名检测](https://dns.tech/) 功能，如果您换域名解析商未过72小时且换了新空间，请耐心等待生效。

### 在智能解析中，为什么联通用户解析到了电信服务器的 IP？
1. 首先请确认您所使用的网络是非杭州华数和北京长宽的线路。
2. 使用 DNSPod 的解析未超过72小时，请耐心等待解析生效。
3. 联通主机服务器宕机，D 监控将联通线路的记录值自动切换到电信服务器的 IP。联通服务器恢复正常，记录值将自动切换回联通的 IP。 
4. 检查本机 DNS 是否与线路相符，若不符则修改本机 DNS 与线路一致即可。
5. 查看本机是否在 hosts 文件中设置域名指向某个 IP。

### 域名更改 IP 后，搜索引擎蜘蛛为什么还是爬之前的服务器？
搜索引擎有自己的更新期，不同的搜索引擎更新期是不同的，其最短更新期为一周，域名修改 IP 后，搜索引擎需要一段时间来更新，请耐心等待搜索引擎更新。


