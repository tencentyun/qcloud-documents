[](id:1)
## 创建 POSIX 客户端

GooseFSx POSIX 客户端指已部署 GooseFSx POSIX 客户端软件，并将 GooseFSx 挂载成本地目录的主机。 POSIX 客户端访问挂载目录，像访问本地文件系统一样访问 GooseFSx。

创建 POSIX 客户端，您只需要提供主机 IP ，输入 root 帐号密码，系统自动将 GooseFSx 挂载到该主机的挂载目录 `/goosefsx/x_${型号}_${实例id}_proxy`，例如 /goosefsx/x_c60_089qyg9w_proxy。
1. 在您指定的主机上部署 POSIX 客户端软件。需要您输入该主机的 root 帐号密码，以便登录该主机部署 POSIX 客户端软件。系统不会保存密码，您可随时修改 root 帐号密码。
2. 将该主机纳入 POSIX 客户端管理节点的管理。
3. 将 GooseFSx 挂载到该 POSIX 客户端。

推荐的主机操作系统版本，详见 [ POSIX 客户端的使用限制](https://cloud.tencent.com/document/product/1424/77960)。

#### 前提条件

- 已创建 GooseFSx 实例。创建指引请参见 [GooseFSx 实例](https://cloud.tencent.com/document/product/1424/77955)。
- 已创建 POSIX 客户端管理节点。在创建 GooseFSx 实例时，会同步创建 POSIX 客户端管理节点。

#### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入**实例列表**。
2. 选择目标实例所在的地域，选择**目标 GooseFSx 实例**，即创建 POSIX 客户端的 GooseFSx 实例。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者**管理**，进入 POSIX 客户端页面。
4. 单击**添加**，添加 POSIX 客户端。
5. 在弹出的添加 POSIX 客户端对话框中，进行如下配置。
 - 通过主机名/主机 IP 模糊匹配，快速找到您需要添加 POSIX 客户端的主机；或者直接输入主机 IP。
 - 输入 root 帐号密码。
6. 单击**确认**。
创建过程预计需要几分钟，在 POSIX 客户端列表查看结果。


## 批量创建 POSIX 客户端
若需批量创建 POSIX 客户端，可通过镜像的方式一次创建一批 GooseFSx POSIX 客户端。首先创建一个相同主机操作系统版本的 GooseFSx POSIX 客户端，接着对此 GooseFSx POSIX 客户端生成镜像，最后通过该镜像批量拉起 GooseFSx POSIX 客户端。

#### 前提条件

- 已创建 GooseFSx 实例。创建指引请参见 [GooseFSx 实例](https://cloud.tencent.com/document/product/1424/77955)。若已创建多个 GooseFSx 实例，请选择要批量创建 POSIX 客户端的实例；若想为多个实例批量创建 POSIX 客户端，请为这些实例分别执行批量创建 POSIX 客户端，因为 GooseFSx POSIX 客户端属于某个 GooseFSx 实例。
- 已创建 POSIX 客户端管理节点。在创建 GooseFSx 实例时，会同步创建 POSIX 客户端管理节点。
- 已创建至少一个相同主机操作系统版本的 GooseFSx POSIX 客户端。
>?若想批量创建不同操作系统版本的 POSIX 客户端，需要先创建不同操作系统版本的 POSIX 客户端，并生成镜像，通过镜像拉起相同操作系统版本的 POSIX 客户端。例如，创建一个 CentOS POSIX 客户端，生成 CentOS POSIX 客户端的镜像，通过镜像批量创建 CentOS POSIX 客户端；创建一个 TLinux POSIX 客户端，生成 TLinux POSIX 客户端的镜像，通过镜像批量创建 TLinux POSIX 客户端；以此类推。



#### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入**实例列表**。
2. 选择目标实例所在的地域，选择**目标 GooseFSx 实例**。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者管理，进入 POSIX 客户端页面。
4. 在 POSIX 客户端列表，选择基于哪个 POSIX 客户端来创建镜像，若没有目标操作系统版本的 POSIX 客户端，请先创建一个，参见 [创建 POSIX 客户端](#1) 指引；单击 **主机 ID**，进入该主机实例的控制台，制作镜像，相关指引可参见 [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942)。
5. 通过镜像批量创建 POSIX 客户端，相关指引可参见 [通过镜像创建实例](https://cloud.tencent.com/document/product/213/44265)。


## 查询 POSIX 客户端

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
 POSIX 客户端列表，展示所有 POSIX 客户端信息。


## 删除 POSIX 客户端

删除 POSIX 客户端，解除 POSIX 客户端挂载到 GooseFSx， POSIX 客户端管理节点不再管理该 POSIX 客户端，卸载 POSIX 客户端软件。

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
4. 勾选要删除的 POSIX 客户端，单击**删除**。



