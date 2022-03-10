## 简介

将域名接入 [内容分发网络（Content Delivery Network，CDN）](https://cloud.tencent.com/document/product/228/2939) 后，所有用户侧资源请求将调度至 CDN 节点进行响应，若节点已缓存该资源，则直接返回内容，若 CDN 节点均未缓存该资源，会将请求透传至域名配置的源站，拉取所需资源。

由于 CDN 节点响应了绝大部分的用户请求，为了方便客户对用户访问进行分析，CDN 按照小时粒度对全网访问日志进行打包。

CDN 日志备份是腾讯云对象存储（Cloud Object Storage，COS）基于 [云函数（Serverless Cloud Function，SCF）](https://cloud.tencent.com/document/product/583) 为用户提供的将 CDN 日志转存至 COS 的功能，可以协助用户将 CDN 日志进行转存以便于进行访问行为分析、服务质量监控等。

用户在指定存储桶配置了日志备份规则后，云函数会按照一定的时间粒度获取 CDN 日志并转存至 COS 存储桶中。

## 注意事项

- 若您此前在对象存储控制台上为存储桶添加了 CDN 日志备份规则，可以在 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 上看到您所创建的 CDN 日志备份函数，请**不要**删除该函数，否则可能导致您的规则不生效。
- 已上线云函数的地域均已支持 CDN 日志备份至 COS，包括有广州、上海、香港、北京、成都、新加坡、孟买、多伦多、硅谷等，更多支持地域可查看 [云函数产品文档](https://cloud.tencent.com/document/product/583)。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 在左侧导航中，单击【应用集成】，找到【CDN 日志备份】。
3. 单击【配置备份规则】，进入规则配置页面。
4. 单击【添加函数】。
>! 如果您尚未开通云函数服务，请前往 [云函数控制台](https://console.cloud.tencent.com/scf) 开通云函数服务，按照提示完成服务授权即可。
>
5. 在弹出的窗口中，配置如下信息：
![](https://main.qcloudimg.com/raw/8a014fbad9e5ee4289b3cc219e89c971.png)
 - **函数名称**：作为函数的唯一标识名称，创建后不可修改。您可以在 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 上查看该函数。
 - **关联存储桶**：存放 CDN 日志的 COS 存储桶。
 - **触发器周期**：CDN 日志备份通过定时触发器来触发备份转存操作，触发周期支持每天、自定义周期。
 - **Cron 表达式**：当触发器周期设置为自定义时，可通过 Cron 指定具体的触发周期规则。Cron 当前以 UTC +8 中国标准时间 （China Standard Time）运行，即北京时间。详细配置策略请参见 [Cron 相关文档](https://cloud.tencent.com/document/product/583/9708#cron-.E8.A1.A8.E8.BE.BE.E5.BC.8F)。
 - **CDN 域名**：可选择转存指定的一个或多个域名的日志。
 - **投递的路径**：日志文件的投递路径，可选择投递至根目录或指定的路径前缀。
 - **SCF 授权**：CDN 日志备份需要授权云函数从您的 CDN 服务中读取日志文件，并将日志文件转存至您指定的存储桶中。因此需要添加此授权。
6. 添加配置后，单击【确认】，等待 CDN 日志备份规则创建完成。创建完成后，可在列表页中查看已创建的 CDN 日志备份规则。
![](https://main.qcloudimg.com/raw/fa352961acb88532ac8645ede23ef52f.png)
您可以对新创建的 CDN 日志备份规则进行如下操作：
 - 单击【查看日志】，查看 CDN 日志备份的历史运行情况。当备份出现报错时，您还可以通过单击【查看日志】，快速跳转到云函数控制台查看日志错误详情。
 - 单击【编辑】，修改 CDN 日志备份规则。
 - 单击【删除】，删除不使用的 CDN 日志备份规则。
