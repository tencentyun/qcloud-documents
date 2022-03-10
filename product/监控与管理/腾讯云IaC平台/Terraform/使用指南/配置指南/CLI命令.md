本文介绍如何使用 Terraform 命令行工具应用 Terraform 代码和管理基础设施。


## 基本功能

### 查看命令列表
Terraform 提供了丰富的命令行操作，可以在命令行输入 `terraform` 查看完整命令列表。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5f54e51ba06d4a64625c2270bd160e82.jpg)
对于特定的子命令可以通过 `-help` 查看详细用法，例如需要查看 `validate` 子命令的完整用法，可以使用命令 `terraform validate -help`。

### 切换工作目录
运行 Terraform 时通常需切换当前工作目录到包含有想要执行的根模块 `.tf` 代码文件的目录下（使用 `cd` 命令），切换后 Terraform 才能够自动发现要执行的代码文件以及参数文件。

#### 全局参数 -chdir
在某些场景下，例如将 Terraform 封装进某些自动化脚本时，从其他路径直接执行特定路径下的根模块代码将十分便捷。可使用全局参数 `-chdir=...` 实现这一目的，您可在任意子命令的参数中使用该参数指定要执行的代码路径。例如：
```
terraform -chdir=environments/production apply
```
`-chdir` 参数指引 Terraform 在执行具体子命令之前切换工作目录，使用该参数后 Terraform 将会在指定路径下读写文件，而非当前工作目录下的文件。
在以下两种场景时，指定 `-chdir` 参数将无效，Terraform 仍会使用当前的工作目录：
- Terraform 处理命令行配置文件中的设置而非执行某个具体的子命令时，该阶段发生在解析 `-chdir` 参数之前。
- 若需使用当前工作目录下的文件作为配置的一部分时，可通过代码中的 `path.cwd` 变量获得对当前工作路径的引用。此时不使用 `-chdir` 参数指定路径， 可通过 `path.root` 来获取代表根模块所在的路径。


### 自动补全
若使用 `bash` 或 `zsh`，则可通过以下命令获取自动补全的支持。
```
terraform -install-autocomplete
```
如需卸载自动补全，可执行以下命令。
```
terraform -uninstall-autocomplete
```

## 基本命令

<dx-accordion>
::: terraform init
`terraform init` 命令用于初始化一个包含 Terraform 配置文件的工作目录。在编写 Terraform 代码或是克隆了 Terraform 项目后应首先执行该命令。

