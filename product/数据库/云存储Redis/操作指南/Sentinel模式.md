## 操作场景
Sentinel（哨兵）是一个独立运行的进程，用于监控 Redis 集群中主从节点的状态，主节点异常时，Sentinel 可以在从节点选举出新的主节点，自动替代原主节点，保障业务平稳运行，是一种高可用解决方案。

## Sentinel 相关命令
云数据库 Redis 4.0及以上版本均默认支持 Sentinel（哨兵）模式，您可以使用如下 Sentinel 相关命令。

### SENTINEL sentinels
列出所监控的 master 相关的 sentinels 信息。

#### 命令格式
`SENTINEL sentinels <任意名称>`

#### 使用示例
![](https://qcloudimg.tencent-cloud.cn/raw/c4f4f73b0874ab3aeea2cee3eb2e2360.png)

### SENTINEL get-master-addr-by-name
获取 master-name 相关的 ip addr 的信息。

#### 命令格式
`SENTINEL get-master-addr-by-name <任意名称>`

#### 使用示例
![](https://qcloudimg.tencent-cloud.cn/raw/e32f8102ab6e7a4083199853c81e363f.png)

## Sentinel 模式连接示例
### 准备工作
- Redis 实例版本为4.0或5.0。
- 数据库实例运行状态正常，处于**运行中**。
- 在  [Redis 控制台](https://console.cloud.tencent.com/redis) 的**实例详情**页面的**网络信息**区域，获取连接数据库的**内网IPv4地址**及端口。具体信息，请参见 [查看实例详情](https://cloud.tencent.com/document/product/239/75437)。
- 已获取访问数据库的账号与密码。具体操作，请参见 [管理账号](https://cloud.tencent.com/document/product/239/36710)。
- 下载客户端 [Jedis](https://github.com/xetorthio/jedis/wiki/Getting-started)，推荐使用最新版本。

### 连接示例
下述示例代码以 [Jedis](https://github.com/redis/jedis) 客户端的3.6.0版本为例，推荐使用最新版本。

- Jedis 为3.6.0版本及以上。
- Lettuce 为5.3.0.RELEASE 版本及以上。
- Spring Data Redis 为2.5.1版本及以上，Spring Data Redis 需要配置 spring.redis.sentinel.password 参数。

您需要根据注释修改参数：连接数据库的 IP、端口及账号密码信息。

#### 通过 Java 方式连接
```
package com.example.demo;

import org.apache.commons.pool2.impl.GenericObjectPoolConfig;
import redis.clients.jedis.JedisSentinelPool;

import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        String masterName = "test";
        Set<String> sentinels = new HashSet<>();
        //如下您需要配置数据库实例的内网IPv4地址及端口
        sentinels.add("XX.XX.XX.XX:6379");
        GenericObjectPoolConfig poolConfig = new GenericObjectPoolConfig();
        String dbPassword = "root:xxx";//您需替换访问数据库的密码
        String sentinelPassword = "root:xxx";//您需替换访问数据库的密码

        JedisSentinelPool jedisSentinelPool =
            new JedisSentinelPool(masterName, sentinels, poolConfig,
                2000, 2000, dbPassword,
                0, null, 2000, 2000,
                sentinelPassword, null);
        System.out.println("jedisSentinelPool.getResource().ping() = " + jedisSentinelPool.getResource().ping());
        jedisSentinelPool.close();
    }
}
```

#### 通过 Spring Data 框架连接
```
package com.example.demo;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.condition.ConditionalOnBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisPassword;
import org.springframework.data.redis.connection.RedisSentinelConfiguration;
import org.springframework.data.redis.connection.jedis.JedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import redis.clients.jedis.JedisPoolConfig;

@SpringBootApplication

public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}

@Configuration
class RedisConfig {
    @Bean
    @Qualifier("jedisConnectionFactory")
    public JedisConnectionFactory connectionFactory() {
        RedisSentinelConfiguration sentinelConfig = new RedisSentinelConfiguration()
            .master("test")
            .sentinel("XX.XX.XX.XX", 6379);//您需要替换为数据库实例的内网IPv4地址及端口
        sentinelConfig.setPassword(RedisPassword.of("xxx"));//您需替换访问数据库的密码
        sentinelConfig.setSentinelPassword(RedisPassword.of("xxx"));//您需替换访问数据库的密码
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        JedisConnectionFactory connectionFactory = new JedisConnectionFactory(sentinelConfig, poolConfig);
        connectionFactory.afterPropertiesSet();
        return connectionFactory;
    }

    @Bean
    @ConditionalOnBean(JedisConnectionFactory.class)
    public RedisTemplate<String, String> redisTemplate(@Qualifier("jedisConnectionFactory") JedisConnectionFactory factory) {
        RedisTemplate<String, String> template = new RedisTemplate<>();
        template.setConnectionFactory(factory);
        template.afterPropertiesSet();
        //test
        template.opsForValue().set("test", "test1");
        System.out.println("template.opsForValue().get(\"test\") = " + template.opsForValue().get("test"));
        return template;
    }

}
```



