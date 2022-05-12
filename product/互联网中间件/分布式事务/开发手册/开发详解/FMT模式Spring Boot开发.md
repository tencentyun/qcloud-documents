## 操作场景
该任务指导您在 FMT 模式下进行 Spring Boot 开发。

FMT 事务，也可以理解为框架托管事务。需要用户仅需要在 **FMT 规范**下正常实现业务逻辑即可实现分布式事务。相对于 TCC事务，省去了编写 Confirm、Cancel 的代码工作。
FMT 事务的实现原理：代理用户执行 PrepareStatement 和 CreateStatement 操作，对执行的 DML 语句进行解析，记录前后象，并生成UNDO信息。鉴于此，FMT 对用户使用的数据库和 SQL 语句会有一定的要求，详见  [FMT规范](https://cloud.tencent.com/document/product/1224/46038)。

## 准备工作
- 参考 [准备工作](https://cloud.tencent.com/document/product/1224/45966) 文档，完成环境配置和开发前准备。
- 参考 [快速部署](https://cloud.tencent.com/document/product/1224/45967) 文档，执行 FMT 初始化脚本


## Maven 配置

通过配置业务代码的 pom.xml 文件，可以引入 DTF 的 SDK 到您的工程中。

>?配置中的 ${dtf.version} 可以参考 [Release Note](https://cloud.tencent.com/document/product/1224/44764) 中，选择**最新版本（推荐）**或指定版本。

``` xml
<dependency>
    <groupId>com.tencent.cloud</groupId>
    <artifactId>spring-boot-dtf</artifactId>
    <version>${dtf.version}</version>
</dependency>
```

>?如果需要同时使用 tsf-sleuth 和 druid，需要切换到 spring-boot-dtf-druid 客户端，配置如下：
```
<dependency>
	<groupId>com.tencent.cloud</groupId>
	<artifactId>spring-boot-dtf-druid</artifactId>
</dependency>  
```
## 客户端配置

在客户端中，支持以下配置自定义：

``` yaml
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

通常情况下，仅需要在dtf.env.groups下配置一个事务分组。例如：
用户 A，创建了一个事务分组`group-x3k9s0ns`，在[分布式事务控制台](https://console.cloud.tencent.com/dtf/)获取该分组的 TC 集群地址为`127.0.0.1:8080;127.0.0.1:8081;127.0.0.1:8082`。该用户访问密钥的 SecretId 为`SID`，SecretKey为`SKEY`。需要在业务应用`app-test`上使用该事物时，配置样例为：
``` yaml
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

>?此时`dtf.env.groups.server`的值为`app-test`。



## 启用分布式事务服务

在@SpringBootApplication注解处增加`@EnableDtf`注解来启用分布式事务服务。

``` java
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

主事务的生命周期可以分为：开启，提交/回滚。

可以根据实际业务的需要选择**通过注解管理主事务**或**通过 API 管理主事务**。

### 通过注解管理主事务

主事务通常建议在入口 Controller 方法处开启。一般注释在**实现类**方法上，并且该类需要注入为 Bean。

以下面注解了`@DtfTransactional`的 order 方法为例：
``` java
@DtfTransactional
@RequestMapping("/order")
public Boolean order(@RequestBody Order order) {
    // 执行业务逻辑或分支事务
}
```
1. 进入 order 方法前 DTF 框架开启主事务。
2. 执行业务逻辑或分支事务。
 - 如果该方法正常执行完毕，返回业务数据（或者 void 方法无返回值），DTF 框架**提交**主事务。
 - 如果该方法执行出现问题，抛出异常时，DTF框架**回滚**主事务。
3. DTF 框架自动关闭当前线程**主事务上下文**。

#### 主事务注解支持的能力包括

| 参数    | 数据类型 | 必填 | 默认值    | 描述                                                          |
| ------- | -------- | ---- | --------- | ------------------------------------------------------------- |
| timeout | Integer  | 否   | 60 × 1000 | 事务超时时间（主事务**开启**到**提交**/**回滚**的时长），单位：毫秒 |
| groupId | String   | 否   |    -      | 在此事务分组下开启主事务                                      |

如果`dtf.env.groups`下只配置了**1个**事务分组 ID，则 @DtfTransactional 注解中**不需要**填写groupId，DTF 框架会自动从配置中获取。

DTF 现在支持通过 @DtfTransactional 传染主事务。当您的主事务有多个入口时，使用多个@DtfTransactional 不会报错。全局事务的开始与结束，将由第一个开始执行的标有 @DtfTransactional  的主事务纳管。


### 通过 API 管理主事务

如果业务存在异步操作或者有特殊诉求（例如：一个主事务不能在单一方法闭环），也可以使用 API 来进行主事务管理。

还是以上面的 order 方法为例，此时需要等待一个 orderCallback 回调来确认提交或回滚主事务：

``` java
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
        // 绑定DTF上下文。
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

FMT 的分支事务管理是自动化的，并且与 TCC 分支事务略有不同。

FMT 分支事务的注解并不会直接触发分支事务生成，而是将注解方法的执行上下文切换为FMT模式。该方法内的所有本地调用所执行的**每1行 DML 语句**都会自行生成**1个分支事务**。

### 通过注解管理分支事务
分支事务通常建议注解在业务的 Service 上。可以注解在**接口**或**实现类**上，并且该类需要注入为 Bean。

以下面注解了`@DtfFmt`的 order 方法为例：

``` java
public interface IOrderService {
    @DtfFmt
    public boolean order(Order order);
}
```

该方法的实现为：
``` java
// public boolean order(Order order);实现
@Transactional
@Override
public boolean order(Order order) {
    orderDao.createOrder(order);
    return true;
}

// orderDao.createOrder(order);实现
public int createOrder(Order order) {
    String sql = "INSERT INTO dtf_demo_order (product_id, qty, account_id) VALUES (?, ?, ?)";
    try {
        GeneratedKeyHolder keyHolder = new GeneratedKeyHolder();
        jdbcTemplate.update(new PreparedStatementCreator() {
            @Override
            public PreparedStatement createPreparedStatement(Connection con) throws SQLException {
                PreparedStatement ps = con.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
                ps.setInt(1, order.getProductId());
                ps.setInt(2, order.getQty());
                ps.setInt(3, order.getAccountId());
                return ps;
            }
        }, keyHolder);
        return keyHolder.getKey().intValue();
    } catch (Exception e) {
        LOG.error("Create order failed.", e);
        throw new RuntimeException("Create order failed.");
    }
}
```

在`orderDao.createOrder(order);`方法中执行了一句Insert语句，此时框架会注册一个分支事务对这个Insert进行全局的事务管理。

分支事务注解支持的参数包括：

| 参数        | 数据类型                     | 必填 | 默认值 | 描述                                                 |
| ----------- | ---------------------------- | ---- | ------ | ---------------------------------------------------- |
| rollbackFor | Class<? extends Throwable>[] | 否   | {}     | 分支事务在识别到以下异常时回滚主事务，未配置时不回滚 |  

rollbackFor：默认为空。若想要在发生异常时回滚，可设置为 Exception。

## 远程请求时传递分布式事务上下文

使用`RestTemplate`或`FeginClient`时，DTF框架支持自动化的分布式事务上下文传递。

如果使用了其他的通信框架，也可以**手动处理分布式事务上下文**。

### 主调 - RestTemplate

使用`RestTemplate`访问下游服务时，DTF 框架自动注入了 TxRestTemplateInterceptor，向请求头中装载分布式事务上下文信息。

DTF 框架注入的请求头信息为：
``` sh
# 事务分组 ID
DTF-Group-ID: ${GroupId}
# 主事务 ID
DTF-Tx-ID: ${TxId}
# 父级分支事务 ID
DTF-Last-Branch-ID: ${LastBranchId}
```

### 主调 - FeginClient

使用`FeginClient`访问下游服务时，DTF 框架自动注入了 TxFeignInterceptor，向请求头中装载分布式事务上下文信息。

需要引入 feign 依赖：

``` xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```

DTF 框架注入的请求头信息为：

``` sh
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

``` properties
# Header key的常量ClientConstant.HTTP_HEADER.GROUP_ID
DTF-Group-ID: ${GroupId}
# Header key的常量ClientConstant.HTTP_HEADER.TX_ID
DTF-Tx-ID: ${TxId}
# Header key的常量 ClientConstant.HTTP_HEADER.LAST_BRANCH_ID
DTF-Last-Branch-ID: ${LastBranchId}
```

并通过 TxContextRestore 切点还原分布式事务上下文。

### 被调 - 手动处理

可以参考  [Spring Free 开发指导](https://cloud.tencent.com/document/product/1224/45970)  中的`远程请求时传递分布式事务上下文`章节。

## 与 TSF 结合使用

引入依赖后（注意 SDK 版本），直接正常使用 TSF 即可。


### 使用方式
目前支持 Greenwich（G）和 Finchley（F）版本的 TSF SDK。您可以单击以下页签，查看对应的使用方式。
<dx-tabs>
::: G&nbsp;版本&nbsp;TSF&nbsp;SDK&nbsp;使用方式
``` xml
<!-- TSF 启动器 -->
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-starter</artifactId>
    <version>1.23.0-Greenwich-RELEASE</version>
</dependency>
```
:::
::: F&nbsp;版本&nbsp;TSF&nbsp;SDK&nbsp;使用方式
>!需要再排除 DTF 中的一些依赖。

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



