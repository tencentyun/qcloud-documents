## 检查详情
- 检查要求：对源和目标数据库的如下参数值进行检查，如果源和目标库的参数值不一致，则会提示校验警告。警告不会阻塞迁移任务，但是会对业务有一定的影响，请评估后自行决定是否修改。
TimeZone，lc_monetary，lc_numeric，array_nulls，server_encoding，DateStyle，extra_float_digits ，gin_fuzzy_search_limit，xmlbinary，constraint_exclusion。

- 业务影响：如果参数未设置一致，可能会导致源库和目标库的数据不一致，具体影响如下。
  - TimeZone：设置实例的时区，此参数值如果不一致，可能会导致迁移后数据错误。
  - lc_monetary：设置实例货币模式，此参数值如果不一致，可能会导致迁移后货币数字错误。
  - lc_numeric：设置实例数字模式，此参数值不一致，可能会导致迁移后数据错误。
  - array_nulls：设置数组是否允许为空，此参数值不一致，可能会导致迁移数据不一致，某一些数据无法迁移成功。
  - server_encoding：设置实例的字符集，此参数值不一致，可能会导致数据保存乱码。
  - DateStyle：设置日期显示格式，此参数值不一致，可能会导致数据无法迁移成功。
  - extra_float_digits ：设置浮点值的输出精度，此参数值不一致，会影响数据精度问题，在高精度的数据库使用场景，会导致迁移后的数据不一致问题。
  - gin_fuzzy_search_limit：设置 GIN 索引返回的集合尺寸的软上限，此参数值不一致，会导致迁移后数据显示结果不一致的问题。
  - xmlbinary：设置 xml 函数转换的结果问题，此参数值不一致，可能会导致在目标库中执行相应函数时与源库的行为不一致的问题。
  - constraint_exclusion：设置约束是否生效，此参数值不一致，可能会导致迁移后数据不一致的问题。 


## 修复方法
1. 使用 superuser 账号登录源数据库。
2. 执行下列示例语句修改对应的参数：
   - 用户可先选择源库的参数修改，如源数据库对应参数不能修改，则需要修改目标库对应参数，目标库的修改请通过 [在线支持](https://cloud.tencent.com/online-service?from=connect-us) 处理。
   - server_encoding 参数无法在源库修改，如果该参数异常，请检查该参数在目标库是否已经创建，如果已经创建，且和源库不一致，则需要申请新的实例，如果未创建，则参考如下方法修改（当前云数据库实例仅支持 UTF8 与 LATIN 两种字符集）。
```
alter system set timezone='参数值';
alter system set lc_monetary='参数值';
alter system set lc_numeric='参数值';
```

