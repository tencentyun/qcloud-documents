## 什么是 SNI
服务器名称指示（Server Name Indication，SNI）是用来改善服务器与客户端 SSL/TLS 的扩展，主要解决一台服务器只能使用一个证书的缺点，支持 SNI 表示服务器支持绑定多个证书。客户端使用 SNI，则需在与服务器建立 SSL/TLS 连接之前指定要连接的域名，服务器会根据这个域名返回一个合适的证书。
>?CLB 支持 SNI 功能正在内测中，如需使用，请通过 [工单申请](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=163&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB)。

## 使用场景
腾讯云负载均衡的七层 HTTPS 监听器支持 SNI，即支持绑定多个证书，监听规则中的不同域名可使用不同证书。如在同一个 CLB 的 HTTPS:443 监听器中，`*.test.com`使用证书1，将来自该域名的请求转发至一组服务器上；`*.example.com`使用证书2，将来自该域名的请求转发至另一组服务器上。

## 操作步骤
### 购买负载均衡
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)。
2. 在 “CLB 实例列表”页中，单击【新建】，购买负载均衡。
>? 传统型负载均衡不支持基于域名和 URL 的转发，因此传统型负载均衡不支持 SNI。

### 配置 HTTPS 监听器并启用 SNI
1. 创建 HTTPS 监听器时，开启 SNI。
![](https://main.qcloudimg.com/raw/1665fb3a16b95979e92bff414a36912e.png)
2. 在该监听器中添加转发规则时，针对不同的域名配置不同的服务器。
![](https://main.qcloudimg.com/raw/3ea592cd74976965bb0d6529881965d6.png)
