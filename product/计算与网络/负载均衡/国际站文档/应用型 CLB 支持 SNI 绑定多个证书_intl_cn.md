## 什么是 SNI？
服务器名称指示（Server Name Indication，SNI）是用来改善服务器与客户端 SSL/TLS 的扩展，主要解决一台服务器只能使用一个证书的缺点，支持 SNI 表示服务器支持绑定多个证书。客户端使用 SNI，则需在与服务器建立 SSL/TLS 连接之前指定要连接的域名，服务器会根据这个域名返回一个合适的证书。CLB 支持 SNI 功能正在内测中，如需使用，请通过 [工单申请](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=163&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB)。

腾讯云应用型负载均衡的七层 HTTPS 监听器支持 SNI，即支持绑定多个证书，监听规则中的不同域名可使用不同证书。
## 使用前提
使用 SNI 支持绑定多证书需以下前提条件：
- 已购买**应用型**负载均衡实例。
- 已拥有证书。

## 操作步骤
### 购买应用型负载均衡
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/loadbalance)。
2. [购买](https://buy.cloud.tencent.com/lb) 应用型负载均衡。

### 创建 HTTPS 监听器并配置 SNI
1. 创建 HTTPS 监听器时，关闭多域名共用证书。
多域名共用证书表示服务器上多个域名共用一个证书，即为关闭 SNI；关闭多域名共用证书即为启用 SNI，服务器支持不同域名使用不同证书。
 ![](https://main.qcloudimg.com/raw/6e8495b977902008382d6bb622116556.png)
2. 在该监听器中添加转发规则时，针对不同的域名可选用不同的服务器证书。
 ![](https://main.qcloudimg.com/raw/94089a2f01a2539df72787ae11804974.png)
