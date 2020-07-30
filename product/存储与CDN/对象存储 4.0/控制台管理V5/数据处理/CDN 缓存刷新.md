## 简介

CDN 缓存刷新是腾讯云对象存储 COS 基于 [云函数服务 SCF](https://cloud.tencent.com/document/product/583) 为用户提供的数据刷新功能，可以协助用户自动刷新 CDN 边缘节点上的缓存数据。当用户为存储桶添加触发规则后，在该存储桶中更新文件时，会自动触发对象存储 COS 为您预配置的云函数，实现自动刷新缓存数据。

> !
> - 若您此前在 COS 控制台上为存储桶添加了缓存刷新规则，可以在 [云函数 SCF](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 控制台上看到您所创建的CDN 缓存刷新函数，请**不要**删除该函数，否则可能导致您的规则不生效。
> - 已上线 SCF 的地域均已支持 CDN 缓存刷新功能，包括有广州、上海、北京、成都、香港、新加坡、孟买、多伦多、硅谷等，更多支持地域可查看 [SCF 产品文档](https://cloud.tencent.com/document/product/583)。
> - CDN 缓存刷新功能可能会受到网络链路不稳定等因素导致失败。如果功能表现不符合您预期，您可以在 COS 控制台单击所创建的函数右侧的【查看日志】，跳转到 SCF 控制台查看日志错误详情，以便定位出错原因。
> - CDN 缓存刷新功能依赖于云函数服务，云函数服务为用户提供了 [免费额度](https://cloud.tencent.com/document/product/583/12282)，超出免费额度的部分需要按照 [SCF 产品定价](https://cloud.tencent.com/document/product/583/12281) 收费。当您使用 CDN 缓存刷新功能时，如果您刷新的次数越多，则将消耗更多的调用次数。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 在左侧导航中，单击【存储桶列表】，选择并单击需要添加 CDN 缓存刷新规则的存储桶，进入存储桶管理页。
3. 单击左侧的【函数计算】，然后找到【CDN缓存刷新函数】配置项。
![](https://main.qcloudimg.com/raw/9ed7c6369bdfc9619e96422059897237.jpg)
> !如果您尚未开通云函数 SCF 服务，请前往 [云函数 SCF 控制台](https://console.cloud.tencent.com/scf) 开通 SCF 服务，按照提示完成服务授权即可。
4. 单击【添加函数】，在弹出的窗口中配置如下信息：
	- **函数名称**：函数名称作为函数的唯一标识名称，创建后不可修改。您可以在 [云函数 SCF](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 控制台上查看该函数。
	- **事件类型**：事件是指触发云函数的操作。以上传操作为例，上传的方式可能是调用 [PUT Object](https://cloud.tencent.com/document/product/436/7749) 接口，也可能是调用 [Post Object](https://cloud.tencent.com/document/product/436/14690) 接口。当选择事件为`PUT 类型`时，只有通过`PUT Object`接口上传文件的操作会触发云函数，从而刷新 CDN 边缘节点的缓存。
	- **触发条件**：您可以指定触发事件的文件源范围，如全部存储桶或者指定的前缀或者指定的后缀。指定前缀或后缀后，规则只对匹配的文件源生效。
	- **指定域名**：指需要刷新的 CDN 域名。
	- **SCF 授权**：CDN 缓存刷新需要授权云函数调用 CDN 的`PurgeUrlsCache`接口，用于清除 CDN 缓存刷新中的数据，以便 CDN 可以回源到 COS 上拉取最新的数据。
![](https://main.qcloudimg.com/raw/d71aab4cf761368192ee921c10965157.png)
5. 添加配置后，单击【确认】，即可看到函数已添加完成。
6. 单击【查看日志】可查看 CDN 缓存刷新的历史运行情况。如果需要删除不需要的 CDN 缓存刷新规则，可以单击【删除】删除相关配置。
