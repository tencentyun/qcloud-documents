## 基本概念

用户可以通过以下地址对 Bucket 内的对象进行访问：

- 默认域名


- CDN 加速域名


- 自定义域名

COS 默认域名由腾讯云定义，不可更改。当用户使用腾讯云内部业务使用该域名访问COS资源，请求将通过内网环境发送和接收；当用户是从公网使用该域名访问时，访问将从公网向 COS 请求文件。CDN 加速域名由腾讯云初始化，可以更改（需要CNAME），访问经由 500+ 的 CDN 加速节点；自定义域名由用户自行进行别名映射，适合需要屏蔽腾讯云地址标识（qcloud）的场景。


## 默认域名

其中 COS 默认域名由腾讯云定义，不可更改，可以用于腾讯云内部业务请求也适用于公网直接访问。在创建 Bucket 后，腾讯云会自动生成一条默认域名，格式为：

`[bucketname]-[appid].cos[area].myqcloud.com`
`例如：test-1250000000.cosgz.myqcloud.com`

此域名不可更改。

获取每个Bucket 中的资源对应 URL，即在 Bucket 的域名后加上相对路径即可，如：

`http://testbucket-1250000000.cosgz.myqcloud.com/test.txt`

若资源的权限为私有，则需要在上述 URL 后加上签名后缀

进入 COS 管理控制台，点击 Bucket 名称进入管理页面，选择【域名管理】页签，即可以看到默认域名

