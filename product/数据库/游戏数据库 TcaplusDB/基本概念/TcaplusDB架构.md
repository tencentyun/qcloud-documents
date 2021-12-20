
TcaplusDB 是一种完全托管的分布式 NoSQL 数据库服务，主要由管理层，接入层，以及存储层构成，其中接入层与存储层由多个连接节点，多个存储节点组成，并且支持横向的扩缩节点。每一层有着不同作用，整体架构图如下：
![](https://main.qcloudimg.com/raw/4c4ae2ad168306895d7744496933936c.png)

#### 管理层
TcaplusDB 管理层用于存放元数据以及管理信息，负责 TcaplusDB 系统的调度与数据管理。

#### 接入层
TcaplusDB 接入层用于处理用户请求，与存储层数据节点交互，并获取数据返回给用户。

#### 存储层
存储层服务为 TcaplusDB 核心服务，用于存放用户数据，并响应接入层请求，返回数据信息。

### TcaplusDB 逻辑结构
TcaplusDB 逻辑结构由集群，表格组，表格组成，其关系图如下：
![](https://main.qcloudimg.com/raw/d2f155b5f7edbe6ac6dd1a45d67500ee.png)

