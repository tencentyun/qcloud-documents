## 前提条件
- 需已 [购买开通 CASB 实例](https://cloud.tencent.com/document/product/1303/53298)。
- 使用腾讯云对象存储（COS）服务并创建相对应的存储桶资源。如未创建存储桶资源，可查阅 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。

## 操作步骤
1. 登录 [云访问安全代理控制台](https://console.cloud.tencent.com/casb)，在左侧导航菜单栏中，单击元数据管理菜单下的**对象存储 COS**，进入对象存储 COS 页面。
![](https://main.qcloudimg.com/raw/2d01c33765a5dd0bb87ae498bfa5cde1.png)
2. 单击左上角的“区域下拉框”，切换区域，同时选择当前区域下的 Casb 实例。
![](https://main.qcloudimg.com/raw/c3bea7583ecfb2183ea8aad00efc6e5d.png)
3. 在对象存储 COS 页面中，单击**资产同步**，对象存储 COS 拉取对应区域的存储桶资源，系统会自动为存储桶资源创建元数据。
>?当对应区域的对象存储 COS 资源有变更后，需要单击**资产同步**，以确保数据一致性、完整性。
> 
![](https://main.qcloudimg.com/raw/7ab5bc310ff00625eb123db033f46bb8.png)
