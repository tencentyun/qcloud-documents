本文介绍使用 DTS 数据迁移功能从 PostgreSQL 迁移数据至腾讯云云原生数据库 TDSQL-C PostgreSQL 的操作指导。

TDSQL-C PostgreSQL 迁移至 TDSQL-C PostgreSQL 场景的迁移要求，与本场景的要求一致，可参考本场景相关内容。

## 注意事项
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您的数据库配置过低，建议您在业务低峰期进行迁移。
- 外网实例迁移时，请确保源实例服务在外网环境下可访问，并且要保持外网连接的稳定性，当网络出现波动或者故障时会导致迁移失败，迁移一旦失败，就需要重新发起迁移任务。
- 除腾讯云数据库 PostgreSQL 之外的其他 PostgreSQL 作为源端时，必须要求源端库具有 replication 权限，否则迁移前校验步骤将不通过。

## 前提条件
- 已 [创建 TDSQL-C PostgreSQL版](https://cloud.tencent.com/document/product/1003/30505)。
- 源数据库和目标数据库符合迁移功能和版本要求，请参见 [数据迁移支持的数据库](https://cloud.tencent.com/document/product/571/58686) 进行核对。
- 已完成 [准备工作](https://cloud.tencent.com/document/product/571/59968)。
- 源数据库需要具备的权限如下：
  - 源库为腾讯云数据库 PostgreSQL 之外的其他 PostgreSQL 时，要求源端库必须具有 replication 权限。  
  - 源库腾讯云数据库 PostgreSQL，要求源数据库必须为创建云数据库实例时的初始化用户。  
  - 如果部分表或者对象无权限，可使用高权限用户执行如下示例语句，对无权限的对象分别授予权限：  
```
grant select on table 表名 to 用户名;
grant select on SEQUENCE 序列名 to 用户名;
grant connect on database 库名 to 用户名;
grant select on large object 大对象oid to 用户名;
GRANT USAGE ON SCHEMA 模式名 to 用户名;
```
- 目标数据库必须为创建云数据库实例时的初始化用户。 
   - 如果目标实例中包含待迁移的 database，且 database 的 owner 非当前迁移用户，可执行以下语句将 database 授予迁移用户：
```
alter database 库名 owner to 迁移用户;
```
   - 如果目标迁移账户为非 `pg_tencentdb_superuser` 角色用户，在校验时，会提示“目标实例权限检查失败，无法获取Schema列表”，请使用如下语句为迁移用户赋予初始化用户权限：
```
grant pg_tencentdb_superuser to 迁移用户;
```

## 应用限制
- 相互关联的数据对象需要同时迁移，否则会导致迁移失败。常见的关联关系：视图引用表、视图引用视图、存储过程/函数/触发器引用视图/表、主外键关联表等。
- 为保障迁移效率，CVM 自建实例迁移不支持跨地域迁移。如需要跨地域迁移，请选择公网接入方式。
- 如果进行整个实例迁移，目标库中不能存在与源库同名的用户和角色。
- **迁移类型**选择**全量 + 增量迁移**时，源数据库中的表必须有主键，否则会出现源库和不目标库数据不一致，对于无主键的表，建议选择**全量迁移**。

## 操作限制
- 迁移过程中请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
- 在结构迁移、全量迁移和增量迁移阶段，请勿执行 DDL 操作，大对象操作，否则会导致迁移数据不一致。
- 如果仅执行全量数据迁移，仅会迁移在发起迁移这一刻之前的数据，如果在迁移过程中向源实例中写入新的数据，源库和目标库的数据会出现不一致。针对有数据写入的场景，为实时保持数据一致性，建议选择全量 + 增量数据迁移。

## 环境要求
>?如下环境要求，系统会在启动迁移任务前自动进行校验，不符合要求的系统会报错。如果用户能够识别出来，可以 参考 [校验项检查要求](https://cloud.tencent.com/document/product/571/61639) 自行修改，如果不能则等系统校验完成，按照报错提示修改。

<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源数据库要求</td>
<td><ul>
<li>源库和目标库网络能够连通。</li>
<li>源库所在的服务器需具备足够的出口带宽，否则将影响迁移速率。</li>
<li>实例参数要求：
<ul>
<li>增量迁移时源库 wal_level 参数值必须为 logical。</li>
<li>增量迁移时源库 max_replication_slots 值必须大于待迁移的 database 数量。</li>
<li>增量迁移时源库 max_wal_senders 值必须大于待迁移的 database 数量。</li></ul>
</ul></td>
<tr> 
<td>目标数据库要求</td>
<td>
<li>仅全量迁移时，目标数据库实例版本必须大于源库实例版本；增量迁移时，支持10.x以上的版本互相迁移。</li>
<li>目标库的可用空间大小须是源库待迁移实例的1.2倍以上。（数据增量迁移会执行 update，delete 操作，导致数据库的表产生碎片，因此迁移完成后目标数据库的表存储空间很可能会比源实例的表存储空间大，这主要是因为源端和目标端不同的 autovcauum 触发条件导致。）</li>
<li>目标库不能有和源库同名的迁移对象。如用户名不能相同，不能存在相同名的表。</li>
<li>增量迁移时目标库 max_worker_processes 值必须大于 max_logical_replication_workers。</li>
</tr>
</table>

## 操作步骤
PostgreSQL 到 TDSQL-C PostgreSQL 的迁移，与 [PostgreSQL 到 PostgreSQL 的迁移](https://cloud.tencent.com/document/product/571/59975) 步骤一致，请参考相关内容进行操作。
