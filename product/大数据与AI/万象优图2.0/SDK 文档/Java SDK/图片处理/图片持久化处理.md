## 简介

本文示例展示了如何在上传图片时自动实现图片处理。

图片上传完成后，对象存储（Cloud Object Storage，COS）会存储原始图片和已处理过的图片。后续用户可以通过普通的下载请求获取处理结果。

## 上传时图片持久化处理

#### 示例代码

[//]: # ".cssg-snippet-upload-with-pic-operation"
```java
  // bucket名需包含appid
// api 请参考 https://cloud.tencent.com/document/product/436/54050
String bucketName = "examplebucket-1250000000";

String key = "test.jpg";
File localFile = new File("E://test.jpg");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
PicOperations picOperations = new PicOperations();
picOperations.setIsPicInfo(1);
// 添加图片处理规则
List<PicOperations.Rule> ruleList = new LinkedList<>();
PicOperations.Rule rule1 = new PicOperations.Rule();
rule1.setBucket(bucketName);
rule1.setFileId("test-1.jpg");
rule1.setRule("imageMogr2/rotate/90");
ruleList.add(rule1);
PicOperations.Rule rule2 = new PicOperations.Rule();
rule2.setBucket(bucketName);
rule2.setFileId("test-2.jpg");
rule2.setRule("imageMogr2/rotate/180");
ruleList.add(rule2);
picOperations.setRules(ruleList);
putObjectRequest.setPicOperations(picOperations);
try {
    PutObjectResult putObjectResult = cosClient.putObject(putObjectRequest);
    CIUploadResult ciUploadResult = putObjectResult.getCiUploadResult();
    System.out.println(putObjectResult.getRequestId());
    System.out.println(ciUploadResult.getOriginalInfo().getEtag());
    for(CIObject ciObject:ciUploadResult.getProcessResults().getObjectList()) {
        System.out.println(ciObject.getLocation());
        System.out.println(ciObject.getEtag());
    }
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}
```

#### 参数说明

PicOperations 类用于记录图像操作，其主要成员说明如下：

| 成员名称  | 描述                                                         | 类型 |
| --------- | ------------------------------------------------------------ | ---- |
| isPicInfo | 是否返回原图信息，0不返回原图信息，1返回原图信息，默认为0    | int  |
| rules     | 处理规则，一条规则对应一个处理结果（目前支持五条规则），不填则不进行图片处理 | List |

#### 返回参数说明

CIUploadResult 类用于返回图片处理结果信息，其主要成员说明如下：

| 成员名称       | 描述         | 类型           |
| -------------- | ------------ | -------------- |
| originalInfo   | 原图信息     | OriginalInfo   |
| processResults | 图片处理结果 | ProcessResults |

  OriginalInfo 类用于记录原图信息，其主要成员说明如下：

| 成员名称  | 描述                                                       | 类型      |
| --------- | ---------------------------------------------------------- | --------- |
| key       | 原图文件名                                                 | String    |
| location  | 图片路径                                                   | String    |
| imageInfo | 原图图片信息                                               | ImageInfo |
| etag      | 原图 ETag 信息（若处理结果图覆盖原图则为结果图 ETag 信息） | String    |

ImageInfo 类用于记录原图图片信息，其主要成员说明如下：

| 成员名称    | 描述         | 类型    |
| ----------- | ------------ | ------- |
| format      | 格式         | String  |
| width       | 图片宽度     | Integer |
| height      | 图片高度     | Integer |
| quality     | 图片质量     | Integer |
| ave         | 图片主色调   | String  |
| orientation | 图片旋转角度 | Integer |

ProcessResults 类用于记录图片处理结果，其主要成员说明如下：

| 成员名称   | 描述               | 类型 |
| ---------- | ------------------ | ---- |
| objectList | 每一个图片处理结果 | List |

CIObject 类用于记录一个图片处理结果，其主要成员说明如下：

| 成员名称       | 描述                       | 类型    |
| -------------- | -------------------------- | ------- |
| key            | 文件名                     | String  |
| location       | 图片路径                   | String  |
| format         | 图片格式                   | String  |
| width          | 图片宽度                   | Integer |
| height         | 图片高度                   | Integer |
| size           | 图片大小                   | Integer |
| quality        | 图片质量                   | Integer |
| etag | 处理结果图 ETag 信息       | String |



## 对云上数据进行图片处理

下面示例展示了如何对已存储在 COS 的图片进行相应处理操作，并将结果存入到 COS。

#### 示例代码

[//]: # ".cssg-snippet-process-with-pic-operation"
```java
String bucketName = "examplebucket-1250000000";
String key = "test.jpg";
ImageProcessRequest imageReq = new ImageProcessRequest(bucketName, key);

PicOperations picOperations = new PicOperations();
picOperations.setIsPicInfo(1);
List<PicOperations.Rule> ruleList = new LinkedList<>();
PicOperations.Rule rule1 = new PicOperations.Rule();
rule1.setBucket(bucketName);
rule1.setFileId("test-1.jpg");
rule1.setRule("imageMogr2/rotate/90");
ruleList.add(rule1);
PicOperations.Rule rule2 = new PicOperations.Rule();
rule2.setBucket(bucketName);
rule2.setFileId("test-2.jpg");
rule2.setRule("imageMogr2/rotate/180");
ruleList.add(rule2);
picOperations.setRules(ruleList);

imageReq.setPicOperations(picOperations);

CIUploadResult result = cosClient.processImage(imageReq);
result.getProcessResults();
result.getOriginalInfo();

try {
    CIUploadResult ciUploadResult = cosClient.processImage(imageReq);
    System.out.println(ciUploadResult.getOriginalInfo().getEtag());
    for(CIObject ciObject:ciUploadResult.getProcessResults().getObjectList()) {
        System.out.println(ciObject.getLocation());
        System.out.println(ciObject.getEtag());
    }
} catch (CosServiceException e) {
    e.printStackTrace();
} catch (CosClientException e) {
    e.printStackTrace();
}
```
