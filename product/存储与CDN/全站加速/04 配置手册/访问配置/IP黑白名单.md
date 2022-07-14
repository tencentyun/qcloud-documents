## 配置场景


若您希望对业务资源的访问来源进行控制，腾讯云 ECDN 为您提供了 IP 黑白名单配置功能。

通过对用户请求端 IP 配置访问控制策略，可以有效限制访问来源，阻拦恶意 IP 盗刷、攻击等问题。

>? 若您的业务已迁移至 CDN 控制台，请参考 [CDN 产品文档](https://cloud.tencent.com/document/product/228)，前往 CDN 控制台进行操作。


## 配置指南

### 查看配置

登录 [ECDN 控制台](https://console.cloud.tencent.com/ecdn)，在菜单栏里选择**域名管理**，单击域名右侧**管理**，即可进入域名配置页面，**访问配置**中可看到 IP 黑白名单配置：
![](https://main.qcloudimg.com/raw/232a95e0cfc751ef39e5ef426644b177.png)

### 修改配置

#### 1. 修改配置

单击**编辑**，选择黑名单/白名单，并填入 IP 或 IP 段列表并单击**确认**，即可启用 IP 黑/白名单配置：
![](https://main.qcloudimg.com/raw/2ad85f101e207b9ef1adadeb4a487bd7.png)
**IP 黑名单**
用户端 IP 匹配黑名单中的 IP 或 IP 段时 ，访问 ECDN 节点时将直接返回403状态码。
**IP 白名单**
用户端 IP 未匹配白名单中的 IP 或 IP 段时 ，访问 ECDN 节点时将直接返回403状态码。
**名单规则**

- IP 黑名单与 IP 白名单二选一，不可同时配置。
- IP 段仅支持 /8、/16、/24、/32 网段，不支持其他网段。
- 不支持`IP：端口`形式的黑白名单，名单最多可输入50个。

## 配置示例

若加速域名`www.test.com`的 IP 黑白名单配置如下：
![](https://main.qcloudimg.com/raw/e4bac1c57fc09d06eab351d289f2c94b.png)
则实际访问情况如下：

1. 用户端 IP 为`1.1.1.1`的用户访问资源`http://www.test.com/test.txt`，匹配白名单，正常返回内容。
2. 用户端 IP 为`2.1.1.1`的用户访问资源`http://www.test.com/test.txt`，未匹配白名单，返回403。

