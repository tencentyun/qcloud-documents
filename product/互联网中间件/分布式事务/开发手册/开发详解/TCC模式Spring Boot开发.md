## 操作场景

该任务指导您在 TCC 模式下进行 Spring Boot 开发。
TCC 事务，也可以理解为手动事务。需要用户提供 Try、Confirm、Cancel 接口并进行实现，同时需要保证三个接口的**幂等性**。

## 准备工作

参考 [准备工作](https://cloud.tencent.com/document/product/1224/45966) 文档。

## Maven 配置

通过配置业务代码的 pom.xml 文件，可以引入 DTF 的 SDK 到您的工程中。

配置中的 ${dtf.version} 可以参考 [Release Note](https://cloud.tencent.com/document/product/1224/44764) 中，选择**最新版本（推荐）**或指定版本。

```xml
<dependency>
    <groupId>com.tencent.cloud</groupId>
    <artifactId>spring-boot-dtf</artifactId>
    <version>${dtf.version}</version>
</dependency>
```

> ?如果需要同时使用 tsf-sleuth 和 druid，需要切换到 spring-boot-dtf-druid 客户端，配置如下：

```
<dependency>
	<groupId>com.tencent.cloud</groupId>
	<artifactId>spring-boot-dtf-druid</artifactId>
</dependency>  
```

## 客户端配置

在客户端中，支持以下配置自定义：

```yaml
dtf:
  env:
    groups:
      ${GroupId}: ${BorkerList}
    secretId: ${SecretId}
    secretKey: ${SecretKey}
    server: ${Server}
```

| 配置项                    | 数据类型 | 必填 | 默认值                                   | 描述                                                         |
| ------------------------- | -------- | ---- | ---------------------------------------- | ------------------------------------------------------------ |
| dtf.env.groups.${GroupId} | String   | 是   | 共享集群 TC 列表，如果是独占集群则需要填写 | 用户的事务分组 ID，单客户端使用多个事务分组时可以配置多项     |
| dtf.env.secretId   | String   | 是   | 无                                       | 用户的腾讯云 SecretID                                         |
| dtf.env.secretKey  | String   | 是   | 无                                       | 用户的腾讯云 SecretKey                                        |
| dtf.env.server     | String   | 否   | ${spring.application.name}               | 客户端服务标识，一个事务分组下，同一服务需要使用相同的标识 |
| dtf.env.fmt  |  Boolean  | 否  | true  | 启动时会对 DB 进行大量初始化工作，若不需使用 fmt 建议禁用 |

通常情况下，仅需要在 dtf.env.groups 下配置一个事务分组。例如：
用户A，创建了一个事务分组`group-x3k9s0ns`，在 [分布式事务控制台](https://console.cloud.tencent.com/dtf/) 获取该分组的 TC 集群地址为`127.0.0.1:8080;127.0.0.1:8081;127.0.0.1:8082`。该用户访问密钥的 SecretId 为`SID`，SecretKey 为`SKEY`。需要在业务应用`app-test`上使用该事物时，配置样例为：

```yaml
spring:
  application:
    name: app-test
dtf:
  env:
    groups:
      group-x3k9s0ns: 127.0.0.1:8080;127.0.0.1:8081;127.0.0.1:8082
    secretId: SID
    secretKey: SKEY
```

> ?此时`dtf.env.groups.server`的值为`app-test`。

## 启用分布式事务服务

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

>?通常建议同时启用本地事务管理`@EnableTransactionManagement`。

## 主事务管理

主事务的生命周期可以分为：开启、提交/回滚。

您可以根据实际业务的需要，选择**通过注解管理主事务**或**通过 API 管理主事务**。

### 通过注解管理主事务

主事务通常建议在入口 Controller 方法处开启。一般注释在**实现类**方法上，并且该类需要注入为 Bean。

以下面注解了`@DtfTransactional`的 order 方法为例：

```java
@DtfTransactional
@RequestMapping("/order")
public Boolean order(@RequestBody Order order) {
    // 执行业务逻辑或分支事务
}
```

1. 进入 order 方法前 DTF 框架**开启**主事务。
2. 执行业务逻辑或分支事务。

- 如果该方法正常执行完毕，返回业务数据（或者 void 方法无返回值），DTF 框架**提交**主事务。
- 如果该方法执行出现问题，抛出异常时，DTF 框架**回滚**主事务。

3. DTF 框架自动关闭当前线程**主事务上下文**。

#### 主事务注解支持的能力包括

| 参数       | 数据类型 | 必填 | 默认值                                             | 描述                                                         |
| ---------- | -------- | ---- | -------------------------------------------------- | ------------------------------------------------------------ |
| timeout    | Integer  | 否   | 60 * 1000                                          | 事务超时时间（所有 Try 阶段），单位：毫秒                    |
| groupId    | String   | 否   | dtf.env.groups<br>仅配置了一个事务分组时，使用该值 | 主事务的事务分组 ID                                          |
| autoCommit | Boolean  | 否   | true                                               | 为 false 时需要手动提交事务，即在能获取到事务上下文的地方显示调用 `DtfTransaction.commit()` |

DTF 目前支持通过 @DtfTransactional 传染主事务。当您的主事务有多个入口时，使用多个 @DtfTransactional 不会报错。全局事务的开始与结束，将由第一个开始执行的标有 @DtfTransactional 的主事务纳管。

> ?如果`dtf.env.groups`下只配置了**1个**事务分组 ID，则 @DtfTransactional 注解中**不需要**填写 groupId，DTF 框架会自动从配置中获取。

### 通过 API 管理主事务

如果业务存在异步操作或者有特殊诉求（例如：一个主事务不能在单一方法闭环），也可以使用 API 来进行主事务管理。

还是以上面的 order 方法为例，此时需要等待一个 orderCallback 回调来确认提交或回滚主事务：

```java
@RequestMapping("/order")
public Boolean order(@RequestBody Order order) {
    try {
        Boolean result;
        // 开启主事务
        DtfTransaction.begin(DTF.DEFAULT_TX_TIMEOUT);
        // 执行业务逻辑或分支事务 > result
        return result;
    } catch(Throwable t) {
        // 回滚主事务
        DtfTransaction.rollback();
    } finally {
        // 关闭当前线程主事务上下文
        DtfTransaction.end();
    }
}

@RequestMapping("/order/callback")
public Boolean orderCallback(@RequestBody OrderCallback orderCallback) {
    try {
        // 绑定 DTF 上下文
        // 如果全局使用 DTF 框架，可以忽略该步骤，框架会自动完成上下文传递。详见[远程请求时传递分布式事务上下文]章节
        DtfTransaction.bind(orderCallback.getGroupId(), orderCallback.getTxId(), orderCallback.getLastBranchId());
        // 处理业务回调逻辑
        if(orderCallback.getResult()) {
            // 回调成功时，提交主事务
            DtfTransaction.commit();
        } else {
            // 回调失败时，回滚主事务
            DtfTransaction.rollback();
        }
        return orderCallback.getResult();
    } catch(Throwable t) {
        // 回滚主事务
        DtfTransaction.rollback();
    } finally {
        // 关闭当前线程主事务上下文
        DtfTransaction.end();
    }
}
```

## 分支事务管理

分支事务的生命周期可以分为：开启、提交/回滚。

可以根据实际业务的需要选择**通过注解管理分支事务**或**通过 API 管理分支事务**。

一个 TCC 分支事务中，需要包含 Try、Confirm、Cancel 三个部分。

- 分支事务的 Try、Confirm、Cancel 方法所在的类需要被**注入为 Bean**。
- 分支事务的 Try、Confirm、Cancel 方法建议使用本地事务管理（例如注解 Spring 的@Transactional）。
- 分支事务的 Try、Confirm、Cancel 方法的参数**保持一致**。
- 分支事务的 Try、Confirm、Cancel 方法的前两个参数固定为`Long txId`和`Long branchId`。

**Try 方法**：

- 本地调用 Try 方法时`txId`和`branchId`参数传`null`，其他参数正常传递。
- 返回值为**业务逻辑**需要的返回值。

**Confirm 方法**：

- 返回值固定为 Boolean 类型。
- 仅在返回 **true** 时视为分支事务 **Confirm 成功**。
- 返回 **false** 或**抛出异常**时，视为分支事务 **Confirm 失败**。

**Cancel 方法**：

- 返回值固定为 Boolean 类型。
- 仅在返回 **true** 时视为分支事务 **Cancel 成功**。
- 返回 **false** 或**抛出异常**时，视为分支事务 **Cancel 失败**。

### 通过注解管理分支事务

分支事务通常建议注解在业务的 Service上。可以注解在**接口**或**实现类**上，并且该类需要注入为 Bean。

以下面注解了`@DtfTcc`的 order 方法为例：

```java
public interface IOrderService {
    @DtfTcc
    public boolean order(Long txId, Long branchId, Order order);

    public boolean confirmOrder(Long txId, Long branchId, Order order);

    public boolean cancelOrder(Long txId, Long branchId, Order order);
}
```

分支事务注解支持的参数包括：

| 参数          | 数据类型                     | 必填 | 默认值                                      | 描述                                                 |
| ------------- | ---------------------------- | ---- | ------------------------------------------- | ---------------------------------------------------- |
| name          | String                       | 否   | @DtfTcc 方法名 + 方法签名 Hash              | 分支事务名称                                         |
| confirmClass  | String                       | 否   | @DtfTcc 注解所在 Class                      | Confirm 操作类名，建议填写 beanname                  |
| confirmMethod | String                       | 否   | confirm 前缀 + @DtfTcc 注解方法名首字母大写 | Confirm 操作方法名                                   |
| cancelClass   | String                       | 否   | @DtfTcc 注解所在 Class                      | Cancel 操作类名，建议填写 beanname                   |
| cancelMethod  | String                       | 否   | Cancel 前缀 + @DtfTcc 注解方法名首字母大写  | Cancel 操作方法名                                    |
| rollbackFor   | Class &lt;? extends Throwable&gt;[] | 否   | {}                                          | 分支事务在识别到以下异常时回滚主事务，未配置时不回滚 |

在上面的例子中：

- `name`：IOrderService.order(Long txId, Long branchId, Order order)
- `confirmClass`：IOrderService
- `confirmMethod`：confirmOrder(Long txId, Long branchId, Order order)
- `cancelClass`：IOrderService
- `cancelMethod`：cancelOrder(Long txId, Long branchId, Order order)
- `rollbackFor`：默认为空。若想要在发生异常时回滚，可设置为 Exception

### 通过 API 管理分支事务（不推荐）

可以参考 [Spring Free 开发指导](https://cloud.tencent.com/document/product/1224/45970) 中的分支事务管理章节。



## 远程请求时传递分布式事务上下文

使用`RestTemplate`或`FeignClient`时，DTF 框架支持自动化的分布式事务上下文传递。

如果使用了其他的通信框架，也可以**手动处理分布式事务上下文**。

### 主调 - RestTemplate

使用`RestTemplate`访问下游服务时，DTF 框架自动注入了 TxRestTemplateInterceptor，向请求头中装载分布式事务上下文信息。

DTF 框架注入的请求头信息为：

```sh
# 事务分组 ID
DTF-Group-ID: ${GroupId}
# 主事务 ID
DTF-Tx-ID: ${TxId}
# 父级分支事务 ID
DTF-Last-Branch-ID: ${LastBranchId}

```

### 主调 - FeignClient

使用`FeignClient`访问下游服务时，DTF 框架自动注入了 TxFeignInterceptor，向请求头中装载分布式事务上下文信息。

需要引入 feign 依赖：

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>

```

DTF 框架注入的请求头信息为：

```sh
# 事务分组 ID
DTF-Group-ID: ${GroupId}
# 主事务 ID
DTF-Tx-ID: ${TxId}
# 父级分支事务 ID
DTF-Last-Branch-ID: ${LastBranchId}

```

### 主调 - 手动处理

可以参考 [Spring Free 开发指导](https://cloud.tencent.com/document/product/1224/45970) 中的**远程请求时传递分布式事务上下文**章节。

### 被调 - Spring MVC - Controller

使用 Spring MVC 的应用，在进入 Controller 前，DTF 框架会自行从请求头中检索下列 Header key。

```properties
# Header key的常量ClientConstant.HTTP_HEADER.GROUP_ID
DTF-Group-ID: ${GroupId}
# Header key的常量ClientConstant.HTTP_HEADER.TX_ID
DTF-Tx-ID: ${TxId}
# Header key的常量 ClientConstant.HTTP_HEADER.LAST_BRANCH_ID
DTF-Last-Branch-ID: ${LastBranchId}
```

检索后通过 TxContextRestore 切点还原分布式事务上下文。

### 被调 - 手动处理

可以参考 [Spring Free 开发指导](https://cloud.tencent.com/document/product/1224/45970) 中的**远程请求时传递分布式事务上下文**章节。

## 与 TSF 结合使用

引入依赖后（注意 SDK 版本），直接正常使用 TSF 即可。

### 使用方式
目前支持 Greenwich（G）和 Finchley（F）版本的 TSF SDK。您可以单击以下页签，查看对应的使用方式。
<dx-tabs>
::: G\s版本\sTSF\sSDK\s使用方式
```xml
<!-- TSF 启动器 -->
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-starter</artifactId>
    <version>1.23.0-Greenwich-RELEASE</version>
</dependency>
```
:::
::: F\s版本\sTSF\sSDK\s使用方式
<dx-alert infotype="notice" title="">
需要再排除 DTF 中的一些依赖。
</dx-alert>

```xml
<!-- TSF 启动器 -->
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-starter</artifactId>
    <version>1.23.5-Finchley-RELEASE</version>
</dependency>
<!-- Spring Boot DTF -->
<dependency>
        <groupId>com.tencent.cloud</groupId>
        <artifactId>spring-boot-dtf</artifactId>
        <version>${dtf.version}</version>
        <exclusions>
                <exclusion>
                        <groupId>org.springframework</groupId>
                        <artifactId>spring-context</artifactId>
                </exclusion>
                <exclusion>
                        <groupId>org.springframework.boot</groupId>
                        <artifactId>spring-boot-starter</artifactId>
                </exclusion>
                <exclusion>
                        <groupId>org.springframework</groupId>
                        <artifactId>spring-aspects</artifactId>
                </exclusion>
                <exclusion>
                        <groupId>org.springframework</groupId>
                        <artifactId>spring-boot-starter-web</artifactId>
                </exclusion>
                <exclusion>
                        <groupId>io.github.openfeign</groupId>
                        <artifactId>feign-core</artifactId>
                </exclusion>
        </exclusions>
</dependency>
```
:::
</dx-tabs>





### 启用 TSF
<dx-codeblock>
:::  java
@SpringBootApplication
@EnableDtf
@EnableTsf
@EnableTransactionManagement
public class OrderApplication {
    public static void main(String[] args) {
        SpringApplication.run(OrderApplication.class, args);
    }
}
:::
</dx-codeblock>
