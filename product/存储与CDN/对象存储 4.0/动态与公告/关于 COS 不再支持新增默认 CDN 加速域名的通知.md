
自2022年3月1日起，对象存储（Cloud Object Storage，COS）服务将不再支持新增默认 CDN 加速域名。您已开启、或曾经开启的默认 CDN 加速域名不会受到影响，可以继续使用，但建议您使用自定义 CDN 加速域名代替默认 CDN 加速域名。关于默认 CDN 加速域名的说明，请参见 [对默认加速域名配置 CDN 加速](https://cloud.tencent.com/document/product/436/18670#.E5.AF.B9.E9.BB.98.E8.AE.A4.E5.8A.A0.E9.80.9F.E5.9F.9F.E5.90.8D.E9.85.8D.E7.BD.AE-cdn-.E5.8A.A0.E9.80.9F)。

针对不同的用户，默认 CDN 加速域名的支持情况如下：

#### COS 新用户

2022年3月1日后新注册的 COS 用户，不支持默认 CDN 加速域名功能。

#### COS 老用户

| 存储桶状态 | 说明 |
|---------|---------|
| 新创建的存储桶 | 2022年3月1日后创建的存储桶，不支持开启默认 CDN 加速域名。 |
| 已创建的存储桶（从未开启过默认 CDN 加速域名） | 截至2022年3月1日，若存储桶从未开启过默认 CDN 加速域名，将不支持开启默认 CDN 加速域名。 |
| 已创建的存储桶（开启过默认 CDN 加速域名，且处于关闭状态） | 截至2022年3月1日，若存储桶曾经开启过默认 CDN 加速域名，但处于关闭状态，支持继续使用默认 CDN 加速域名。 |
| 已创建的存储桶（已开启默认 CDN 加速域名，且处于开启状态） | 截至2022年3月1日，若存储桶已开启默认 CDN 加速域名，且处于开启状态，支持继续使用默认 CDN 加速域名。 |


#### 查看默认 CDN 加速域名

您可以通过以下两种途径查看处于开启和关闭状态下的默认 CDN 加速域名，在2022年3月1日后，这些域名对应的存储桶支持继续使用默认 CDN 加速域名。

#### 途径一：COS 控制台

1. 登录 [COS 控制台](https://console.cloud.tencent.com/cos5)。
2. 单击**存储桶列表**，进入指定存储桶【域名与传输管理】下的【默认 CDN 加速域名】，可查看当前存储桶处于开启状态下的默认 CDN 加速域名，关闭状态下的默认 CDN 加速域名请前往 [CDN 控制台](https://console.cloud.tencent.com/cdn/domains) 查看。
![](https://qcloudimg.tencent-cloud.cn/raw/d9216bcf4e2aed86a426eb770130df4f.png)

#### 途径二：CDN 控制台

您可以在 [CDN 控制台](https://console.cloud.tencent.com/cdn/domains) 的【域名管理】中查看处于开启和关闭状态下的默认 CDN 加速域名，域名形如`<BucketName-APPID>.file.myqcloud.com`，接入方式为 COS 源。

>! 截至2022年3月1日，处于关闭状态下的默认 CDN 域名支持继续使用；但对于已删除的默认 CDN 加速域名，CDN 控制台无记录，将无法支持继续使用。

![](https://qcloudimg.tencent-cloud.cn/raw/0619c827ad236a607d63b25c3a246c26.png)
