## 操作场景
该任务指导您在 TCC 模式下进行 Spring Free 开发。

TCC 事务，也可以理解为手动事务。需要用户提供 Try、Confirm、Cancel 接口并进行实现，同时需要保证三个接口的**幂等性**。


## 准备工作
参考 [准备工作](https://cloud.tencent.com/document/product/1224/45966) 文档。

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
用户 A，创建了一个事务分组`group-x3k9s0ns`，在 [分布式事务控制台](https://console.cloud.tencent.com/dtf/) 获取该分组的 TC 集群地址为`127.0.0.1:8080;127.0.0.1:8081;127.0.0.1:8082`。该用户访问密钥的 SecretId 为`SID`，SecretKey 为`SKEY`。需要在业务应用`app-test`上使用该事物时，配置样例为：
``` java
DtfEnv.setServer("app-test");
DtfEnv.setSecretId("SID");
DtfEnv.setSecretKey("SKEY");
DtfEnv.addTxmBroker("group-x3k9s0ns", "127.0.0.1:8080;127.0.0.1:8081;127.0.0.1:8082");
```


### 注册 TCC

对应用内的 TCC 信息进行手动注册。

``` java
// 获取 TCC 实例
TCC.getInstance(Object confirmClassInstance, String confirmMethodName, Object cancelClassInstance,
                String cancelMethodName);
// 或
TCC.getInstance(Object confirmClassInstance, Method confirmMethod, Object cancelClassInstance,
                Method cancelMethod);
// 注册 TCC 信息
TccRegistry.register(String tccName, TCC tccInstance);
```

>!TCC 的名称（tccName）需要保持稳定，并且在一个应用中不可重复。

例如：
``` java
/**
  * 注册 TCC 信息
  */
private static void registerTcc() {
    ITransferService transferService = new TransferService();
    // debit 的 Confirm 和 Cancel
    TccRegistry.register("debit",
            TCC.getInstance(transferService, "confirmDebit", transferService, "cancelDebit"));
    // credit 的 Confirm 和 Cancel
    TccRegistry.register("credit",
            TCC.getInstance(transferService, "confirmCredit", transferService, "cancelCredit"));
}
```

示例中注册了两个 TCC：`debit`（扣款）和`credit`（入账）。

`debit`中参数如下：

| 参数 |  说明 |
| --- | ---|
| `confirmClassInstance` |TransferService 的实例 transferService | 
| `confirmMethodName` | TransferService中 名称为 confirmDebit 的方法 | 
| `cancelClassInstance` | TransferService 的实例 transferService |
| `cancelMethodName` | TransferService 中名称为 cancelDebit |

`credit`中参数如下：

| 参数 | 说明  |
| --- | ---|
| `confirmClassInstance` | TransferService 的实例 transferService |
| `confirmMethodName` | TransferService 中名称为 confirmCredit 的方法 |
| `cancelClassInstance` | TransferService 的实例 transferService |
| `cancelMethodName` | TransferService 中名称为 cancelCredit 的方法 |



### 启用分布式事务服务
在用户应用处理逻辑完成，并且完成**客户端配置**和**注册 TCC**步骤后，可以使用 API 来开启分布式事务服务。
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

#### 提交/回滚主事务
``` java
// 提交主事务
DtfTransaction.commit();
// 回滚主事务
DtfTransaction.rollback();
```

#### 关闭主事务上下文

>!该操作仅关闭**当前线程**的主事务上下文，不会对主事务状态产生影响。

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


### 分支事务管理

分支事务的生命周期可以分为：开启、提交/回滚。

一个 TCC 分支事务中，需要包含 Try、Confirm、Cancel 三个部分。

- 分支事务的 Try、Confirm、Cancel 方法的参数**保持一致**。
- 分支事务的 Try、Confirm、Cancel 方法的前两个参数固定为`Long txId`和`Long branchId`。

**Try 方法**：
- 本地调用 Try 方法时`txId`和`branchId`参数传`null`，其他参数正常传递。
- 返回值为`业务逻辑`需要的返回值。

**Confirm 方法**：
- 返回值固定为 Boolean 类型。
- 仅在返回 true 时视为分支事务 Confirm 成功。
- 返回 false 或抛出异常时，视为分支事务 Confirm 失败。

**Cancel 方法**：
- 返回值固定为 Boolean 类型。
- 仅在返回 true 时视为分支事务 Cancel 成功。
- 返回 false 或抛出异常时，视为分支事务 Cancel 失败。

#### 开启分支事务
``` java
DtfTccBranch.begin(String name, Object[] params);
```

| 参数  | 说明 |
| ---- | ---- |
| `name` | TCC 名称 |
|`params` | Try 方法的业务参数，前两个参数（即`Long txId`和`Long branchId`） 填 null |

#### 检查主事务状态是否为 Trying
仅在 Trying 状态时允许提交分支事务，该接口主要用于防止分支事务 Try 阶段延迟提交本地事务。
``` java
DtfTccBranch.checkTxTrying();
```

#### 结束分支事务

>!该操作仅关闭**当前线程**的分支事务上下文，不会对分支事务状态产生影响。

``` java
DtfTccBranch.end();
```

示例：

``` java
// === 开启主事务 ===

// 开启分支事务1：扣款
Long branchId1 = DtfTccBranch.begin("debit", new Object[] { null, null, this.to, this.amount });
// 执行 Try 方法1
transferService.debit(txId, branchId1, this.to, this.amount);
// 关闭分支事务1上下文
DtfTccBranch.end();

// 开启分支事务2：入账
Long branchId2 = DtfTccBranch.begin("credit", new Object[] { null, null, this.from, this.amount });
// 执行Try方法2
transferService.credit(txId, branchId2, this.from, this.amount);
// 关闭分支事务2上下文
DtfTccBranch.end();

// === 提交 / 回滚主事务 ===
```

>?在执行 Try 方法的本地事务末尾，需要使用`DtfTccBranch.checkTxTrying();`接口防止 Try 阶段延迟提交本地事务。



### 远程请求时传递分布式事务上下文

#### 主调
需要从上下文中提取`groupId`，`txId`，`lastBranchId`三个数据传递到下游。

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
根据上游业务的特性手动获取`groupId`，`txId`，`lastBranchId`三个数据。

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
