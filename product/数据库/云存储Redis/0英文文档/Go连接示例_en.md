**Preparations before running**:

Use the client Go-redis and download it at https://github.com/alphazero/Go-Redis

**Sample codes**:
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
   // Connect to the Redis server 192.168.0.195:6379 and authorize the use of instanceId password
   spec := redis.DefaultSpec().Host(host).Port(port).Password(instanceId+":"+pass);
   client, err := redis.NewSynchClientWithSpec(spec)



   if err != nil { // Whether an error occurs with the connection

      log.Println("error on connect redis server")

      return

   }



   newvalue :=[]byte("QcloudV5!");

   err=client.Set("name",newvalue);

   if err != nil { // Incorrect set value

      log.Println(err)

      return

   }

   

   value, err := client.Get("name") // Value

   if err != nil { 

      log.Println(err)

      return

   }

   fmt.Println("name value is:",fmt.Sprintf("%s", value)) //Output

} 

```

**Execution results**:
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Go-1.png)
