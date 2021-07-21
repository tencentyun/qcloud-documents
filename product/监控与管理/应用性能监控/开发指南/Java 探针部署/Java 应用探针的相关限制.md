# 支持列表
安装 3.0 Java 探针之前，请确保您的系统满足探针对相关应用的版本限制。

## JVM
| 名称               | 支持版本               |
| ------------------ | ---------------------- |
| IBM J9 VM          | 6,7,8                  |
| OpenJDK            | 6,7,8,9,10,11,13,14    |
| Oracle Hotspot JVM | 6,7,8,9,10,11,12,13,14 |

## 应用服务容器

| 容器名称                 | 支持版本                         |
| ------------------------ | -------------------------------- |
| Apache  Resin            | 3.0.x ~ 4.0.x                    |
| Apache Tomcat            | 5.5.x  ~ 9x                      |
| Eclipse Jetty            | 6.x  ~ 9x                        |
| IBM WebSphere            | 7.0、8.0、8.5.x                  |
| JBoss Application Server | 4.x ~ 7.x                        |
| Oracle GlassFish Server  | 3.x ~ 4.x                        |
| WebLogic Server          | 10.3.x、12.1.x、12.2.x、12.2.1.3 |
| Wildfly                  | 8.x～19.x                        |

## 数据库
| 数据库                      | 支持版本                                                     |
| --------------------------- | ------------------------------------------------------------ |
| Apache  Derby               | 10.2.2.0 , 10.10.1.1 ,  10.11.1.1 , 10.13.1.1                |
| Apache Derby（derbyclient） | 10.9.1.0                                                     |
| IBM DB2                     | db2jcc（1.4.2）、db2jcc4（10.1,11.1）                            |
| Microsoft  SQL Server       | sqljdbc4（4.0）、jtds（1.2  ~1.3.1）                             |
| MySQL                       | 3.0.x ~ 8.x                                                  |
| Oracle                      | ojdbc5（11.1.x ~  11.2.x）、ojdbc6（11.1.x ~  12.1.x）、ojdbc7（12.1.0.2.0）、classes12（10g）、ojdbc14（10.2.0.4.0） |
| PostgreSql                  | 9.3-1104-jdbc4  、9.4.1208、42.0.0、42.1.4                   |
| Sybases                     | 支持                                                         |
| 达梦                        | Dm7JdbcDriver17                                              |
| 神通                        | 支持                                                         |
| 金仓                        | 支持                                                         |

## 数据库连接池

| 数据库连接池 | 支持版本                                          |
| ------------ | ------------------------------------------------- |
| C3p0         | c3p0（0.9.5.1 ~ 0.9.5.5）<br/>c3p0（0.9.1 ~ 0.9.1.2） |
| Dbcp         | commons-dbcp（1.4）                                 |
| Druid        | druid（1.0.4 ,  1.0.5， 1.0.15 ， 1.0.25）          |
| Hibernate    | hibernate-core（4.2.2.Final）                       |
| Mybatis      | mybatis（3.3.0）                                    |
| Proxool      | proxool（0.8.3）                                    |
| WebLogic     | 10.3.6, 12.1,  12.2                               |
| Hikaricp     | 2.4.0 ~ 3.4.2                                     |
| Spring-Jdbc  | spring-jdbc（3.2.17.RELEASE）                       |

## NoSQL

| NoSQL     | 支持版本                                                     |
| --------- | ------------------------------------------------------------ |
| Memcached | memcached-client（3.0.x）<br/>spymemcached     （2.10.x ~ 2.12.x ）<br/>xmemcached      （1.4.3+ , 2.0.x ~ 2.1.x ） |
| MongoDB   | 2.6.x ~ 2.14.x 、3.0.x ~ 3.12.x                              |
| Redisson  | 2.9.x ~ 2.15.x,  3.5.x ~ 3.12.x                              |
| Redis     | Jedis（2.7.x ~  3.x、1.5.2）<br/>Jedis 2.6.3 ~ 2.10.2 连接池<br/>spring-data-redis     （1.6.0.RELEASE~ 2.3.X.RELEASE） |

## Java 框架

