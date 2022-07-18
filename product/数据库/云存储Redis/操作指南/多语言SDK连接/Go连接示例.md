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

   const host=192.xx.xx.195
   const port=6379
   const instanceId="84ffd722-b506-4934-9025-64xxx997b"
   const pass="123d7sq"
   // 连接 Redis 服务器 192.xx.xx.195:6379 并授权 instanceId 密码
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
![](https://main.qcloudimg.com/raw/013f96ad8b05ed5c1eceb4638c24f3b1.png)
