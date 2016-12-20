**运行前必备**：

安装node-redis，安装命令：
npm install hiredis redis

**示例代码**：

```
var redis = require("redis");

/**以下参数分别填写您的redis实例内网IP，端口号，实例id和密码*/
var host = "192.168.0.2",
port = "6379",
instanceid = "c532952f-55dc-4c22-a941-63057e560788",
pwd = "1234567q";
//连接redis
var client  = redis.createClient(port, host, {detect_buffers: true});
// redis连接错误
client.on("error", function(error) {
    console.log(error);
});
//鉴权
client.auth(instanceid + ":" + pwd);

/**接下来可以愉快的开始操作redis实例 */
//设置key
client.set("redis", "tencent", function(err, reply){
    if (err) {
        console.log(err);  
            return;  
    }
    console.log("set key redis " + reply.toString() + ", value is tencent");  
});

//获取key
client.get("redis", function (err, reply) {
    if (err) {
        console.log(err);  
        return;  
    }
    console.log("get key redis is:" + reply.toString());
    //程序结束关闭客户端
    client.end();
});
```

**运行结果**：
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/NodeJS-1.jpg)