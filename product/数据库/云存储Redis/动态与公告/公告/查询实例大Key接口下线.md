尊敬的腾讯云用户，您好！
腾讯云数据库 Redis 计划于**2022年10月31日**下线查询实例大 Key 接口 [DescribeInstanceMonitorBigKey](https://cloud.tencent.com/document/api/239/38922)，将由数据库智能管家 DBbrain 对应接口 [DescribeRedisTopBigKeys](https://cloud.tencent.com/document/product/1130/72832) 提供查询大 Key 列表的能力。 

数据库智能管家 DBbrain 是一款数据库智能诊断和优化产品。DBbrain 为用户提供实时的性能诊断和安全防护，高效地帮助用户定位故障原因、优化建议、协助用户从源头进行预防，并通过 AI 调参能力，提升数据库整体性能。

数据库智能管家对应接口 [DescribeRedisTopBigKeys](https://cloud.tencent.com/document/product/1130/72832)，可通过指定 Key 的排序字段、Key 类型，快速查询实例中大 Key 信息，包含：大 Key 过期时间、内存大小、元素个数及最大元素长度。

## 下线接口列表
DescribeInstanceMonitorBigKey 接口及其相关联的接口 DescribeInstanceMonitorBigKeySizeDist 与 DescribeInstanceMonitorBigKeyTypeDist 将同步下线。

| 接口名称                                                     | 接口功能              |
| :----------------------------------------------------------- | :-------------------- |
| [DescribeInstanceMonitorBigKey](https://cloud.tencent.com/document/api/239/38922) | 查询实例大 Key         |
| [DescribeInstanceMonitorBigKeySizeDist](https://cloud.tencent.com/document/api/239/40601) | 查询实例大 Key 大小分布 |
| [DescribeInstanceMonitorBigKeyTypeDist](https://cloud.tencent.com/document/api/239/38921) | 查询实例大 Key 类型分布 |

