## 创建Bucket

登录管理中心后，您可以通过万象优图的管理控制台创建一个Bucket，创建完成后可对该Bucket进行自定义配置。

进入COS管理控制台，点击“创建Bucket”，会弹出如下图所示的对话框：

支持两种方式：

1. 新建：新创建一个Bucket，由于万象优图的存储功能是基于对象存储服务（COS）的，新创建的Bucket也可以在COS控制台里查询到。
2. 选择已有COS Bucket：通过此种方式，本质上是为一个COS上的Bucket开通图片处理服务。

![创建Bucket](https://mc.qcloudimg.com/static/img/9b48fe8d2debeb9dd2651fb89524c417/image.png)

**请注意：**

+ Bucket 数量上限是200个（不区分地区）。但是 Bucket下目录、文件数量没有限制。
+ Bucket 创建于项目下，一个 Bucket 只能属于一个项目。
+ Bucket 名称支持小写字母和数字的组合，不支持特殊符号及下划线，且不能超过 40 字节。
+ 同一个 APPID 的所有项目下 Bucket 名称是唯一的，不能重名。
+ Bucket 默认提供两种访问权限：公有读私有写和私有读写。
  > 1. 公有读私有写：任何人（包括匿名访问者）都对该Bucket中的文件有读权限，但只有Bucket创建者及有相应权限的账号才对该Bucket中的文件有写权限。

  > 2. 私有读写：只有该Bucket的创建者及有相应权限的账号才对该Bucket中的文件有读写权限，其他任何人对该Bucket中的文件都没有读写权限。
  > 3. 如果后续需要修改Bucket权限，可进COS控制台空间属性修改

+ 创建 Bucket 时候可以选择所在地区， 地区一旦设置后将无法修改。

  点击”创建“，即可在页面Bucket列表中看到创建的Bucket：

  ![Bucket列表](https://mc.qcloudimg.com/static/img/c80bfdfb9ecda20eecd3ec4b28ea9317/image.jpg)


## 多园区及访问域名

存储服务支持多园区，目前开放了华南地区，华北、华东尚在部署中，不同地区的默认访问域名不
同。用户可以根据自己的业务场景选择就近的地区创建。

| 地区   | 区域表示  | 默认域名                                    | 状态   |
| ---- | ----- | --------------------------------------- | ---- |
| 华南   | picgz | [bucketname]-[appid].picgz.myqcloud.com | 已上线  |
| 华北   | pictj | [bucketname]-[appid].pictj.myqcloud.com | 已上线  |
| 华东   | picsh | [bucketname]-[appid].picsh.myqcloud.com | 部署中  |
| 新加坡  | -     | -                                       | 敬请期待 |

内网跨区域访问： 不同区域的不同腾讯云产品之间无法直接进行访问。若需要实现内网跨区域的访问， 例如，所在区域为广州的 CVM 需要使用新加坡的 存储服务 上的数据，则需要使用 VPC 部署专属网络通道，实现高速访问体验。 [点击查看 VPC 相关信息](https://cloud.tencent.com/product/vpc.html)

## Bucket删除

万象优图暂不提供Bucket删除的操作。