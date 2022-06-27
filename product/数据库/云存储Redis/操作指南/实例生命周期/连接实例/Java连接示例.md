本文列举客户端 Java 代码示例，辅助您使用 SSL 加密或不加密的方式访问数据库。

## 准备工作
- 在 [Redis 控制台](https://console.cloud.tencent.com/redis) 的**实例详情**页面的**网络信息**区域，获取连接数据库的**内网IPv4地址**及端口。具体信息，请参见 [查看实例详情](https://cloud.tencent.com/document/product/239/75437)。
- 已获取访问数据库的账号与密码。具体操作，请参见 [管理账号](https://cloud.tencent.com/document/product/239/36710)。
- 下载客户端 [Jedis](https://github.com/xetorthio/jedis/wiki/Getting-started)，推荐使用最新版本。
- 如果使用 SSL 加密方式连接数据库，请 [开通 SSL 加密](https://cloud.tencent.com/document/product/239/75865)，获取 SSL 认证证书文件。

## 未开通 SSL 加密方式连接示例
您需要根据注释修改参数：连接数据库的 IP、端口及账号密码信息。
```
import redis.clients.jedis.Jedis;

public class HelloRedis {

  public static void main(String[] args) {
        try {
            /**以下参数，如果为内网访问，分别填写您的 Redis 实例内网 IP、端口号、实例 ID 和密码；
                        如果为外网访问，分别配置实例外网地址、端口号及其密码，无需设置实例 ID*/
            String host = "192.xx.xx.195";
            int port = 6379;
            String instanceid = "crs-09xxxqv";
            String password = "123ad6aq";
            //连接 Redis
            Jedis jedis = new Jedis(host, port);
            //鉴权
            jedis.auth(instanceid + ":" + password);

            /**接下来可以开始操作 Redis 实例，可以参考 https://github.com/xetorthio/jedis */
            //设置 Key
            jedis.set("redis", "tencent");
            System.out.println("set key redis suc, value is: tencent");
            //获取 Key
            String value = jedis.get("redis");
            System.out.println("get key redis is: " + value);

            //关闭退出
            jedis.quit();
            jedis.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

 **运行结果**：
![img](https://main.qcloudimg.com/raw/d6103ac896b55e6412a1dd172aedc412.jpg) 

## 通过 SSL 加密方式连接示例
您需要根据注释修改参数：SSL 证书文件、连接数据库的 IP、端口及账号密码信息。

```java
import org.apache.commons.pool2.impl.GenericObjectPoolConfig;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSocketFactory;
import javax.net.ssl.TrustManager;
import javax.net.ssl.TrustManagerFactory;
import java.io.FileInputStream;
import java.io.InputStream;
import java.security.KeyStore;
import java.security.SecureRandom;


public class Main {

    public static void main(String[] args) throws Exception {
        KeyStore trustStore = KeyStore.getInstance("jks");
        //ca.jks 为证书文件名称。
        try (InputStream inputStream = new FileInputStream("ca.jks") ){
            trustStore.load(inputStream, null);
        }
        TrustManagerFactory trustManagerFactory =      TrustManagerFactory.getInstance("PKIX");
        trustManagerFactory.init(trustStore);
        TrustManager[] trustManagers = trustManagerFactory.getTrustManagers();

        SSLContext sslContext = SSLContext.getInstance("TLS");
        sslContext.init(null, trustManagers, new SecureRandom());
        SSLSocketFactory sslSocketFactory =  sslContext.getSocketFactory();
        GenericObjectPoolConfig genericObjectPoolConfig = new GenericObjectPoolConfig();

        //with ssl config jedis pool
        //vip 为连接数据库的内网 IPv4 地址，6379为默认的端口号，pwd 为默认账号的密码。您需根据实际情况替换。
        JedisPool pool = new JedisPool(genericObjectPoolConfig, "vip",
                6379, 2000, "pwd", 0, true, sslSocketFactory, null, null);
        Jedis jedis = pool.getResource();
        System.out.println(jedis.ping());
        jedis.close();
    }
}
```