| Java框架                     | 支持版本                                                     |
| ---------------------------- | ------------------------------------------------------------ |
| Apache  Struts               | struts2-core（2.0.x~2.5.x）                                    |
| Enterprise  Java Beans （EJB） | 2.0 、3.0                                                    |
| Java  Server Faces （JSF）     | jsf-api（jsf-api）                                             |
| Java Server Pages            | jsp-api（2.1,2.2）                                             |
| Jfinal                       | Jfinal（3.2）                                                  |
| Play Framework               | 1.2.6 ,  2.1.3，2.2.6 , 2.3.8 , 2.4.6，2.4.8，2.5.9          |
| Spring Boot                  | spring-boot（1.5.x），spring-boot（2.x+）                        |
| Spring Cloud                 | Spring Cloud Webflux 5.0.7.RELEASE ~ 5.2.8.RELEASE<br/>Spring  Cloud Webflux   5.0.7.RELEASE ~ 5.2.8.RELEASE （不支持 5.1.2.RELEASE, 5.1.7.RELEASE,   5.1.8.RELEASE）  <br/>Spring Cloud Gateway  2.0.0.RELEASE ~ 2.2.5.RELEASE<br/>Feign（9.0.x~11.0.x）<br/>Spring Cloud OpenFeign（2.0.0.RELEASE-2.2.6.RELEASE） |
| Spring                       | 3.x ~5.x                                                     |

## RPC（远程过程调用）

| RPC              | 支持版本                                                     |
| ---------------- | ------------------------------------------------------------ |
| Dubbo            | dubbox（ 2.8.0 ~ 2.8.4）<br/>alibaba dubbo（2.4.10~2.6.8）<br/>apache dubbo （2.7.2～2.7.7） |
| GRPC             | 1.0.1、1.6.1、1.10.1、1.12.0                                 |
| Twitter  Finagle | finagle-thrift_2.10（6.22.0）                                  |
| Thrift           | libthrift（0.5 ,  0.8.0 , 0.9.3）                              |

## WebService

| WebService       | 支持版本                                  |
| ---------------- | ----------------------------------------- |
| Apache  Axis2    | Axis（1.6.x ~1.7.x）                        |
| Apache CXF       | 2.1.x~3.0.x，3.1.x                        |
| Axis             | Axis（1.4）                                |
| GlassFish-Jersey | jersey-client（2.0~2.30.1）<br/>Jersey（2.9） |
| Java JAX-RS      | jaxrs-api（3.0.x）                          |
| Java JAX-WS      | jaxws-api（2.0.x~2.2.x）                    |
| Resteasy         | resteasy-jaxrs（2.0.x~3.0.x）               |
| Spring WS        | spring-ws-core（2.1.x  - 2.4.x）            |
| Sun-Jersey       | jersey-client（1.0.3~1.19.x）               |

## HTTP 调用

| 框架                     | 支持版本                                        |
| ------------------------ | ----------------------------------------------- |
| com.ning.asyncHttpClient | async-http-client（1.6.x ~ 1.9.x）                |
| HttpClient               | 3.x～4.x                                        |
| HttpURLConnection        | JDK1.6 、1.7、1.8                               |
| okHttp                   | 2.4.0<br/>3.4.0，3.5.0，3.8.1<br/>4.0.0 ~ 4.2.2 |
| org.asynchttpclient      | async-http-client（2.0.32）                       |

## 网络通信

| 框架  | 支持版本                        |
| ----- | ------------------------------- |
| Mina  | mina-core（2.0.9）                |
| Netty | 3.2.x ~  3.10.x、4.0.x ~ 4.10.x |

## 消息中间件

| 消息中间件          | 支持版本                                                     |
| ------------------- | ------------------------------------------------------------ |
| ActiveMQ            | 3.5.x~3.6.x                                                  |
| Kafka               | kafka  client（2.0.x-2.5.x）<br/>spring kafka（2.2.0.RELEASE～2.4.4.RELEASE） |
| JMS and  Spring-JMS | JMS 1.1                                                      |
| RabbitMQ            | Spring RabbitMQ 2.2.X.RELEASE，3.5.x - 4.x，5.0.x～5.8.x     |
| RocketMQ            | Apache RocketMQ  4.1.0，4.4.0～4.7.1 <br/>Alibaba RocketMQ 3.2.6、3.4.6、3.5.x |

## 日志组件

| 组件名称 | 支持版本                                  |
| -------- | ----------------------------------------- |
| Log4j    | log4j（1.2.x）<br/>log4j-core（2.0.x~2.14.x） |
| SLF4J    | slf4j-api（1.1.x ~ 2.0.0-alpha1）           |
| Logback  | logback-core（0.9.x~1.3.0-alpha5）          |

## 其他

| 组件                   | 支持版本                          |
| ---------------------- | --------------------------------- |
| Quartz   Job Scheduler | Quartz（1.8.3~ 2.2.x）              |
| Scala                  | Scala   2.9 - 2.10 async tracking |







