云数据库 MySQL 目前支持以下版本：MySQL 5.7、MySQL 5.6、MySQL 5.5，各个版本相关特性，请参见 [官方文档](https://dev.mysql.com/doc/refman/5.7/en/)。MySQL 官方服务生命周期支持策略如下：

| Release            | GA Date | Premier Support End | Extended Support End | Sustaining Support End |
| :------------------ | :------- | :------------ | :------------- | :-----------|
| MySQL Database 5.0 | Oct-05  | Dec-11              | Not Available        | Indefinite             |
| MySQL Database 5.1 | Dec-08  | Dec-13              | Not Available        | Indefinite             |
| MySQL Database 5.5 | Dec-10  | Dec-15              | Dec-18               | Indefinite             |
| MySQL Database 5.6 | Feb-13  | Feb-18              | Feb-21               | Indefinite             |
| MySQL Database 5.7 | Oct-15  | Oct-20              | Oct-23               | Indefinite             |
| MySQL Database 8.0 | Apr-18  | Apr-23              | Apr-26               | Indefinite             |

>?
> - MySQL 5.5 官方延长服务截止至2018年12月，过期后没有明确的服务支持说明，可能问题修复周期较长，强烈建议您使用更高版本的 MySQL。
> - MySQL 5.6 及其以上版本不再支持 MyISAM 存储引擎，建议您使用性能更好、更稳定的 InnoDB 引擎。
> - 目前 MySQL 5.6、5.7 版本支持三种复制方式：异步、半同步、强同步；5.5 版本支持异步方式。
