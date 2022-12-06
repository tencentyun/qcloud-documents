## 安装 Terraform
前往 [Terraform 官网](https://developer.hashicorp.com/terraform/downloads)，使用命令行直接安装 Terraform 或下载二进制安装文件。

## 认证和鉴权
### 获取凭证
在首次使用 Terraform 之前，请前往 [云 API 密钥页面](https://console.cloud.tencent.com/cam/capi) 申请安全凭证 SecretId 和 SecretKey。若已有可使用的安全凭证，则跳过该步骤。
1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在左侧导航栏，选择**访问密钥 > API 密钥管理**。
2. 在 API 密钥管理页面，单击**新建密钥**，即可以创建一对 SecretId/SecretKey。



### 鉴权

#### 方式1：（推荐）使用环境变量注入账号的访问密钥
请将如下信息添加至环境变量配置：
```
export TENCENTCLOUD_SECRET_ID="xxx"			# 替换为账号访问密钥的SecretId
export TENCENTCLOUD_SECRET_KEY="xxx"		# 替换为账号访问密钥的SecretKey
```

#### 方式2：在 Terraform 配置文件的 provider 代码块中填写账号的访问密钥
在用户目录下创建 `provider.tf` 文件，输入如下内容：
>! 使用此方式请务必注意配置文件中密钥的安全性。
>
```
provider "tencentcloud" {
  secret_id = "xxx"											# 替换为账号访问密钥的SecretId
  secret_key = "xxx"										# 替换为账号访问密钥的SecretKey
}
```

## 创建 TKE 集群
您可以通过 [容器服务控制台](https://console.cloud.tencent.com/tke2/overview) 或 [云 API](https://cloud.tencent.com/document/product/1278/46696) 创建集群，操作详情见 [创建一个标准集群](https://cloud.tencent.com/document/product/457/32189)。 
您也可以通过 [腾讯云 Terraform](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/1.79.0) 创建集群，操作详情见 [使用 Terraform 管理 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。 

## 使用 Terraform 创建 TKE 节点池
  
1. 创建一个工作目录，并在工作目录中创建名为 `main.tf` 的 Terraform 配置文件。
`main.tf` 文件内容如下：

   ```
   # 标识使用腾讯云的Terraform Provider
   terraform {
     required_providers {
       tencentcloud = {
         source = "tencentcloudstack/tencentcloud"
         version = "~> 1.78.13"
       }
     }
   }
   
   # 定义本地变量，实际使用时按需修改下列变量实际值。后面各代码块中会引用下列变量的值。
   # 实际使用时您也可以通过引用Terraform相关resource实例（如集群tencentcloud_kubernetes_cluster）的方式获取需要的值。
   locals {
   	region = "xxx"								# 使用的地域，如ap-beijing，即北京
   	cluster_id = "cls-xxx" 				# 节点池关联的集群Id
   	node_pool_name = "xxx"				# 节点池名称，如tke-tf-demo-node-pool
   	node_pool_vpc_id = "vpc-xxx"	# 节点池关联的VPC Id
   	node_pool_subnet_ids = ["subnet-xxx", "subnet-xxx"]		# 节点池关联的子网Id数组
   	max_node_size = xxx						# 节点池最大节点数量
   	min_node_size = xxx						# 节点池最小节点数量
   	cvm_instance_type = "xxx"			# 节点池CVM机型，可选值参考https://cloud.tencent.com/document/api/213/15749获取
   	cvm_pass_word = "xxx"					# 节点池CVM机器登录密码，请注意密码安全性
   	security_group_ids = ["sg-xxx", "sg-xxx"] 						# 节点池关联的安全组Id数组
   }
   
   # 腾讯云Porvier的基本配置
   provider "tencentcloud" {
   	# 如果使用配置文件中写入密钥的方式，在此处写入SecretId和SecretKey。但更推荐使用环境变量注入的方式。
   	# secret_id  = "xxx"
   	# secret_key = "xxx"
     region = local.region 			
   }
   
   # 声明TKE节点池资源
   resource "tencentcloud_kubernetes_node_pool" "example_node_pool" {
     cluster_id = local.cluster_id
     max_size   = local.max_node_size
     min_size   = local.min_node_size
     name       = local.node_pool_name
     vpc_id     = local.node_pool_vpc_id
     subnet_ids = local.node_pool_subnet_ids
     auto_scaling_config {
       instance_type = local.cvm_instance_type
       # key_ids = ["xxx"]                                # 设置节点池CVM机器登录密钥
       password = local.cvm_pass_word                     # 设置节点池CVM机器登录密码，请注意密码安全性
       security_group_ids = local.security_group_ids
     }
   }
   ```
   

2. 执行以下命令，初始化 Terraform 的运行环境。
   ```
   terraform init
   ```
返回信息如下所示：
   ```   
   Initializing the backend...
   
   Initializing provider plugins...
   - Finding tencentcloudstack/tencentcloud versions matching "~> 1.78.13"...
   - Installing tencentcloudstack/tencentcloud v1.78.13...
   ...
   
   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.
   
   ...
   ```

3. 执行以下命令，查看 Terraform 根据配置文件生成的资源规划。
   ```
   terraform plan
   ```
返回信息如下所示：

   ```   
   Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
     + create
   
   Terraform will perform the following actions:
   ...
   
   Plan: 1 to add, 0 to change, 0 to destroy.
   ...
   ```
4. 执行以下命令，创建资源。
   ```
   terraform apply
   ```
	 返回信息如下所示：
   ```
   ...
   Plan: 1 to add, 0 to change, 0 to destroy.
   
   Do you want to perform these actions?
     Terraform will perform the actions described above.
     Only 'yes' will be accepted to approve.
   
     Enter a value: 
   ```
根据提示输入 `yes` 创建资源，返回信息如下所示： 
   ```
   ...
   Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
   ```
   
   至此，上述步骤完成了节点池的创建。您可以在腾讯云控制台查看创建的资源。



## 使用 Terraform 删除 TKE 节点池配置

如果您需要删除已创建的节点池资源，可以执行以下命令。

```
terraform destroy
```

返回信息如下所示：
```
...
Plan: 0 to add, 0 to change, 1 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: 
```
根据提示输入 `yes` 确认执行计划，返回信息如下所示： 
 
```
...
Destroy complete! Resources: 1 destroyed.
```



## 相关文档

- [Terraform 官方文档](https://developer.hashicorp.com/terraform)
- [腾讯云Terraform Provider](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud)
- [腾讯云 TKE 节点池](https://cloud.tencent.com/document/product/457/43719)
