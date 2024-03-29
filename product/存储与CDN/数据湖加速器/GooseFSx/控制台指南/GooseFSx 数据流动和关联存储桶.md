## 创建关联存储桶

创建关联存储桶，将对象存储（Cloud Object Storage，COS）的存储桶，关联到 GooseFSx 的关联目录；关联目录是 GooseFSx 的一级目录，是新目录。关联目录名默认是存储桶名称，建议您使用默认名称，可直观体现关联到哪个存储桶。

>? 请关联同地域的存储桶。
>

### 前提条件

已创建 GooseFSx 实例。


### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入 **实例列表**。
2. 选择目标实例所在的地域，选择目标 GooseFSx 实例，即创建关联存储桶的 GooseFSx 实例。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者**管理**，进入“数据流动”页面。
4. 单击**添加**，添加关联存储桶。
5. 选择要关联的 COS 存储桶，输入关联目录名、默认值是存储桶名称，单击**确认**即可。
创建完成后，可在关联存储桶列表查看结果。或在创建 GooseFSx 实例时，同步创建关联存储桶，操作步骤类似。

## 解除关联存储桶

解除关联存储桶，解除 COS 存储桶关联 GooseFSx，删除该关联存储桶的所有数据流动任务。解除关联存储桶后，GooseFSx 无法与该存储桶流动数据。若重新关联该存储桶，只能关联到 GooseFSx 新目录。在解除关联之前，请确认关联目录的数据已沉降到 COS 存储桶。

通常用法是当完成加速任务后，停止读写 GooseFSx 关联目录，将关联目录的数据沉降到 COS 存储桶，解除关联存储桶，删除关联目录，释放 GooseFSx 空间。

### 前提条件

- 已创建 GooseFSx 实例。
- 已创建关联存储桶。

### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入 **实例列表**。
2. 选择目标实例所在的地域，选择目标 GooseFSx 实例。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者**管理**，进入“数据流动”页面。
4. 在关联存储桶列表中找到待解除项，单击**解除关联**。
5. 单击**确认**。

## 查询关联存储桶

查询关联存储桶，查询到所有的关联存储桶，查询某个关联存储桶的所有数据流动任务。

### 前提条件

- 已创建 GooseFSx 实例。
- 已创建关联存储桶。

### 操作步骤

1. 登录 [数据加速器控制台](https://console.cloud.tencent.com/goosefs)，进入 **实例列表**。
2. 选择目标实例所在的地域，选择目标 GooseFSx 实例。
可通过勾选可用区/状态/类型等快速找到目标实例，或者通过名称关键字模糊匹配搜索出目标实例。
3. 单击实例 ID 或者**管理**，进入“数据流动”页面。
4. 在关联存储桶列表中，查询关联存储桶的信息。
 1. 单击关联存储桶列表的存储桶 ID，查看该关联存储桶的所有数据流动任务。
 2. 单击“查看数据流动任务”操作，查看该关联存储桶的所有数据流动任务。
 3. 关联存储桶列表的“数据流动任务”列，统计该关联存储桶的数据流动任务的数量。
