## 步骤说明

1. 初始化客户端cosclient
2. 执行createBucket 创建bucket, 创建bucket时可指定bucket的权限(公有读写或私有读)

### 代码示例

1 调用createBucket创建bucket, 代码示例如下所示

```java
// 1 初始化用户身份信息(appid, secretId, secretKey)
COSCredentials cred = new BasicCOSCredentials("AKIDXXXXXXXX", "1A2Z3YYYYYYYYYY");
// 2 设置bucket的区域, COS地域的简称请参照 https://www.qcloud.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing-1"));
// 3 生成cos客户端
COSClient cosclient = new COSClient(cred, clientConfig);

String bucketName = "publicreadbucket-1251668577";
CreateBucketRequest createBucketRequest = new CreateBucketRequest(bucketName);
// 设置bucket的权限为PublicRead(公有读私有写), 其他可选Private(私有读写), PublicReadWrite(公有读写)
createBucketRequest.setCannedAcl(CannedAccessControlList.PublicRead);
Bucket bucket = cosclient.createBucket(createBucketRequest);
```

