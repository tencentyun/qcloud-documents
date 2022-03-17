## 操作场景
该任务指导您在 Saga 模式下进行 Spring Free 开发。
手动启动 Saga 事务，需要用户自行编写 Execute，Compensate 接口的实现，并保证这两个方法的**幂等性**。

## 准备工作

- 需要在 [分布式事务控制台](https://console.cloud.tencent.com/dtf) 中创建一个事务分组（参考 [新建事务分组](https://cloud.tencent.com/document/product/1224/45930#.E6.96.B0.E5.BB.BA.E4.BA.8B.E5.8A.A1.E5.88.86.E7.BB.84)）。
- 需要在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中，获取账号的 SecretID 和 SecretKey（该账号能够在控制台中查询到事务分组即可）。
- 需要能够连接到 Maven。



## 接入步骤
### 1. 引入 DTF SDK

通过以下方式引入 Spring Free 版本的 DTF SDK。

```xml
<dependency>
    <groupId>com.tencent.cloud</groupId>
    <artifactId>dtf-core</artifactId>
    <version>{dtf.version}</version>
</dependency>
```

>?version 填写 Release Note 中最新版本的即可。



### 2. 客户端配置

在客户端中，使用以下方式添加基本配置。

``` java
DtfEnv.setServer(String server);
DtfEnv.setSecretId(String secretId);
DtfEnv.setSecretKey(String secretKey);
DtfEnv.addTxmBroker(String groupId, String txmBrokerList);
```

| 配置项        | 数据类型 | 必填 | 默认值 | 描述                                                         |
| ------------- | -------- | ---- | ------ | ------------------------------------------------------------ |
| groupId       | String   | 是   | 无     | 用户的事务分组 ID                                            |
| txmBrokerList | String   | 是   | 无     | TC 集群节点列表                                               |
| secretId      | String   | 是   | 无     | 用户的腾讯云 SecretID                                         |
| secretKey     | String   | 是   | 无     | 用户的腾讯云 SecretKey                                        |
| server        | String   | 是   | 无     | 客户端服务标识，一个事务分组下，同一服务需要使用相同的标识 |
| dtf.env.fmt  |  Boolean  | 否  | true  | 启动时会对 DB 进行大量初始化工作，若不需使用 fmt 建议禁用 |

>?通常情况下，仅需要在 dtf.env.groups 下配置一个事务分组。



### 3. 注册 Saga

使用以下接口，手动注册 Saga 接口。

```java
private static void registerSaga() {
    ITransferService transferService = new TransferService();
    // debit 的 compensate
    SagaRegistry.register("com.tencent.cloud.dtf.demo.transfer.TransferService.debit",
            SagaRegistry.SAGA.getInstance(transferService, "compensateDebit"));
    // credit 的 compensate
    SagaRegistry.register("com.tencent.cloud.dtf.demo.transfer.TransferService.credit",
            SagaRegistry.SAGA.getInstance(transferService, "compensateCredit"));
}
```

注册方式可以参考 SagaRegistry.register() 和 SAGA.getInstance() 的 javadoc。



### 4. 启动分布式事务服务

通过以下方式启动分布式事务服务。

```java
public static void main(String[] args) {
        // 设置参数
        initEnv();
        // 注册 Saga
        registerSaga();
        // 启动分布式事务客户端
        DtfClient.start();
    }
```


### 5. 开启主事务[](id:step5) 

通过以下接口开启主事务。
主事务注解方法正常返回时提交主事务，在抛出异常时进行回滚。

```java
Long txId = DtfTransaction.begin(Integer timeout);
// 或
Long txId = DtfTransaction.begin(String groupId, Integer timeout);
```

| 参数    | 数据类型 | 必填 | 默认值                                               | 描述                                    |
| ------- | -------- | ---- | ---------------------------------------------------- | --------------------------------------- |
| timeout | Integer  | 否   | 60 * 1000                                            | 事务超时时间（所有 Try 阶段），单位：毫秒 |
| groupId | String   | 否   | DtfEnv.addTxmBroker 仅配置了一个事务分组时，使用该值 | 主事务的事务分组 ID                      |



### 6. 开启分支事务

通过以下接口开启分支事务。

```java
Long branchId1 = DtfTccBranch.begin("name", new Object[] {null, null, this.to, this.amount});
```

分支事务注解支持的参数包括：

| 参数     | 数据类型      | 必填 | 默认值 | 描述                           |
| -------- | ------------- | ---- | ------ | ------------------------------ |
| name     | String        | 否   | 无     | 分支事务名称，请在同一事务分组 |
| 参数列表 | Array &lt;String&gt; | 否   | 无     | 参数列表，前两个参数固定为 null |



### 7. Compensate 操作

一个分支事务中，需要包含 Execute 和 Compensate 两个部分。可以使用 [步骤5](#step5) 中的默认值简化配置。

- 分支事务的 Execute 和 Compensate 方法的参数**保持一致**。
- 分支事务的 Execute 和 Compensate 方法的前两个参数固定为 `Long txId` 和 `Long branchId`。

Execute 方法：
- 本地调用 Execute 方法时 `txId` 和 `branchId` 参数传 `null`，其他参数正常传递。
- 返回值为**业务逻辑**需要的返回值。

Compensate 方法：
- 返回值固定为 Boolean 类型。
- 仅在返回 `true` 时视为分支事务 Compensate 成功。
- 返回 `false` 或**抛出异常**时，视为分支事务 Compensate 失败。

```java
void debit(Long txId, Long branchId, Account account, int amount) throws Exception;

boolean compensateDebit(Long txId, Long branchId, Account account, int amount);
```



### 8. 远程请求（自行处理）

- **上游处理**：
需要从上下文中提取 `txId`、`groupId`、`lastBranchId` 三个内容传递到下游。
```properties
txId: DtfContextHolder.get().getTxId();
groupId: DtfContextHolder.get().getGroupId();
lastBranchId: DtfContextHolder.get().getBranchIdStack().peek();
```
 >?建议放到下列 Header 的 key 中，下游可以通过 DTF SDK 自行注入。
```properties
ClientConstant.HTTP_HEADER.TX_ID: txId
ClientConstant.HTTP_HEADER.GROUP_ID: groupId
ClientConstant.HTTP_HEADER.LAST_BRANCH_ID: lastBranchId
```

- **下游处理**：
下游可以使用以下方法将从上游传递的三个变量绑定到本地，重新开启全局事务。
```java
DtfContextHolder.bind(txId, lastBranchId, groupId);
```
