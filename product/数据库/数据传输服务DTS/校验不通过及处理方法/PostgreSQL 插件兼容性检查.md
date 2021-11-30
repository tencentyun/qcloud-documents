
## 检查详情
- 检查要求：检查源库已存在的插件，目标库是否也同样存在。
在迁移过程前，无需在目标库中创建插件，迁移过程中 DTS 会自动为目标实例创建与源端匹配的插件。如果目标端无法创建对应的插件，或者目标库插件版本与源库不一致时，则会提示校验警告。警告不会阻塞迁移任务，但是会对业务造成一样的影响。
   
- 业务影响：PostgreSQL 的插件较多，大多数插件兼容性问题并不影响数据迁移，但是存储引擎类的插件兼容性问题（例如 timescaledb，pipelinedb，postgis），可能会导致迁移任务失败。

## 修复方法
- 非引擎类的插件兼容性问题（如 pg_hint_plan，pg_prewarm，tsearch2，hll，rum，zhparser），一般可以忽略，用户可自行评估业务情况处理。
- 引擎类的插件兼容性问题（如 timescaledb，pipelinedb，postgis），建议通过 [在线支持](https://cloud.tencent.com/online-service?from=connect-us) 处理。

