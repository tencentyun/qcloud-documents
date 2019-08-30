## 密钥问题

### 在哪里查看 APPID、SecretId、SecretKey 等密钥信息呢？

存储桶名称的后半部分即为 APPID 信息，您可以登录 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket) 查看。SecretId、SecretKey 等信息，请登录访问管理控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中查看。

### 临时密钥的有效时间是多长？

最长2小时，即7200秒。临时密钥过期后，持有过期临时密钥的请求将会被拒绝。有关临时密钥的介绍请参见 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)。

### 密钥相关信息如 APPID、SecretId 等信息泄露了，如何处理？

用户可删除已泄露的密钥，并新建一个密钥，详情请参见 [密钥管理](https://cloud.tencent.com/document/product/436/10074)。

### 如何对私有读写的文件生成具有时效性的访问链接？

详情请参见 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048) 文档，设定密钥有效时间。

## ACL+ Policy 等权限问题

### 进行上传下载等操作时，报错“403 Forbidden”、权限拒绝等该如何处理？

请按照以下步骤逐步排查问题：

1. 请检查您的以下配置信息是否正确：
   BucketName、APPID、Region、SecretId、SecretKey 等。
2. 确保上述信息正确的前提下，请检查是否使用子账号操作，若使用子账号请检查主账号是否已对子账号授权。否则，请先登录主账号对子账号授权。
   授权详情请参见 [访问管理权限设置相关案例](https://cloud.tencent.com/document/product/436/12514)。
3. 若使用临时密钥进行操作，请检查当前操作是否在获取临时密钥时设置的 Policy 中。否则请修改相关 Policy 设置。
4. 若以上步骤仍无法解决问题，请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=83&level2_id=84&source=0&data_title=%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8%20COS&step=1) 联系我们。

### 使用存储桶默认域名访问公有读存储桶时会返回文件列表，如何隐藏文件列表信息？

您可以为对应存储桶设置一条 deny anyone 的 Get Bucket 权限。操作步骤如下：

登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)，选择存储桶列表，进入对应存储桶的**权限管理**页面。

#### 方法 1：

1. 找到 **Policy权限设置项**，在【图形设置】下单击【添加策略】。
2. 按照下图所示添加对应权限设置，单击【确定】保存。
   ![Polcy图形设置](https://main.qcloudimg.com/raw/c739d31636d117757449c7e0e106ad84.png)

#### 方法 2：

找到 **Policy 权限设置项**，单击【策略语法】>【编辑】，输入以下表达式：
```
{
  "Statement": [
    {
      "Action": [
        "name/cos:GetBucket",
        "name/cos:GetBucketObjectVersions"
      ],
      "Effect": "Deny",
      "Principal": {
        "qcs": [
          "qcs::cam::anyone:anyone"
        ]
      },
      "Resource": [
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/*"
      ]
    }
  ],
  "version": "2.0"
}
```

>!请将“qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/*”中的相关信息进行以下替换：
> - “ap-beijing”替换为您的存储桶所在地域。
> - “1250000000”替换为您的 APPID 信息。
> - “examplebucket-1250000000”替换为您的存储桶名称。
>
> 其中，APPID 为存储桶名称的后半部分，您可以在 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket) 查看存储桶名称。

### COS 的 ACL 限制是针对存储桶还是账号？上传文件时是否可以指定权限？

ACL 限制针对账号。不建议上传文件时指定权限，容易导致 ACL + Policy 策略超过1000条而出现报错。

### 如何授权协作者访问指定存储桶？

协作者账号是一类特殊的子账号，详情请参见 [访问策略语言概述](https://cloud.tencent.com/document/product/436/18023)。

### 多个业务需要对存储桶进行操作，是否可以根据存储桶或其他维度隔离权限？

登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，进入用户管理页面，可以给不同的业务开启子账号，并赋予不同的授权操作。

### 进行上传文件或创建存储桶等操作时，报错“your policy or acl has reached the limit (Status Code: 400; Error Code: PolicyFull)”该如何处理？

COS 每个主账号下存储桶和对象 ACL + Policy 的规则数量最多为1000条，当设置的相关 ACL 或 Policy 策略大于1000条时，会出现此报错，因此建议删除无用的 ACL 或 Policy 策略。

>! 我们不建议使用文件级别的 ACL 或 Policy。建议您在调用 API 或 SDK 时，若不需要对文件进行特别的 ACL 控制时， 请将 ACL 相关参数（如 x-cos-acl、ACL 等）置空，保持继承存储桶权限。

### 如何为子公司或员工创建子账号，并授予特定存储桶的访问权限？

详情请参见 [授权子账号访问 COS ](https://cloud.tencent.com/document/product/436/11714)，创建子账号并对其授权。

### 如何授权某些特定子账号只对某个存储桶有操作权限？

若希望子账号只有特定存储桶的操作权限，可以使用子账号添加路径。详情请参见 [子账号访问存储桶列表](https://cloud.tencent.com/document/product/436/17061)。

### 如何使用 A 账号对 B 账号授权 A 账号下存储桶的写权限？

详情请参见 [ACL 访问控制实践](https://cloud.tencent.com/document/product/436/12470) 和 [CAM 访问管理实践](https://cloud.tencent.com/document/product/436/12469) 进行授权。

## 防盗链问题

### 开启 CDN 加速并使用 CDN 域名访问资源，防盗链配置不生效怎么办？

若您使用 CDN 加速域名访问资源，CDN 缓存等因素可能影响 COS 防盗链的稳定性，建议您到 [CDN 控制台](https://console.cloud.tencent.com/cdn) 配置防盗链，文档请参见 [CDN 防盗链配置](https://cloud.tencent.com/document/product/228/6292)。

### 能否设置白名单允许访问，并且浏览器单独打开链接也允许访问？

在设置防盗链时选择允许空 referer，即可在设置白名单的情况下，实现浏览器单独打开链接也可以访问。

### 设置了存储桶 test 的防盗链白名单，允许`a.com`访问，但是`a.com`下的网页播放器却不能播放存储桶 test 下的视频文件？

网页中使用 Windows Media Player、Flash Player 等播放器播放视频链接时，在请求里的 referer 为空，导致没命中白名单，建议设置白名单时允许空 referer。

## 加密与备份等其他问题

### COS 支持文件加密吗？

支持在服务端进行文件加密，详情请参见 [服务端加密](https://cloud.tencent.com/document/product/436/18145)。

### 请问 COS 的标准存储，低频存储，归档存储数据都有备份吗？

COS 的数据通过多副本或纠删码方式在底层存储，分布式存储引擎在一个地域的多个可用区中分布，可靠性99.999999999%，多副本和纠删码存储是底层逻辑，对用户不可见。

### 同一账号下某个桶请求量太大是否影响其他桶的访问？

请求量大不会影响，但频率过快会影响，详情请参见 [请求速率与性能优化](https://cloud.tencent.com/document/product/436/13653)。
