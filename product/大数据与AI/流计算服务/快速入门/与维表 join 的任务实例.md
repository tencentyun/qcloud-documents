实际需求场景里 join 操作比较常见，这里在之前单表聚合统计的基础上演示如何与维表 join 后进行聚合计算。
1. 在 TencentDB 里创建维表
```
 CREATE TABLE `dim_page` (
  `page_id` varchar(32) NOT NULL,
  `page_name` varchar(32) NOT NULL,
  PRIMARY KEY (`page_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 
```
2. 添加数据进维表
![](https://main.qcloudimg.com/raw/f512d88911729c8a9baecd0a8ee2add5.png)
3. 创建结果表
 ```
 CREATE TABLE `demo_join_sink` (
  `record_time` varchar(32) NOT NULL,
  `page_name` varchar(32) NOT NULL,
  `pv` bigint(20) NOT NULL,
  `uv` bigint(20) NOT NULL,
  PRIMARY KEY (`record_time`,`page_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```
4. 新建 Topic 
 按之前的操作在 project 再新建一个topic当做join的结果输出流，用作记录按 record_time、page_name聚合后的 pv、uv 数。
 ![](https://main.qcloudimg.com/raw/d52ea278487645f5e6100ee12bd2b278.png)
5. 新建 Integrator
 新建 Integrator 与刚才创建的 demo_join_sink 表绑定并启动 Integrator。
  在之前代码基础上添加以下代码，补全 TencentDB 相关信息。 
 ```
 CREATE TABLE `dimPage` (
  `page_id` VARCHAR,
  `page_name` VARCHAR,
  PRIMARY KEY(`page_id`)
 ) WITH (
  `type` = 'cdb',
  `instanceId` = '',
  `user` = '',
  `password` = '',
  `database` = '',
  `table` = 'dim_page'
);
CREATE TABLE `demoJoinSink` (
  `record_time` VARCHAR,
  `page_name` VARCHAR,
  `pv` BIGINT,
  `uv` BIGINT,
  PRIMARY KEY ( `record_time`, `page_name` )
) WITH (
  `type` = 'cdp',
  `project` = 'demo',
  `topic` = 'demoJoinSink'
);

 INSERT INTO demoJoinSink
 SELECT
  SUBSTRING(a.record_time, 1, 16) as record_time,
  b.page_name as page_name,
  count(a.user_id) as pv,
  count(DISTINCT a.user_id) as uv
FROM demoSource a
JOIN dimPage b
on a.page_id = b.page_id
GROUP BY SUBSTRING(a.record_time, 1, 16),b.page_name;
```

6. 调试、保存、发布运行
 按照之前的流程调试、保存、发布运行就可以看到两表 join 后的计算结果了。
