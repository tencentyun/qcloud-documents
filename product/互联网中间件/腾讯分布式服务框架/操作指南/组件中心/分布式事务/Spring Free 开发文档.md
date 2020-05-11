## 准备工作
- 在 [分布式事务控制台中](https://console.cloud.tencent.com/tsf/transaction) 创建一个事务分组（参考 [分布式事务-控制台基本操作](https://cloud.tencent.com/document/product/649/31208)）。
- 在 [访问密钥](https://console.cloud.tencent.com/cam/capi) 中获取账号的 SecretID 和 SecretKey（该账号能够在控制台中查询到事务分组即可）。
若您还没有创建密钥，单击【新建密钥】即可完成创建。直接复制 SecretID 和 SecretKey 即可。 
- 需要能够连接到 Maven（请参考 [SDK 下载](https://cloud.tencent.com/document/product/649/20231)，安装相关依赖）。
- 下载 Demo（[Demo 地址](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/dtf-demo/dts-demo.zip)）。
- 创建数据库（参考 Demo 文件中的 sql 文件），并自行修改各 application.yml 中的数据库对应信息。



## 开发步骤
### 1. 引入 DTS SDK

通过以下方式引入 Spring Cloud 版本的 DTS SDK。version 填写 Release Note 中的最新版本即可。请在 pom.xml 中修改。
``` xml
<dependency>
    <groupId>com.tencent.cloud</groupId>
    <artifactId>dts-core</artifactId>
    <version>0.0.1-RELEASE</version>
</dependency>
```


### 2. 客户端配置

在客户端中，支持以下配置自定义 ，请在工程中的 application.yml 中配置。

``` java
private static void initEnv() {
    DtsEnv.setServer("客户端服务标识");
    DtsEnv.setSecretId("SecretID");
    DtsEnv.setSecretKey("SecretKey");
    DtsEnv.addTxmBroker("事务分组ID", "独占集群列表");
}
```

| 配置项              | 数据类型 | 必填 | 默认值                                   | 描述                                                         |
| ------------------- | -------- | ---- | ---------------------------------------- | ------------------------------------------------------------ |
| DtsEnv.addTxmBroker | String   | 是   | 共享集群 TC 列表，如果是独占集群则需要填写 | 用户的事务分组 ID，单客户端使用多个事务分组时可以配置多项     |
| DtsEnv.setSecretId  | String   | 是   | 无                                       | 用户的腾讯云 SecretID                                         |
| DtsEnv.setSecretKey | String   | 是   | 无                                       | 用户的腾讯云 SecretKey                                        |
| DtsEnv.setServer    | String   | 是   | ${spring.application.name}               | 客户端服务标识，一个事务分组下，同一服务需要使用相同的标识 |

>?通常情况下，仅需要在 dts.env.groups 下配置一个事务分组。


### 3. 注册 TCC

使用以下接口，手动注册 TCC 接口。
``` java
private static void registerTcc() {
    ITransferService transferService = new TransferService();
    // debit的confirm和cancel
    MTHandlerRegistry.register("name1", TCC.getInstance(transferService, "confirmDebit", transferService, "cancelDebit"));
    // credit的confirm和cancel
    MTHandlerRegistry.register("name2", TCC.getInstance(transferService, "confirmCredit", transferService, "cancelCredit"));
}
```
注册方式比较多，可以参考 MTHandlerRegistry.register() 和 TCC.getInstance() 的 javadoc。


### 4. 启动分布式事务服务

通过以下方式启动分布式事务服务。
``` java
public static void main(String[] args) {
    // 设置参数
    initEnv();
    // 注册TCC
    registerTcc();
    // 启动分布式事务客户端
    DtsClient.start();
}
```

### 5. 开启主事务

通过以下接口开启主事务。
主事务注解方法正常返回时提交主事务，在抛出异常时进行回滚。

``` java
Long txId = DtsTransaction.begin(Integer timeout);
// 或
Long txId = DtsTransaction.begin(String groupId, Integer timeout);
```

| 参数    | 数据类型 | 必填 | 默认值                                               | 描述                                    |
| ------- | -------- | ---- | ---------------------------------------------------- | --------------------------------------- |
| timeout | Integer  | 否   | 60 * 1000                                            | 事务超时时间（所有 Try 阶段），单位：毫秒 |
| groupId | String   | 否   | DtsEnv.addTxmBroker 仅配置了一个事务分组时，使用该值 | 主事务的事务分组 ID                      |



### 6. 开启分支事务

通过以下接口开启分支事务。
``` java
Long branchId1 = DtsMTBranch.begin("name", new Object[] {null, null, this.to, this.amount});
```

分支事务注解支持的参数包括：

| 参数     | 数据类型            | 必填 | 默认值 | 描述                           |
| -------- | ------------------- | ---- | ------ | ------------------------------ |
| name     | String              | 否   | 无     | 分支事务名称，请在同一事务分组 |
| 参数列表 | Array&lt;String&gt; | 否   | 无     | 参数列表，前两个参数固定为 null |


### 7. Confirm 和 Cancel 操作

一个分支事务中，需要包含 Try、Confirm、Cancel 三个部分。可以使用步骤6中的默认值简化配置。
- 分支事务的 Try、Confirm、Cancel 方法的参数`保持一致`。
- 分支事务的 Try、Confirm、Cancel 方法的前两个参数固定为`Long txId`和`Long branchId`。

#### Try 方法
  - 本地调用 Try 方法时`txId`和`branchId`参数传`null`，其他参数正常传递。
  - 返回值为`业务逻辑`需要的返回值。

#### Confirm 方法
  - 返回值固定为`boolean`类型。
  - 仅在返回`true`时视为分支事务`Confirm成功`。
  - 返回`false`或`抛出异常`时，视为分支事务`Confirm失败`。

#### Cancel 方法
  - 返回值固定为`boolean`类型。
  - 仅在返回`true`时视为分支事务`Cancel成功`。
  - 返回`false`或`抛出异常`时，视为分支事务`Cancel失败`。

``` java
public interface IOrderService {
    public boolean order(Long txId, Long branchId, Order order);

    public boolean confirmOrder(Long txId, Long branchId, Order order);

    public boolean cancelOrder(Long txId, Long branchId, Order order);
}
```


### 8. 远程请求

#### 自行处理

- 上游处理：
需要从上下文中提取`txId`、`groupId`、`lastBranchId`三个内容传递到下游。
``` properties
txId: DtsContextHolder.get().getTxId();
groupId: DtsContextHolder.get().getGroupId();
lastBranchId: DtsContextHolder.get().getBranchIdStack().peek();
```
建议放到下列 Header 的 key 中，下游可以通过 DTS SDK 自行注入。
``` properties
ClientConstant.HTTP_HEADER.TX_ID: txId
ClientConstant.HTTP_HEADER.GROUP_ID: groupId
ClientConstant.HTTP_HEADER.LAST_BRANCH_ID: lastBranchId
```

- 下游处理：
下游可以使用以下方法将从上游传递的三个变量绑定到本地，重新开启全局事务。
``` java
DtsContextHolder.bind(txId, lastBranchId, groupId);
```

