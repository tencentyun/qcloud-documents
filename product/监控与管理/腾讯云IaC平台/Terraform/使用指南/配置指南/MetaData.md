Metadata 是 Terraform 支持的内置元参数，可以在 provider、resource、data、module 块中使用。主要包括：
- `depends_on`：显式声明依赖关系。
- `count`：创建多个资源实例。
- `for_each`：迭代集合，为集合中每一个元素创建一个对应的资源实例。
- `provider`：指定非默认 Provider 实例。
- `lifecycle`：自定义资源的生命周期行为。
- `dynamic`：构建重复内嵌块。

### depends_on
使用 `depends_on` 可以显式声明资源间由 Terraform 无法自动推导出的隐含依赖关系。适用于仅当资源间确实存在依赖关系，但彼此间没有数据引用的场景。例如：
```bash
variable "availability_zone" {
  default = "ap-guangzhou-6"
}

resource "tencentcloud_vpc" "vpc" {
  name       = "guagua_vpc_instance_test"
  cidr_block = "10.0.0.0/16"
}

resource "tencentcloud_subnet" "subnet" {
  depends_on = [tencentcloud_vpc.vpc]
  availability_zone = var.availability_zone
  name              = "guagua_vpc_subnet_test"
  vpc_id            = tencentcloud_vpc.vpc.id
  cidr_block        = "10.0.20.0/28"
  is_multicast      = false
}
```

### count
`count` 参数可以是任意自然数，Terraform 会创建 `count` 个资源实例，每一个实例都对应一个独立的基础设施对象，并且在执行 Terraform 代码时，这些对象是被分别创建、更新或者销毁的。例如：
```bash
resource "tencentcloud_instance" "foo" {
  availability_zone = var.availability_zone
  instance_name     = "terraform-testing"
  image_id          = "img-ix05e4px"
  ...
  count                      = 3
  tags = {
    Name = "Server ${count.index}"
  }
  ...
```
- **count.index**：代表当前对象对应的 count 下标索引（从0开始）
- **访问多资源实例对象**：`.`


### for_each
`for_each` 是 Terraform 0.12.6 引入的新特性。一个 `resource` 块不允许同时声明 `count` 与 `for_each`。`for_each` 参数可以是一个 map 或是一个 set(string)，Terraform 会为集合中每一个元素都创建一个独立的基础设施资源对象，并且和 count 一样，每一个基础设施资源对象在执行 Terraform 代码时都是独立创建、修改、销毁的。例如：
- **map**
```bash
resource "tencentcloud_cfs_access_group" "foo" {
  for_each = {
      test1_access_group = "test1"
      test2_access_group = "test2"
  }
  name        = each.key
  description = each.value
}
```
- **set(string)**
```bash
resource "tencentcloud_eip" "foo" {
  for_each = toset(["awesome_gateway_ip1", "awesome_gateway_ip2"])
  name = "awesome_gateway_ip"
}

```

### provider
若声明了同一类型 Provider 的多个实例，则在创建资源时可以通过指定 provider 参数选择要使用的 Provider 实例。若未指定 provider 参数，那么 Terraform 默认使用资源类型名中第一个单词所对应的 Provider 实例。例如：
```bash
provider "tencentcloud" {
  region = "ap-guangzhou"
  # secret_id = "my-secret-id"
  # secret_key = "my-secret-key"
}

provider "tencentcloud" {
  alias  = "tencentcloud-beijing"
  region = "ap-beijing"
  # secret_id = "my-secret-id"
  # secret_key = "my-secret-key"
}

resource "tencentcloud_vpc" "foo" {
    name         = "ci-temp-test-updated"
    cidr_block   = "10.0.0.0/16"
    dns_servers  = ["119.29.29.29", "8.8.8.8"]
    is_multicast = false

    tags = {
        "test" = "test"
    }
    provider     = tencentcloud.tencentcloud-beijing
}
```

### lifecycle
每个资源实例都具有创建 、更新和销毁三个阶段，而 `lifecycle` 块可指定一个不同的行为方式。Terraform 支持如下几种 `lifecycle`：
<dx-accordion>
::: create_before_destroy
默认情况下，当 Terraform 需要修改一个由于服务端 API 限制导致无法直接升级的资源时，Terraform 会删除现有资源对象，再用新的配置参数创建一个新的资源对象取代。`create_before_destroy` 参数可以修改这个行为，使 Terraform 首先创建新对象，只有在新对象成功创建并取代老对象后再销毁老对象。例如：
```bash
lifecycle {
  create_before_destroy = true
}
```
许多基础设施资源需具备唯一的名字或标识属性，而新老对象并存时也需符合该约束。有些资源类型具备特别的参数，可为每个对象名称添加一个随机前缀以防止冲突，而 Terraform 不能默认采用这种行为，您需在使用` create_before_destroy` 前解每一种资源类型的该类约束。


