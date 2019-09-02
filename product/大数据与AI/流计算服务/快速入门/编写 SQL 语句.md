在实例列表页单击实例名字，并选择“分析开发”页签，进入到实例开发页面。
实例开发页可用于作业的 SQL 开发、作业调试以及发布上线操作。页面如下：
![](https://main.qcloudimg.com/raw/cc08b42a15efcb09119d08cdb3037941.png)


#### 通过界面操作，自动生成 DDL 语句
1. 单击编辑器上方的【选择数据流】，出现如下界面的弹窗。
![](https://main.qcloudimg.com/raw/9ba3cdcd375634313654eaf4e97ad57f.png)
2. 在项目名下拉框中选择在之前新创建的流连接的项目名。
3. 在 Topic 下拉框中选择在作为数据源使用的 Topic。
4. 单击【添加】，在 IDE 中可看到已自动生成 DDL 语句，代码如下图所示：
![](https://main.qcloudimg.com/raw/f73b40bfedaa84cbf023e8cf17ed6e34.png)

#### 继续添加输出 Topic 以及在 IDE 中编写计算逻辑语句
整个 SQL 代码如下：
```
CREATE TABLE `demoSource` (
  `record_time` VARCHAR,
  `user_id` VARCHAR,
  `page_id` VARCHAR
) WITH (
  `type` = 'cdp',
  `project` = 'demo',
  `topic` = 'demoSource'
);
CREATE TABLE `demoSink` (
  `record_time` VARCHAR,
  `pv` BIGINT,
  `uv` BIGINT,
  PRIMARY KEY ( `record_time` )
) WITH (
  `type` = 'cdp',
  `project` = 'demo',
  `topic` = 'demoSink'
);
INSERT INTO demoSink
SELECT
  SUBSTRING(record_time, 1, 16) as record_time,
  count(user_id) as pv,
  count(DISTINCT user_id) as uv
FROM demoSource
GROUP BY SUBSTRING(record_time, 1, 16);
```
>!流计算的 SQL 支持标准 SQL 2003 规范。





