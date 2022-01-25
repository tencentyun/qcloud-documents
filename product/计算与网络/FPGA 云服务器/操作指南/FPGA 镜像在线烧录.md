## 操作场景
本文介绍如何使用 [在线烧录 FPGA 镜像](https://cloud.tencent.com/document/product/213/68353) API 接口进行 FPGA 镜像在线烧录。


## 操作步骤

### 配置存储桶
1. 参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)，创建一个用于存放 FPGA 镜像文件的存储桶。
2. 单击存储桶 ID，进入存储桶配置页面。
3. 选择左侧菜单栏中的**权限管理** > **Policy权限设置**，单击 “Policy权限设置”中的**添加策略**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9e29fc7e82976bdb539bb8920fc9d874.png)
4. 在弹出的“添加策略”窗口中进行配置：
   1. 在“选择模板”步骤中，进行以下配置。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e4f0405e9cd1e1d1a34fbb52a4bfa264.png)
    - **被授权用户**：选择**指定用户**。
    - **资源范围**：选择**整个存储桶**。
    - **选择模板**：选择“只读对象（含列出对象列表）”。
   2. 单击**下一步**，完成权限配置。
   3. 在“配置策略”步骤中，进行以下配置。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/330610c96baa4bc46b33251d2d8c503f.png)
    - **效力**：选择“允许”。
    - **用户**：选择“云服务 - 腾讯云 CVM”。
    - **资源**：选择“整个存储桶”。
    - **操作**：选择“读操作（含列出对象列表）”。
5. 单击**完成**，完成权限配置。


### 上传镜像文件并获取 COS URL
1. 参考 [上传对象](https://cloud.tencent.com/document/product/436/13321)，将需烧录的 FPGA 镜像文件上传到已配置的存储桶。
<dx-alert infotype="notice" title="">
目前仅支持 xclbin 格式的 FPGA 镜像文件。
</dx-alert>
2. 单击已上传的镜像文件所在行右侧的**详情**，进入对象详情页。
3. “基本信息”的“对象地址”即为需获取的 COS URL。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7230412eb78e32c72af41dec9028ff11.png)


### 进行烧录
1. 通过 [API Inspector 工具](https://console.cloud.tencent.com/cvm/instance/index?rid=1)、[命令行工具 TCCLI](https://cloud.tencent.com/document/product/440) 或其他工具调用腾讯云 [在线烧录 FPGA 镜像](https://cloud.tencent.com/document/product/213/68353) API 接口进行烧录。
2. 您在发起烧录流程后，需关注以下事项：
 - 可调用 [查看实例列表](https://cloud.tencent.com/document/product/213/15728) 接口，通过返回字段 `LatestOperation`  及 `OperationState`（当 `LatestOperation` 为 `ProgramFpgaImage` 时，`OperationState` 表示当前的烧录情况），获取 FPGA 镜像烧录流程的状态。
<dx-alert infotype="explain" title="">
由于 [查看实例列表](https://cloud.tencent.com/document/product/213/15728) 接口仅支持查询实例最近一次的操作状态，若您在发起镜像烧录后进行了其他实例操作，则可能无法获取镜像烧录流程的状态。后续可使用云审计查看镜像烧录状态，详情请参见 [查看操作记录事件详情](https://cloud.tencent.com/document/product/629/56259)。
</dx-alert>
 - 由于目前 xilinx FPGA 卡的 user pf 和 mgmt pf 不互通，在发起烧录流程之后，还需要在子机内部执行以下命令，重新加载 xocl 驱动才可将 FPGA 镜像信息更新到 FPGA shell。
 ```
 modprobe -r xocl && modprobe xocl
 ```
