## 历史版本和数据

### 历史版本区别

**Q：XML API与4.0版本的JSON格式API有什么关系？**

A：4.0版本的JSON格式API接口即2016年9月之后，用户接入COS使用的API，上传域名为[Region].file.myqcloud.com。4.0版本的JSON格式API接口日后将保持维护状态，可以正常使用但是不发展新特性。其与标准XML的API 底层架构相同，数据互通，可以交叉使用，但是接口不兼容，域名不一致。

**Q：XML API与3.0版本的JSON格式API有什么关系？**

A：3.0版本的JSON格式API接口即2016年10月之前，用户接入COS使用的API，上传域名为web.file.myqcloud.com。对于使用3.0版本的JSON格式API接口的用户，COS将主动帮助用户缓慢迁移数据，转发请求，客户无需变更。其与标准XML的API 底层架构不同，数据不互通，接口不兼容。

**Q: 如何判断是哪个版本的API？**

A: 使用bucket 的 上传域名和下载域名结构具有如下特征：

| 地区   | 版本       | 示例下载地址                                   | 示例上传地址                                   |
| ---- | ---------- | ---------------------------------------- | ---------------------------------------- |
| 上海   | v3-JSON  | bucket-[8 位 100 开头数字].cos.myqcloud.com   | web.file.myqcloud.com                    |
| 华南   | v4-JSON  | bucket-[9 位 125 开头数字].cosgz.myqcloud.com | gz.file.myqcloud.com                     |
| 华北   | v4-JSON  | bucket-[9 位 125 开头数字].costj.myqcloud.com | tj.file.myqcloud.com                     |
| 华东   | v4-JSON  | bucket-[9 位 125 开头数字].cossh.myqcloud.com | sh.file.myqcloud.com                     |
| 华南   | v4-XML  | bucket-[9 位 125 开头数字].cn-south.myqcloud.com | bucket-[9 位 125 开头数字].cn-south.myqcloud.com |
| 华北   | v4-XML  | bucket-[9 位 125 开头数字].cn-north.myqcloud.com | bucket-[9 位 125 开头数字].cn-north.myqcloud.com |
| 华东   | v4-XML  | bucket-[9 位 125 开头数字].cn-east.myqcloud.com | bucket-[9 位 125 开头数字].cn-east.myqcloud.com |
| 新加坡  | v4-XML  | bucket-[9 位 125 开头数字].sg.myqcloud.com    | bucket-[9 位 125 开头数字].sg.myqcloud.com    |

**Q: 想要用XML API，文档在哪？**

A：API 文档 https://www.qcloud.com/document/product/436/7751。

### 历史版本数据 

**Q: 我已经拥有了COS V3的Bucket和Object，可不可以使用XML API？**

A：不可以，XML API是基于COS V4的架构，与COS V3数据不互通。

**Q: 我用 V3 JSON API新创建了Bucket和Object，可不可以使用XML API来管理？**

A：不可以，XML API是基于COS V4的架构，与COS V3数据不互通。

**Q: 我用 V3 控制台新创建了Bucket和Object，可不可以使用XML API来管理？**

A：不可以，XML API是基于COS V4的架构，与COS V3数据不互通。

**Q: 我用XML API创建了Bucket和Object，可不可以使用V3-JSON API？**

A：不可以，XML API是基于COS V4的架构，与COS V3数据不互通。

**Q: 我已经拥有了COS V4的Bucket和Object，可不可以使用XML API？**

A：可以，XML API是基于COS V4的架构，可以用XML API操作由JSON API产生的数据。

**Q: 我用 V4 JSON API新创建了Bucket和Object，可不可以使用XML API来管理？**

A：可以，XML API是基于COS V4的架构，可以用XML API操作由JSON API产生的数据。

**Q: 我用 V4 控制台新创建了Bucket和Object，可不可以使用XML API来管理？**

A：可以，XML API是基于COS V4的架构，可以用XML API操作由JSON API产生的数据。

**Q: 我用XML API创建了Bucket和Object，可不可以使用V4-JSON API？**

A：可以，数据可创建，除了权限以外的配置生效，但是强烈不建议使用。

**Q: 计费是否有变化？**

A: 标准存储的计费没有发生变化，具体可以查看产品介绍页。新推出的存储级别只能通过V4-XML API来使用。


## XML API与JSON API使用问题

### 权限问题

**Q: XML API 密钥与JSON API的密钥是否通用了？**

A: 相互通用，9 位数 125 开头的 APPID 请使用腾讯云提供的 API 密钥，可以通过 COS 控制台查看，也可以通过 https://console.qcloud.com/capi 查看个人 API 秘钥。

