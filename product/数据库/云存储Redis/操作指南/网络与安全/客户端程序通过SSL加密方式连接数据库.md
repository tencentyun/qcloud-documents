
本文列举常用的客户端程序代码示例，辅助您使用 SSL 加密方式访问数据库。

## 准备工作

- 已 [开通 SSL 加密](https://cloud.tencent.com/document/product/239/75865)，获取 SSL 认证证书文件。
- 在 [Redis 控制台](https://console.cloud.tencent.com/redis) 的**实例详情**页面的**网络信息**区域，获取连接数据库的**内网IPv4地址**及端口。具体信息，请参见 [查看实例详情](https://cloud.tencent.com/document/product/239/75437)。
- 已获取访问数据库的账号与密码。具体操作，请参见 [管理账号](https://cloud.tencent.com/document/product/239/36710)。

## Java
下述示例代码以 [Jedis](https://github.com/redis/jedis) 客户端的3.6.0版本为例，推荐使用最新版本。您需要根据注释修改参数：SSL 证书文件、连接数据库的 VIP、端口及账号密码信息。

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
        //vip 为连接数据库的内网 IPv4 地址，6379为默认的端口号，pwd 为默认账号的密码，您需根据实际情况替换。
        JedisPool pool = new JedisPool(genericObjectPoolConfig, "vip",
                6379, 2000, "pwd", 0, true, sslSocketFactory, null, null);
        Jedis jedis = pool.getResource();
        System.out.println(jedis.ping());
        jedis.close();
    }
}
```

## Python
下述示例代码以 [redis-py](https://github.com/andymccurdy/redis-py) 客户端为例，推荐使用最新版本。 您需要根据注释修改参数：SSL 证书文件、连接数据库的 VIP、端口及账号密码信息。

```
import redis3 as redis3

if __name__ == "__main__":
# vip 为连接数据库的内网 IPv4 地址，6379为默认的端口号，pwd 为默认账号的密码，ca.pem 为获取的 SSL 证书文件，您需根据实际情况替换。
    client = redis3.Redis(host="vip", port=6379, password="pwd", ssl=True, ssl_cert_reqs="required",
                          ssl_ca_certs="ca.pem")
    print(client.ping())
```

