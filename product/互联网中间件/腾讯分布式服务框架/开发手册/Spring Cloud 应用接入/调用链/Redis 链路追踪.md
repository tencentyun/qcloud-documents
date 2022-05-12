## 添加依赖
考虑到 Redis 库的多样性，以及 spring-data-redis 库的易用性，目前只对`spring-boot-starter-data-redis`进行支持，在引用 spring-boot-starter-data-redis 时不要指定版本，只需要整个工程依赖 parent pom 即可：

```xml
<parent>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-dependencies</artifactId>
    <version>tsf 的版本号（1.14以后开始支持 Redis）</version>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-redis</artifactId>
     </dependency>
</parent>
```

`spring-boot-starter-data-redis`的版本为 parent pom 文件管理的 Redis Starter 的版本。在代码中具体使用时，引入 RedisTemplate，然后使用其方法即可。不建议直接引用 Jedis 和 Lettuce 相关的依赖，spring-boot-starter-data-redis 会自动引用相关的依赖，并做适配。
如果通过其他方式引入 Redis 客户端（例如直接 new Jedis），则将无法在 TSF 的链路中查看到相应的信息。

## 16.1-Finchley-RELEASE 版本 Redis 调用链使用方式

### lettuce 方式
使用 lettuce 方式，pom 依赖如下：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

不需要额外依赖，自动依赖了 lettuce 方面的 jar 包，可以直接使用。通过该配置，也具有链路追踪的能力。

### jedis 方式
使用 jedis 方式，pom 依赖如下：

```xml
<dependency>
    <groupId>org.springframework.data</groupId>
    <artifactId>spring-data-redis</artifactId>
</dependency>
<!-- redis -->
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
</dependency>
```

通过以上配置，也能使用 SDK 的链路追踪能力。
