从0.14版本开始，Doris 支持通过 S3 协议直接从支持 S3 协议的在线存储系统导入数据。

本文档主要介绍如何导入腾讯云对象存储（兼容 S3 协议） 中存储的数据。也支持导入其他支持 S3协议的对象存储系统导入，如 AWS S3 、百度云的 BOS 和阿里云的 OSS 等。

## 适用场景
- 源数据在支持 S3 协议的存储系统中，如 COS，S3，BOS，OSS 等。
- 数据量在几十到百 GB 级别。

## 准备工作
1. 准备 AWS_ACCESS_KEY 和 AWS_SECRET_KEY。
首先需要找到或者添加腾讯云的访问密钥。路径是：在腾讯云搜索访问密钥，使用已有密钥或单击**新建密钥**。然后获取其中的 SecretId，SecretKey，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b2eb378ff371e2f93d08b3bbeff538c0.png)

2. 准备 REGION 和 ENDPOINT。
REGION 可以在创建桶的时候选择也可以在桶列表中查看到。ENDPOINT 的格式就是`http://cos.<REGION>.myqcloud.com`。其他云存储系统可以从相应的文档中找到与 S3 兼容的相关信息。

## 开始导入
导入方式和 [Broker Load](https://cloud.tencent.com/document/product/1387/70831) 基本相同，只需要将 `WITH BROKER broker_name ()` 语句替换成如下部分：
```
    WITH S3
    (
        "AWS_ENDPOINT" = "AWS_ENDPOINT",
        "AWS_ACCESS_KEY" = "AWS_ACCESS_KEY",
        "AWS_SECRET_KEY"="AWS_SECRET_KEY",
        "AWS_REGION" = "AWS_REGION"
    )
```

完整示例如下：
```
    LOAD LABEL example_db.exmpale_label_1
    (
        DATA INFILE("s3://your_bucket_name/your_file.txt")
        INTO TABLE load_test
        COLUMNS TERMINATED BY ","
    )
    WITH S3
    (
        "AWS_ENDPOINT" = "AWS_ENDPOINT",
        "AWS_ACCESS_KEY" = "AWS_ACCESS_KEY",
        "AWS_SECRET_KEY"="AWS_SECRET_KEY",
        "AWS_REGION" = "AWS_REGION"
    )
    PROPERTIES
    (
        "timeout" = "3600"
    );
```

## 常见问题
S3 SDK 默认使用 virtual-hosted style 方式。但某些对象存储系统可能没开启或没支持 virtual-hosted style 方式的访问，此时我们可以添加 `use_path_style` 参数来强制使用 path style 方式：
```
  WITH S3
  (
        "AWS_ENDPOINT" = "AWS_ENDPOINT",
        "AWS_ACCESS_KEY" = "AWS_ACCESS_KEY",
        "AWS_SECRET_KEY"="AWS_SECRET_KEY",
        "AWS_REGION" = "AWS_REGION",
        "use_path_style" = "true"
  )
```
