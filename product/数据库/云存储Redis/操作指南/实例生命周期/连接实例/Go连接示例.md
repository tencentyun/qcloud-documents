**运行前必备**：

下载客户端 [Go-redis](https://github.com/alphazero/Go-Redis)。

**示例代码**：
```
package main

import(

   "fmt"

   "redis"

   "log"

)

func main() {

   const host=192.168.0.195
   const port=6379
   const instanceId="84ffd722-b506-4934-9025-645bb2a0997b"
   const pass="1234567q"
   // 连接Redis服务器 192.168.0.195:6379 并授权 instanceId 密码
   spec := redis.DefaultSpec().Host(host).Port(port).Password(instanceId+":"+pass);
   client, err := redis.NewSynchClientWithSpec(spec)

   if err != nil { // 是否连接出错

      log.Println("error on connect redis server")

      return

   }

   newvalue :=[]byte("QcloudV5!");

   err=client.Set("name",newvalue);

   if err != nil { // 设置值出错

      log.Println(err)

      return

   }

   value, err := client.Get("name") // 取值

   if err != nil { 

      log.Println(err)

      return

   }

   fmt.Println("name value is:",fmt.Sprintf("%s", value)) //输出

} 

```

**运行结果**：
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Go-1.png)
