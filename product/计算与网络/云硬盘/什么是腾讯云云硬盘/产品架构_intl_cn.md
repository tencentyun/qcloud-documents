本节介绍云硬盘后台分布式存储系统的设计和实现，其存储系统架构如下图所示：
![](//mccdn.qcloud.com/static/img/5bf39a359912506f94ab5e205422eb42/image.png)

云硬盘的后台分布式存储系统主要分为三个模块：Client模块、Master模块，Chunk server模块。
- **Client模块**：Client通常部署在hypervisor上，主要有两个功能：
	- 一是负责磁盘虚拟化。将存储池抽象的volume（虚拟磁盘）空间映射为本地盘，存储池的volume由分布在不同Chunk server上的Block组成，client负责将它们映射为统一的逻辑地址；
	- 二是存储协议转换。将用户的IO请求按照固定的块大小进行拆分，并将请求路由到不同的Chunk server。

- **Chunk server模块**：Chunk Server是存储节点，负责管理分配Block，保存用户数据。
	- 采用每份数据冗余三份的方式保存用户数据以保障数据安全，每个Block块会分布在不同的三台Chunk server上。
	- 进行用户访问鉴权以保障用户数据隔离，只有合法的Client才能访问Chunk server数据，鉴权控制粒度是盘和用户粒度。

- **Master模块**：Master模块主要负责管理Client到Chunk server的路由，以及Chunk server的故障剔除和恢复。
	- Master将路由信息推送到Client，Client根据路由信息对用户IO请求实施转发。
	- Maste负责监控Chunk server的状态，当集群出现坏盘或者死机时候，及时对其进行剔除，并启动数据迁移和恢复。