
## 操作场景
通过 DescribeInvocationTasks 查询到的命令输出限制最多24 KB。本⽂以云服务器为例，介绍如何配置使完成的命令输出上传⾄指定 COS 桶中。
## 前提条件
1. 运⾏命令的⽬标实例是云服务器 CVM，此功能暂时不⽀持 Lighthouse。
2. ⽬标实例状态需处于 **运⾏中**，且已安装⾃动化助⼿客户端，详情请参⻅ [安装自动化助手客户端](https://cloud.tencent.com/document/product/1340/51945) 。
3. 已创建⽤于存储命令输出的 COS 存储桶。

## 操作步骤
1. 进⼊访问管理⻚⾯，单击 **新建⻆⾊**。
 <img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/b4cd968994c62a14d678b1d36078f8d5.png" />      
2. 选择⻆⾊载体是 **腾讯云产品服务**。
 <img style="width:750px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/33e407bfa831ffae2f452d3e489e8512.png" />
3. 选择⻆⾊载体信息是 **云服务器(cvm)**。
 <img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/463706cd747f623e5fd562ae2ed23b8a.png" />      
4. 搜索并配置预设策略 **QcloudCOSDataWriteOnly**。
 <img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/f9805b09b00722a3c456d26762ae7b09.png" />      
5. 输⼊⾃定义⻆⾊名称，完成⻆⾊创建。
 <img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/0c63dce861b79e8cfa995305cb1f8f66.png" />      
6. 找到目标实例，打开实例设置-绑定/修改角色。
  <img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/3bb0cd1d9abbd55fde2304ba45aa8be6.png" />     
 选择已创建的角色并绑定。
 <img style="width:500px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/9121185643e3013d309ff325bd6a1e1d.png" />     
7. 创建存储桶并复制其访问域名。
 <img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/38fa4e7fc74a74fda46ecbf22e475aa0.png" />     
8. RunCommand、InvokeCommand 接⼝均⽀持 COS 相关的参数，OutputCOSBucketUrl 填写步骤7中复制的存储桶域名，OutputCOSKeyPrefix 可选填。
 <img style="width:850px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/56b6ecaf0c9b831b3b3133fbf258b555.png" />     
9. 执⾏命令后可在 COS ⽂件列表中查看命令的完整输出。⽂件路径按以下格式组织：` /{OutputCOSKeyPrefix}/{实例ID}/{InvocationTaskID}.log`
例如： `/test/ins-s023oibx/invt-pvmkhci0.log`。
 <img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/0e60fdc2085564e18d48dbb07c403f36.png" />     

