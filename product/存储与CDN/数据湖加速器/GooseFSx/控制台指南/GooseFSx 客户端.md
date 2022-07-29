## 创建 POSIX 客户端

POSIX 客户端指将 GooseFSx 的 POSIX 客户端软件部署到您的主机，将 GooseFSx 挂载成主机的本地目录，以 POSIX 文件语义访问 GooseFSx，像访问本地目录一样。

创建 POSIX 客户端，您只需要提供主机 IP 和挂载目录（挂载目录，是您主机的本地目录，将 GooseFSx 挂载到该目录），输入 root 帐号密码，系统自动将 GooseFSx 挂载到该主机的该挂载目录：
1. 在您指定的主机上部署 POSIX 客户端软件。需要您输入该主机的 root 帐号密码，以便登录该主机部署 POSIX 客户端软件。系统不会保存密码，您可随时修改 root 帐号密码。
2. 将该主机纳入 POSIX 客户端管理节点的管理。
3. 将 GooseFSx 挂载到该客户端的挂载目录。

推荐的主机操作系统版本，详见 [POSIX 客户端的使用限制](https://cloud.tencent.com/document/product/1424/77960)。

#### 前提条件

- 已创建 GooseFSx 实例。创建指引请参见 [GooseFSx 实例](https://cloud.tencent.com/document/product/1424/77955)。
- 已创建 POSIX 客户端管理节点。在创建 GooseFSx 实例时，会同步创建 POSIX 客户端管理节点。

#### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入**实例列表**。
2. 选择目标实例所在的地域，选择**目标 GooseFSx 实例**，即创建客户端的 GooseFSx 实例。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者**管理**，进入 POSIX 客户端页面。
4. 单击**添加**，添加客户端。
5. 在弹出的添加客户端对话框中，进行如下配置。
 - 通过主机名/主机 IP 模糊匹配，快速找到您需要添加客户端的主机；或者直接输入主机 IP。
 - 输入挂载目录，例如\mnt\test\，将 GooseFSx 挂载到该挂载目录。
6. 单击**添加**，输入root 帐号密码。
7. 单击**确认**。
创建过程预计需要几分钟，在客户端列表查看结果。


### 查询 POSIX 客户端

查询 POSIX 客户端，查询挂载到 GooseFSx 的 POSIX 客户端，包括自动添加和手动添加的 POSIX 客户端。

#### 前提条件

- 已创建 GooseFSx 实例。创建指引请参见 [GooseFSx 实例](https://cloud.tencent.com/document/product/1424/77955)。
- 已创建 POSIX 客户端管理节点。在创建 GooseFSx 实例时，会同步创建 POSIX 客户端管理节点。
- 已创建 POSIX 客户端。


#### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入**实例列表**。
2. 选择目标实例所在的地域，选择目标 GooseFSx 实例，即 POSIX 客户端所属的 GooseFSx 实例。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者**管理**，进入 POSIX 客户端页面。
客户端列表，展示所有客户端信息。


### 删除 POSIX 客户端

删除 POSIX 客户端，解除挂载目录挂载到 GooseFSx，POSIX 客户端管理节点不再管理该客户端，卸载 POSIX 客户端软件。

删除 POSIX 客户端后，可再次执行创建 POSIX 客户端，挂载到 GooseFSx。

#### 前提条件

- 已创建 GooseFSx 实例。创建指引请参见 [GooseFSx 实例](https://cloud.tencent.com/document/product/1424/77955)。
- 已创建 POSIX 客户端管理节点。在创建 GooseFSx 实例时，会同步创建 POSIX 客户端管理节点。
- 已创建 POSIX 客户端。


#### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入**实例列表**。
2. 选择目标实例所在的地域，选择目标 GooseFSx 实例，即待删除的 POSIX 客户端。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者**管理**，进入 POSIX 客户端页面。
4. 勾选要删除的客户端，单击**删除**。



