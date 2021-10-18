## 功能介绍
HDFS 联邦管理为您提供快速搭建 HDFS 联邦的能力，HDFS 联邦可以实现命名空间的可扩展性、提升文件系统读写性能、提供隔离的特性。
>!
>- 目前新建联邦采用的节点为 Router 节点，建议先扩容 Router 节点作为新的联邦节点。
>- 添加 NameService 后，NameService 名称不可修改，不可以删除。
>- Router 节点作为联邦节点后，该节点不可被缩容。

## 操作步骤
1. 登录 [弹性 MapReduce 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的集群 **ID/名称**进入集群详情页。
2. 在集群详情页中单击左侧菜单**集群服务**，然后选择 **HDFS 组件**右上角**操作 > 联邦管理**，即可进入联邦管理页面。
 ![](https://main.qcloudimg.com/raw/74a896acb3792f5de537e9370878d90e.png)
3. 单击**添加 NameService** 即可进行 HDFS 联邦新建，需要输入 NameService 名称，选择联邦类型、选择 NameNode 节点、选择 Router 节点（Router-based Federation 选择）等。
![](https://main.qcloudimg.com/raw/c8598493f982227f6b7dfb31ddefeb59.png)
点击选择节点即可开始进行节点选择。
    - NameNode 节点需要选择2个节点，将会部署 NameNode 进程和 ZKFC 进程。
    - Router 节点第一次新建联邦时需要至少选择两个节点；联邦已经存在后，Router 节点可复用，为可选项。
4. 添加挂载表
 - 在已经成功新增 NameService 后，即可进行添加挂载表操作，对集群的现有目录做出映射。
 - 建议只对全局一级目录进行 NameService 映射，以避免配置复杂度过高。
![](https://main.qcloudimg.com/raw/ba05492d3bcb4ce6e8599b91f8c7252d.png)
