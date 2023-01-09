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



## 使用 Terraform 创建 TKE 集群

1. 创建一个工作目录，并在工作目录中创建名为 `main.tf` 的 Terraform 配置文件。
<dx-alert infotype="explain" title="">
   `main.tf` 文件描述的是以下 Terraform 配置：
   - 创建一个新的 VPC，并创建一个该 VPC 下的 Subnet 子网。
   - 创建一个 TKE 托管集群。
   - 在该 TKE 集群下创建一个节点池。
</dx-alert>
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
locals {
 region = "xxx"								# 使用的地域，如ap-beijing，即北京
 zone1 = "xxx"									# 地域下的一个可用区，如ap-beijing-1，即北京一区
 vpc_name = "xxx"							# 设置VPC的名字，如tke-tf-demo
 vpc_cidr_block = "xxx"				# VPC的CIDR设置，如10.0.0.0/16	
 subnet1_name = "xxx"					# 子网1的名字，如tke-tf-demo-sub1
 subnet1_cidr_block = "xxx"		# 子网1的CIDR设置，如10.0.1.0/24
 cluster_name = "xxx"					# TKE集群的name，如tke-tf-demo-cluster
 network_type = "xxx"					# TKE托管集群的网络模式，如GR，表示使用Global Route
 cluster_cidr = "xxx"					# 集群的容器网络，不能与网络冲突，如172.26.0.0/20
 cluster_version = "xxx"				# TKE集群的Kubernetes版本，如1.22.5
}
   
   
# 腾讯云Porvier的基本配置
provider "tencentcloud" {
 # 如果使用配置文件中写入密钥的方式，在此处写入SecretId和SecretKey。但更推荐使用环境变量注入的方式。
 # secret_id  = "xxx"
 # secret_key = "xxx"
  region = local.region 			
}
   
# 声明VPC资源
resource "tencentcloud_vpc" "vpc_example" {
  name = local.vpc_name
  cidr_block   = local.vpc_cidr_block
}
     
# 声明子网资源
resource "tencentcloud_subnet" "subnet_example" {
  availability_zone = local.zone1
  cidr_block        = local.subnet1_cidr_block
  name              = local.subnet1_name
  vpc_id            = tencentcloud_vpc.vpc_example.id			# 指定子网资源所属VPC为前面创建的
}
   
