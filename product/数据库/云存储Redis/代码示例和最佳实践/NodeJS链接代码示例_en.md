**Preparations before running**:

Install node-redis by executing the following command:
npm install hiredis redis

**Sample Codes**:

```
var redis = require("redis");

/**Input your Redis instance's private IP, port number, instance ID and password for the following fields*/
var host = "192.168.0.2",
port = "6379",
instanceid = "c532952f-55dc-4c22-a941-63057e560788",
pwd = "1234567q";
//Connect to Redis
var client  = redis.createClient(port, host, {detect_buffers: true});
// Redis connection error
client.on("error", function(error) {
    console.log(error);
});
//Authentication
client.auth(instanceid + ":" + pwd);

/**Then start to work with the Redis instance */
//Set the key
client.set("redis", "tencent", function(err, reply){
    if (err) {
        console.log(err);  
            return;  
    }
    console.log("set key redis " + reply.toString() + ", value is tencent");  
});

//Get the key
client.get("redis", function (err, reply) {
    if (err) {
        console.log(err);  
        return;  
    }
    console.log("get key redis is:" + reply.toString());
    //Close the client when the program ends
    client.end();
});
```

**Execution results**:
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/NodeJS-1.jpg)
