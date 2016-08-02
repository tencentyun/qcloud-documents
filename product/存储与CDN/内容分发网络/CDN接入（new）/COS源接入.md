
### 1. 添加域名

您可在CDN控制台的 **域名管理** 页面，点击 **添加域名**： 

![](//mccdn.qcloud.com/static/img/7a092461c30a209a468fb4a74f0358f9/image.jpg)

- 选择接入方式

您可选择使用 **自有源** 或 **对象存储COS**，默认以 **自有源** 方式接入：

![](//mccdn.qcloud.com/static/img/cc69fddfddcea3b812aea0334163c5cb/image.jpg)

### 2. 填写基本信息

**对象存储COS接入：**有效信息的填写您可参考下图

![](//mccdn.qcloud.com/static/img/721b59a9928357f4ab8c6610bf250eb8/image.jpg)

**注意有如下限制：**
+ 域名和COS的项目归属需一致
+ 您的访问域名必须是备案过的域名，否则审核不通过。
+ COS内容管理均需要在COS控制台或COS支持的客户端进行操作，COS控制台地址：[http://console.qcloud.com/cos](http://console.qcloud.com/cos) 。
+ 如果选择COS，您该项目下没有对应的COS没有Bucket，需要进入COS控制台进行创建。

**业务类型**：CDN可将域名归为四种类型业务，分别是网页图片/小文件、大文件下载、流媒体直播、流媒体点播，用户可根据自身域名对应业务类型，来进行选择。

### 3. 填写配置信息

点击下一步，进入“填写配置信息”页面，可在页面上选择所需的基础配置，具体配置详情可在下方配置说明当中查看。

![](//mccdn.qcloud.com/static/img/ca5b32b474e186c2502262cd1640f9ab/image.jpg)

- 确认信息

点击下一步，进入“确认信息”页面，确认接入域名的基本信息和配置信息，若需修改可点击上一步，若无需修改，可直接点击“提交”。

![](//mccdn.qcloud.com/static/img/6fd22aee34ca6562cff9ea33d9db76d7/image.jpg)

- 提交信息

点击“提交”后，进入到“完成”页面，此时域名已经添加完成，还需进入到“接入管理”查看添加域名当前的状态。

![](//mccdn.qcloud.com/static/img/4645139e2f5e555a44ea6cfaab4a02f0/image.jpg)

- 域名审核

添加完成时，域名处于审核状态，腾讯云的同学会对您的域名进行进一步审核，审核时间约10分钟。有疑问请联系客服或者大客户经理。

- 分配CDN域名

审核通过后，您的域名进入开启状态，此时会分配对应的CDN域名，以 **.cdn.dnsv1.com** 后缀。

![](//mccdn.qcloud.com/static/img/fbbd19258c6ee036498eb651ec5ce663/image.jpg)

### 4. 绑定CNAME

**最后一步，您需要到接入域名的DNS服务商（如dnspod）处，把域名cname到cdn域名，生效后即可完成接入。[详情请点击这里](http://bbs.qcloud.com/forum.php?mod=viewthread&tid=5090&extra=page%3D1)**

### 5. 管理域名

整个流程完成后，您就可以通过添加的加速域名进行访问，此时访问会经过腾讯云CDN节点。您可在”域名管理“页面中点击”管理“进入“域名配置”页面对加速域名进行查看，或更改其配置；自有源接入用户可更改源站地址，对象存储接入用户可更改Bucket。

**注：**如果您在COS创建Bucket（[参见创建Bucket](http://www.qcloud.com/doc/product/227/%E5%88%9B%E5%BB%BA%20buckett)） 时，选择CDN加速，则在CDN接入管理中将默认加入一条接入记录，他会随着您创建的Bucket的删除而同步删除。其具体配置会参照你创建Bucket的配置进行设置，且不可更改。