![](https://mc.qcloudimg.com/static/img/4fd194c09b5a2c994867238878649d77/image.png)

**默认域名-内网跨区域访问： 默认域名可以用于在同区域的不同腾讯云产品之间进行访问。但是，若需要实现内网跨区域的访问， 例如，所在区域为广州的 CVM 需要使用新加坡的 COS 上的数据，则需要使用 VPC 部署专属网络通道，实现高速访问体验。 [点击查看 VPC 相关信息](https://cloud.tencent.com/product/vpc.html)**


## CDN 加速域名

CDN 加速域名由腾讯云初始化，可以更改（需要 CNAME），访问经由 500+ 的 CDN 加速节点，可获得更高的带宽和更低的等待时延。在创建 Bucket 后，腾讯云会默认生成一条 CDN 加速域名，格式为：

`[bucketname]-[appid].file.myqcloud.com`

可以在创建 Bucket 时候选择开启 CDN 加速。也可以在后续，到 COS 控制台的【域名管理】中，开启 CDN 加速，则外网可以直接访问 CDN 加速域名，如：

`http://testbucket-1250000000.file.myqcloud.com/testdir/test.txt`

同时CDN控制台会新增一条域名，这条域名也就是CDN加速域名.

**注：同一个APPID下最多可以创建100条CDN加速域名。**

用户还可以修改 CDN 加速域名：

进入 COS 管理控制台，选择 Bucket 列表页面，点击选择一个Bucket

![](https://mc.qcloudimg.com/static/img/297fc0dfb01119f83f1fe788a868e45f/image.png)

进入**域名管理**页面，选择**加速域名**，点击**修改**，开启 CDN 加速

![](https://mc.qcloudimg.com/static/img/1ccf623ef070b8d689825090ea32ceb7/image.png)

## 自定义域名

根据用户的需要，可能不希望类似 “qcloud.com” 等域名显示在网站或服务上。例如，如果在腾讯云 COS 上托管网站，用户可能会首选 `http://myblog.net/`， 而不是 `http://myblog-1250000000.file.myqcloud.com`。

可以通过自定义域名的方式实现上述需求，其中需要 CDN 控制台创建 CNAME 记录将 `http://myblog.net/`映射到 `http://myblog-1250000000.file.myqcloud.com`。

您可以通过添加自定义域名直接指向 Bucket ，绑定后可通过自定义域名直接访问 Bucket 中的内容。添加自定义域名以后，您还可以选择开启 CDN 加速来快速访问，为避免业务中涉及的安全问题，建议您使用自定义域名方式访问 COS；

- 自定义域名后，为保证域名正常访问 COS，需先修改 DNS 记录 CNAME 到指定地址，才能生效。
- 您绑定的域名需在工信部备案，否则自定义域名将无法访问。

进入 COS 管理控制台，选择 Bucket列表页面，点击选择一个Bucket

![](https://mc.qcloudimg.com/static/img/297fc0dfb01119f83f1fe788a868e45f/image.png)

## 示例一（开启 CDN 加速）

### 选择一个Bucket

进入 COS 管理控制台，选择 Bucket 列表页面，点击选择一个Bucket

![](//mccdn.qcloud.com/static/img/ac01c306c5314d64b1afce45e7c0a093/image.png)

### 添加域名

进入**域名管理**页面，选择**自定义域名**，点击**添加域名**，添加用户已有的域名。

![](//mccdn.qcloud.com/static/img/00c00593d5dfc71feef320d226bd18b6/image.png)

复制** CNAME 地址**，

![](//mccdn.qcloud.com/static/img/c620574738d836d2a4ba96b26a3eef51/image.png)

### 域名解析

进入云解析管理控制台，点击已绑定的自定义域名，

![](//mccdn.qcloud.com/static/img/706dbd1854f7ac85768a8dffc58e130c/image.png)

添加一条 CNAME 记录

![](//mccdn.qcloud.com/static/img/56678b11886365cff3c9c258076d3424/image.png)

*注：记录值是之前复制的 CNAME 地址，添加后，大约需15分钟左右生效，请耐心等待*

### 结果验证

自定义域名绑定成功后，便可以通过自定义域名地址下载 Bucket 中的文件。假如，您的testnew 存储桶中有一个index.htm文件，绑定的自定义域名为 www.srcostest.com

**绑定前**

您可以通过默认域名外网访问地址加文件路径访问：testnew-10014284.cos.myqcloud.com/index.htm

![](//mccdn.qcloud.com/static/img/939165a47b8da3c678577a9ff945e80a/image.png)

**绑定后**

您可以通过自定义域名地址加文件路径访问：www.srcostest.com/index.htm

![](//mccdn.qcloud.com/static/img/32e0a9be3c5fc82754014ccc497c4b1d/image.png)

> 注：开启静态网站功能，可通过自定义域名直接打开浏览文件，关于如何开启静态网站功能，请参考 [静态网站托管](/doc/product/430/5896) 。

## 示例二（关闭 CDN 加速）

### 选择一个Bucket

进入 COS 管理控制台，选择 Bucket 列表页面，点击选择一个Bucket

![](//mccdn.qcloud.com/static/img/ac01c306c5314d64b1afce45e7c0a093/image.png)

复制**外网访问地址**

![](//mc.qcloudimg.com/static/img/38bbe6419e5df31cee3e8d083e620de5/image.png)

### 域名解析

进入云解析管理控制台，点击已绑定的自定义域名，

![](//mccdn.qcloud.com/static/img/706dbd1854f7ac85768a8dffc58e130c/image.png)

添加一条 CNAME 记录

![](//mc.qcloudimg.com/static/img/a626c5a09f1e12c8bb772c6238d1b812/image.png)

*注：记录值是之前复制的外网访问地址，添加后，大约需15分钟左右生效，请耐心等待*

### 添加域名

进入**域名管理**页面，选择**自定义域名**，点击**添加域名**，添加用户已有的域名。

![](//mc.qcloudimg.com/static/img/d653a13cfd55c55b1e88baabef37cf36/image.png)

*注：添加域名时，需要关闭 CDN 加速，大约几分钟后，域名状态为已上线即可*

### 结果验证

自定义域名绑定成功后，便可以通过自定义域名地址下载Bucket中的文件。假如，您的testnew存储桶中有一个index.htm文件，绑定的自定义域名为 www.srcostest.com

**绑定前**

您可以通过默认域名外网访问地址加文件路径访问：testnew-10014284.cos.myqcloud.com/index.htm

![](//mccdn.qcloud.com/static/img/939165a47b8da3c678577a9ff945e80a/image.png)

**绑定后**

您可以通过自定义域名地址加文件路径访问：www.srcostest.com/index.htm

![](//mccdn.qcloud.com/static/img/32e0a9be3c5fc82754014ccc497c4b1d/image.png)

> 注：开启静态网站功能，可通过自定义域名直接打开浏览文件，关于如何开启静态网站功能，请参考 [静态网站托管](/doc/product/430/5896) 。
