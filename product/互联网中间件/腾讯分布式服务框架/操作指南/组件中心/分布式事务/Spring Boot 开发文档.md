##  准备工作
- 在 [分布式事务控制台中](https://console.cloud.tencent.com/tsf/transaction) 创建一个事务分组（参考 [分布式事务-控制台基本操作](https://cloud.tencent.com/document/product/649/31208)）。
- 在 [访问密钥](https://console.cloud.tencent.com/cam/capi) 中获取账号的 SecretID 和 SecretKey（该账号能够在控制台中查询到事务分组即可）。
若您还没有创建密钥，单击【新建密钥】即可完成创建。直接复制 SecretID 和 SecretKey 即可。 
- 需要能够连接到 Maven（请参考 [SDK 下载](https://cloud.tencent.com/document/product/649/20231)，安装相关依赖）。
- 下载 Demo（[Demo 地址](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/dtf-demo/dts-demo.zip)）。
- 创建数据库（参考 Demo 文件中的 sql 文件），并自行修改各 application.yml 中的数据库对应信息。


## 开发步骤
### 1. 引入 DTS SDK

通过以下方式引入 Spring Boot 版本的 DTS SDK。version 填写 Release Note 中的最新版本即可。请在 pom.xml 中修改。
``` xml
<dependency>
    <groupId>com.tencent.cloud</groupId>
    <artifactId>spring-boot-dts</artifactId>
    <version>0.0.1-RELEASE</version>
</dependency>
```



### 2. 客户端配置

在客户端中，支持以下配置自定义 ，请在工程中的 application.yml 中配置。
``` yml
dts:
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
| dts.env.groups.{groupId} | String   | 是   | 共享集群 TC 列表，如果是独占集群则需要填写 | 用户的事务分组 ID，单客户端使用多个事务分组时可以配置多项     |
| dts.env.groups.secretId  | String   | 是   | 无                                       | 用户的腾讯云 SecretID                                         |
| dts.env.groups.secretKey | String   | 是   | 无                                       | 用户的腾讯云 SecretKey                                        |
| dts.env.groups.server    | String   | 是   | ${spring.application.name}               | 客户端服务标识，一个事务分组下，同一服务需要使用相同的标识 |

>?通常情况下，仅需要在 dts.env.groups 下配置一个事务分组。


### 3. 启用分布式事务服务

在 @SpringBootApplication 注解处增加 @EnableDTS 来启用分布式事务服务。
>?建议同时启用本地事务管理：@EnableTransactionManagement。

``` java
@SpringBootApplication
@EnableDTS
@EnableTransactionManagement
public class OrderApplication {
    public static void main(String[] args) {
        SpringApplication.run(OrderApplication.class, args);
    }
}
```



### 4. 开启主事务

通过以下注解开启主事务：
>?
>- 主事务通常在入口 Controller 处开启。一般建议标记在`实现类`上。注解所在的方法所在的类需要注入为 Bean。
>- 主事务注解方法正常返回时提交主事务，在抛出异常时进行回滚。

``` java
@DtsTransactional
@RequestMapping("/order")
public Boolean order(@RequestBody Order order) {
    // 业务逻辑
}
```

主事务注解支持的能力包括：

| 参数    | 数据类型 | 必填 | 默认值                                         | 描述                                    |
| ------- | -------- | ---- | ---------------------------------------------- | --------------------------------------- |
| timeout | Integer  | 否   | 60 * 1000                                      | 事务超时时间（所有 Try 阶段），单位：毫秒 |
| groupId | String   | 否   | dts.env.groups 仅配置了一个事务分组时，使用该值 | 主事务的事务分组 ID                      |


### 5. 开启分支事务

通过以下注解开启分支事务。
>?
>- 分支事务通常标记在 Service 上。可以标记在`接口`或`实现类`上。
>- 分支事务最好被 Spring 的 @Transactional 注解管理。

``` java
@DtsMT
public boolean order(Long txId, Long branchId, Order order);
```

分支事务注解支持的参数包括：

| 参数          | 数据类型 | 必填 | 默认值                                      | 描述                           |
| ------------- | -------- | ---- | ------------------------------------------- | ------------------------------ |
| name          | String   | 否   | @DtsMT 方法名 + 方法签 Hash                   | 分支事务名称，请在同一事务分组 |
| confirmClass  | String   | 否   | @DtsMT 注解所在 Class                         | confirm 操作类名                |
| confirmMethod | String   | 否   | confirm 前缀 + @DtsMT 注解方法名首字母大写    | confirm 操作方法名              |
| cancelClass   | String   | 否   | @DtsMT 注解所在 Class                         | cancel 操作类名                 |
| cancelMethod  | String   | 否   | cancel 前缀 + @DtsMT 注解方法名首字母大写 | cancel 操作方法名               |



### 6. Confirm 和 Cancel 操作

一个分支事务中，需要包含 Try、Confirm、Cancel 三个部分。可以使用步骤5中的默认值简化配置。

- 分支事务的 Try、Confirm、Cancel 方法所在的类需要被`注入为Bean`。
- 分支事务的 Try、Confirm、Cancel 方法最好被 Spring 的 @Transactional 注解管理
- 分支事务的 Try、Confirm、Cancel 方法的参数`保持一致`。
- 分支事务的 Try、Confirm、Cancel 方法的前两个参数固定为`Long txId`和`Long branchId`。

#### Try方法：
  - 本地调用 Try 方法时`txId`和`branchId`参数传`null`，其他参数正常传递。
  - 返回值为`业务逻辑`需要的返回值。

#### Confirm方法：
  - 返回值固定为`boolean`类型。
  - 仅在返回`true`时视为分支事务`Confirm 成功`。
  - 返回`false`或`抛出异常`时，视为分支事务`Confirm 失败`。

#### Cancel方法：
  - 返回值固定为`boolean`类型。
  - 仅在返回`true`时视为分支事务`Cancel成功`。
  - 返回`false`或`抛出异常`时，视为分支事务`Cancel失败`。

``` java
public interface IOrderService {
    @DtsMT
    public boolean order(Long txId, Long branchId, Order order);

    public boolean confirmOrder(Long txId, Long branchId, Order order);

    public boolean cancelOrder(Long txId, Long branchId, Order order);
}
```



### 7. 远程请求

#### 使用 RestTemplate + Spring MVC 切点

使用 RestTemplate 访问下游服务（也使用了 DTS SDK）的 Controller。DTS SDK 框架托管了全局事务传递的处理。

使用以下方式进行常规注入即可。

``` java
@Bean
public RestTemplate restTemplate() {
    return new RestTemplate();
}
```

#### 自行处理

- 上游处理：
需要从上下文中提取`txId`,`groupId`,`lastBranchId`三个内容传递到下游。
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
DtsTransaction.bind(txId, lastBranchId, groupId);
```

