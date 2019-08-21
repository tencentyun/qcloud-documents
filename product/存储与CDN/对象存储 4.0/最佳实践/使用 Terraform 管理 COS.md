
野鹤
运营一片闲云

查找系统/模块
所有系统
查找系统/模块
最常使用
文档中心 | 官网文档中心
文章编辑器 | 官网文档中心
文档时效跟踪工具 | 官网文档中心
用户意见跟踪系统 | 官网文档中心
自测跟踪工具 | 官网文档中心
闲云
官网内容运营
专栏
控制台运营
社区
开发者实验室
消息中心
问答运营
官网文档中心
文章编辑器
文档中心
文档中心（国际站）
Github链接转换工具
检查工具
自测跟踪工具
用户意见跟踪系统
文档时效跟踪工具
官网入门中心
产品入门教程
首页管理
项目实践中心
腾讯云账号运营
登录邮箱修改工具
国际版跳过PayPal工具
国际站实名信息录入
过滤规则管理
中文检测查询
查询账号信息
申请国际站账号
账号注销工具
修改手机号申请
修改邮箱申请
帐号登录方式管理
API密钥查询
云API产品接口管理
白名单管理
剔除登录态工具
全局票据管理
内部账户管理工具
封禁账号
角色管理
社区线下活动
首页运营
活动管理
新建活动
工作人员管理
评论管理
举报管理
权限管理
新建直播
直播管理
官网工具运营
专属实验室
腾讯云学院
国际站官网运营
移动端运营
官网 TVP 管理
日志工具
控制台监控
帐号安全
访问管理(CAM)
官网监控
社区沙龙
故障诊断
社区审核
实名认证工具
控制台业务自助运营
Tea 开发
TCB 控制台运营
（2）执行`terraform apply`命令，进行部署资源，上传 picture.jpg。
​
> ?
> - Terraform 可管理 COS Object 的 upload、ACL、content、ETag、storage_class 等属性，详情请参见 [tencentcloud_cos_bucket_object](https://www.terraform.io/docs/providers/tencentcloud/r/cos_bucket_object.html) 的 Argument Reference 章节。
> - Terraform 目前不支持下载对象，因为 Terraform 定位资源编排工具，更关注多云资源的编排和部署。
​
#### 4. 查询资源
​
4.1 执行`terraform show`命令，查看全部资源信息（即查看所有存储桶和对象的元数据）。
​
若需查询指定存储桶或对象的指定信息，则需要编写配置文件，然后执行`terraform apply`命令。
​
4.2 精细化查询存储桶信息。
​
（1）编写 data source 配置文件，定义精细化查询条件。假设查询以 example 为前缀的存储桶，示例如下：
```
data "tencentcloud_cos_buckets" "cos_buckets" {
  bucket_prefix      = "example"  # 存储桶前缀
  result_output_file = "mytestpath"  # 保存查询结果文件名
}
```
​
以 data 开头的`*.tf`配置文件定义查询条件。
​
- tencentcloud_cos_buckets：描述资源类型是存储桶，详情请参见 [Terraform 页面](https://www.terraform.io/docs/providers/tencentcloud/d/cos_buckets.html) 的左侧目录。
- cos_buckets：描述资源名称，由用户自定义。
​
（2）执行`terraform apply`命令，进行查询。查询结果保存在文件 mytestpath。
​
>?若需查询存储桶的属性信息，详情请参见 [tencentcloud_cos_buckets](https://www.terraform.io/docs/providers/tencentcloud/d/cos_buckets.html) 的 Argument Reference 章节。
​
4.3 精细化查询对象信息。
​
（1）编写 data source 配置文件，定义精细化查询条件。假设查询对象 picture.jpg 的元数据，示例如下：
​
```
data "tencentcloud_cos_bucket_object" "mycos" {
  bucket             = "examplebucket-1250000000"  # 存储桶名称，格式为 BucketName-APPID
  key                = "picture.jpg"  # 对象键
  result_output_file = "mytestpath"  # 保存查询结果文件名
}
​
```
​
（2）执行`terraform apply`命令，进行查询。查询结果保存在文件 mytestpath。
​
> ?若需查询对象的属性信息，详情请参见 [tencentcloud_cos_bucket_object](https://www.terraform.io/docs/providers/tencentcloud/d/cos_bucket_object.html) 的 Argument Reference 章节。
​
#### 5. 删除资源
​
执行`terraform destroy`命令删除工作目录下的所有资源。
​
若需删除指定的存储桶或对象，从配置文件中，删除定义该存储桶或对象资源的配置信息，然后执行`terraform apply`命令。建议您使用`terraform show`命令来检查删除结果。
​
​
简介
安装 Terraform
使用 Terraform 管理 COS
简介
Terraform 是一个开源自动化资源编排工具，使用代码管理维护 IT 资源，取代手动操作。

腾讯云于2017年开始支持 terraform 进行资源编排，截止目前共有10余款基础产品完美支持 terraform，涉及计算、存储、网络、数据库等类别。本文为您详细介绍如何使用 Terraform 管理 COS。

安装 Terraform
Terraform 安装简单，具体请参见 腾讯云 Terraform 应用指南（一） 的“安装 Terraform ”章节。

使用 Terraform 管理 COS
1. 初始化
（1）创建工作目录，例如 terraform-test 目录。
（2）为 Terraform 创建或准备好腾讯云账号，并获取 SecretID 和 SecretKey。
（3）编写 provider 配置文件，将您的 SecretID 和 SecretKey 等账号信息写入配置文件 provider.tf，保存在工作目录（terraform-test 目录）下，配置文件 provider.tf 示例如下：

provider "tencentcloud" {
    secret_id  = "AKIDdFUUEjgud7WpujygoiNsENJ1UigO****"
    secret_key = "yjFWbN4oJbeQwDG4e0AKN9f191f4****"
    region     = "ap-beijing"
}
说明：
其他配置方式，详情请参见 腾讯云 Terraform 应用指南（一） 的“配置腾讯云 provider 文件”章节。

（4）执行 init 命令，初始化工作目录（例如 terraform-test），示例如下：

[root@tigger terraform-test]#terraform init
若打印如下信息，则表示初始化成功。

Terraform has been successfully initialized!
说明：
每个 Terraform 项目都需要一个工作目录，所有操作均在此目录进行。有些 Terraform 命令可在参数中指定工作目录，详情请参见 腾讯云 Terraform 应用指南（三）。若不指定，默认当前目录是工作目录。

2. 创建存储桶
（1）编写 resource 配置文件，定义资源。假设创建私有存储桶 examplebucket-1250000000，示例如下：

resource "tencentcloud_cos_bucket" "mycos" {
  bucket = "examplebucket-1250000000"     #存储桶名称，存储桶名称格式为 BucketName-APPID
  acl    = "private"  #ACL 权限为私有
}
注意：
实际操作时，请务必将存储桶名称后缀替换为用户的真实 APPID，否则，COS 将拒绝创建存储桶。

以 resource 开头的*.tf配置文件定义资源。

tencentcloud_cos_bucket：描述资源类型是存储桶。其他资源类型详情请参见 Terraform 页面 的左侧目录。
mycos：描述资源名称，由用户自定义。
若创建支持静态网站的存储桶，示例如下：

resource "tencentcloud_cos_bucket" "examplebucket2" {
  bucket = "examplebucket2-1250000000"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}
若设置 CORS，示例如下：

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
说明：
Terraform 可管理 COS bucket 的 website、ACL、cors_rules、lifecycle_rules 等属性，详情请参见 tencentcloud_cos_bucket 的 Argument Reference 章节。

（2）执行terraform apply命令，进行部署资源，创建存储桶 examplebucket-1250000000。您可登录 COS 控制台，查看刚创建的存储桶 examplebucket-1250000000。

说明：
若存储桶 examplebucket-1250000000 已存在，Terraform 将先删除原存储桶，再创建空存储桶。

一般在运行terraform apply命令之前，可先执行terraform plan命令。terraform plan命令可以实现在不对实际资源或状态进行任何更改的前提下，验证执行计划是否符合预期。

3. 创建对象资源
（1）编写 resource 配置文件，定义资源。假设上传文件 picture.jpg 到存储桶 examplebucket-1250000000，示例如下：

resource "tencentcloud_cos_bucket_object" "myobject" {
  bucket = "examplebucket-1250000000"  # 存储桶名称，格式为 BucketName-APPID
  key    = "picture.jpg"   # 对象键
  source = "D:\folder\picture.jpg"  # 待上传文件路径，需要包含路径和文件名
}
（2）执行terraform apply命令，进行部署资源，上传 picture.jpg。

说明：
Terraform 可管理 COS Object 的 upload、ACL、content、ETag、storage_class 等属性，详情请参见 tencentcloud_cos_bucket_object 的 Argument Reference 章节。
Terraform 目前不支持下载对象，因为 Terraform 定位资源编排工具，更关注多云资源的编排和部署。
4. 查询资源
4.1 执行terraform show命令，查看全部资源信息（即查看所有存储桶和对象的元数据）。

若需查询指定存储桶或对象的指定信息，则需要编写配置文件，然后执行terraform apply命令。

4.2 精细化查询存储桶信息。

（1）编写 data source 配置文件，定义精细化查询条件。假设查询以 example 为前缀的存储桶，示例如下：

data "tencentcloud_cos_buckets" "cos_buckets" {
  bucket_prefix      = "example"  # 存储桶前缀
  result_output_file = "mytestpath"  # 保存查询结果文件名
}
以 data 开头的*.tf配置文件定义查询条件。

tencentcloud_cos_buckets：描述资源类型是存储桶，详情请参见 Terraform 页面 的左侧目录。
cos_buckets：描述资源名称，由用户自定义。
（2）执行terraform apply命令，进行查询。查询结果保存在文件 mytestpath。

说明：
若需查询存储桶的属性信息，详情请参见 tencentcloud_cos_buckets 的 Argument Reference 章节。

4.3 精细化查询对象信息。

（1）编写 data source 配置文件，定义精细化查询条件。假设查询对象 picture.jpg 的元数据，示例如下：

data "tencentcloud_cos_bucket_object" "mycos" {
  bucket             = "examplebucket-1250000000"  # 存储桶名称，格式为 BucketName-APPID
  key                = "picture.jpg"  # 对象键
  result_output_file = "mytestpath"  # 保存查询结果文件名
}
（2）执行terraform apply命令，进行查询。查询结果保存在文件 mytestpath。

说明：
若需查询对象的属性信息，详情请参见 tencentcloud_cos_bucket_object 的 Argument Reference 章节。

5. 删除资源
执行terraform destroy命令删除工作目录下的所有资源。

若需删除指定的存储桶或对象，从配置文件中，删除定义该存储桶或对象资源的配置信息，然后执行terraform apply命令。建议您使用terraform show命令来检查删除结果。
