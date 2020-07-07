# FMT事务

FMT事务，也可以理解为框架托管事务。需要用户仅需要在`FMT规范`下正常实现业务逻辑即可实现分布式事务。相对于TCC事务，省去了编写Confirm，Cancel的代码工作。

## 准备工作

参考[准备工作](https://tcloud-doc.isd.com/document/product/1224/45966)章节进行。

参考[快速部署](https://tcloud-doc.isd.com/document/product/1224/45967#.E5.88.9D.E5.A7.8B.E5.8C.96.E6.95.B0.E6.8D.AE.E5.BA.93.EF.BC.88mysql.E5.8D.B3.E5.8F.AF.EF.BC.89)，执行FMT初始化脚本。

## FMT规范

FMT事务的实现原理是：代理用户执行`PrepareStatement`和`CreateStatement`操作，对执行的DML语句进行解析，记录前后象，并生成UNDO信息。鉴于此，FMT对用户使用的数据库和SQL语句会有一定的要求，详见[FMT规范](http://www.tencent.com)。

## Maven配置

通过配置业务代码的pom.xml文件，可以引入DTF的SDK到您的工程中。

> 配置中的${dtf.version}可以参考[Release Note](https://tcloud-doc.isd.com/document/product/1224/44764)中，选择`最新版本（推荐）`或指定版本。

``` xml
<dependency>
    <groupId>com.tencent.cloud</groupId>
    <artifactId>spring-boot-dtf</artifactId>
    <version>${dtf.version}</version>
</dependency>
```

## 客户端配置

在客户端中，支持以下配置自定义

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
| dtf.env.groups.${GroupId} | String   | 是   | 共享集群TC列表，如果是独占集群则需要填写 | 用户的事务分组ID，单客户端使用多个事务分组时可以配置多项     |
| dtf.env.groups.secretId   | String   | 是   | 无                                       | 用户的腾讯云SecretID                                         |
| dtf.env.groups.secretKey  | String   | 是   | 无                                       | 用户的腾讯云SecretKey                                        |
| dtf.env.groups.server     | String   | 否   | ${spring.application.name}               | 客户端服务标识，一个事务分组下，同一服务需要使用相同的标识。 |

> 注：通常情况下，仅需要在dtf.env.groups下配置一个事务分组。

例如：

用户A，创建了一个事务分组`group-x3k9s0ns`，在[分布式事务控制台](https://console.cloud.tencent.com/dtf/)获取该分组的TC集群地址为`127.0.0.1:8080;127.0.0.1:8081;127.0.0.1:8082`。该用户访问密钥的SecretId为`SID`，SecretKey为`SKEY`。需要在业务应用`app-test`上使用该事物时，配置样例为：

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

> 注：此时`dtf.env.groups.server`的值为`app-test`。

---

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

> 注：通常建议同时启用本地事务管理`@EnableTransactionManagement`

---

## 主事务管理

主事务的生命周期可以分为：`开启`，`提交`/`回滚`。

可以根据实际业务的需要选择`通过注解管理主事务`或`通过API管理主事务`。

### 通过注解管理主事务

> 注：主事务通常建议在入口Controller方法处开启。一般注释在`实现类`方法上，并且该类需要注入为Bean。

以下面注解了`@DtfTransactional`的order方法为例：

``` java
@DtfTransactional
@RequestMapping("/order")
public Boolean order(@RequestBody Order order) {
    // 执行业务逻辑或分支事务
}
```

进入order方法前DTF框架`开启`主事务。

执行业务逻辑或分支事务。

如果该方法正常执行完毕，返回业务数据（或者void方法无返回值），DTF框架`提交`主事务。

如果该方法执行出现问题，抛出异常时，DTF框架`回滚`主事务。

DTF框架自动关闭当前线程`主事务上下文`。

#### 主事务注解支持的能力包括

| 参数    | 数据类型 | 必填 | 默认值    | 描述                                                          |
| ------- | -------- | ---- | --------- | ------------------------------------------------------------- |
| timeout | Integer  | 否   | 60 * 1000 | 事务超时时间（主事务`开启`到`提交`/`回滚`的时长），单位：毫秒 |
| groupId | String   | 否   |           | 在此事务分组下开启主事务                                      |

> 注：如果`dtf.env.groups`下只配置了`1个`事务分组ID，则@DtfTransactional注解中`不需要`填写groupId，DTF框架会自动从配置中获取。

---

### 通过API管理主事务

如果业务存在异步操作或者有特殊诉求（例如：一个主事务不能在单一方法闭环），也可以使用API来进行主事务管理。

还是以上面的order方法为例，此时需要等待一个orderCallback回调来确认提交或回滚主事务：

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
        // 如果全局使用DTF框架，可以忽略该步骤，框架会自动完成上下文传递。详见[远程请求时传递分布式事务上下文]章节
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

---

## 分支事务管理

FMT的分支事务管理是自动化的，并且与TCC分支事务略有不同。

FMT分支事务的注解并不会直接触发分支事务生成，而是将注解方法的执行上下文切换为FMT模式。该方法内的所有本地调用所执行的`每1行DML语句`都会自行生成`1个分支事务`。

### 通过注解管理分支事务

> 注：分支事务通常建议注解在业务的Service上。可以注解在`接口`或`实现类`上，并且该类需要注入为Bean。

以下面注解了`@DtfFmt`的order方法为例：

``` java
public interface IOrderService {
    @DtfFmt
    public boolean order(Order order);
}
```

该方法的实现为:

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

---

## 远程请求时传递分布式事务上下文

使用`RestTemplate`或`FeginClient`时，DTF框架支持自动化的分布式事务上下文传递。

如果使用了其他的通信框架，也可以`手动处理分布式事务上下文`。

### 主调 - RestTemplate

使用`RestTemplate`访问下游服务时，DTF框架自动注入了TxRestTemplateInterceptor，向请求头中装载分布式事务上下文信息。

DTF框架注入的请求头信息为：

``` sh
# 事务分组ID
DTF-Group-ID: ${GroupId}
# 主事务ID
DTF-Tx-ID: ${TxId}
# 父级分支事务ID
DTF-Last-Branch-ID: ${LastBranchId}
```

### 主调 - FeginClient

使用`FeginClient`访问下游服务时，DTF框架自动注入了TxFeignInterceptor，向请求头中装载分布式事务上下文信息。

需要引入feign依赖

``` xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```

DTF框架注入的请求头信息为：

``` sh
# 事务分组ID
DTF-Group-ID: ${GroupId}
# 主事务ID
DTF-Tx-ID: ${TxId}
# 父级分支事务ID
DTF-Last-Branch-ID: ${LastBranchId}
```

### 主调 - 手动处理

可以参考[Spring Free开发指导](https://tcloud-doc.isd.com/document/product/1224/45970#.E8.BF.9C.E7.A8.8B.E8.AF.B7.E6.B1.82.E6.97.B6.E4.BC.A0.E9.80.92.E5.88.86.E5.B8.83.E5.BC.8F.E4.BA.8B.E5.8A.A1.E4.B8.8A.E4.B8.8B.E6.96.87)中的`远程请求时传递分布式事务上下文`章节。

### 被调 - Spring MVC - Controller

使用Spring MVC的应用，在进入Controller前，DTF框架会自行从请求头中检索下列Header key。

``` properties
# Header key的常量ClientConstant.HTTP_HEADER.GROUP_ID
DTF-Group-ID: ${GroupId}
# Header key的常量ClientConstant.HTTP_HEADER.TX_ID
DTF-Tx-ID: ${TxId}
# Header key的常量 ClientConstant.HTTP_HEADER.LAST_BRANCH_ID
DTF-Last-Branch-ID: ${LastBranchId}
```

并通过TxContextRestore切点还原分布式事务上下文。

### 被调 - 手动处理

可以参考[Spring Free开发指导](https://tcloud-doc.isd.com/document/product/1224/45970#.E8.BF.9C.E7.A8.8B.E8.AF.B7.E6.B1.82.E6.97.B6.E4.BC.A0.E9.80.92.E5.88.86.E5.B8.83.E5.BC.8F.E4.BA.8B.E5.8A.A1.E4.B8.8A.E4.B8.8B.E6.96.87)中的`远程请求时传递分布式事务上下文`章节。

## 与TSF结合使用

DTF框架完全兼容TSF应用，请按照下面的指引使用。

> 注：目前仅支持Greenwich版本的TSF SDK。

### Maven POM

``` xml
<!-- TSF 启动器 -->
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-starter</artifactId>
</dependency>
```

### 启用TSF

``` java
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
