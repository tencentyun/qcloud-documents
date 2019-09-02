## 1. Environment and dependency

Environment: Install Java JDK [[download address](http://www.oracle.com/technetwork/java/javase/downloads/index.html?spm=5176.775974146.2.4.9Oqs71)] on Tencent Cloud CVM

Dependency  Memcached-Java-Client.2.5.1 [[download address]](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/memcached-java-2.5.1.zip) is used in this example. SpyMemcached client is not supported currently

## 2. Steps

Create a new Java project in your local computer, and import the downloaded Memcached-Java-Client.2.5.1 source code.

Write the source code and export it as a JAR package.

Upload the exported JAR package onto Tencent Cloud CVM and run java -jar ***.jar. (Note: NoSQL server of the private network can only be accessed from the CVM)

Sample code: MemcachedDemo.java

```
/**
 * qcloud cmem java-memcached2.5.1-client demo
 * Usage:
 * 1. memcached2.5.1 source code address: http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/memcached-java-2.5.1.zip
 * 2. Download the source code and put it into the project
 * 3. Implement corresponding feature by referencing demo code
 */

package com.qcloud.memcached.demo;
import com.danga.MemCached.MemCachedClient;
import com.danga.MemCached.SockIOPool;

import java.util.Date;

public class MemcachedDemo {
    public static void main(String[] args){

        //In the console, click "NoSQL Fast Storage", and you can see IP:Port assigned by the system in "Management View".
        //You need to access via private IP, without the need of account and password
        final String ip = "**.***.***.**";
        final String port = "****";

        System.out.println("start test qcloud cmem - " + ip + ":" + port);

        MemCachedClient memcachedClient = null;

        try{
            //Set the list of cache servers. You can specify multiple cache servers when using distributed cache
            String[] servers = {ip + ":" + port};

            //Set socket connection pool instance
            SockIOPool pool = SockIOPool.getInstance();
            pool.setServers(servers);//Set the list of cache servers available for the connection pool
            pool.setFailover(true);//Set failover
            pool.setInitConn(10);//Set the initial number of connections available for each cache server
            pool.setMinConn(5);//Set the minimum number of connections available for each server
            pool.setMaxConn(250);//Set the maximum number of connections available for each server
            pool.setMaintSleep(30);//Set the sleep time of maintenance thread of the connection pool
            pool.setNagle(false);//Set whether to use Nagle algorithm. Since the amount of our communication data is generally large (relative to that of TCP control data), and prompt response is required, <br> you need to set this value to false (default is true) </br>
            pool.setSocketTO(3000);//Set socket read timeout
            pool.setAliveCheck(true);//Set alive check
            pool.initialize();

            memcachedClient = new MemCachedClient();

            //Store the data into the cache
            memcachedClient.set("cmem", "qcloud cmem service");

            //Store the data into the cache, and set expiration time
            Date date = new Date(1000);
            memcachedClient.set("test_expire", "test_expire_value", date);

            //Obtain cache data
            System.out.println("get: cmem = " + memcachedClient.get("cmem"));
            System.out.println("get: test_expire = " + memcachedClient.get("test_expire"));

            //Store multiple data entries into cmem
            for(int i = 0; i < 100; i++){
                String key = "key-" + i;
                String value = "value-" + i;
                memcachedClient.set(key, value);
            }

            System.out.println("Complete the setup");
        } catch (Exception e) {
            e.printStackTrace();
        }
        if (memcachedClient != null) {
            memcachedClient = null;
        }
    }
}
```
