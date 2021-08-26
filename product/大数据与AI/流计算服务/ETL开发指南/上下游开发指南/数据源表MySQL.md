## 介绍

MySQL 数据源表支持对 MySQL 数据库的全量和增量读取，并保证 Exactly Once 语义。MySQL 数据源表底层使用 Debezium 来做 CDC（Change Data Capture）。其工作机制如下：

1. 获取一个全局读锁，从而阻塞住其他数据库客户端的写操作。
2. 开启一个可重复读语义的事务，来保证后续在同一个事务内读操作都是在一个一致性快照中完成的。
3. 读取 Binlog 的当前位置。
4. 读取连接器中配置的数据库和表的模式（schema）信息。
5. 释放全局读锁，允许其他的数据库客户端对数据库进行写操作。
6. 扫描全表，当全表数据读取完后，会从第3步中得到的 Binlog 位置获取增量的变更记录。

Flink 作业运行期间会周期性执行快照，记录下 Binlog 位置，当作业崩溃恢复时，便会从之前记录的 Binlog 点继续处理，从而保证 Exactly Once 语义。

## 示例
创建 ETL 作业后，进入**开发调试**页面，在数据源表处单击**添加**。
![](https://main.qcloudimg.com/raw/98805c5711b5de7fcf5cc88327928cee.png)
根据示例正确填写 MySQL 数据源表相应信息。
![](https://main.qcloudimg.com/raw/a50e86b8df13637e02d66eac7afa3454.png)
如信息填写无误，ETL 作业会自动获取数据源表中所有字段的名称和类型。
![](https://main.qcloudimg.com/raw/838c4911037f0003509ac09e26eed218.png)

## 类型映射

<table>
  <tr>
    <th><b>MySQL 字段类型</th>
    <th><b>Flink 字段类型</th>
  </tr>
  <tr>
    <td>TINYINT</td>
    <td>TINYINT</td>
  </tr>
  <tr>
    <td>SMALLINT</td>
    <td rowspan="2">SMALLINT</td>
  </tr>
  <tr>
    <td>TINYINT UNSIGNED</td>
  </tr>
  <tr>
    <td>INT</td>
    <td rowspan="3">INT</td>
  </tr>
  <tr>
    <td>MEDIUMINT</td>
  </tr>
  <tr>
    <td>SMALLINT UNSIGNED</td>
  </tr>
  <tr>
    <td>BIGINT</td>
    <td rowspan="2">BIGINT</td>
  </tr>
  <tr>
    <td>INT UNSIGNED</td>
    <td></td>
  </tr>
  <tr>
    <td>BIGINT UNSIGNED</td>
    <td>DECIMAL(20, 0)</td>
  </tr>
  <tr>
    <td>FLOAT</td>
    <td>FLOAT</td>
  </tr>
  <tr>
    <td>DOUBLE</td>
    <td rowspan="2">DOUBLE</td>
  </tr>
  <tr>
    <td>DOUBLE PRECISION</td>
  </tr>
  <tr>
    <td>NUMERIC(p, s)</td>
    <td rowspan="2">DECIMAL(p, s)</td>
  </tr>
  <tr>
    <td>DECIMAL(p, s)</td>
  </tr>
  <tr>
    <td>BOOLEAN</td>
    <td rowspan="2">BOOLEAN</td>
  </tr>
  <tr>
    <td>TINYINT(1)</td>
  </tr>
  <tr>
    <td>DATE</td>
    <td>DATE</td>
  </tr>
  <tr>
    <td>TIME [(p)]</td>
    <td>TIME [(p)] [WITHOUT TIMEZONE]</td>
  </tr>
  <tr>
    <td>DATETIME [(p)]</td>
    <td>TIMESTAMP [(p)] [WITHOUT TIMEZONE]</td>
  </tr>
  <tr>
    <td rowspan="2">TIMESTAMP [(p)]</td>
    <td>TIMESTAMP [(p)]</td>
  </tr>
  <tr>
    <td>TIMESTAMP [(p)] WITH LOCAL TIME ZONE</td>
  </tr>
  <tr>
    <td>CHAR(n)</td>
    <td rowspan="3">STRING</td>
  </tr>
  <tr>
    <td>VARCHAR(n)</td>
  </tr>
  <tr>
    <td>TEXT</td>
  </tr>
  <tr>
    <td>BINARY</td>
    <td rowspan="3">BYTES</td>
  </tr>
  <tr>
    <td>VARBINARY</td>
  </tr>
  <tr>
    <td> BLOB</td>
  </tr>
</table>

## 注意事项
### 用户权限
用于同步的源数据库的用户必须拥有以下权限 SHOW DATABASES、REPLICATION SLAVE、REPLICATION CLIENT、SELECT 和 RELOAD。

### 数据库参数设置
binlog_row_image 参数的参数运行值应当设置为 FULL。

## WITH 参数
MySQL 数据源表基于数据库 MySQL CDC 开发，两者具有相同的 WITH 参数，具体参数配置方式可参见 [数据库 MySQL CDC](https://cloud.tencent.com/document/product/849/52698)。

