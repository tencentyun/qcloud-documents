# TCC事务

TCC事务，也可以理解为手动事务。需要用户提供Try，Confirm，Cancel接口并进行实现，同时需要保证三个接口的`幂等性`。

## 准备工作

参考[准备工作](https://tcloud-doc.isd.com/document/product/1224/45966)章节进行。

## Maven配置

通过配置业务代码的pom.xml文件，可以引入DTF的SDK到您的工程中。

> 配置中的${dtf.version}可以参考[Release Note](https://tcloud-doc.isd.com/document/product/1224/44764)中，选择`最新版本（推荐）`或指定版本。

``` xml
<dependency>
    <groupId>com.tencent.cloud</groupId>
    <artifactId>dtf-core</artifactId>
    <version>${dtf.version}</version>
</dependency>
```

## 客户端配置

在客户端中，使用以下API进行DTF的配置设置。

``` java
DtfEnv.setServer(String server);
DtfEnv.setSecretId(String secretId);
DtfEnv.setSecretKey(String secretKey);
DtfEnv.addTxmBroker(String groupId, String txmBrokerList);
```

| 配置项        | 数据类型 | 必填 | 默认值 | 描述                                                         |
| ------------- | -------- | ---- | ------ | ------------------------------------------------------------ |
| groupId       | String   | 是   | 无     | 用户的事务分组ID                                             |
| txmBrokerList | String   | 是   | 无     | TC集群节点列表                                               |
| secretId      | String   | 是   | 无     | 用户的腾讯云SecretID                                         |
| secretKey     | String   | 是   | 无     | 用户的腾讯云SecretKey                                        |
| server        | String   | 是   | 无     | 客户端服务标识，一个事务分组下，同一服务需要使用相同的标识。 |

> 注：通常情况下，仅需要在使用`DtfEnv.addTxmBroker()`配置一个事务分组。

例如：

用户A，创建了一个事务分组`group-x3k9s0ns`，在[分布式事务控制台](https://console.cloud.tencent.com/dtf/)获取该分组的TC集群地址为`127.0.0.1:8080;127.0.0.1:8081;127.0.0.1:8082`。该用户访问密钥的SecretId为`SID`，SecretKey为`SKEY`。需要在业务应用`app-test`上使用该事物时，配置样例为：

``` java
DtfEnv.setServer("app-test");
DtfEnv.setSecretId("SID");
DtfEnv.setSecretKey("SKEY");
DtfEnv.addTxmBroker("group-x3k9s0ns", "127.0.0.1:8080;127.0.0.1:8081;127.0.0.1:8082");
```

---

## 注册TCC

对应用内的TCC信息进行手动注册。

``` java
// 获取TCC实例
TCC.getInstance(Object confirmClassInstance, String confirmMethodName, Object cancelClassInstance,
                String cancelMethodName);
// 或
TCC.getInstance(Object confirmClassInstance, Method confirmMethod, Object cancelClassInstance,
                Method cancelMethod);
// 注册TCC信息
TccRegistry.register(String tccName, TCC tccInstance);
```

> 注：TCC的名称（tccName）需要保持稳定，并且在一个应用中不可重复。

例如：

``` java
/**
  * 注册TCC信息
  */
private static void registerTcc() {
    ITransferService transferService = new TransferService();
    // debit的confirm和cancel
    TccRegistry.register("debit",
            TCC.getInstance(transferService, "confirmDebit", transferService, "cancelDebit"));
    // credit的confirm和cancel
    TccRegistry.register("credit",
            TCC.getInstance(transferService, "confirmCredit", transferService, "cancelCredit"));
}
```

示例中注册了两个TCC：`debit`（扣款）和`credit`（入账）。

`debit`中

- `confirmClassInstance`：TransferService的实例transferService
- `confirmMethodName`：TransferService中名称为confirmDebit的方法
- `cancelClassInstance`：TransferService的实例transferService
- `cancelMethodName`：TransferService中名称为cancelDebit

`credit`中

- `confirmClassInstance`：TransferService的实例transferService
- `confirmMethodName`：TransferService中名称为confirmCredit的方法
- `cancelClassInstance`：TransferService的实例transferService
- `cancelMethodName`：TransferService中名称为cancelCredit的方法

---

## 启用分布式事务服务

在用户应用处理逻辑完成，并且完成`客户端配置`和`注册TCC`步骤后，可以使用API来开启分布式事务服务。

``` java
// 启动分布式事务客户端
DtfClient.start();
```

> 注：该API会启动分布式事务监听。

---

## 主事务管理

主事务的生命周期可以分为：`开启`，`提交`/`回滚`。

开启主事务

> 注：在`客户端配置`步骤中只添加了一个事务分组时，可以使用`开启主事务：使用默认事务分组`。添加了多个事务分组时，必须使用`开启主事务：使用指定事务分组`。

``` java
// 开启主事务：使用默认事务分组
DtfTransaction.begin(Integer timeout);
// 开启主事务：使用指定事务分组
DtfTransaction.begin(Integer timeout, String groupId)
```

提交/回滚主事务

``` java
// 提交主事务
DtfTransaction.commit();
// 回滚主事务
DtfTransaction.rollback();
```

关闭主事务上下文

> 注：该操作仅关闭`当前线程`的主事务上下文，不会对主事务状态产生影响。

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

---

## 分支事务管理

分支事务的生命周期可以分为：`开启`，`提交`/`回滚`。

一个TCC分支事务中，需要包含Try，Confirm，Cancel三个部分。

- 分支事务的Try，Confirm，Cancel方法的参数`保持一致`。
- 分支事务的Try，Confirm，Cancel方法的前两个参数固定为`Long txId`和`Long branchId`。

- Try方法：
  - 本地调用Try方法时`txId`和`branchId`参数传`null`，其他参数正常传递。
  - 返回值为`业务逻辑`需要的返回值。
- Confirm方法：
  - 返回值固定为`boolean`类型。
  - 仅在返回`ture`时视为分支事务`Confirm成功`。
  - 返回`false`或`抛出异常`时，视为分支事务`Confirm失败`。
- Cancel方法：
  - 返回值固定为`boolean`类型。
  - 仅在返回`ture`时视为分支事务`Cancel成功`。
  - 返回`false`或`抛出异常`时，视为分支事务`Cancel失败`。

开启分支事务

``` java
DtfTccBranch.begin(String name, Object[] params);
```

`name`：TCC名称。

`params`：Try方法的业务参数，前两个参数（即`Long txId`和`Long branchId`）填null。

检查主事务状态是否为Trying

> 仅有Trying状态的时候允许提交分支事务，该接口主要用于防止分支事务Try阶段延迟提交本地事务。

``` java
DtfTccBranch.checkTxTrying();
```

结束分支事务

> 注：该操作仅关闭`当前线程`的分支事务上下文，不会对分支事务状态产生影响。

``` java
DtfTccBranch.end();
```

示例：

``` java
// === 开启主事务 ===

// 开启分支事务1：扣款
Long branchId1 = DtfTccBranch.begin("debit", new Object[] { null, null, this.to, this.amount });
// 执行Try方法1
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

> 注：在执行Try方法的本地事务末尾，需要使用`DtfTccBranch.checkTxTrying();`接口防止Try阶段延迟提交本地事务。

---

## 远程请求时传递分布式事务上下文

### 主调

需要从上下文中提取`groupId`，`txId`，`lastBranchId`三个数据传递到下游。

使用以下API提取

``` java
String groupId = DtfContextHolder.get().getGroupId();
Long txId = DtfContextHolder.get().getTxId();
Long lastBranchId = DtfContextHolder.get().getBranchIdStack().peek();
```

> 建议放到下列Header的key中，下游可以通过DTF SDK自行注入。

``` properties
# Header key的常量ClientConstant.HTTP_HEADER.GROUP_ID
DTF-Group-ID: ${GroupId}
# Header key的常量ClientConstant.HTTP_HEADER.TX_ID
DTF-Tx-ID: ${TxId}
# Header key的常量 ClientConstant.HTTP_HEADER.LAST_BRANCH_ID
DTF-Last-Branch-ID: ${LastBranchId}
```

### 被调

根据上游业务的特性手动获取`groupId`，`txId`，`lastBranchId`三个数据。

> 如果上游使用的是DTF封装的RestTemplate或Fegin，请从以下请求头中获取：

``` properties
# Header key的常量ClientConstant.HTTP_HEADER.GROUP_ID
DTF-Group-ID: ${GroupId}
# Header key的常量ClientConstant.HTTP_HEADER.TX_ID
DTF-Tx-ID: ${TxId}
# Header key的常量 ClientConstant.HTTP_HEADER.LAST_BRANCH_ID
DTF-Last-Branch-ID: ${LastBranchId}
```

> 如果是其他方式传递，则需要用户按照接口协议自行获取。

获取了三个数据后，通过API绑定分布式事务上下文。

``` java
DtfTransaction.bind(${GroupId}, ${TxId}, ${LastBranchId});
```