# 声明TKE集群资源
resource "tencentcloud_kubernetes_cluster" "managed_cluster_example" {
  vpc_id = tencentcloud_vpc.vpc_example.id 								# 引用前面创建获得的VPC Id
  cluster_name = local.cluster_name
  network_type = local.network_type
  cluster_cidr = local.cluster_cidr
  cluster_version = local.cluster_version
}
```


2. （可选）若您首次使用腾讯云容器服务，您需要为当前服务角色授权，赋予容器服务操作权限后才能正常地访问您的其他云服务资源。如果您已完成过授权，请直接跳过此步骤。
  - 您可以在首次登录 [容器服务控制台](https://console.cloud.tencent.com/tke2) 时，对当前账号授予腾讯云容器服务操作云服务器 CVM、负载均衡 CLB、云硬盘 CBS 等云资源的权限。详情请参见 [服务授权](https://cloud.tencent.com/document/product/457/43416#.E9.A2.84.E8.AE.BE.E7.AD.96.E7.95.A5-qcloudaccessfortkerole.3Ca-id.3D.22qcloudaccessfortkerole.22.3E.3C.2Fa.3E)。
  - 您也可以在 Terraform 配置文件中完成授权。您需要在工作目录下新建 `cam.tf` 文件，文件内容如下：
   ```
   # 创建服务预设角色TKE_QCSRole
   resource "tencentcloud_cam_role" "TKE_QCSRole" {
     name        = "TKE_QCSRole"
     document    = <<EOF
   {
     "statement": [
       {
         "action":"name/sts:AssumeRole",
         "effect":"allow",
         "principal":{
           "service":"ccs.qcloud.com"
         }
       }
     ],
     "version":"2.0"
   }
   EOF
     description = "当前角色为 腾讯云容器服务 服务角色，该角色将在已关联策略的权限范围内访问您的其他云服务资源。"
   }
   
   # 创建服务预设角色IPAMDofTKE_QCSRole
   resource "tencentcloud_cam_role" "IPAMDofTKE_QCSRole" {
     name = "IPAMDofTKE_QCSRole"
     document    = <<EOF
   {
     "statement": [
       {
         "action":"name/sts:AssumeRole",  
         "effect":"allow",
         "principal":{
           "service":"ccs.qcloud.com"
         }
       }
     ],
     "version":"2.0"
   }
   EOF
     description = "当前角色为 容器服务IPAMD支持 服务角色，该角色将在已关联策略的权限范围内访问您的其他云服务资源。"
   }
   
   # 预设策略 QcloudAccessForTKERole
   data "tencentcloud_cam_policies" "qca" {
     name = "QcloudAccessForTKERole"
   }
   
   # 预设策略 QcloudAccessForTKERoleInOpsManagement
   data "tencentcloud_cam_policies" "ops_mgr" {
     name = "QcloudAccessForTKERoleInOpsManagement"
   }
   
   # 预设策略 QcloudAccessForIPAMDofTKERole
   data "tencentcloud_cam_policies" "qcs_ipamd" {
     name = "QcloudAccessForIPAMDofTKERole"
   }
   
   # 角色TKE_QCSRole关联QcloudAccessForTKERole策略
   resource "tencentcloud_cam_role_policy_attachment" "QCS_QCA" {
     role_id   = lookup(tencentcloud_cam_role.TKE_QCSRole, "id")
     policy_id = data.tencentcloud_cam_policies.qca.policy_list.0.policy_id
   }
   
   # 角色TKE_QCSRole关联策略QcloudAccessForTKERoleInOpsManagement
   resource "tencentcloud_cam_role_policy_attachment" "QCS_OpsMgr" {
     role_id   = lookup(tencentcloud_cam_role.TKE_QCSRole, "id")
     policy_id = data.tencentcloud_cam_policies.ops_mgr.policy_list.0.policy_id
   }
   
   # 角色IPAMDofTKE_QCSRole关联策略QcloudAccessForIPAMDofTKERole
   resource "tencentcloud_cam_role_policy_attachment" "QCS_Ipamd" {
     role_id   = lookup(tencentcloud_cam_role.IPAMDofTKE_QCSRole, "id")
     policy_id = data.tencentcloud_cam_policies.qcs_ipamd.policy_list.0.policy_id
   }
   ```
   

3. 执行以下命令，初始化 Terraform 的运行环境。
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

4. 执行以下命令，查看 Terraform 根据配置文件生成的资源规划。
   ```
   terraform plan
   ```
返回信息如下所示：
   ```   
   Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
     + create
   
   Terraform will perform the following actions:
   ...
   
   Plan: 3 to add, 0 to change, 0 to destroy.
   ...
   ```
4. 执行以下命令，创建资源。
   ```
   terraform apply
   ```
	 返回信息如下所示：
   ```
   ...
   Plan: 3 to add, 0 to change, 0 to destroy.
   
   Do you want to perform these actions?
     Terraform will perform the actions described above.
     Only 'yes' will be accepted to approve.
   
     Enter a value: 
   ```
根据提示输入 `yes` 创建资源，返回信息如下所示： 
   ```
   ...
   Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
   ```
   
   至此，上述步骤完成了 VPC、子网、TKE 托管集群的创建。您可以在腾讯云控制台查看创建的资源。



## 使用 Terraform 删除 TKE 集群

如果您需要删除已创建的 VPC、子网、TKE 托管集群资源，可以执行以下命令。

```
terraform destroy
```

返回信息如下所示：

```
...
Plan: 0 to add, 0 to change, 3 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: 
```
根据提示输入 `yes` 确认执行计划，返回信息如下所示： 
 
```
...
Destroy complete! Resources: 3 destroyed.
```



## 相关文档

- [Terraform 官方文档](https://developer.hashicorp.com/terraform)
- [腾讯云Terraform Provider](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud)
- [腾讯云 TKE 标准集群](https://cloud.tencent.com/document/product/457/6759)