**Q: XML API 签名与JSON API的签名是否通用了？**

A: 相互不通用，XML API和JSON API各自有各自的签名方式。

JSON API签名：https://www.qcloud.com/document/product/436/6054

XML API签名：https://www.qcloud.com/document/product/436/7778 。

**Q: XML API 设置的ACL权限与JSON API设置的ACL权限是否通用了？**

A: 相互不通用，XML API和JSON API各自有各自的ACL权限。

**Q: XML API 设置的ACL权限与目前控制台设置的ACL权限是否通用了？**

A: 相互不通用，控制台的ACL与JSON API设置的ACL权限一致，目前控制台和XML API各自有各自的ACL权限。

**Q: XML API 来访问JSON API设置的ACL权限的Bucket会发生什么？**

A: 默认权限，所有者有权限，其他人无权限，Bucket为Private。

**Q: XML API 来访问控制台设置的ACL权限的Bucket会发生什么？**

A: 默认权限，所有者有权限，其他人无权限，Bucket为Private。

**Q: JSON API 来访问XML API设置的ACL权限的Bucket会发生什么？**

A: 默认权限，所有者有权限，其他人无权限，Bucket为Private。

**Q: 控制台来访问XML API设置的ACL权限的Bucket会发生什么？**

A: 默认权限，所有者有权限，其他人无权限，Bucket为Private。

### 上传下载问题

**Q: XML API的上传域名是什么？**

A: V4 XML API 上传域名根据地域分区，例如bucket-[9 位 125 开头数字].cn-south.myqcloud.com。V4 JSON API 上传域名使用 gz.file.myqcloud.com 和 tj.file.myqcloud.com。V3 JSON API 上传域名是 web.file.myqcloud.com。

**Q: XML API上传路径？**

A: 举例上传一个文件 Put http://BucketName-UID.Region.myqcloud.com/ObjectName 具体参看 API 文档。

### 秘钥问题

**Q: 如何查找判定秘钥位置？**

A: 秘钥在 https://console.qcloud.com/cos4/secret 查看，根据您创建的 Bucket 下载地址，后面那一串数字所对应的 APPID 即可以使用的秘钥。

**Q: 如何修改秘钥？**

A: 暂时不支持修改秘钥，后续会支持。

**Q: 不小心通过「云 API 秘钥」修改了秘钥，会有什么影响？**

A: 可以通过 https://console.qcloud.com/capi 查看修改。注意修改后，可能导致数据侧和 CDN 侧秘钥不同步的问题。如果遇到问题暂时无法解决，CDN 相关问题只能通过重新绑定 CDN 域名（包括默认赠送的域名也需关闭再开启）。数据侧无法访问的问题只能通过重新创建 Bucket 解决。

## 功能性能差异

### 功能差异

**Q: 目前XML API有哪些功能？**

A: Bucket级别的创建，删除，查询，列出；Object级别的创建，删除，查询，下载，修改属性；分块上传，追加上传。

**Q: XML API功能是否覆盖了 JSON API？**

A: 是的。

**Q: XML API的鉴权和之前有什么不一样？**

A: 支持跨账户授权，支持根账户之间的相互授权操作，支持根账户与子账户之间的相互授权操作。

**Q: 未来是否还发展JSON API？**

A: JSON API只维护现状，不发展新功能，长期和使用（不建议使用)。

**Q: 未来XML API有什么新的功能？**

A: 批量删除，跨域操作，生命周期管理，手动复制，跨区域自动复制，静态网站，表单上传，版本管理，回调，日志记录。

### 性能差异

**Q: XML API和JSON API是否有性能差异？**

A: 同属一套架构，无差异。

**Q: 4.0 与 3.0 对比有哪些 QPS 的优化？**

A: 3.0 的单目录下操作速度不得大于 20 qps 的限制解除。4.0 针对单 Bucket 的平均服务能力达到 100 qps，最大服务能力达到 500 qps，无需再担心分目录的问题。

**Q: 如果 QPS 超过 500 怎么办？**

A: 建议您将请求速率控制在 500 以内，否则可能导致失败率。如果实在要超出，建议创建多个 Bucket 来分摊流量。如果实在要求在同 Bucket 中使用，请联系大客户经理，或 rtx 找 h_cos_helper 评估。同时可以参见产品文档 - 常见问题 - 性能优化。

**Q: 4.0 与 3.0 对比有哪些速度的优化？**

A: 3.0 上传速度不佳，4.0 支持并发上传，单文件支持并发分片，因此单线程速度提升至 20 MB/s，单文件速度提升至 数十数百 MB/s，多线程提升至无限大。

