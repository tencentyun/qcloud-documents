
## 输入变量
- 通过输入变量，可自定义 Terraform 模块，且无需修改模块本身的源代码。通过此特性，您可在不同的 Terraform 配置间共享模块，使模块可组合和可重用。
- 输入变量支持动态传入。例如，在创建或修改基础设施时传入值、在代码中定义 Provider 时用变量替代硬编码的访问密钥、由创建基础设施的用户决定创建所需尺寸的主机等。
- 您可将一组 Terraform 代码理解为一个函数，则输入变量即为函数的入参。

### 定义输入变量
输入变量通过 `variable` 块进行定义。例如：
```bash
variable "image_id" {
  type = string
}

variable "availability_zone_names" {
  type    = list(string)
  default = ["us-west-1a"]
}

variable "docker_ports" {
  type = list(object({
    internal = number
    external = number
    protocol = string
  }))
  default = [
    {
      internal = 8300
      external = 8300
      protocol = "tcp"
    }
  ]
}
```

`variable` 关键字后即为变量名。在一个 Terraform 模块（同一个文件夹中的所有 Terraform 代码文件，不包含子文件夹）中变量名必须唯一。在代码中可以通过 `var.<NAME>` 的方式引用变量的值。

`variable` 块可以使用下列的可选参数进行声明：
- `default`：指定输入变量默认值。
- `type`：指定输入变量只能被赋予特定的值。
- `description`：指定输入变量的描述。
- `validation`：指定输入变量的验证规则。
- `sensitive`：在配置中使用变量时限制 Terraform UI 输出。
- `nullable`：指定输入变量是否可以为 `null`。

#### 类型
输入变量块中通过 type 定义类型：
- 基本类型：`string`、`number`、`bool`。
- 复合类型：`list(<TYPE>)`、`set(<TYPE>)`、`map(<TYPE>)`、`object({<ATTR NAME> = <TYPE>, ... })`、`tuple([<TYPE>, ...])`。

#### 描述
简要描述每个变量的用途。例如：
```bash
variable "image_id" {
  type        = string
  description = "The id of the machine image (AMI) to use for the server."
}
```

#### 自定义校验规则
Terraform 0.13.0 前，只能用类型约束确保输入参数的类型正确。Terraform 0.13.0 已引入输入变量自定义校验规则。例如：
```bash
variable "image_id" {
  type        = string
  description = "The id of the machine image (AMI) to use for the server."

  validation {
    condition     = length(var.image_id) > 4 && substr(var.image_id, 0, 4) == "ami-"
    error_message = "The image_id value must be a valid AMI id, starting with \"ami-\"."
  }
}
```
其中，condition 参数为 bool 类型参数，可通过表达式来判断输入变量是否合法。当 contidion 为 true 时输入变量合法，否则不合法。condition 表达式中只能通过 `var.<变量名称>` 引用当前定义的变量，并且它的计算不能产生错误。若表达式的计算产生错误是输入变量验证的一种判定手段，那么可以使用 can 函数来判定表达式的执行是否抛错。例如：
```bash
variable "image_id" {
  type        = string
  description = "The id of the machine image (AMI) to use for the server."

  validation {
    # regex(...) fails if it cannot find a match
    condition     = can(regex("^ami-", var.image_id))
    error_message = "The image_id value must be a valid AMI id, starting with \"ami-\"."
  }
}
```
上述示例中，若输入的 `image_id` 不符合正则表达式的要求，那么 regex 函数调用会抛出一个错误，并会被 can 函数捕获，输出 false。condition 表达式若为 false，Terraform 会返回 error_message 中定义的错误信息。error_message 应该完整描述输入变量校验失败的原因，以及输入变量的合法约束条件。


### 使用输入变量
输入变量可以通过 `var.<变量名称>` 的形式访问，只能在声明该变量的模块内访问。例如：
```bash
resource "tencentclould_instance" "example" {
  instance_type = "t2.micro"
  ami           = var.image_id
}
```



### 输入变量赋值

#### 命令行参数
在命令行上指定单个变量，需要在执行 `terraform plan` 和 `terraform apply` 命令时使用 `-var` 选项。例如：
```bash
terraform apply -var="image_id=ami-abc123"
terraform apply -var='image_id_list=["ami-abc123","ami-def456"]' -var="instance_type=t2.micro"
terraform apply -var='image_id_map={"us-east-1":"ami-abc123","us-east-2":"ami-def456"}'
```

