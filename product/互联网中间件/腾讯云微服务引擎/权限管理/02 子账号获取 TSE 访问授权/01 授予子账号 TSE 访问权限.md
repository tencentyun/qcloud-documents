## CAM 基本概念

主账号通过给子账号绑定策略实现授权，策略设置可精确到 **[API，资源，用户/用户组，允许/拒绝，条件]** 维度。

### 账号体系

- **主账号**：拥有腾讯云所有资源，可以任意访问其任何资源。
- **子账号**：包括子用户和协作者。
  - **子用户**： 由主账号创建，完全归属于创建该子用户的主账号。
  - **协作者**：本身拥有主账号身份，被添加作为当前主账号的协作者，则为当前主账号的子账号之一，可切换回主账号身份。
- **身份凭证**：包括登录凭证和访问证书两种，**登录凭证**指用户登录名和密码，**访问证书**指云 API 密钥（SecretId 和 SecretKey）。

### 资源与权限

- **资源**：资源是云服务中被操作的对象，如一个云服务器实例、COS 存储桶、VPC 实例等。
- **权限**：权限是指允许或拒绝某些用户执行某些操作。默认情况下，**主账号拥有其名下所有资源的访问权限**，而**子账号没有主账号下任何资源的访问权限**。
- **策略**：策略是定义和描述一条或多条权限的语法规范。**主账号**通过将**策略关联**到用户/用户组完成授权。



## 子账号使用 TSE

在对子账户进行授权前，请确保主账号已完成获取访问授权，并已拥有 TSE_QCSRole 的角色，详情参考 [主账号获取访问授权](https://cloud.tencent.com/document/product/649/16869)。

子账号使用 TSE 时，需要对两方面进行授权：

1. 使用 TSE 的过程中，涉及到访问用户其他的云产品资源（VPC、TKE 等），如查看用户子网所在的可用区信息等场景。因此，需要授予子账号访问其他云产品的权限，详细操作参见 [步骤1：授予子账号访问其他云产品的权限](#step1)。
2. 子账号使用 TSE 还需要获得读写权限，详细操作参见 [步骤2：授予子账号使用 TSE 的权限](#step2)。

>? 使用云原生 API 网关时，子账号授权操作请参见 [子账号获取云原生 API 网关权限](https://cloud.tencent.com/document/product/1364/72786)。



[](id:step1)

### 步骤1：授予子账号访问其他云产品的权限

#### 新建自定义访问其他云产品策略

1. 使用主账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam)。
2. 在左侧导航栏选择**策略**，单击**新建自定义策略**。
3. 在选择创建策略方式的弹出框中，选择**按策略语法创建**，进入按策略语法创建页。
4. 在 [按策略语法创建页](https://console.cloud.tencent.com/cam/policy/createV2) 中，选择**空白模板**，并单击**下一步**。
5. 您可参照下方调用接口表格和策略语法，根据实际需要，授予子账号合适的其他云产品调用权限，生成自定义策略，填写所有信息后单击**完成**。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/a00b7bfbb82ad3ca43d73ff1b09988a7.jpg">
   TSE 平台使用中涉及到以下云产品的调用，主账号需要对子账号进行单独授权才能保证对应 TSE 产品功能的使用。自定义策略中 TSE 中涉及到的对云产品的调用如下：[](id:msg)
<table>
<thead>
<tr>
<th>云产品</th>
<th>接口名</th>
<th>接口作用</th>
<th>影响到 TSE 平台的操作</th>
</tr>
</thead>
<tbody><tr>
<td>云服务器（CVM）</td>
<td>DescribeZones</td>
<td>查询可用区</td>
<td>创建实例时查看子网所在可用区</td>
</tr>
<tr>
<td>私有网络（VPC）</td>
<td>DescribeVpcs</td>
<td>查询 VPC 列表</td>
<td>创建实例时选择实例访问地址所属 VPC</td>
</tr>
<tr>
<td>私有网络（VPC）</td>
<td>DescribeSubnets</td>
<td>查询 VPC 列表</td>
<td>创建实例时选择实例访问地址所属子网</td>
</tr>
<tr>
<td>云监控（Monitor）</td>
<td>GetMonitorData</td>
<td>拉取指标监控数据</td>
<td>查看 TSE 中监控数据</td>
</tr>
<tr>
<td>云监控（Monitor）</td>
<td>DescribeDashboardMetricData</td>
<td>拉取指标监控数据</td>
<td>查看 TSE 中监控数据</td>
</tr>
<tr>
<td>容器服务（TKE）</td>
<td>DescribeClusters</td>
<td>拉取集群信息</td>
<td>TSE 北极星网格绑定 K8S 集群</td>
</tr>
<tr>
<td>容器服务（TKE）</td>
<td>DescribeClusterSecurity</td>
<td>拉取集群密钥信息</td>
<td>TSE 北极星网格绑定 K8S 集群</td>
</tr>
</tbody></table>
   策略语法示例如下：
   <dx-codeblock>
   :::  json
   {
     "version": "2.0",
     "statement": [
       {
         "effect": "allow",
         "action": [
           "vpc:DescribeVpcEx",
           "vpc:DescribeSubnetEx",
           "monitor:GetMonitorData",
           "monitor:DescribeDashboardMetricData",
           "tke:DescribeClusters",
           "tke:DescribeClusterSecurity"
         ],
         "resource": [
           "*"
         ]
       }
     ]
   }
   :::
   </dx-codeblock>

#### 将自定义策略关联到子账户

1. 使用主账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam)。
2. 在左侧导航栏，单击**策略**，进入策略管理列表页。
3. 在右侧单击**自定义策略**进行筛选，找到步骤1.1中创建好的自定义策略，单击操作列的**关联用户/组/角色**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/cac57000257d960e6f34b01b732b36c7.jpg)
4. 选择需要授予该权限的子账号，单击**确定**即可完成授权。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/4012ea11ccdabf42ef2bf973514fd21a.png" width=700px>  
5. 单击**确定**完成授权。该策略会显示在用户的策略列表中。
   ![](https://qcloudimg.tencent-cloud.cn/raw/afc708af2fede59d2f16af998defe9f8.png)

[](id:step2)
### 步骤2：授予子账号使用 TSE 权限

<dx-tabs>
::: 操作级授权
详细操作请参见 [操作级授权](https://cloud.tencent.com/document/product/1364/75735)。
:::
::: 资源级授权
详细操作请参见 [资源级授权](https://cloud.tencent.com/document/product/1364/70801)。
:::
::: 标签级授权
详细操作请参见 [标签级授权](https://cloud.tencent.com/document/product/1364/70801)。
:::

</dx-tabs>
