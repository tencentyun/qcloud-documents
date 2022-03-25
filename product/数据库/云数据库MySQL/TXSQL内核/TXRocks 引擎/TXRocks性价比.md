TXRocks 的性能与 InnoDB 接近，但由于 LSM Tree 存储结构，减少了 InnoDB ⻚⾯半满和碎⽚浪费，相⽐ InnoDB，TXRocks 的存储空间可以节省更多，因此具备超高性价比。

## 背景信息
在腾讯云数据库产品中，TXRocks 为 InnoDB 的重要补充，在性能相近的基础上，TXRocks 做了部分优化和改进，在存储空间上，相比 InnoDB 更为节省，下文将从空间占用和性能来对比两个引擎。

## TXRocks 空间占用比 InnoDB 更低
![](https://qcloudimg.tencent-cloud.cn/raw/a78abe5aad73af1391396d1d139f52fc.png)
**测试场景**：sysbench 灌1000万⾏数据，完成后 TXRocks 触发 compaction。
上图为测试条件下分别使用 TXRocks 和 InnoDB 存储引擎时的空间占用情况。由此可见，TXRocks 空间占用比 InnoDB 更低。

## TXRocks 性能与 InnoDB 基本持平
![](https://qcloudimg.tencent-cloud.cn/raw/94a2e715d6549b1232306a49e31b5869.png)
**测试场景**：实例8核32GB场景，6张表500万⾏数据，每个测试均重启后冷启动测试，每个 case 跑1200秒。
上图为测试场景条件下分别使用 TXRocks 和 InnoDB 存储引擎时的性能对比，通过对比可以发现 TXRocks 和 InnoDB 性能相近。
**sysbench 命令关键参数**：
```
sysbench --table-size=5000000 --tables=6 --threads=32 --time=1200
```

## 总结
TXRocks 是一款性能与 InnoDB 相似，但是空间占用较低的腾讯云数据库 MySQL 存储引擎产品。保证了业务性能需要的同时还能降低存储成本，关于 TXRocks 的详细介绍请参见 [TXRocks 概述](https://cloud.tencent.com/document/product/236/71455)。

