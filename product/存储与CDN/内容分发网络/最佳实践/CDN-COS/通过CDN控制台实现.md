<style> 
table th:nth-of-type(1) { width:18%; } 
table th:nth-of-type(2){ width:82%; } 
</style>

本文详细描述了通过 CDN 加速 COS 的整体操作流程和具体的操作方法。

## 前提条件

1. 完成腾讯云账号注册、实名认证。
2. 创建 COS 存储桶，详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。

## 操作指南

### 添加域名

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧导航栏中，单击**域名管理**进入域名管理页面，单击**添加域名**。 ![img](https://main.qcloudimg.com/raw/3d2e458b232cdc89fafb546045a92bc1.png)

### 选择 COS 作为源站

#### 第一部分：域名配置

在域名处填充您需要加速的区域，自身的服务域名，为其选择项目、加速类型、是否开启 IPv6 访问和标签：
<img src="https://main.qcloudimg.com/raw/1d61e97e96d35779b33b00122aa1b5e8.png" width="60%">

#### 第二部分：源站配置

配置业务源站相关信息，CDN 节点在缓存无资源时，会回源站拉取并缓存：
<img src="https://qcloudimg.tencent-cloud.cn/raw/0851c32e32ed6133ba9b096174db4042.png" width="60%">


1. 在**域名配置**中的**源站类型**中选择：COS 源（即对象存储）。
2. 根据源站支持情况，选择回源请求协议。
3. 在源站地址中选择对应的**存储桶**。
4. 开启**私有存储桶访问**，需前往 COS-bucket 权限管理先对 CDN 服务授权。确认授权后可手动开启。
5. 回源 HOST 默认，无需修改。



输入**添加域名**页面所有配置后，单击**确认添加**完成添加域名操作，请耐心等待域名配置下发至全网节点，下发时间约5 - 10分钟。

### 最后一步：配置 CNAME

添加域名成功后，在**域名管理**页面，可以查看到 CDN 为您的域名分配的加速 CNAME。
![](https://main.qcloudimg.com/raw/f588a7ee5d9497b355f3492b0016c350.png)

您需要前往接入域名的 DNS 服务商（如 Dnspod）处，为此域名添加上该 CNAME 记录，待 **DNS 配置生效后**，即可进行加速服务。详情请参见 [CNAME 配置](https://cloud.tencent.com/doc/product/228/3121)。

## 建议配置

1. 配置完成后，为 COS 下的资源文件做好预热。提前将静态资源预热至 CDN 加速节点，降低源站压力，提高响应与下载速度。详情可见 <a href="https://cloud.tencent.com/document/product/228/40273"> 缓存预热</a>。
2. 配置好跨域的头部参数。解决资源的跨域权限问题，详情可见 <a href="https://cloud.tencent.com/document/product/228/41737#.E5.A4.B4.E9.83.A8.E5.8F.82.E6.95.B0">HTTP 响应头配置</a>。
3. 若客户源站的资源已修改，建议刷新缓存后再重新进行预热。详情可见 <a href="https://cloud.tencent.com/document/product/228/6299">缓存刷新</a>。