- **用法**
`terraform init [options]`
该命令执行一系列不同的初始化步骤来初始化当前目录。即使多次运行也是安全的，若报错也不会删除配置文件或者状态信息。
- **常用参数**
 - `-input=true`：是否在取不到输入变量值时提示用户输入。
 - `-lock=false`：是否在运行时锁定状态文件。
 - `-lock-timeout=\`：尝试获取状态文件锁时的超时时间，默认为0，意为一旦发现锁已被其他进程获取立即报错。
 - `-no-color`：禁止输出中包含颜色。
 - `-upgrade`：是否升级模块代码以及插件。
- **拷贝源模块**
默认情况下，`terraform init` 命令认为工作目录存在配置并尝试初始化。您也可以通过 `-from-module=MODULE-SOURCE` 选项在空白工作目录下运行 `terraform init`，则会先将指定模块拷贝到当前目录再执行初始化操作，这种特殊的使用方式适用于以下两种场景：
 - 对于 source 对应的版本控制系统，可使用该方式签出指定版本代码并为它初始化工作目录。
 - 如果模块源指向的是一个样例项目，该方式可以把样例代码拷贝到本地目录以便后续基于样例编写新的代码。
如果是常规运行操作建议用独立的步骤从版本控制系统中签出代码，使用版本控制系统所属的工具。
- **Backend 初始化**
在执行 init 时，会分析根模块代码以寻找 Backend 配置，并使用给定的配置设定初始化 Backend 存储。
若在已经初始化 Backend 后重复执行 init 命令，会更新工作目录以使用新的 Backend 设置。init 可能会根据改变的内容提示用户是否确认进行状态迁移。您可按需使用以下参数：
 - `-force-copy`：可跳过提示直接确认迁移状态。
 - `-reconfigure`：使 init 忽略任何现有配置，防止任何状态迁移。
 - `-backend=false`：可跳过 Backend 配置。
 注意某些 init 步骤需要已经被初始化的 Backend，推荐只在已经初始化过 Backend 后使用该参数。
 - `-backend-config`：可以用来动态指定 Backend 配置。
- **初始化子模块**
init 会搜索 module 块，并通过 source 参数取回模块代码。您可按需使用以下参数：
 - `-upgrade`：将所有模块升级到最新版本的代码。默认情况下，模块安装之后重新运行 init 命令会继续安装上次执行 init 后新增的模块，但不会修改已被安装的模块。
 - `-get=false`：可跳过子模块安装步骤。
 需注意其他 init 步骤需要模块树完整，建议只在成功安装过模块以后使用该参数。
- **插件安装**
参数说明如下：
 - `-upgrade`：将之前所有已安装的插件升级到符合 version 约束的最新版本，此参数对手动安装的插件无效。
 - `-get-plugins=false`：跳过插件安装。Terraform 会使用已安装在当前工作目录下或是插件缓存路径中的插件。如果这些插件不足以覆盖需求，那么 init 会失败。
 - `-plugin-dir=PATH`：跳过插件安装，只从指定目录加载插件。该参数会跳过用户插件目录以及所有当前工作目录下的插件。要在使用过该参数后恢复默认行为，请使用 `-plugin-dir=""` 参数重新执行 init。
 - `-verify-plugins=false`：在下载插件后跳过验证签名（不推荐）。官方插件都会经 HashiCorp 签名，Terraform 会验证这些签名。可以使用该参数跳过签名验证（Terraform 不会验证手动安装的插件的签名）。


:::
::: terraform plan
`terraform plan` 命令用来创建变更计划。Terraform 会先运行一次 refresh（该行为也可以被显式关闭）：
 - 若检测到变更后，可决定要执行的变更使现有状态迁移到代码描述的期待状态。您还可使用可选参数 `-out`，将变更计划保存在一个文件中，以便日后使用 `terraform apply` 命令来执行该计划。
 - 若未检测到任何变更，则会提示无任何需执行的变更。

该命令可以方便地审查状态迁移的所有细节，而不会实际更改现有资源以及状态文件。例如，在将代码提交到版本控制系统前可以先执行 `terraform plan`，确认变更行为符合预期。
 
- **用法**
`terraform plan [options]`
默认情况下，plan 命令不需要参数，使用当前工作目录下的代码和状态文件执行 refresh。
- **常用参数**：
 - `-compact-warnings`：如果 Terraform 仅生成了告警信息而无错误信息，则以只显示消息总结的精简形式展示告警。
 - `-destroy`：生成销毁所有资源的计划。
 - `-detailed-exitcode`：当命令退出时返回一个详细的返回码。如果有该参数，那么返回码将会包含更详细的含义：
   - 0 = 成功的空计划（没有变更）
   - 1 = 错误
   - 2 = 成功的非空计划（有变更）
 - `-input=true`：在取不到值的情况下是否提示用户给定输入变量值。
 - `-lock=true`：与 apply 类似。
 - `-lock-timeout=0s`：与 apply 类似。
 - `-no-color`：关闭彩色输出。
 - `-out=path`：将变更计划保存到指定路径下的文件中，之后可使用 `terraform apply` 执行该计划。
 - `-parallelism-n`：限制 Terraform 遍历图的最大并行度，默认值为10。
 - `-refresh=true`：计算变更前先执行 refresh。
 - `-state=path`：状态文件的位置，默认为 `"terraform.tfstate"`。如果启用了远程 Backend 则该参数设置无效。
 - `-target=resource`：目标资源的地址，该参数可反复声明，用以对基础设施进行部分更新。
 - `-var 'foo=bar'`：与 apply 类似。
 - `-var-file=foo`：与 apply 类似。
- **部分更新**
使用 `-target` 参数可以使 Terraform 专注于一部分的资源。可以使用资源地址来标记这个集合，资源地址说明如下：
 - 若给定地址能够定位到一个资源，那么只该资源会被标记。如果该资源使用了 `count` 参数而未给定具体访问下标，则该资源所有实例都会被标记。
 - 如果给定地址定位到了模块，那么该模块内所有资源及其内嵌模块资源都会被标记。
<dx-alert infotype="explain" title="">
标记部分资源并计算更新计划的能力针对较罕见场景，例如，从之前的错误中恢复或绕过某些 Terraform 的设计限制。对于常规操作不推荐使用 `-target` 参数，因为它会造成无法检测的配置漂移以及使人无法从代码推导出当前真实的状态。
</dx-alert>
- **安全警告**
被保存的变更计划文件（使用 `-out` 参数）内部可能含有敏感信息，Terraform 本身并不会加密计划文件。如需移动或保存该文件，强烈建议您自行加密。Terraform 预期将增强计划文件的安全性，您可持续关注。


:::
::: terraform apply
`terraform apply` 为 Terraform 中最重要的命令。apply 命令用来生成执行计划（可选）并执行，使得基础设施资源状态符合代码的描述。

- **用法**
`terraform apply [options] [dir-or-plan]`
默认情况下，apply 会扫描当前目录下的代码文件，并执行相应的变更。也可以通过参数指定其他代码文件目录。
在设计自动化流水线时也可以显式分为创建执行计划、使用 apply 命令执行该执行计划两个独立步骤。如果没有显式指定变更计划文件，terraform apply 会自动创建一个新的变更计划，并提示用户是否批准执行。如果生成的计划不包含任何变更，terraform apply 会立即退出，不会提示用户输入。

- **常用参数**
 - `-backup-path`：保存备份文件的路径。默认等于 `-state-out` 参数后加上` ".backup"` 后缀。设置为 "-" 可关闭备份（不推荐）。
 - `-compact-warnings`：如果 Terraform 仅生成了告警信息而无错误信息，则显示消息仅以总结的精简形式展示告警。
 - `-lock=true`：执行时是否先锁定状态文件。
 - `-lock-timeout=0s`：尝试重新获取状态锁的间隔。
 - `-input=true`：在无法获取输入变量的值时是否提示用户输入。
 - `-auto-approve`：跳过交互确认步骤，直接执行变更。
 - `-no-color`：禁用输出中的颜色。
 - `-parallelism=n`：限制 Terraform 遍历图时的最大并行度，默认值为10。
 - `-refresh=true`：指定变更计划及执行变更前是否先查询记录的基础设施对象现在的状态以刷新状态文件。如果命令行指定了要执行的变更计划文件，该参数设置无效。
 - `-state=path`：保存状态文件的路径，默认值 `"terraform.tfstate"`。如果使用了远程 Backend 则该参数设置无效。该参数不影响其他命令，例如执行 init 时会找不到它设置的状态文件。如果要使所有命令都可以使用同一个特定位置的状态文件，请使用 Local Backend。
 - `-state-out=path`：写入更新的状态文件的路径，默认情况使用 `-state` 的值。该参数在使用远程 Backend 时设置无效。
 - `-target=resource`：通过指定资源地址指定更新目标资源。
 - `-var 'foo=bar'`：设置一组输入变量的值。该参数可以反复设置以传入多个输入变量值。
 - `-var-file=foo`：指定一个输入变量文件。


:::
::: terraform destroy
`terraform destroy` 命令可以用来销毁并回收所有 Terraform 管理的基础设施资源。

#### **用法**
`terraform destroy [options]`
Terraform 管理的资源会被销毁，在执行销毁动作前会通过交互式界面征求用户的确认。该命令可以接收所有 apply 命令的参数，但不可以指定 plan 文件。
 - 若 `-auto-approve` 参数为 true，则不会征求用户确认直接销毁。
 - 若使用 `-target` 参数指定了某项资源，那么不但会销毁该资源，同时也会销毁一切依赖于该资源的资源。

<dx-alert infotype="explain" title="">
`terraform destroy` 将执行的所有操作都可以随时通过执行 `terraform plan -destroy` 命令来预览。
</dx-alert>


:::
::: terraform graph
`terraform graph` 命令用于生成代码描述的基础设施或是执行计划的可视化图形。它的输出是 DOT 格式，可以使用 GraphViz 来生成图片。

- **用法**
`terraform graph [options] [DIR]`
该命令生成 DIR 路径下的代码锁描述的 Terraform 资源的可视化依赖图（如果 DIR 参数缺省则使用当前工作目录）。
- **常用参数**
 - `-type`：用来指定输出的图表的类型。Terraform 为不同的操作创建不同的图。代码文件默认类型为 `"plan"`，变更计划文件默认类型为 `"apply"`。
 - `-draw-cycles`：用彩色的边高亮图中的环，可以帮助分析代码中的环错误（Terraform 禁止环状依赖）。
 - `-type=plan`：生成图表的类型。包含 plan、plan-destroy、apply、validate、input、refresh。
- **创建图片文件**
`terraform graph` 命令输出的是 DOT 格式的数据，可通过以下命令 GraphViz 转换为图形文件：
```
terraform graph | dot -Tsvg > graph.svg
```
若未安装 GraphViz，您可通过以下命令进行安装：
 - CentOS：`yum install graphviz`
 - Windows：`choco install graphviz`
 - Mac：`brew install graphviz`
得到输出的图片类似下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/dfa0f17c2481d3ac81b94433af3a64af.png)

:::
::: terraform show
`terraform show` 命令从状态文件或是变更计划文件中打印可读的输出信息。这可以用来检查变更计划以确定所有操作都是预期的，或是审查当前的状态文件。

<dx-alert infotype="notice" title="">
可通过添加 `-json` 参数输出机器可读的 JSON 格式输出，但输出时所有标记为 sensitive 的敏感数据都会以明文形式被输出。
</dx-alert>

-  **用法**
`terraform show [options] [path]`
- **常用参数**
 - `path`：指定一个状态文件或是变更计划文件。如果没有给定 path，那么会使用当前工作目录对应的状态文件。
 - `-no-color`：与 apply 类似。
 - `-json`：以 JSON 格式输出。
- **JSON 格式输出**
可以使用 `terraform show -json` 命令打印 JSON 格式的状态信息。如果指定了一个变更计划文件，`terraform show -json` 会以 JSON 格式记录变更计划、配置以及当前状态。

:::
::: terraform import
`terraform import` 命令用来将已经存在的资源对象导入 Terraform。

若存在已有一组运行着的基础设施资源，但未使用 Terraform 来构建和管理。此时已为其编写了对应的 Terraform 代码，则可使用 `terraform import` 将资源对象“导入”到 Terraform 状态文件中去。

- **用法**
`terraform import [options] ADDRESS ID`
`terraform import` 会根据资源 ID（ID 取决于被导入的资源对象的类型）找到相应资源，并将其信息导入到状态文件中 ADDRESS 对应的资源上。ADDRESS 必须符合在资源地址中描述的合法资源地址格式，`terraform import` 不但可以把资源导入到根模块中，也可以导入到子模块中。
<dx-alert infotype="notice" title="">
Terraform 中每个资源对象都仅对应唯一一个实际的基础设施对象，需避免将同一个对象导入到两个以及更多不同的地址上，这会导致 Terraform 产生不可预测的行为。
</dx-alert>
- **常用参数**
 - `-backup=path`：生成状态备份文件的地址，默认情况下是 `-state-out` 路径加 `".backup"` 后缀名。设置为"-"可以关闭备份（不推荐）。
 - `-config=path`：包含含有导入目标的 Terraform 代码的文件夹路径。默认为当前工作目录。
 - `-input=true`：是否允许提示输入 Provider 配置信息。
 - `-lock=true`：如果 Backend 支持，是否锁定状态文件。
 - `-lock-timeout=0s`：重试获取状态锁的间隔。
 - `-no-color`：如果指定，则不会输出彩色信息。
 - `-parallelism=n`：限制 Terraform 遍历图的最大并行度，默认值为10。
 - `-state=path`：要读取的状态文件的地址。默认为配置的 Backend 存储地址，或是 `"terraform.tfstate"` 文件。
 - `-state-out=path`：指定修改后的状态文件的保存路径，默认情况下覆盖源状态文件。使用该参数可以生成一个新的状态文件，避免破坏现有状态文件。
 - `-var 'foo=bar'`：通过命令行设置输入变量值。
 - `-var-file=foo`：类似 apply 命令。
- **Provider 配置**
Terraform 会尝试读取要导入的资源对应的 Provider 的配置信息。如果找不到相关 Provider 的配置，Terraform 会提示输入相关的访问凭据。您可输入凭据，也可通过环境变量来配置访问凭据。
Terraform 在读取 Provider 配置时唯一的限制是不能依赖于“非输入变量”的输入。例如，Provider 配置不能依赖于数据源的输出。
若您需导入腾讯云资源，Terraform 会使用 `secret_id` 及 `secret_key` 输入变量来配置 tencentcloudProvier。配置文件如下：
```
variable "secret_id" {}
variable "secret_key" {}

provider "tencentcloud" {
      secret_id = var.secret_id
      secret_key = var.secret_key
    }
```
配置完成后，您可执行类似如下命令，导入资源：
```
terraform import tencentcloud_instance.foo ins-2s6ewubw
```


:::
</dx-accordion>






