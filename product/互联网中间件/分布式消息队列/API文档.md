TDMQ Pulsar 版相关接口如下表所示。

<style>
table th:nth-of-type(1) {
width: 300px;        
}
</style>

## 集群相关接口

| 接口名称                                                     | 接口功能         |
| :----------------------------------------------------------- | :--------------- |
| [CreateCluster](https://cloud.tencent.com/document/api/1179/52193) | 创建集群         |
| [DeleteCluster](https://cloud.tencent.com/document/api/1179/52185) | 删除集群         |
| [DescribeBindClusters](https://cloud.tencent.com/document/api/1179/52191) | 获取专享集群列表 |
| [DescribeClusterDetail](https://cloud.tencent.com/document/api/1179/52184) | 获取集群详情     |
| [DescribeClusters](https://cloud.tencent.com/document/api/1179/52183) | 获取集群列表     |
| [ModifyCluster](https://cloud.tencent.com/document/api/1179/52189) | 更新集群信息     |

## 命名空间相关接口

| 接口名称                                                     | 接口功能             |
| :----------------------------------------------------------- | :------------------- |
| [CreateEnvironment](https://cloud.tencent.com/document/api/1179/46081) | 创建命名空间         |
| [DeleteEnvironments](https://cloud.tencent.com/document/api/1179/46080) | 删除命名空间         |
| [DescribeEnvironmentAttributes](https://cloud.tencent.com/document/api/1179/46079) | 获取命名空间属性     |
| [DescribeEnvironmentRoles](https://cloud.tencent.com/document/api/1179/49051) | 获取命名空间角色列表 |
| [DescribeEnvironments](https://cloud.tencent.com/document/api/1179/46078) | 获取命名空间列表     |
| [ModifyEnvironmentAttributes](https://cloud.tencent.com/document/api/1179/46077) | 修改命名空间属性     |

## 主题相关接口

| 接口名称                                                     | 接口功能     |
| :----------------------------------------------------------- | :----------- |
| [CreateTopic](https://cloud.tencent.com/document/api/1179/46088) | 新增主题     |
| [DeleteTopics](https://cloud.tencent.com/document/api/1179/46087) | 删除主题     |
| [DescribeTopics](https://cloud.tencent.com/document/api/1179/46086) | 查询主题列表 |
| [ModifyTopic](https://cloud.tencent.com/document/api/1179/46085) | 修改主题     |

## 消息相关接口

| 接口名称                                                     | 接口功能     |
| :----------------------------------------------------------- | :----------- |
| [AcknowledgeMessage](https://cloud.tencent.com/document/api/1179/57459) | 确认消息     |
| [ReceiveMessage](https://cloud.tencent.com/document/api/1179/57458) | 接收消息     |
| [SendBatchMessages](https://cloud.tencent.com/document/api/1179/53441) | 批量发送消息 |
| [SendMessages](https://cloud.tencent.com/document/api/1179/53440) | 发送单条消息 |



## 生产消费相关接口

| 接口名称                                                     | 接口功能     |
| :----------------------------------------------------------- | :----------- |
| [CreateSubscription](https://cloud.tencent.com/document/api/1179/46075) | 创建订阅关系 |
| [DeleteSubscriptions](https://cloud.tencent.com/document/api/1179/46074) | 删除订阅关系 |
| [DescribeProducers](https://cloud.tencent.com/document/api/1179/46073) | 生产者列表   |
| [DescribeSubscriptions](https://cloud.tencent.com/document/api/1179/46072) | 消费订阅列表 |
| [ResetMsgSubOffsetByTimestamp](https://cloud.tencent.com/document/api/1179/46083) | 消息回溯     |

## 环境角色授权相关接口

| 接口名称                                                     | 接口功能         |
| :----------------------------------------------------------- | :--------------- |
| [CreateEnvironmentRole](https://cloud.tencent.com/document/api/1179/62402) | 创建环境角色授权 |
| [CreateRole](https://cloud.tencent.com/document/api/1179/62401) | 创建角色         |
| [DeleteEnvironmentRoles](https://cloud.tencent.com/document/api/1179/62400) | 删除环境角色授权 |
| [DescribeRoles](https://cloud.tencent.com/document/api/1179/62399) | 获取角色列表     |
| [ModifyEnvironmentRole](https://cloud.tencent.com/document/api/1179/62398) | 修改环境角色授权 |
| [ModifyRole](https://cloud.tencent.com/document/api/1179/62397) | 修改角色         |


## 其他接口

| 接口名称                                                     | 接口功能                     |
| :----------------------------------------------------------- | :--------------------------- |
| [DeleteRoles](https://cloud.tencent.com/document/api/1179/62403) | 删除角色                     |
| [DescribeBindVpcs](https://cloud.tencent.com/document/api/1179/52187) | 获取租户 VPC 绑定关系          |
| [DescribeNamespaceBundlesOpt](https://cloud.tencent.com/document/api/1179/59039) | 运营端获取命名空间 bundle 列表 |
| [DescribeNodeHealthOpt](https://cloud.tencent.com/document/api/1179/59038) | 运营端获取节点健康状态         |
| [SendMsg](https://cloud.tencent.com/document/api/1179/56772) | 发送消息                     |
