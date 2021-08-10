## 检查详情
检查目标库用户是否与源数据库的用户重复。

## 修复方法
在整实例迁移的场景下，如果目标实例中存在和源实例一模一样的帐号，需要将目标实例中的同名帐号删除。
- 如果目标库中的帐号为初始化帐号，请使用初始化帐号登录至数据库中，执行以下语句。
```
create user 新用户 with password '密码';
grant pg_tencentdb_superuser to 新用户名;
alter user 新用户 with CREATEDB;
alter user 新用户 with CREATEROLE;
```
- 如果目标库中的帐号为新增用户，则使用新创建的用户登录至数据库中，删除冲突用户。
```
drop user 冲突用户;
# 如果冲突用户存在资源依赖，则请先修改依赖对象的owner，如表的owner修改语句为：
alter table 表名 owner to 新用户;
```
当冲突用户删除完成后，请重新执行校验任务。

