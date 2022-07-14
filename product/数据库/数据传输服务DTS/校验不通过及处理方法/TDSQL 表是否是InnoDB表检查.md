## TDSQL MySQL/MariaDB 检查详情

当目标库是 TDSQL MySQL 或腾讯云数据库 MariaDB 时，只支持迁移或同步 InnoDB 表，如果待迁移或同步对象中含有非 InnoDB 的表，则校验不通过。

## 修复方法

按照界面提示在迁移或同步对象中移除非 InnoDB 的表，然后重新执行校验任务。
