
![](//mc.qcloudimg.com/static/img/9d0f230cf9ba1de913d75df2cda1bb60/image.png)

## 注册与登录

您需要一个腾讯云账户才能使用 Bucket，如果您还没有账户，请您先访问[腾讯云](http://www.qcloud.com)注册一个账号，并完成登录。


1、如您需注册账号，[请参考指南]()，并完成注册.

2、如您已有账号，请按照屏幕完成操作.

## 创建 Bucket

1、完成注册与登录后，您就可以开始使用 COS 管理控制台 创建 Bucket。**必须**先创建一个 Bucket,然后才能在管理控制台中存储数据。
2、进入 COS 管理控制台，点击 **立即创建 Bucket** ，会弹出创建 Bucket 对话框：

![](//mccdn.qcloud.com/static/img/a72342e5d10c18ccba9dde905fcd8695/image.png)

**注意事项**

- Bucket 创建于项目下，一个 Bucket 只能属于一个项目，选择后不可以修改。
- Bucket 名称支持小写字母和数字的组合，不支持特殊符号及下划线，且不能超过 40 字节。
- Bucket 一旦创建后，不支持重命名。
- Bucket 默认提供两种访问权限：公有读私有写和私有读写。


3、点击 **创建** ，即可在页面 Bucket 列表中看到创建的 Bucket：

![](https://mc.qcloudimg.com/static/img/61d5969c7ef5a2e96fa28a56811c6582/image.png)

## 多园区及访问域名
1、COS 支持多园区存储，目前开放了华北、华南、华东三个地区。不同地区默认访问域名不同。推荐用户根据自己的业务场景选择就近的地区存储，可以提高上传、下载速度。

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

下一步：[上传 Object]()

