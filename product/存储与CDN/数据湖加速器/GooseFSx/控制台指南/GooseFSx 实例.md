## 创建实例

数据加速器 GooseFSx 为对象存储（Cloud Object Storage，COS）加速，GooseFSx 从 COS 加载数据，以便应用能够以高性能、低延时的优势访问到缓存在 GooseFSx 的数据。GooseFSx 产生的计算结果沉降到 COS，实现持久化/低成本保存。为实现数据从 COS 加载或沉降到 COS，需要将 COS 存储桶关联到 GooseFSx 目录，指定 COS 存储桶的数据流动到 GooseFSx 目录。

用户的主机通过部署 POSIX 客户端 ，将 GooseFSx 挂载成本地目录。部署 POSIX 客户端软件的主机称为 POSIX 客户端。启用 POSIX 客户端，会在您指定的 VPC，部署 POSIX 客户端管理节点，管理 POSIX 客户端。

### 前提条件

1. 在创建数据加速器 GooseFSx 之前，您需要了解使用 GooseFSx 的主机所在地域、可用区、VPC 网络，系统会将 GooseFSx 实例部署在相同地域和可用区，并在该 VPC 网络部署 POSIX 客户端管理节点。
2. GooseFSx 开服的产品类型，详见 [产品类型](https://cloud.tencent.com/document/product/1424/77952)。
3. 开服的地域，详见 [适用地域](https://cloud.tencent.com/document/product/1424/77954)。
4. 若您有其他需求，或者因资源不足而创建 GooseFSx 失败，您可咨询 [在线客服](https://cloud.tencent.com/act/event/Online_service?from=doc_582) 提前预留资源。
5. 开通数据加速器服务的操作指引，详见 [快速入门](https://cloud.tencent.com/document/product/1424/77950)。


### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)。
2. 选择创建数据加速器 GooseFSx，进入创建页面。
 - 地域：选择要创建 GooseFSx 的地域。地域一旦选定不可修改。
 - 可用区：可用区是指在同一地域内，电力和网络互相独立的物理区域。同一地域不同可用区之间的内网互通。建议将 GooseFSx 部署到与主机相同的可用区，避免跨可用区所产生的时延。
 - 标签：可选项，可在创建 GooseFSx 实例后进行配置或修改。详见 [标签](https://cloud.tencent.com/document/product/1424/77957)。
 - 类型：GooseFSx 的不同产品类型性能和价格不一样。详见 [产品类型](https://cloud.tencent.com/document/product/1424/77952)。
 - 容量：根据业务需求，选择合适的容量；此容量是您的可用容量，您无须考虑冗余保护、元数据消耗等。
 - 关联存储桶：可选项，可在创建 GooseFSx 实例后进行配置或修改。实现 GooseFSx 目录与 COS 存储桶关联，详见 [数据流动和关联存储桶](https://cloud.tencent.com/document/product/1424/77959)。
 -  POSIX 客户端所属 VPC 网络：选择与主机相同的 VPC 网络。
 -  POSIX 客户端所属子网：建议选择与主机相同的子网络，避免跨子网所产生的时延。
3. 单击**立即购买**。
在实例列表，可查看正在创建的实例。创建过程预计10分钟左右。

<span id="1"></span>
## 查询实例

查询实例，查看实例的详细信息，例如类型、容量、计费方式、创建时间等，查询实例的 POSIX 客户端，详见 [管理 GooseFSx POSIX 客户端](https://cloud.tencent.com/document/product/1424/77956)；查询实例的关联存储桶和数据流动任务，详见 [数据流动和关联存储桶](https://cloud.tencent.com/document/product/1424/77959) 和 [数据流动任务](https://cloud.tencent.com/document/product/1424/77958)。

### 前提条件

已创建 GooseFSx 实例。

### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入**实例列表**。
2. 选择目标实例所在的地域，选择目标 GooseFSx 实例，即待查询的 GooseFSx 实例。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者**管理**，查看实例的详细信息。


## 修改实例

修改实例，修改实例的名称和描述，修改实例的 POSIX 客户端，详见 [管理 GooseFSx POSIX 客户端](https://cloud.tencent.com/document/product/1424/77956)；修改实例的关联存储桶和数据流动任务，详见 [数据流动和关联存储桶](https://cloud.tencent.com/document/product/1424/77959) 和 [数据流动任务](https://cloud.tencent.com/document/product/1424/77958)；修改实例的标签，详见 [GooseFSx 标签](https://cloud.tencent.com/document/product/1424/77957)。

### 前提条件

已创建 GooseFSx 实例。

### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入**实例列表**。
2. 选择目标实例所在的地域，选择待修改的 GooseFSx 实例。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者**管理**，修改名称和描述。

## 删除实例

>! 
> - 请谨慎删除实例，一旦删除不可恢复；在删除前请确认该实例的数据已持久化到  COS。
> - 如需查看哪些主机上会删除 POSIX 客户端软件、解除哪些关联存储桶和哪些数据流动任务，请参见 [查询实例](#1)。
>

删除实例，会自动删除挂载该实例的使用 POSIX 客户端，会自动解除关联该实例的关联存储桶，会自动删除所有数据流动任务。

### 前提条件

已创建 GooseFSx 实例。

### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosef)，进入**实例列表**。
2. 选择目标实例所在的地域，选择目标 GooseFSx 实例，即待删除的 GooseFSx 实例。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击**删除**。
4. 在弹出的对话框中，确认待删除的实例名称，单击**确认**。

