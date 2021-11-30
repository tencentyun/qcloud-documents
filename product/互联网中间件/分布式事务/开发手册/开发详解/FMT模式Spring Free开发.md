## 操作场景
该任务指导您在 FMT 模式下进行 Spring Free 开发。

FMT 事务，也可以理解为框架托管事务。需要用户仅需要在 **FMT 规范**下正常实现业务逻辑即可实现分布式事务。相对于 TCC 事务，省去了编写 Confirm、Cancel 的代码工作。
FMT 事务的实现原理：代理用户执行 PrepareStatement 和 CreateStatement 操作，对执行的 DML 语句进行解析，记录前后象，并生成 UNDO 信息。鉴于此，FMT 对用户使用的数据库和 SQL 语句会有一定的要求，详见  [FMT 规范](https://cloud.tencent.com/document/product/1224/46038)。


## 准备工作
- 参考 [准备工作](https://cloud.tencent.com/document/product/1224/45966) 文档，完成环境配置和开发前准备。
- 参考 [快速部署](https://cloud.tencent.com/document/product/1224/45967) 文档，执行 FMT 初始化脚本.

## 开发步骤
### Maven 配置
通过配置业务代码的 pom.xml 文件，可以引入 DTF 的 SDK 到您的工程中。

配置中的 ${dtf.version} 可以参考 [Release Note](https://cloud.tencent.com/document/product/1224/44764) 中，选择**最新版本（推荐）**或指定版本。

``` xml
<dependency>
    <groupId>com.tencent.cloud</groupId>
    <artifactId>dtf-core</artifactId>
    <version>${dtf.version}</version>
</dependency>
```

### 客户端配置

在客户端中，使用以下 API 进行 DTF 的配置设置。

``` java
DtfEnv.setServer(String server);
DtfEnv.setSecretId(String secretId);
DtfEnv.setSecretKey(String secretKey);
DtfEnv.addTxmBroker(String groupId, String txmBrokerList);
```
配置项说明：

| 配置项        | 数据类型 | 必填 | 默认值 | 描述                                                         |
| ------------- | -------- | ---- | ------ | ------------------------------------------------------------ |
| groupId       | String   | 是   | 无     | 用户的事务分组 ID。                                             |
| txmBrokerList | String   | 是   | 无     | TC 集群节点列表。                                               |
| secretId      | String   | 是   | 无     | 用户的腾讯云 SecretID。                                         |
| secretKey     | String   | 是   | 无     | 用户的腾讯云 SecretKey。                                        |
| server        | String   | 是   | 无     | 客户端服务标识，一个事务分组下，同一服务需要使用相同的标识。 |
| dtf.env.fmt  |  Boolean  | 否  | true  | 启动时会对 DB 进行大量初始化工作，若不需使用 fmt 建议禁用。 |

通常情况下，仅需要在使用`DtfEnv.addTxmBroker()`配置一个事务分组。例如：
用户 A，创建了一个事务分组`group-x3k9s0ns`，在 [分布式事务控制台](https://console.cloud.tencent.com/dtf/) 获取该分组的 TC 集群地址为`127.0.0.1:8080;127.0.0.1:8081;127.0.0.1:8082`。该用户访问密钥的 SecretId 为 `SID`，SecretKey 为 `SKEY`。需要在业务应用`app-test`上使用该事物时，配置样例为：
``` java
DtfEnv.setServer("app-test");
DtfEnv.setSecretId("SID");
DtfEnv.setSecretKey("SKEY");
DtfEnv.addTxmBroker("group-x3k9s0ns", "127.0.0.1:8080;127.0.0.1:8081;127.0.0.1:8082");
```


### 代理数据源

对应用内的数据源（DataSource）信息进行手动代理。

``` java
DtfDataSourceProxyUtil.dataSourceProxy(String dataSourceName, DataSource dataSource);
```

>!数据源的名称（dataSourceName）需要保持稳定，并且在一个应用中不可重复。

例如：
``` java
/**
  * 代理数据源
  */
private static MysqlDataSource proxyDataSource() {
    MysqlDataSource ds = new MysqlDataSource();
    ds.setUrl(URL1);
    ds.setUser(USER1);
    ds.setPassword(PASSWORD);
    return DtfDataSourceProxyUtil.dataSourceProxy("DATA_SOURCE1", ds);
}
```

### 启用分布式事务服务
在用户应用处理逻辑完成，并且完成**客户端配置**和**代理数据源**步骤后，可以使用 API 来开启分布式事务服务。
``` java
// 启动分布式事务客户端
DtfClient.start();
```

### 主事务管理

主事务的生命周期可以分为：开启、提交/回滚。

#### 开启主事务
在**客户端配置**步骤中只添加了一个事务分组时，可以使用**开启主事务：使用默认事务分组**。添加了多个事务分组时，必须使用**开启主事务：使用指定事务分组**。

``` java
// 开启主事务：使用默认事务分组
DtfTransaction.begin(Integer timeout);
// 开启主事务：使用指定事务分组
DtfTransaction.begin(Integer timeout, String groupId)
```

#### 标识一次FMT事务
每一次数据库操作都需要进行标识。
``` java
DtfContextHolder.get().pushBranchType(DTF.BranchType.FMT);
```

#### 提交/回滚主事务
``` java
// 提交主事务
DtfTransaction.commit();
// 回滚主事务
DtfTransaction.rollback();
```

#### 关闭主事务上下文

>?该操作仅关闭**当前线程**的主事务上下文，不会对主事务状态产生影响。

``` java
DtfTransaction.end();
```

使用示例：
``` java
public boolean execute() {
    // 业务检查
    Long txId = DtfTransaction.begin(10000);
    try {
        // 执行各个分支事务或业务逻辑
        // 标识一次FMT事务
        DtfContextHolder.get().pushBranchType(DTF.BranchType.FMT);
        // ... excute SQL
        // 提交主事务
        DtfTransaction.commit();
        return true;
    } catch (Throwable e) {
        // 回滚主事务
        DtfTransaction.rollback();
        LOG.error("Bank transfer failed.", e);
        return false;
    } finally {
        // 关闭主事务上下文
        DtfTransaction.end();
    }
}
```


### 远程请求时传递分布式事务上下文

#### 主调
需要从上下文中提取 `groupId`、`txId`、`lastBranchId` 三个数据传递到下游。

使用以下 API 提取：
``` java
String groupId = DtfContextHolder.get().getGroupId();
Long txId = DtfContextHolder.get().getTxId();
Long lastBranchId = DtfContextHolder.get().getBranchIdStack().peek();
```

建议放到下列 Header 的 key 中，下游可以通过 DTF SDK 自行注入。
``` properties
# Header key 的常量 ClientConstant.HTTP_HEADER.GROUP_ID
DTF-Group-ID: ${GroupId}
# Header key 的常量 ClientConstant.HTTP_HEADER.TX_ID
DTF-Tx-ID: ${TxId}
# Header key 的常量 ClientConstant.HTTP_HEADER.LAST_BRANCH_ID
DTF-Last-Branch-ID: ${LastBranchId}
```

#### 被调
根据上游业务的特性手动获取 `groupId`、`txId`、`lastBranchId` 三个数据。

如果上游使用的是 DTF 封装的 RestTemplate 或 Fegin，请从以下请求头中获取：
``` properties
# Header key 的常量 ClientConstant.HTTP_HEADER.GROUP_ID
DTF-Group-ID: ${GroupId}
# Header key 的常量 ClientConstant.HTTP_HEADER.TX_ID
DTF-Tx-ID: ${TxId}
# Header key 的常量 ClientConstant.HTTP_HEADER.LAST_BRANCH_ID
DTF-Last-Branch-ID: ${LastBranchId}
```

如果是其他方式传递，则需要用户按照接口协议自行获取。

获取了三个数据后，通过 API 绑定分布式事务上下文。
``` java
DtfTransaction.bind(${GroupId}, ${TxId}, ${LastBranchId});
```
