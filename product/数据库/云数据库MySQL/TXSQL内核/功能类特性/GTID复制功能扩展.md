## 功能介绍
GTID 模式下复制支持 create as select、create/drop temporary table，同时更新事务表和非事务表等语句。

## 适用场景
该功能适用于需要对 GTID 的功能限制进行适当破除需求的场景。

## 使用说明
增加参数 cdb_more_gtid_feature_supported 用于该功能开关，默认为 off。
当 gtid_mode=ON、enforce_gtid_consistency=ON 复制支持如下用法：
- `create table t2 select * from t;`
- `begin;create temporary table xx (id int); insert into xx select *from t2;insert into t1 select * from xx;commit;`
