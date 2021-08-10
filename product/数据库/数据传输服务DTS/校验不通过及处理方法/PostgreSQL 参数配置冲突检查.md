## 检查详情
对源和目标数据库参数值进行检查，如下参数值尽量保持一致，如果不一致，则会提示校验警告。警告不会阻塞迁移任务，但是会有一样的业务影响，请评估后自行决定是否修改。

源和目标端的 TimeZone，lc_monetary，lc_numeric，array_nulls，server_encoding，DateStyle，extra_float_digits ，gin_fuzzy_search_limit，xmlbinary，constraint_exclusion 参数值尽量保持一致，如果不一致，则会提示校验警告，不会阻塞迁移流程。


## 修复方法
1. 使用 superuser 帐号登录源数据库。
2. 执行下列示例语句修改对应的参数：
用户可先选择源库的参数修改，如源数据库对应参数不能修改，则需要修改目标库对应参数，目标库的修改请提交工单处理。
```
alter system set timezone='参数值';
alter system set lc_monetary='参数值';
alter system set lc_numeric='参数值';
```
3. 其中 server_encoding 参数源库无法修改，请确认原数据库此参数值，当前云数据库实例仅支持 UTF8 与 LATIN 两种字符集。//目标库是否已经创建，如果已经创建且和源库不一致，需要使用新实例。
