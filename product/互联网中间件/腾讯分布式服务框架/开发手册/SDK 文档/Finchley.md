## Spring Cloud TSF Finchley
基于 Spring Cloud Finchley 版本 SDK，支持 spring boot 2.0.x。

---

### 1.16.0-Finchley-RELEASE（2019-10-11）

#### 新特性
- kafka的链路追踪能力。
- 增加 swagger-ui依赖包。

#### 优化
- 集成spring-cloud-tsf-swagger包后, 本地启动无需设置tsf.swagger.enabled=false。
- 集成spring-cloud-tsf-swagger包后, 支持本地使用swagger-ui进行调试。

#### Bug 修复
- 修复DEBUG 日志级别启动时, spring-cloud-tsf-sleuth包空指针异常。
- 修复引入swagger包后, 低版本guava包引起冲突。
- 配置回调功能空指针异常。

#### 版本建议

- 支持向后兼容，建议全量升级。

---

### 1.14.3-Finchley-RELEASE（2019-09-10）

#### Bug 修复
- 限流Bug fix。
- TsfContext.putTag覆盖bug fix。

#### 版本建议

- 支持向后兼容，建议全量升级。

---

### 1.14.2-Finchley-RELEASE（2019-08-14）

#### Bug 修复
- 修复使用RedisConnectionFactory获取Redis连接，这种方式使用时的一个类型转化错误。
- 修复在给span.tag(key,value)传入value时没判空抛出异常的问题。

#### 版本建议
- 支持向后兼容，建议全量升级。

---

### 1.14.1-Finchley-RELEASE（2019-07-24）

#### Bug 修复
- 修复tsf sdk依赖的scheduler和业务自身的scheduler相互影响的问题
- 修复spring-cloud-tsf-route 包路由不生效的问题
- 修复spring-cloud-tsf-ratelimit包限流不准确问题
- 修复 spring-cloud-tsf-sleuth 包数据源和Mybatis兼容性问题

#### 版本建议
- 支持向后兼容，建议全量升级。

---

### 1.14.0-Finchley-RELEASE（2019-06-21）

#### 新特性

- 支持 MySQL JDBC、Redis、MongoDB、CMQ 组件调用链。	

#### 版本建议

- 支持向后兼容，建议全量升级。

---

### 1.12.4-Finchley-RELEASE（2019-08-15）

#### Bug 修复

- 修复tsf sdk依赖的scheduler和业务自身的scheduler相互影响的问题
- 修复spring-cloud-tsf-route 包路由不生效的问题
- 修复spring-cloud-tsf-ratelimit包限流不准确问题

#### 版本建议

- 支持向后兼容，建议全量升级。

---

### 1.12.3-Finchley-RELEASE（2019-05-17）

#### Bug 修复

- 修复 Finchley 版本服务调用监控问题。

#### 版本建议
- 支持向后兼容，建议全量升级。

---

### 1.12.2-Finchley-RELEASE（2019-04-22）

#### Bug 修复
- 修复 Finchley 版本 TSF Route 启动问题。
- 修复 Finchley 版本 Feign HttpClient 调用链问题。

#### 版本建议
- 支持向后兼容，建议全量升级。

---

### 1.12.1-Finchley-RELEASE（2019-03-25）

#### Bug 修复

- 修复配置回调功能未生效问题。

#### 版本建议

- 支持向后兼容，建议全量升级。

---

### 1.12.0-Finchley-RELEASE（2019-03-13）

#### 新特性

- 支持自动重注册，服务鉴权/路由/限流策略本地缓存。
- 服务路由支持基于可用区和地域就近访问策略。

#### 优化

- 升级分布式配置监听，精确并减小监听范围，处理更新为空的场景，避免大范围 key 刷新事件。
- 优化分部署配置回调触发逻辑。

#### Bug 修复

- spring-cloud-commons 升级到1.3.1解决 RetryTemplate 会导致 LoadBalanceInterceptor thread unsafe 问题。
- 修复启用 hystrix 时配置会导致 tsf-route 与 feignbuilder 冲突的问题。

#### 版本建议

- 支持向后兼容，建议全量升级。