**运行前必备**：

使用客户端Jedis，下载和参考地址：https://github.com/xetorthio/jedis/wiki/Getting-started

**示例代码**：

```
import redis.clients.jedis.Jedis;

public class HelloRedis {

  public static void main(String[] args) {
        try {
            /**以下参数分别填写您的redis实例内网IP，端口号，实例id和密码*/
            String host = "192.168.0.195";
            int port = 6379;
            String instanceid = "84ffd722-b506-4934-9025-645bb2a0997b";
            String password = "1234567q";
            //连接redis
            Jedis jedis = new Jedis(host, port);
            //鉴权
            jedis.auth(instanceid + ":" + password);

            /**接下来可以愉快的开始操作redis实例，可以参考：https://github.com/xetorthio/jedis */
            //设置key
            jedis.set("redis", "tencent");
            System.out.println("set key redis suc, value is: tencent");
            //获取key
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
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/JAVA-1.jpg)