#### 参数文件
设置大量变量时，推荐在变量参数文件中指定它们的值（文件名以 `.tfvars` 或 `.tfvars.json` 结尾），并在命令行上使用 `-var-file` 指定该文件。例如：
```bash
terraform apply -var-file="testing.tfvars"
```
定义参数文件使用与 Terraform 语言文件相同的基本语法，但仅包含变量名分配。例如：
```bash
image_id = "ami-abc123"
availability_zone_names = [
  "us-east-1a",
  "us-west-1c",
]
```
Terraform 会自动加载许多变量定义文件：
- 文件名为 `terraform.tfvars` 或 `terraform.tfvars.json` 的文件。
- 文件名称以 `.auto.tfvars` 或 `.auto.tfvars.json` 结尾的文件。
- 对于 `.json` 结尾的文件，需要使用 JSON 语法定义。例如：
```bash
{
  "image_id": "ami-abc123",
  "availability_zone_names": ["us-west-1a", "us-west-1c"]
}
```


#### 环境变量
通过定义 `TF_VAR_` 为前缀的环境变量来指定输入变量。例如：
```bash
export TF_VAR_image_id=ami-abc123
export TF_VAR_availability_zone_names='["us-west-1b","us-west-1d"]'
```


### 输入变量优先级
- 若同时使用多种赋值方式时，同一个变量可能会被赋值多次。Terraform会使用新值覆盖旧值。Terraform 加载变量值的顺序是：
  1. 环境变量
 2. `terraform.tfvars` 文件（若存在）
 3. `terraform.tfvars.json` 文件（若存在）
 4. 所有的 `.auto.tfvars` 或 `.auto.tfvars.json` 文件，以字母顺序排序处理
 5. 通过 -var 或 -var-file 命令行参数传递的输入变量，按照在命令行参数中定义的顺序加载
- 若多种赋值方式均未能成功对变量赋值，那么 Terraform 会尝试使用默认值。对于没有定义默认值的变量，Terraform 会采用交互界面方式要求用户输入。对于某些 Terraform 命令，如果执行时带有 -input=false 参数禁用了交互界面传值方式，则会报错。

## 输出变量
输出变量使有关基础结构的信息在命令行上可用，并且可以供其他 Terraform 配置使用。输出值类似于传统编程语言中的返回值。


### 应用场景
- 子模块可以使用输出变量向父模块传递其资源属性。
- 根模块可以使用输出变量在运行 `terraform apply` 后在 CLI 输出中打印某些值。
- 使用远程状态时，其他配置可以通过 `terraform_remote_state` 数据源访问根模块输出。


### 定义输出变量
输出变量通过 `output` 块进行声明。例如：
```bash
output "instance_ip_addr" {
  value = tencentclould_instance.server.private_ip
}
```

#### 可选参数
- **description**
指定输出值的描述信息。例如：
```
output "instance_ip_addr" {
  value       = tencentclould_instance.server.private_ip
  description = "The private IP address of the main server instance."
}
```
- **sensitive**
在执行 `terraform plan` 和 `terraform apply` 命令时，在 CLI 中隐藏输出变量的值。
- **depends_on**
Terraform 会解析代码所定义的各种 data、resource 以及它们之间的依赖关系。例如，创建虚拟机所使用的 `image_id` 参数是通过 `data` 查询得到的，那么虚拟机实例就依赖于这个镜像的 `data`。Terraform 会首先创建 `data`，得到查询结果后，再创建虚拟机 `resource`。
一般来说，`data` 及 `resource` 之间的创建顺序是由 Terraform 自动计算的，不需要代码的编写者显式指定。但有时有些依赖关系无法通过分析代码得出，此时可以在代码中通过 `depends_on` 显式声明依赖关系。例如：
```
output "instance_ip_addr" {
  value       = tencentclould_instance.server.private_ip
  description = "The private IP address of the main server instance."

  depends_on = [
    # Security group rule must be created before this IP address could
    # actually be used, otherwise the services will be unreachable.
    tencentclould_security_group_rule.local_access,
  ]
}
```

## 本地变量
若需使用较复杂的表达式计算某一个值，并且反复使用时，则可赋予复杂表达式一个局部值后，再反复引用该局部值。您可将输入变量理解为函数的入参，输出值为函数的返回值，则局部值相当于函数内定义的局部变量。
 

### 本地变量的定义
本地变量通过 `locals` 块进行声明。例如：
```
locals {
  service_name = "forum"
  owner        = "Community Team"
}
```
同时，本地变量不限于文字常量，也包括本模块的其他变量（变量、资源属性或其他局部值）， 以便转换或组合使用它们。例如：
```
locals {
  # Ids for multiple sets of EC2 instances, merged together
  instance_ids = concat(tencentclould_instance.blue.*.id, tencentclould_instance.green.*.id)
}

locals {
  # Common tags to be assigned to all resources
  common_tags = {
    Service = local.service_name
    Owner   = local.owner
  }
}
```

### 使用本地变量
通过 `local.<NAME>` 表达式引用本地变量。例如：
```
resource "tencentclould_instance" "example" {
  # ...

  tags = local.common_tags
}
```
