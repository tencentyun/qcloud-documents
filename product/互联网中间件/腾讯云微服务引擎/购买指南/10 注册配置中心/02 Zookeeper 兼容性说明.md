本文为您介绍腾讯云 Zookeeper 和社区版 Zookeeper 的兼容性，帮助您在使用腾讯云 Zookeeper 时根据业务需求选择更加适合您的版本。

## 概述
Zookeeper 目前版本号已经稳定在3.x.y。目前腾讯云提供了多个子版本：3.4.14、3.5.9、3.6.3。

## 兼容性说明
腾讯云 Zookeeper 完美兼容社区 Zookeeper，其中主版本和子版本是完全向下兼容的。兼容性说明如下：

| Zookeeper 版本 | 可兼容社区版本 | 兼容性 |
| ---- | ---- | ---- |
| 3.4.14	| ≤ 3.4.14	| 100% |
| 3.5.9	| ≤ 3.5.9	| 100% |
| 3.6.3	| ≤ 3.6.3	| 100% |

## Zookeeper 版本选择建议
- 如果是自建 Zookeeper 上云，建议选择对应主版本的子版本即可。例如：自建 Zookeeper 是3.4.0版本，则选择 Zookeeper 的3.4版本。
- 当在云上找不到对应的版本时，建议向上选择版本。例如：自建是3.3.0版本，则建议使用3.4.14版本。

## Zookeeper 客户端版本选择建议
- 优先使用和Zookeeper对应主版本号以及子版本号一致的客户端。例如：Zookeeper 版本是3.4.14，则选择客户端3.4的版本。
- 当无法保证子版本号一致的时候，建议向下选择版本。例如：Zookeeper 版本是3.4.14，可以选择客户端3.3的版本。