:::
::: prevent_destroy
`prevent_destroy` 参数是一个保险措施，只要它被设置为 true 时，Terraform 会拒绝执行任何可能会销毁该基础设施资源的变更计划。`prevent_destroy` 参数可以预防意外删除关键资源，例如错误地执行了 terraform destroy，或者是意外修改了资源的某个参数，导致 Terraform 决定删除并重建新的资源实例。
在 resource 块内声明了 `prevent_destroy = true` 会导致无法执行 terraform destroy。例如：
```bash
lifecycle {
  prevent_destroy = true
}
```
需谨慎使用 `prevent_destroy` 参数，需要注意的是，该措施无法防止在删除 resource 块后 Terraform 删除相关资源，因对应的 `prevent_destroy = true` 声明也被一并删除了。

:::
::: ignore_changes
默认情况下，Terraform 检测到代码描述的配置与真实基础设施对象之间有任何差异时，都会计算一个变更计划来更新基础设施对象，使之符合代码描述的状态。在一些非常罕见的场景下，实际的基础设施对象会被 Terraform 之外的流程所修改，会 Terraform 不停地尝试修改基础设施对象以弥合和代码之间的差异。此时，可以通过设定 `ignore_changes` 来指示 Terraform 忽略某些属性的变更。`ignore_changes` 的值定义了一组在创建时需要按照代码定义的值来创建，但在更新时不需要考虑值的变化的属性名。例如：
```bash
resource "tencentcloud_instance" "foo" {
...
lifecycle {
  ignore_changes = [
    # Ignore changes to tags, e.g. because a management agent
    # updates these based on some ruleset managed elsewhere.
    tags,
  ]
}
```
:::
</dx-accordion>
 

### dynamic
在例如 resource 的顶级块中，通常只能以类似 `name = expression` 的形式进行一对一的赋值。一般情况下均可使用该赋值形式，但当某些资源类型包含了可重复的内嵌块时，无法使用表达式循环赋值。例如：
```bash
resource "tencentcloud_tcr_instance" "foo" {
  name                  = "example"
  instance_type		    = "basic"
  open_public_operation = true
  security_policy {
    cidr_block = "10.0.0.1/24"
  }
  security_policy {
    cidr_block = "192.168.1.1/24"
  }
}

```
此时，可使用 `dynamic` 块来动态构建重复且类似 security_policy 的内嵌块。例如：
```bash
resource "tencentcloud_tcr_instance" "foo" {
  name                  = "example"
  instance_type         = "basic"
  open_public_operation = true
  dynamic "security_policy" {
    for_each = toset(["10.0.0.1/24", "192.168.1.1/24"])
    content {
      cidr_block = security_policy.value
    }
  }
}
```

`dynamic` 可以在 resource、data、provider 和 provisioner 块内使用。`dynamic` 块类似于 for 表达式，它产生的是内嵌块，可以迭代一个复杂类型数据并为每一个元素生成相应的内嵌块。在上述示例中：

- `dynamic` 的标签（也就是 `"security_policy"`）确定了要生成的内嵌块种类。
- `for_each` 参数提供了需要迭代的复杂类型值。
- `iterator` 参数（可选）设置了表示当前迭代元素的临时变量名。若未设置 `iterator`，则临时变量名默认为 `dynamic` 块的标签（即 `security_policy`）。
- `labels` 参数（可选）是一个表示块标签的有序列表，用来按次序生成一组内嵌块。有 `labels` 参数的表达式中可使用临时的 `iterator` 变量。
- 内嵌的 `content` 块定义了要生成的内嵌块的块体。可以在 `content` 块内部使用临时的 `iterator` 变量。

`for_each` 参数：
- 由于 `for_each` 参数可以是集合或者结构化类型，可使用 for 表达式或展开表达式来转换一个现有集合的类型。
- `for_each` 的值必须是不为空的 map 或者 set。如需根据内嵌数据结构或者多个数据结构的元素组合来声明资源实例集合，可使用 Terraform 表达式和函数来生成合适的值。

`iterator` 变量（上述示例中的 setting）具备以下属性：
- key：若迭代容器是 map，则 key 为当前元素的键。若迭代容器是 list，则 key 为当前元素在 list 中的下标序号。若是由 `for_each` 表达式产出的 set，则 key 和 value 相等，此时不应使用 key。
- value：当前元素的值。一个 `dynamic` 块只能生成属于当前块定义过的内嵌块参数。无法生成例如 lifecycle、provisioner 这样的元参数，Terraform 必须在确保对这些元参数求值的计算是成功的。



