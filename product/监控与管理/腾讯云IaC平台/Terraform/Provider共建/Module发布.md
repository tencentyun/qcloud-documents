## 操作场景

Module 是 Terraform 组合多种资源的配置形态。在部分多资源场景下，使用 Module 能够更好地抽象业务，减少配置成本。您可将 Github 中的 Modules 发布到 [terraform 仓库](https://registry.terraform.io/)。本文介绍如何创建及发布 Terraform TencentCloud Module。


## 操作步骤

### 创建公共 Module
在 GitHub 中新建代码仓库。
- 命名格式为 `terraform-<PROVIDER>-<NAME>`，例如 [terraform-tencentcloud-vpc](https://github.com/terraform-tencentcloud-modules/terraform-tencentcloud-vpc)。
- 基本 Module 需包含以下文件：
```
.
├── main.tf # 编写模块资源
├── variables.tf # 声明模块变量
├── outputs.tf # 声明模块输出
├── LICENCE # 声明许可
└── README.md # 自述文件
```
<dx-alert infotype="explain" title="">
建议添加 example 目录，存放该模块引入和使用示例。您可参考 [examples](https://github.com/terraform-tencentcloud-modules/terraform-tencentcloud-vpc/tree/master/examples) 进行添加。
</dx-alert>


### 发布 Module 
1. 登录 [registry.terraform.io](https://registry.terraform.io/)，选择页面右上角的 **Publish**，并在下拉列表中单击 **Module**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/21b9530913836f7264352c09d27f25d1.png)
2. 在页面中展开 “Select Repository on GitHub” 下拉列表，可在列表中查看个人账户下有管理权限的 Modules 仓库，选择需发布的 Module。如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/8d0bd74baf57150f418e4639663695b6.png" style="width:60%"/> <dx-alert infotype="notice" title="">
Module 可以使用个人 GitHub 仓库发布。若仓库名称符合 `terraform-tencentcloud-<NAME>`，则该 Modules 也会收录在 tencentcloud 的 Modules 中。
</dx-alert>
3. 勾选 “ I agree to the Terms of Use.”后，单击 **PUBLISH MODULE**。
4. 该仓库将会在几分钟后，自动同步到 terraform registry 中。如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/ee190688dfae59967dd84f22450eee4c.png" style="width:60%"/>
