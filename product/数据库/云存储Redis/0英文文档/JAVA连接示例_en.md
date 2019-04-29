**Preparations before running**:

Use the client Jedis and download it at https://github.com/xetorthio/jedis/wiki/Getting-started

**Sample codes**:

```
import redis.clients.jedis.Jedis;

public class HelloRedis {

  public static void main(String[] args) {
        try {
            /**Input your Redis instance's private IP, port number, instance ID and password for the following fields*/
            String host = "192.168.0.195";
            int port = 6379;
            String instanceid = "84ffd722-b506-4934-9025-645bb2a0997b";
            String password = "1234567q";
            //Connect to Redis
            Jedis jedis = new Jedis(host, port);
            //Authentication
            jedis.auth(instanceid + ":" + password);

            /**Then start to work with the Redis instance by referring to:https://github.com/xetorthio/jedis */
            //Set the key
            jedis.set("redis", "tencent");
            System.out.println("set key redis suc, value is: tencent");
            //Get the key
            String value = jedis.get("redis");
            System.out.println("get key redis is: " + value);

            //Close to exit
            jedis.quit();
            jedis.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**Execution results**:
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/JAVA-1.jpg)
