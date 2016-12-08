## 创建 Bucket
登录控制台后，您可以通过 COS 管理控制台创建一个 Bucket，且可以对 Bucket 的各项配置进行自定义设置。

进入 COS 管理控制台，点击 **立即创建 Bucket** ，会弹出创建 Bucket 对话框：

![](https://mc.qcloudimg.com/static/img/eb79b292988425981082ff2c3fbdac91/Free-Converter.com-qq20161117-1-48840304.jpg)

**注意事项**

- Bucket 数量上限是200个（不区分地区）。但是 Bucket下目录、文件数量没有限制。
- Bucket 创建于项目下，一个 Bucket 只能属于一个项目，支持切换项目。
- Bucket 名称支持小写字母和数字的组合，不支持特殊符号及下划线，且不能超过 40 字节。
- 腾讯云 COS 中，同一个 APPID 的所有项目下 Bucket 名称是唯一的，不能重名。
- Bucket 默认提供两种访问权限：公有读私有写和私有读写。
- 创建 Bucket 时候可以选择所在地区， 地区一旦设置后将无法修改。 



点击 **创建** ，即可在页面 Bucket 列表中看到创建的 Bucket：

![](https://mc.qcloudimg.com/static/img/61d5969c7ef5a2e96fa28a56811c6582/image.png)

## 多园区及访问域名
COS 支持多园区存储，目前开放了华北、华南、华东三个地区。不同地区默认访问域名不同。推荐用户根据自己的业务场景选择就近的地区存储，可以提高上传、下载速度。

| 地区   | 区域表示 | 默认下载域名                                  | 上传域名                 | 状态   |
| ---- | ---- | --------------------------------------- | -------------------- | ---- |
| 华南   | gz   | [bucketname]-[appid].cosgz.myqcloud.com | gz.file.myqcloud.com | 已上线  |
| 华北   | tj   | [bucketname]-[appid].costj.myqcloud.com | tj.file.myqcloud.com | 已上线  |
| 华东   | sh   | [bucketname]-[appid].cossh.myqcloud.com | sh.file.myqcloud.com | 已上线  |
| 新加坡  | -    | -                                       | -                    | 敬请期待 |

**内网跨区域访问： 不同区域的不同腾讯云产品之间无法直接进行访问。若需要实现内网跨区域的访问， 例如，所在区域为广州的 CVM 需要使用新加坡的 COS 上的数据，则需要使用 VPC 部署专属网络通道，实现高速访问体验。 [点击查看 VPC 相关信息](https://www.qcloud.com/product/vpc.html)**

## 访问权限
> 公有读私有写：任何人（包括匿名访问者）都对该Bucket中的文件有读权限，但只有Bucket创建者及有相应权限的账号才对该Bucket中的文件有写权限。
>
> 
> 私有读写：只有该Bucket的创建者及有相应权限的账号才对该Bucket中的文件有读写权限，其他任何人对该Bucket中的文件都没有读写权限。

如后续需要修改Bucekt权限，可通过控制台空间属性修改。


