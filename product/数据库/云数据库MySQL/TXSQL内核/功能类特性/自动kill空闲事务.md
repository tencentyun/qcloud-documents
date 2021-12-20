## 功能介绍
Kill 超过一定时长的空闲事务，及时释放资源。

## 支持版本
- 内核版本 MySQL 5.6 20180915 及以上
- 内核版本 MySQL 5.7 20180918 及以上
- 内核版本 MySQL 8.0 20200630 及以上

## 适用场景
对于处于开启事务状态的连接（显示使用 begin、start transaction 或者隐式开启事务），如果超时时间内没有下一条语句执行，kill 连接。

## 使用说明
通过参数 cdb_kill_idle_trans_timeout 控制是否开启该功能，0为不用，非0启用，与 session的wait_timeout 值相比取较小值。

| 参数名                      | 动态 | 类型  | 默认 | 参数值范围    | 说明                                                         |
| --------------------------- | ---- | ----- | ---- | ------------- | ------------------------------------------------------------ |
| cdb_kill_idle_trans_timeout | YES  | ulong | 0    | [0, 31536000] | 0代表关闭该功能，否则代表会 kill 掉 cdb_kill_idle_trans_timeout 秒的空闲事务 |

>?用户目前无法直接修改以上参数的参数值，如需修改可 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行修改。
>
