TSF 支持实现 JDBC 规范的 MySQL 驱动器和各类连接池（如 Tomcat-JDBC、DBCP、Hikari、Druid），在使用时需引入 SpringBoot 相关依赖和 MySQL 驱动依赖：

```
<!-- spring-boot-starter-jdbc -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId>
    <version>RELEASE</version>
</dependency>
<!-- mysql -->
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>RELEASE</version>
</dependency>
```

引入依赖后，根据需要添加相关数据库连接池依赖或直接使用 SpringBoot 默认选项。
