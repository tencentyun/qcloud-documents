## 操作场景

该任务指导您在 Saga 模式下进行 Spring Free 开发。
手动启动 Saga 事务，需要用户自行编写 Execute和 Compensate 接口的实现，并保证这两个方法的**幂等性**。

## 准备工作

- 需要在 [分布式事务控制台](https://console.cloud.tencent.com/dtf) 中创建一个事务分组（参考 [新建事务分组](https://cloud.tencent.com/document/product/1224/45930#.E6.96.B0.E5.BB.BA.E4.BA.8B.E5.8A.A1.E5.88.86.E7.BB.84)）。
- 需要在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中，获取账号的 SecretID 和 SecretKey（该账号能够在控制台中查询到事务分组即可）。
- 需要能够连接到 Maven。


## 接入步骤
### 1. 引入 DTF SDK

通过以下方式引入 Spring Cloud 版本的 DTF SDK。

```xml
<dependency>
    <groupId>com.tencent.cloud</groupId>
    <artifactId>dtf-core</artifactId>
    <version>{dtf.version}</version>
</dependency>
```

>?version 填写 Release Note 中最新版本的即可。


### 2. 客户端配置

在客户端中，支持以下配置自定义：

```yml
dtf:
  env:
    groups:
      {事务分组ID 1}: [{独占集群列表}]
      {事务分组ID 2}: [{独占集群列表}]
    secretId: {SecretID}
    secretKey: {SecretKey}
    server: {客户端服务标识}
```

| 配置项                   | 数据类型 | 必填 | 默认值                                   | 描述                                                         |
| ------------------------ | -------- | ---- | ---------------------------------------- | ------------------------------------------------------------ |
| dtf.env.groups.{groupId} | String   | 是   | 共享集群TC列表，如果是独占集群则需要填写 | 用户的事务分组 ID，单客户端使用多个事务分组时可以配置多项。     |
| dtf.env.groups.secretId  | String   | 是   | 无                                       | 用户的腾讯云 SecretID。                                         |
| dtf.env.groups.secretKey | String   | 是   | 无                                       | 用户的腾讯云 SecretKey。                                        |
| dtf.env.groups.server    | String   | 是   | ${spring.application.name}               | 客户端服务标识，一个事务分组下，同一服务需要使用相同的标识。 |

>?通常情况下，仅需要在 dtf.env.groups 下配置一个事务分组。



### 3. 启用分布式事务服务

在 @SpringBootApplication 注解处增加 `@EnableDtf` 注解来启用分布式事务服务。

```java
@SpringBootApplication
@EnableDtf
@EnableTransactionManagement
public class OrderApplication {
    public static void main(String[] args) {
        SpringApplication.run(OrderApplication.class, args);
    }
}
```

>?建议同时启用本地事务管理：@EnableTransactionManagement。



### 4. 开启主事务

通过以下注解开启主事务。
主事务通常在入口 Controller 处开启。一般建议标记在**实现类**上。注解所在的方法所在的类需要注入为 Bean。

主事务注解方法正常返回时提交主事务，在抛出异常时进行回滚。

```java
@DtfTransactional
@RequestMapping("/order")
public Boolean order(@RequestBody Order order) {
    // 业务逻辑
}
```

主事务注解支持的能力包括

| 参数       | 数据类型 | 必填 | 默认值                                         | 描述                                                         |
| ---------- | -------- | ---- | ---------------------------------------------- | ------------------------------------------------------------ |
| timeout    | Integer  | 否   | 60 * 1000                                      | 事务超时时间（所有 Try 阶段），单位：毫秒                      |
| groupId    | String   | 否   | dtf.env.groups仅配置了一个事务分组时，使用该值 | 主事务的事务分组 ID                                           |
| autoCommit | Boolean  | 否   | true                                           | 为false时需要手动提交事务，即在能获取到事务上下文的地方显示调用`DtfTransaction.commit()` |



### 5. 开启 Saga 分支事务[](id:step5)

通过以下注解开启分支事务。
>?
>- 分支事务通常标记在 Service 上。可以标记在**接口**或**实现类**上。
>- 分支事务最好被 Spring 的 @Transactional 注解管理。

```java
@DtfSaga
public boolean order(Long txId, Long branchId, Order order);
```

分支事务注解支持的参数包括：

| 参数             | 数据类型 | 必填 | 默认值                                     | 描述                           |
| ---------------- | -------- | ---- | ------------------------------------------ | ------------------------------ |
| name             | String   | 否   | @DtfSaga 方法名+方法签名 Hash                | 分支事务名称，请在同一事务分组 |
| compensateClass  | String   | 否   | @DtfSaga 注解所在 Class                      | compensate 操作类名             |
| compensateMethod | String   | 否   | execute 前缀 + @DtfSaga 注解方法名首字母大写 | compensate 操作方法名           |


### 6. Compensate 操作

一个分支事务中，需要包含 Execute 和 Compensate 两个部分。可以使用 [步骤5](#step5) 中的默认值简化配置。

- 分支事务的 Execute 和 Compensate 方法所在的类需要被**注入为 Bean**。
- 分支事务的 Execute 和 Compensate 方法最好被 Spring 的 @Transactional 注解管理
- 分支事务的 Execute 和 Compensate 方法的参数**保持一致**。
- 分支事务的 Execute 和 Compensate 方法的前两个参数固定为 `Long txId` 和 `Long branchId`。

Execute 方法：
  - 本地调用 Execute 方法时 `txId` 和 `branchId` 参数传 `null`，其他参数正常传递。
  - 返回值为**业务逻辑**需要的返回值。

Compensate 方法：
 - 返回值固定为 Boolean 类型。
 - 仅在返回 `true` 时视为分支事务 `Compensate 成功`。
 - 返回 `false` 或**抛出异常**时，视为分支事务 `Compensate 失败`。

```java
public interface IOrderService {

    @DtfSaga
    boolean order(Long txId, Long branchId, Order order);

    boolean compensateOrder(Long txId, Long branchId, Order order);

}
```


### 7. 远程请求

#### 方式一：使用 RestTemplate + Spring MVC 切点

使用 RestTemplate 访问下游服务（也使用了 DTF SDK）的 Controller。DTF SDK 框架托管了全局事务传递的处理。

使用以下方式进行常规注入即可。

```java
@Bean
public RestTemplate restTemplate() {
    return new RestTemplate();
}
```

####  方式二：使用 Feign

需要引入 openfeign 依赖：
```xml
<dependency>;
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>;
```

然后按照正常方式使用 Feign 即可：
```java
@FeignClient("spring-cloud-payment")
public interface PaymentProxy {
    @RequestMapping("/pay")
    public Boolean pay(@RequestBody Payment payment);
}

```

#### 方式三：自行处理

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
DtfContextHolder.set(new DtfContext(txId, lastBranchId, groupId));
```

### 8. 与 TSF 结合使用

直接正常使用 TSF 即可，引入依赖。

>?目前仅支持 G 版本 TSF SDK。

```xml
<!-- TSF 启动器 -->
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-starter</artifactId>
</dependency>
```

启用 TSF：

```java
@SpringBootApplication
@EnableDtf
@EnableTsf
@EnableTransactionManagement
public class OrderApplication {
    public static void main(String[] args) {
        SpringApplication.run(OrderApplication.class, args);
    }
}
```
