## 删除问题

### 通过控制台无法删除存储桶，提示“目录非空”或“请删除存储桶中的有效数据”怎么办？

1. 请确认您使用的控制台版本是 V4 还是 V5 版本，V4 版本请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=83&level2_id=84&source=0&data_title=%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8%20COS&level3_id=91&radio_title=%E6%8E%A7%E5%88%B6%E5%8F%B0%E9%97%AE%E9%A2%98&queue=28&scene_code=14471&step=2) ，申请升级到 V5 版本控制台。
2. 登录对象存储 [ V5 版本控制台](https://console.cloud.tencent.com/cos5)，进入需要删除的存储桶，单击【未完成上传】管理项将文件碎片删除。
3. 回到【存储桶列表】删除对应存储桶。

## 静态网站

### 开启了静态网站功能，但是仍无法显示图片？

请检查是否有浏览器、CDN 缓存。可以通过 curl、wget 命令来避免浏览器缓存。若使用 CDN 域名访问，可以在 [CDN 控制台](https://console.cloud.tencent.com/cdn) 进行缓存刷新操作。

### 使用 CDN 域名无法访问配置好的静态网站怎么办？

请根据以下步骤进行排查确认 CDN 加速域名配置。

1. 源站类型请注意源站选择静态网站源站。
2. 回源鉴权、CDN 服务授权需根据存储桶的权限进行对应设置：
 - 当存储桶权限为私有读时，需要对 CDN 服务授权并开启回源鉴权。
 - 当存储桶权限为公有读时，无需对 CDN 服务授权并开启回源鉴权。
3. CDN 鉴权需要根据存储桶的权限进行对应设置：

a. 当存储桶权限为私有读时：
 
| CDN 鉴权配置 | CDN 加速域名访问 | COS 域名访问    | 常见场景         |
| ------------ | ---------------- | --------------- | ----------------------------------- |
| 关闭（默认） | 可访问           | 需使用 COS 鉴权 | 可直接访问 CDN 域名，保护源站数据   |
     | 开启         | 需使用 URL 鉴权  | 需使用 COS 鉴权 | 全链路保护访问，支持 CDN 鉴权防盗链 |

b. 当存储桶权限为公有读时：

| CDN 鉴权配置 | CDN 加速域名访问 | COS 域名访问 | 常见场景          |
| ------------ | ---------------- | ------------ | ---------------------------------------- |
| 关闭（默认） | 可访问         | 可访问      | 全站许可公共访问，通过 CDN 或源站均可访问       |
| 开启     | 需使用 URL 鉴权  | 可访问      | 对 CDN 访问开启防盗链，但不保护源站访问，不推荐 |

4. 确认以上配置无误后，请确认您访问 CDN 加速域名使用的协议和静态网站的 **强制 HTTPS** 配置：

   - 当您访问 CDN 加速域名使用的是 HTTP 协议，**请勿开启强制 HTTPS** 选项。
   - 当您访问 CDN 加速域名使用的是 HTTPS 协议，建议对 CDN 加速域名配置 **开启回源跟随301/302**。参考文档：[回源跟随302配置](https://cloud.tencent.com/document/product/228/7183)。
5. 如果按照以上步骤排查后，仍无法解决问题，您可以 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=83&level2_id=84&source=0&data_title=%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8%20COS&step=1) 联系我们，进行进一步的问题排查。

## 跨域设置

### 如何设置存储桶里的文件 headers 返回“Access-Control-Allow-Origin:* ”？

进行跨域设置，设置 Origin 为`*`。详情请参阅 [设置跨域访问](https://cloud.tencent.com/document/product/436/11488) 最佳实践文档。

### 上传提示错误“get ETag error, please add "ETag" to CORS ExposeHeader setting. ”该如何处理？

请按照下图配置跨域规则，尝试切换浏览器，测试是否可行。详情请参阅 [设置跨域访问](https://cloud.tencent.com/document/product/436/11488)。
![](https://main.qcloudimg.com/raw/489ba5c2abee71caa34a58b8b6cb09db.png)

### 同时使用了腾讯云 COS 和 CDN，COS 跨域无法正常工作该如何处理？

若您使用的域名是 CDN 加速域名，请在 CDN 控制台配置跨域，详情请参阅 [跨域配置](https://cloud.tencent.com/document/product/228/6296#.E8.B7.A8.E5.9F.9F.E9.85.8D.E7.BD.AE) 文档。

### 跨域设置是否支持来源 Origin 模糊匹配？

V5（XML）版本控制台支持二级域名的模糊匹配。V4（JSON）版本控制台不支持二级泛域名设置。

## 自定义 Headers

### 是否支持批量自定义对象头部（Headers）？

COS 暂不支持批量自定义头部。

## 回源设置

### 回源地址的作用？

进行数据迁移。当 COS 上没有用户请求访问的资源时，将通过回源地址实时拉取资源。

### 设置回源时，COS 上不存在回源地址的相应资源或路径时，COS 会在用户首次访问后自动创建目录吗？

会，COS 会自动拉取并创建目录。

## 其他功能

### COS 支持设置回调吗？例如为上传的每个图像创建一个缩略图保存至另一个存储桶？

您可以结合COS 与 无服务器云函数 SCF 进行设置。相关实践文档请参阅 [获取 COS 上的图像并创建缩略图](https://cloud.tencent.com/document/product/583/9734)。

### COS 是否支持某个文件夹大小的统计？

COS 支持查看当前文件夹的对象数量及对象所占的容量大小，详情请参阅 [查看文件夹详情](https://cloud.tencent.com/document/product/436/35185) 。
