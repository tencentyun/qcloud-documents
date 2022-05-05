**运行前必备**：
下载客户端 [Jedis](https://github.com/xetorthio/jedis/wiki/Getting-started)。

**示例代码**：

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
![](https://main.qcloudimg.com/raw/d6103ac896b55e6412a1dd172aedc412.jpg)

