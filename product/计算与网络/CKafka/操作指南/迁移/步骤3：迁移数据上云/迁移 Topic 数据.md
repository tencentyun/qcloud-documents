### 简介

客户在迁移上云过程中，需要把旧实例上未消费完的消息迁移到新实例对应的 topic 中时。可参考本教程进行操作，即可将旧集群的未消费数据同步到新集群中。

### 前提条件

1.  保证原实例所有消费/生产已停止。
2.  保证原实例待迁移的消息保留时间足够长，即在迁移过程中避免topic消息过期自动删除。
3.  同时迁移脚本是 python 脚本，需要安装 python2，且 python2 版本>2.7.1，推荐2.7.5
4.  下载迁移工具 [migrateToCkafkaTool](https://ckafka-1300957330.cos.ap-guangzhou.myqcloud.com/ckafka-demo/migrateToCkafkaTool.zip)。工具包目录如下，进入 migrateToCkafkaTool 目录下，修改 data-migrate.py 文件的配置后，执行 python data-migrate.py 即可
    ![](https://qcloudimg.tencent-cloud.cn/raw/d688a99a733f34c714a252e611d55b31.png)

### 工具原理

脚本会扫描老集群的所有 group 列表，并取出 group 订阅中的且仍有未消费消息的 topic 列表。脚本将取出未消费完 group 订阅 topic 的 **group 提交位置** 和 **topic 末端位置**(如果一个 topic 被多个 group 订阅，那么 group 提交位置将取最小的那个)。然后将此区间位置的消息消费后再生产到新实例的对应 topic 分区中。

### 操作演示

#### 1. 在目标集群新建对应的 Topic

假设原集群是：ckafka-47bd7goz, 目标新集群是：ckafka-kzamzogr。如下图所示：新集群已经建好了相同分区数的 topic。即 test1,test2,test3,test4。
![](https://qcloudimg.tencent-cloud.cn/raw/445cfffd2eac70de446772991b507baf.png)![](https://qcloudimg.tencent-cloud.cn/raw/f292cb1f4fd486a4e815a7a3d3b8d9dd.png)



原集群 ckafka-47bd7goz 有两个 group，test123-group 和 test34-group，它们分别订阅主题 test1,test2,test3 和 test3,test4。

![](https://qcloudimg.tencent-cloud.cn/raw/2aaf56e2c0f0244730bfc3da9b32c78f.png)![](https://qcloudimg.tencent-cloud.cn/raw/7848c46de10d89da4faa9df50f08c111.png)

#### 2. 下载工具包

下载迁移工具后，打开脚本填入原实例和新实例地址配置后，checkFlag 设置为0，运行脚本先预检查一下将要迁移的 topic 和位置。
![](https://qcloudimg.tencent-cloud.cn/raw/c9da1c8f0587b691475390e51699db6a.png)
运行脚本后，将输出一些信息，同时当前目录会同时写入一份文本日志。
![](https://qcloudimg.tencent-cloud.cn/raw/dae1bd45024dcd9e89cc7cf68ac37e3f.png)

#### 3. 查看输出信息

通过屏幕输出或者文本日志文件检查 **Prepare to migrate** 的信息，这是将要迁移的位点信息。
![](https://qcloudimg.tencent-cloud.cn/raw/7273a1a29eff4f5f7220c95867664408.png)
以 test3 为例，它同时被 test123-group 和 test34-group 订阅，检查原集群的订阅情况。

![](https://qcloudimg.tencent-cloud.cn/raw/72cec46de106e5d92e3ed68588670995.png)

![](https://qcloudimg.tencent-cloud.cn/raw/e4a5a0356d78f5c997b7e6d55ea3b96a.png)

按照预定逻辑，一个 topic 被多个 group 订阅应该从提交最小的那个位置开始同步，即187800，检查输出信息与预期一致。
![](https://qcloudimg.tencent-cloud.cn/raw/c3b7d835b40329d44160a640aba07980.png)

还有一种情况是原集群主题 test1 由于消息已经过期，但是 group 的提交位置在过期消息的区间，因此同步只会从 test1 还未过期的最早消息位置同步。
![](https://qcloudimg.tencent-cloud.cn/raw/a5c42710e07d8c46ac47c3507ee98eee.png)
![](https://qcloudimg.tencent-cloud.cn/raw/70fd3a38a9dad69d079d7168d6861134.png)
以 test1 的0分区为例，脚本会提示 test1 主题0分区的5226位置（topic 最存活消息最小位置）已经超过 group 订阅的提交 offset 的3713位置（该位置的消息已过期），因此同步开始的位置设置到了5226。又由于5226同样也是该分区目前最大的 offset（该分区目前存活消息总数为0）代表无消息可迁移，因此输出 skip migrate...的文本信息，代表跳过迁移本分区的数据。
![](https://qcloudimg.tencent-cloud.cn/raw/ccd2cc44af16ca56163ca19166e6fe95.png)

#### 4. 开始迁移

经上步检查过输出的信息确认无误后，修改 checkFlag=1 开始迁移。
![](https://qcloudimg.tencent-cloud.cn/raw/8f520a319ab8c5bc7b78e9dceb286d40.png)

#### 5. 检查迁移后数据是否数量一致

以 test3 为例,预期迁移 test123-group 未消费的76522条消息,已经全部成功写入新实例的test3主题中，迁移数据完成。
![](https://qcloudimg.tencent-cloud.cn/raw/26c3ae1c656c568878f1554b778ace67.png)
![](https://qcloudimg.tencent-cloud.cn/raw/b08f32e640599369b1f0d8957600f764.png)
