
## 检查详情
- 检查要求：源端为分片实例情况下，源端必须关闭 Balancer 才能发起迁移。
- 检查说明：增量迁移会获取 Oplog，开启 Balancer 的情况下，源端 moveChunk 可能会导致最终目的端数据不一致。

## 修复方法
1. 登录源数据库。
2. 使用如下命令关闭源端 Balancer。
```
sh.stopBalancer()
sh.getBalancerState()
```
3. 重新执行校验任务。

