## 步骤说明

1. 初始化客户端cosclient
2. 执行deleteBucket删除bucket, bucket必须不包含任何数据, 否则需要先清空数据。

### 代码示例

1 调用deleteBucket创建bucket, 代码示例如下所示

```java
// 1 初始化用户身份信息(appid, secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://www.qcloud.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);

// bucket名称需包含appid
String bucketName = "publicreadbucket-1251668577";
// 删除bucket, 只能删除不包含任何数据的bucket
cosclient.deleteBucket(bucketName);
```

