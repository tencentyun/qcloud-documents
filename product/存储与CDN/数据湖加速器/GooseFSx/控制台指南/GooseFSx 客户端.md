[](id:1)
## 自动创建 POSIX 客户端


GooseFSx POSIX 客户端指已部署 GooseFSx POSIX 客户端软件，并将 GooseFSx 挂载成本地目录的主机。 POSIX 客户端访问挂载目录，像访问本地文件系统一样访问 GooseFSx。

创建 POSIX 客户端，您只需要提供主机 IP ，输入 root 帐号密码，系统自动将 GooseFSx 挂载到该主机的挂载目录 `/goosefsx/x_${型号}_${实例id}_proxy`，例如 /goosefsx/x_c60_089qyg9w_proxy。
1. 在您指定的主机上部署 POSIX 客户端软件。需要您输入该主机的 root 帐号密码，以便登录该主机部署 POSIX 客户端软件。系统不会保存密码，您可随时修改 root 帐号密码。
2. 将该主机纳入 POSIX 客户端管理节点的管理。
3. 将 GooseFSx 挂载到该 POSIX 客户端。

推荐的主机操作系统版本，详见 [ POSIX 客户端的使用限制](https://cloud.tencent.com/document/product/1424/77960)。

#### 前提条件

- 已创建 GooseFSx 实例。创建指引请参见 [GooseFSx 实例](https://cloud.tencent.com/document/product/1424/77955)。
- 已创建 POSIX 客户端管理节点。在创建 GooseFSx 实例时，会同步创建 POSIX 客户端管理节点。
- 已为主机添加安全组规则，详见 [POSIX 客户端安全组规则](#rule)。若您同时为 POSIX 客户端设置拒绝策略的安全组，请确保未拒绝 POSIX 客户端安全组规则。
- 已创建 Linux 主机。主机操作系统若是 Windows，请采用 [手动创建 POSIX 客户端](#windows)。

#### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入**实例列表**。
2. 选择目标实例所在的地域，选择**目标 GooseFSx 实例**，即创建 POSIX 客户端的 GooseFSx 实例。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者**管理**，进入 POSIX 客户端页面。
4. 单击**添加**，添加 POSIX 客户端。
5. 在弹出的添加 POSIX 客户端对话框中，进行如下配置。
 - 通过主机名/主机 IP 模糊匹配，快速找到您需要添加 POSIX 客户端的主机；或者直接输入主机 IP。
 >?请确认已为该主机添加安全组规则，详见 [POSIX 客户端安全组规则](#rule)。若您同时为 POSIX 客户端设置拒绝策略的安全组，请确保未拒绝 POSIX 客户端安全组规则。
 - 输入 root 帐号密码。
6. 单击**确认**。
创建过程预计需要几分钟，在 POSIX 客户端列表查看结果。





## 手动创建 POSIX 客户端（Linux）

#### 前提条件

- 已创建 GooseFSx 实例。创建指引请参见 [GooseFSx 实例](https://cloud.tencent.com/document/product/1424/77955)。
- 已创建 POSIX 客户端管理节点。在创建 GooseFSx 实例时，会同步创建 POSIX 客户端管理节点。
- 已为主机添加安全组规则，详见 [POSIX 客户端安全组规则](https://cloud.tencent.com/document/product/1424/77956#rule)。若您同时为 POSIX 客户端设置拒绝策略的安全组，请确保未拒绝 POSIX 客户端安全组规则。



#### 操作步骤

1. 登录您需要添加 POSIX 客户端的主机，根据主机所在地域、选择对应命令下载部署脚本。
 - 北京地域的主机执行如下命令，从北京 COS 桶下载：
```
wget https://goosefs-cfg-bj-1308338417.cos.ap-beijing.myqcloud.com/client_env_package/agent/install-goosefsx-client.sh
```
 - 上海地域的主机执行如下命令，从上海 COS 桶下载：
```
wget https://goosefs-cfg-bj-1308338417.cos.ap-beijing.myqcloud.com/client_env_package/agent/install-goosefsx-client.sh
```
 - 广州地域的主机执行如下命令，从广州 COS 桶下载：
```
wget https://goosefs-cfg-bj-1308338417.cos.ap-beijing.myqcloud.com/client_env_package/agent/install-goosefsx-client.sh
```
 - 南京地域的主机执行如下命令，从南京 COS 桶下载：
```
wget https://goosefs-cfg-bj-1308338417.cos.ap-beijing.myqcloud.com/client_env_package/agent/install-goosefsx-client.sh
```
>?从任何地域的对象存储 COS 桶下载的部署脚本是一样的。

2. 修改部署脚本的权限，执行命令：
```
chmod 777 install-goosefsx-client.sh
```
3. 需要准备2个入参，分别为地域和 POSIX 客户端管理节点 IP地址的字符串（比如主机是北京地域，登录 [GooseFSx 控制台](https://console.cloud.tencent.com/goosefs/goosefsx) 可查看 POSIX 客户端管理节点 IP 地址，详情可参加 [查询 POSIX 客户端](https://cloud.tencent.com/document/product/1424/77956#.E6.9F.A5.E8.AF.A2-posix-.E5.AE.A2.E6.88.B7.E7.AB.AF)），然后执行命令：
```
./install-goosefsx-client.sh ap-bejing 10.0.0.138:55533,10.0.0.103:55533,10.0.0.183:55533
```
4. 登录 [GooseFSx 控制台](https://console.cloud.tencent.com/goosefs/goosefsx) 查看添加的客户端，创建过程预计需要几分钟，可在 POSIX 客户端列表查看结果。





## TAT 自动化助手创建 POSIX 客户端（Linux）

#### 前提条件

-  已创建 GooseFSx 实例。创建指引请参见 [GooseFSx 实例](https://cloud.tencent.com/document/product/1424/77955)。
-  已创建 POSIX 客户端管理节点。在创建 GooseFSx 实例时，会同步创建 POSIX 客户端管理节点。
-  已为主机添加安全组规则，详见 [POSIX 客户端安全组规则](https://cloud.tencent.com/document/product/1424/77956#rule)。若您同时为 POSIX 客户端设置拒绝策略的安全组，请确保未拒绝 POSIX 客户端安全组规则。



#### 操作步骤

1. 登录自动化助手：登录 [CVM 控制台](https://console.cloud.tencent.com/cvm)，在左侧导航栏选择**自动化助手 > 我的命令**，地域选择 GooseFSx 所在地域。
2. 单击**创建命令**，自定义名称，例如 crtGooseFSx，其他保持默认值，在“命令内容”粘贴如下内容：
```
wget https://goosefs-cfg-sh-1308338417.cos.ap-shanghai.myqcloud.com/client_env_package/agent/install-goosefsx-client.sh

chmod 777 install-goosefsx-client.sh

./install-goosefsx-client.sh ap-shanghai 10.0.0.138:55533,10.0.0.103:55533,10.0.0.183:55533
```
3. 在命令列表选择，刚才创建的命令，例如 crtGooseFSx，单击“执行”操作，进入“执行命令”页，选择执行实例，单击“执行命令”。
4. 在“执行命令”页的“执行详情”，查看命令执行状态，等待命令执行。
5. 登录 [GooseFSx 控制台](https://console.cloud.tencent.com/goosefs/goosefsx) 查看到添加的客户端，创建过程预计需要几分钟，可在 POSIX 客户端列表查看结果。


[](id:windows)
## 手动创建 POSIX 客户端（Windows）

使用打包 GooseFSx 部署脚本的 Windows 镜像创建 POSIX 客户端。


#### 前提条件

-  已创建 GooseFSx 实例。创建指引请参见 [GooseFSx 实例](https://cloud.tencent.com/document/product/1424/77955)。
-  已创建 POSIX 客户端管理节点。在创建 GooseFSx 实例时，会同步创建 POSIX 客户端管理节点。
-  已为主机添加安全组规则，详见 [POSIX 客户端安全组规则](https://cloud.tencent.com/document/product/1424/77956#rule)。若您同时为 POSIX 客户端设置拒绝策略的安全组，请确保未拒绝 POSIX 客户端安全组规则。



#### 操作步骤

1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm)，创建 CVM 主机，选择打包 GooseFSx 部署脚本的 Windows 镜像，可从镜像市场或共享镜像里选择。
2. 进入 win 主机的 C 盘，编辑脚本 start_agent.bat，将 IP 地址依次修改为 GooseFSx 实例的 POSIX 客户端管理节点的 IP：
```
goosefsx_cluster_member_windows_client.exe -server_addr 10.0.0.47:55533,10.0.0.213:55533,10.0.0.211:55533  -agent_method add -os_version windows                             
```
3. 重启该 Windows 主机。
4. 登录 [GooseFSx 控制台](https://console.cloud.tencent.com/goosefs/goosefsx) 查看到添加的客户端，创建过程预计需要几分钟，可在 POSIX 客户端列表查看结果。





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


[](id:rule)
## POSIX 客户端安全组规则

POSIX 客户端需要放通如下端口与 GooseFSx 通信，相关指引请参见 [配置安全组](https://cloud.tencent.com/document/product/213/15377)。若您同时为 POSIX 客户端设置拒绝策略的安全组，请确保未拒绝 POSIX 客户端安全组规则。
 
| 协议 | 方向     | 端口                               | IP                      |
| ---- | -------- | ---------------------------------- | ----------------------- |
| TCP  | 入站规则 | 1191、22、10080、8445、60000-61000 | GooseFSx 所属 VPC 的所有 IP |
| ICMP | 入站规则 | ALL                                | GooseFSx 所属 VPC 的所有 IP |
