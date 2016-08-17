## 1. 开通CDN服务
开通CDN服务时，您需要进行以下步骤：

1). 在腾讯云官网，[CDN产品介绍页](https://www.qcloud.com/product/cdn.html) 了解CDN产品，点击【立即使用】；

2). 未认证用户请先完成实名认证，已认证用户可直接进入下一项。查看[实名认证指引](https://www.qcloud.com/doc/product/378/3629)；

3). 选择适合您的计费方式（查看[计费说明](https://www.qcloud.com/doc/product/228/562)），开通CDN服务：

![](https://mccdn.qcloud.com/static/img/d5c70cd18181ccfc2877b33a4f558015/image.png)

## 2. 接入域名

1). 进入[CDN控制台](https://console.qcloud.com/cdn)，在【域名管理】菜单栏点击【添加域名】：

![](https://mccdn.qcloud.com/static/img/aab5853c8e017d5abe14b043a5b3afab/image.png)

2). 填写基本信息，输入加速域名、选择业务类型和合适的接入方式：

![](https://mccdn.qcloud.com/static/img/51963c24685f4ca9bcff6adb755e3578/image.png)

3). 根据实际业务需要，进行定制化配置，如缓存配置、防盗链配置等：

![](https://mccdn.qcloud.com/static/img/7c6a1d69406e92c51c9b0296e9c5e306/image.png)

4). 核对基本信息和配置信息，如需修改点击“上一步”，确认信息无误后点击【提交】：

![](https://mccdn.qcloud.com/static/img/cfcc85c013aaffa8583ab437c489af37/image.png)

5). 提交成功后，域名添加完成，请耐心等待域名配置（约10分钟）。

![](https://mccdn.qcloud.com/static/img/8bd9ee32953db24d825be3ddcb9c47d6/image.png)

## 3. 配置CNAME
1). 域名配置完成后，系统会为您分配对应的CDN域名，以 .cdn.dnsv1.com 为后缀：

![](https://mccdn.qcloud.com/static/img/93257fff3cdf7311a2108bfec8d9fab0/image.png)

2). 您需要到接入域名的DNS服务商处完成CNAME配置，将域名CAME到CDN域名，配置方法请点击[CNAME配置说明](https://www.qcloud.com/doc/product/228/3121) ；

3). 验证域名是否已经CNAME成功：不同的DNS服务商，CNAME生效的时间略有不同，一般会在半个小时之内生效。您也可以通过PING的方式来查询CNAME是否生效，如果PING到后缀为cdntip.com或后缀为tcdn.qq.com表示域名CNAME已生效。
![](https://mccdn.qcloud.com/static/img/dbf7687249e59b5d0aeef4f9cdadfec5/image.png)
