## 操作场景

创建完产品后，用户可以在 Topic 管理页面配置允许设备发布或订阅通信的主题。设备 Topic 列表从产品 Topic 列表继承，Topic 列表仅能通过产品层级进行增加、删除、修改操作。

## 操作步骤

### 添加自定义 Topic

1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)，单击左侧菜单**产品列表**。
2. 进入产品列表页面，单击产品名称，选择 **Topic 管理**。
3. 进入 Topic 管理页面，单击**添加自定义 Topic**，即可定义 Topic 名称并赋予设备操作权限。
	- 操作名称：名称命名支持字母、数字、下划线组合；不同层级之间用/分层+表示一级，使用/+/命名，不能/+aaa/；长度限制为1 - 255位。
	- 操作权限：可选择“订阅”、“发布”或“订阅和发布”，可修改。

![](https://qcloudimg.tencent-cloud.cn/raw/c472b78d92821685aa3dbcef3cd629c2.png)

### 编辑自定义 Topic

通过单击 Topic 权限列表的**编辑**，即可修改相应 Topic 权限的名称和权限。
![](https://qcloudimg.tencent-cloud.cn/raw/4b8c860f19ad2be6f2f161c29ebe330f.png)

### 删除 Topic 权限

通过单击 Topic 权限列表的**删除**，即可删除相应的 Topic 权限。



