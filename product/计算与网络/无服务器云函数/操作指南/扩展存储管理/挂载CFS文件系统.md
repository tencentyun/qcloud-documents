## 操作场景

[腾讯云文件存储 CFS](https://cloud.tencent.com/product/cfs) 提供可扩展的共享文件存储服务，可与腾讯云服务器、容器服务或者批量处理等服务搭配使用。CFS 符合标准的 NFS 文件系统访问协议，为多个计算节点提供共享的数据源，支持弹性容量和性能的扩展，现有应用无需修改即可挂载使用，是一种高可用、高可靠的分布式文件系统，适合于大数据分析、媒体处理和内容管理等场景。
CFS 成本低廉，采用按量计费模式，以小时为计费周期，您只需为实际使用的存储空间付费。CFS 计费详情请参见 [计费概述](https://cloud.tencent.com/document/product/582/9553)。

腾讯云云函数 SCF 支持与 CFS 无缝集成，只需进行相关配置，您的函数即可轻松访问存储在 CFS 文件系统中的文件。使用 CFS 的优势如下：
- 函数执行空间不受限。
- 多个函数可共用一个文件系统，实现文件共享。

## 操作步骤

### 关联授权策略
>!如需使用 CFS 功能，云函数需要能够操作您 CFS 资源的权限。

请参考以下步骤为账号进行授权操作：
1. 请参考 [修改角色](https://cloud.tencent.com/document/product/598/19389)，为 `SCF_QcsRole` 角色关联 `QcloudCFSReadOnlyAccess` 策略。关联成功则如下图所示：
如您使用的账号未进行该操作，则可能出现函数无法保存，CFS 相关功能无法使用等问题。
![](https://main.qcloudimg.com/raw/dec5c3f4d54aeeb25fce8450f584afa4.png)
2. 如您使用账号为子账号，则请联系主账号并参考 [子用户权限设置](https://cloud.tencent.com/document/product/598/36256) 为您的子账号关联 `QcloudCFSReadOnlyAccess` 策略。关联成功则如下图所示：
如您使用的子账号未进行该操作，则可能出现无法使用 CFS 相关功能的问题。
![](https://main.qcloudimg.com/raw/4e83ee59c61f86484b3f56b356ac32d5.png)




### 创建私有网络 VPC
请参考 [快速搭建 IPv4 私有网络](https://cloud.tencent.com/document/product/215/30716) 完成 VPC 创建。

### 创建 CFS 资源
请参考 [创建 CFS 文件系统](https://cloud.tencent.com/document/product/582/9132) 完成创建操作。
>!目前云函数仅支持添加网络类型为 VPC 的 CFS 文件系统作为挂载点。请在创建的 CFS 文件系统时，选择与函数所在相同的 VPC，以确保网络能够互通。

### 挂载并使用 CFS 文件系统
1. 登录云函数控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
2. 在“函数服务”页面，选择需配置的函数名。
3. 在“函数管理”页面的**函数配置**页签中，单击右上角的**编辑**。
4. 在“私有网络”中，勾选启用并选择 CFS 文件系统所在的 VPC。如下图所示：
![](https://main.qcloudimg.com/raw/b2e88b9fcb5e5045cc9951d75f498eca.png)
5. 在“文件系统”中勾选启用，并按照以下信息进行挂载。如下图所示：
![](https://main.qcloudimg.com/raw/5df4693e17f05892edb610e04f420de2.png)
 - **用户ID**及**用户组ID**：这两个值等同于 CFS 文件系统中的用户及用户组。云函数默认用户及用户组值为 10000，来操作您的 CFS 文件系统。请按需设置文件的拥有者及相应组的权限，并确保您的 CFS 文件系统已配置相应权限。详情请参见 [权限设置](https://cloud.tencent.com/document/product/582/10951)。
 - **远程目录**：为云函数需访问 CFS 文件系统的远端目录，由文件系统和远端目录两部分组成。
 -  **本地目录**：为本地文件系统的挂载点。您可使用 `/mnt/` 目录的子目录挂载 CFS 文件系统。
 -  **文件系统ID**：在下拉列表中选择需挂载的文件系统。
 -  **挂载点ID**：在下拉列表中选择对应文件系统的挂载点 ID。
6.  单击页面下方的**保存**即可完成配置。
您可执行以下函数代码，开始使用 CFS 文件系统。
```
'use strict';
var fs = requiret('fs');
exports.main_handler = async (event, context) => {
      await fs.promises.writeFile('/mnt/myfolder/filel.txt', JSON.stringify(event)); 
      return event;
};
```

### SCF 使用 CFS 文件系统性能测试
您可以使用此 [脚本](https://github.com/tencentyun/scf_cfs_demo) 测试 SCF 使用 CFS 时的性能。

