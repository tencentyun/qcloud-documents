
## Terraform 是什么？
[Terraform](https://www.terraform.io/) 是一款使用 Go 编写、运行在客户端、开源的资源编排工具。基于 HashiCorp Plugin 的架构设计，赋予 Terraform 高度可扩展的特性。目前腾讯云也基于 Terraform Plugin 实现了 TencentCloud Provider，支持通过  Terraform 管理腾讯云上资源。示意图如下：
![](https://qcloudimg.tencent-cloud.cn/raw/d8c9eb0619e3bfab3f57dad1474a291c.png)

[TencentCloud Provider](https://github.com/tencentcloudstack/terraform-provider-tencentcloud) 基于 tencentcloud-sdk-go 实现，目前已经提供了超过183个 Resource 和158个 Data Source，覆盖计算、存储、网络、容器服务、负载均衡、中间件、数据库、云监控等超过30款产品，已满足众多用户的基本上云需求。

您可通过腾讯云提供的 [Terraform 文档](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs) 及 [Terraform 编写样例](https://github.com/tencentcloudstack/terraform-provider-tencentcloud/tree/master/examples)，来快速了解并开始使用 Terraform。同时，[Terraform Module](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest) 已支持部分资源且仍在扩展中，请您保持关注。

## Terraform 优势

### 多云编排
Terraform 适用于多云方案，您可将相类似的基础结构部署到腾讯云、其他云提供商或本地数据中心。开发人员能够使用相同的工具和相似的配置文件同时管理不同云提供商的资源。


### 基础设施及代码
基础设施可以使用高级配置语法 HCL 进行描述，使得基础设施能够被代码化和版本化，从而可以进行共享和重复使用。示例如下：
```bash
resource "tencentcloud_mysql_instance" "mysql" {
    mem_size          = 16000
    cpu               = 4
    volume_size       = 50
    charge_type       = "PREPAID"
    instance_name     = "testAccMysql"
    engine_version    = "5.5"
    root_password     = "test1234"
    availability_zone = var.availability_zone
    internet_service  = 1
    intranet_port     = 3360
    prepaid_period    = 1

    tags = {
        purpose = "for test"
    }

    parameters = {
        max_connections = "1000"
    }
    count = 1
}
```

### 执行计划
Terraform 具备 “Planning” 步骤，在此步骤中 Terraform 会生成执行计划。执行计划会显示当调用 apply 时 Terraform 的状态，您可通过该能力在 Terraform 操作基础设施时避免任何意外。示例如下：
```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
+ create

Terraform will perform the following actions:

# tencentcloud_ckafka_instance.foo will be created
+ resource "tencentcloud_ckafka_instance" "foo" {
    + band_width         = (known after apply)
    + disk_size          = 500
    + disk_type          = "CLOUD_BASIC"
    + id                 = (known after apply)
    + instance_name      = "tf-test"
    + kafka_version      = "1.1.1"
    + msg_retention_time = 1300
    + partition          = (known after apply)
    + period             = 1
    + public_network     = (known after apply)
    + renew_flag         = 0
    + subnet_id          = "subnet-dvzsb5ro"
    + vpc_id             = "vpc-fvl16x63"
    + zone_id            = 100006

    + config {
        + auto_create_topic_enable   = true
        + default_num_partitions     = 3
        + default_replication_factor = 3
        }

    + dynamic_retention_config {
        + bottom_retention        = (known after apply)
        + disk_quota_percentage   = (known after apply)
        + enable                  = 1
        + step_forward_percentage = (known after apply)
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.
```


### 资源拓扑
Terraform 建立了资源图，并行创建和修改任何非依赖性资源。使 Terraform 尽可能高效地构建基础设施，操作人员可以深入了解基础设施中的依赖性。您可执行以下命令：
```bash
terraform graph | dot -Tsvg > graph.svg
```
生成资源示意图如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/dfa0f17c2481d3ac81b94433af3a64af.png)


### 自动变更
您可在基础设施上通过最少的人工干预工作，应用复杂的变更集。通过前文中的执行计划及资源拓扑，您可准确获取 Terraform 动态，避免可能的人为错误。

### 远程状态管理
Terraform 引入了远程状态存储机制 Backend，目前腾讯云可通过对象存储 COS 来管理用户的 tfState 文件，避免将文件保存在本地，造成丢失。同时，远程存储使多人同时对 Terraform 资源进行管理成为可能。
