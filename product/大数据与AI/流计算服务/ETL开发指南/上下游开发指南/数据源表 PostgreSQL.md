## 介绍
PostgreSQL 数据源表支持对 PostgreSQL 数据库的全量和增量读取，并保证 Exactly Once 语义。PostgreSQL 数据源表底层使用 Debezium 来做 CDC（Change Data Capture）。其工作机制如下：
1. 开启一个 ERIALIZABLE、READ ONLY、DEFERRABLE 级别的事务，主要是为了确保后续其他客户端对数据的修改对当前事务不可见,。
2. 为所有被追踪的表开启一个 ACCESS SHARE MODE 锁，这个锁会防止 DDL 语句进行表结构的变更，但不会影响正常的数据变更操作。
3. 读取 transaction log 的当前位置。
4. 扫描追踪表，并为每条数据生成同步记录，并向下游发送。
5. 提交事务，记录全量阶段完成，会从第3步中得到的 transaction log 位置获取增量的变更记录。

Flink 作业运行期间会周期性执行快照，记录下 transaction log 位置，当作业崩溃恢复时，便会从之前记录的 transaction log 点继续处理，从而保证 Exactly Once 语义。

## 示例
创建 ETL 作业后，进入**开发调试**页面，在数据源表处单击**添加**。
![](https://main.qcloudimg.com/raw/98805c5711b5de7fcf5cc88327928cee.png)
根据示例正确填写 Postgresql 数据源表相应信息。
![](https://main.qcloudimg.com/raw/3164db6200d0d1421b7a7e50430defb3.png)
如信息填写无误，ETL 作业会自动获取数据源表中所有字段的名称和类型。
![](https://main.qcloudimg.com/raw/838c4911037f0003509ac09e26eed218.png)



## 类型映射

<table>
  <tr>
    <th><b>Postgres CDC 字段类型</th>
    <th><b>Flink 字段类型</th>
  </tr>
  <tr>
    <td>SMALLINT</td>
    <td rowspan="4">SMALLINT</td>
  </tr>
  <tr>
    <td>INT2</td>
  </tr>
  <tr>
    <td>SMALLSERIAL</td>
  </tr>
  <tr>
    <td>SERIAL2</td>
  </tr>
   <tr>
    <td>INTEGER</td>
    <td rowspan="2">INT</td>
  </tr>
  <tr>
    <td>SERIAL</td>
  </tr>
  <tr>
    <td>BIGINT</td>
    <td rowspan="2">BIGINT</td>
  </tr>
  <tr>
    <td>BIGSERIAL</td>
  </tr>
  <tr>
    <td>REAL</td>
    <td rowspan="2">FLOAT</td>
  </tr>
  <tr>
    <td>FLOAT4</td>
  </tr>
    <tr>
    <td>FLOAT8</td>
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
    <td>BOOLEAN</td>
  </tr>
  <tr>
    <td>DATE</td>
    <td>DATE</td>
  </tr>
  <tr>
    <td>TIME [(p)] [WITHOUT TIMEZONE]</td>
    <td>TIME [(p)] [WITHOUT TIMEZONE]</td>
  </tr>
  <tr>
    <td>TIMESTAMP [(p)] [WITHOUT TIMEZONE]</td>
    <td>TIMESTAMP [(p)] [WITHOUT TIMEZONE]</td>
  </tr>
  <tr>
    <td>CHAR(n)</td>
    <td rowspan="5">STRING</td>
  </tr>
  <tr>
    <td>CHARACTER(n)</td>
  </tr>
  <tr>
    <td>VARCHAR(n)</td>
  </tr>
  <tr>
    <td>CHARACTER VARYING(n)</td>
  </tr>
  <tr>
    <td>TEXT</td>
  </tr>
  <tr>
    <td>BYTEA</td>
     <td>BYTES</td>
  </tr>
</table>

## 注意事项
### 用户权限
用于同步的源数据库的用户必须拥有以下权限 REPLICATION、LOGIN、SCHEMA、DATABASE、SELECT。

### 版本限制
仅支持的 PostgreSQL 版本为9.6及以上版本。

### 数据库参数设置
wal_level 参数的参数运行值应当设置为 logical。

## WITH 参数
PostgreSQL 数据源表基于 PostgreSQL CDC 开发，两者具有相同的 WITH 参数，具体参数配置方式可参见 [数据库 PostgreSQL CDC](https://cloud.tencent.com/document/product/849/60315)。

