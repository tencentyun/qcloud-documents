## 简介

Terraform 是一款开源自动化资源编排工具，使用代码管理维护 IT 资源，取代手动操作。

腾讯云于2017年开始支持 terraform 进行资源编排，截止目前共有10余款基础产品完美支持 terraform，涉及计算、存储、网络、数据库等类别。本文为您详细介绍如何使用 Terraform 管理 COS。

## 安装 Terraform

Terraform 安装简单，具体请参见 [腾讯云 Terraform 应用指南（一）](https://cloud.tencent.com/developer/article/1473713) 的“安装 Terraform”章节。

## 使用 Terraform 管理 COS 

#### 1. 初始化
（1）创建工作目录，例如 terraform-test 目录。
（2）为 Terraform 创建或准备好腾讯云账号，并获取 SecretID 和 SecretKey。
（3）编写 provider 配置文件，将您的 SecretID 和 SecretKey 等账号信息写入配置文件 provider.tf，保存在工作目录（terraform-test 目录）下，配置文件 provider.tf 示例如下：
```
provider "tencentcloud" {
	secret_id  = "AKIDdFUUEjgud7WpujygoiNsENJ1UigO****"
	secret_key = "yjFWbN4oJbeQwDG4e0AKN9f191f4****"
	region     = "ap-beijing"
}
```

> ?其他配置方式，详情请参见 [腾讯云 Terraform 应用指南（一）](https://cloud.tencent.com/developer/article/1473713) 的“配置腾讯云 provider 文件”章节。

（4）执行 init 命令，初始化工作目录（例如 terraform-test），示例如下：
```
[root@tigger terraform-test]#terraform init
```

若打印如下信息，则表示初始化成功。
```sh
Terraform has been successfully initialized!
```

>?每个 Terraform 项目都需要一个工作目录，所有操作均在此目录进行。有些 Terraform 命令可在参数中指定工作目录，详情请参见 [腾讯云 Terraform 应用指南（三）](https://cloud.tencent.com/developer/article/1482560)。若不指定，默认当前目录是工作目录。

#### 2. 创建存储桶
（1）编写 resource 配置文件，定义资源。假设创建私有存储桶 examplebucket-1250000000，示例如下：
```
resource "tencentcloud_cos_bucket" "mycos" {
  bucket = "examplebucket-1250000000"     #存储桶名称，存储桶名称格式为 BucketName-APPID
  acl    = "private"  #ACL 权限为私有
}
```

>!实际操作时，请务必将存储桶名称后缀替换为用户的真实 APPID，否则，COS 将拒绝创建存储桶。

以 resource 开头的`*.tf`配置文件定义资源。
- tencentcloud_cos_bucket：描述资源类型是存储桶。其他资源类型详情请参见 [Terraform 页面](https://www.terraform.io/docs/providers/tencentcloud/r/cos_bucket.html) 的左侧目录。
- mycos：描述资源名称，由用户自定义。

若创建支持静态网站的存储桶，示例如下：

```
resource "tencentcloud_cos_bucket" "examplebucket2" {
  bucket = "examplebucket2-1250000000"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}
```

若设置 CORS，示例如下：

```
resource "tencentcloud_cos_bucket" "examplebucket3" {
  bucket = "examplebucket3-1250000000"
  acl    = "public-read-write"

  cors_rules {
    allowed_origins = ["http://*.abc.com"]
    allowed_methods = ["PUT", "POST"]
    allowed_headers = ["*"]
    max_age_seconds = 300
    expose_headers  = ["Etag"]
  }
}
```

> ?Terraform 可管理 COS bucket 的 website、ACL、cors_rules、lifecycle_rules 等属性，详情请参见 [tencentcloud_cos_bucket](https://www.terraform.io/docs/providers/tencentcloud/r/cos_bucket.html) 的 Argument Reference 章节。

（2）执行`terraform apply`命令，进行部署资源，创建存储桶 examplebucket-1250000000。您可登录 [COS 控制台](https://console.cloud.tencent.com/cos5)，查看刚创建的存储桶 examplebucket-1250000000。

> ?若存储桶 examplebucket-1250000000 已存在，Terraform 将先删除原存储桶，再创建空存储桶。

一般在运行`terraform apply`命令之前，可先执行`terraform plan`命令。`terraform plan`命令可以实现在不对实际资源或状态进行任何更改的前提下，验证执行计划是否符合预期。

#### 3. 创建对象资源

（1）编写 resource 配置文件，定义资源。假设上传文件 picture.jpg 到存储桶 examplebucket-1250000000，示例如下：
```
resource "tencentcloud_cos_bucket_object" "myobject" {
  bucket = "examplebucket-1250000000"  # 存储桶名称，格式为 BucketName-APPID
  key    = "picture.jpg"   # 对象键
  source = "D:\folder\picture.jpg"  # 待上传文件路径，需要包含路径和文件名
}
```

（2）执行`terraform apply`命令，进行部署资源，上传 picture.jpg。

> ?
> - Terraform 可管理 COS Object 的 upload、ACL、content、ETag、storage_class 等属性，详情请参见 [tencentcloud_cos_bucket_object](https://www.terraform.io/docs/providers/tencentcloud/r/cos_bucket_object.html) 的 Argument Reference 章节。
> - Terraform 目前不支持下载对象，因为 Terraform 定位资源编排工具，更关注多云资源的编排和部署。

#### 4. 查询资源

4.1 执行`terraform show`命令，查看全部资源信息（即查看所有存储桶和对象的元数据）。

若需查询指定存储桶或对象的指定信息，则需要编写配置文件，然后执行`terraform apply`命令。

4.2 精细化查询存储桶信息。

（1）编写 data source 配置文件，定义精细化查询条件。假设查询以 example 为前缀的存储桶，示例如下：
```
data "tencentcloud_cos_buckets" "cos_buckets" {
  bucket_prefix      = "example"  # 存储桶前缀
  result_output_file = "mytestpath"  # 保存查询结果文件名
}
```

以 data 开头的`*.tf`配置文件定义查询条件。

- tencentcloud_cos_buckets：描述资源类型是存储桶，详情请参见 [Terraform 页面](https://www.terraform.io/docs/providers/tencentcloud/d/cos_buckets.html) 的左侧目录。
- cos_buckets：描述资源名称，由用户自定义。

（2）执行`terraform apply`命令，进行查询。查询结果保存在文件 mytestpath。

>?若需查询存储桶的属性信息，详情请参见 [tencentcloud_cos_buckets](https://www.terraform.io/docs/providers/tencentcloud/d/cos_buckets.html) 的 Argument Reference 章节。

4.3 精细化查询对象信息。

（1）编写 data source 配置文件，定义精细化查询条件。假设查询对象 picture.jpg 的元数据，示例如下：

```
data "tencentcloud_cos_bucket_object" "mycos" {
  bucket             = "examplebucket-1250000000"  # 存储桶名称，格式为 BucketName-APPID
  key                = "picture.jpg"  # 对象键
  result_output_file = "mytestpath"  # 保存查询结果文件名
}

```

（2）执行`terraform apply`命令，进行查询。查询结果保存在文件 mytestpath。

> ?若需查询对象的属性信息，详情请参见 [tencentcloud_cos_bucket_object](https://www.terraform.io/docs/providers/tencentcloud/d/cos_bucket_object.html) 的 Argument Reference 章节。

#### 5. 删除资源

执行`terraform destroy`命令删除工作目录下的所有资源。

若需删除指定的存储桶或对象，从配置文件中，删除定义该存储桶或对象资源的配置信息，然后执行`terraform apply`命令。建议您使用`terraform show`命令来检查删除结果。

