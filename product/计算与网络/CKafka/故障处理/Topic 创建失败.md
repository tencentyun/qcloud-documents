## 问题概述

Topic 创建失败。


## 可能原因

- 已创建的所有 Topic 的分区数之和达到实例规格的分区数上限。
- 在删除 Topic 期间创建同名 Topic。
- Topic 已经存在集群当中。



## 解决方法

- **已创建的所有 Topic 的分区数之和达到实例规格的分区数上限**
建议对 Kafka 实例扩容，或者删除不需要的 Topic。
![](https://qcloudimg.tencent-cloud.cn/raw/02420c74f53287536ba470820ca40f35.jpg)

- **在删除 Topic 期间创建同名 Topic**
Topic 删除是异步操作，下发删除指令后，系统会异步的删除该 Topic 的元数据。若在此期间创建同名 Topic，系统会提示 Topic 已经存在，届时请您稍后重试。这里需要等待1分钟左右，再进行重建操作。

- **Topic 已经存在集群当中**
Topic 已经存在集群当中，创建重名的 Topic 就会提示 Topic 已经存在，建议重新设置 Topic 名称。
