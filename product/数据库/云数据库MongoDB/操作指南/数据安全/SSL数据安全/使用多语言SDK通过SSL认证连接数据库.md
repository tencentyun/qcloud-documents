## Java
**keytool** 为 Java 原生自带的密钥和证书管理工具，方便用户能够管理自己的公钥/私钥及证书，用于认证服务。keytool 将密钥（key）和证书（certificates）存储在 keystore 密钥库中。 

使用 keytool 工具转换证书格式：
```
keytool -importcert -trustcacerts -file <certificate file> -keystore <trust store> -storepass <password>
```
- `-file <certificate file>`：指 SSL 证书或 TLS 证书文件 **MongoDB-CA.crt**。
- `-keystore <trust store>`：指定密钥库的名称。
- `-storepass <password> `：指定密钥库的密码。

设置 JVM 系统属性的密钥库，请根据实际替换 trustStore 与 password，以指向正确的密钥库。URI 拼接也请替换为访问数据库的用户密码信息。
```
System.setProperty("javax.net.ssl.trustStore", trustStore);
System.setProperty("javax.net.ssl.trustStorePassword", password);

import com.mongodb.MongoClientURI;
import com.mongodb.MongoClientOptions;

String uri = "mongodb://mongouser:password@10.x.x.1:27017/admin";
MongoClientOptions opt = MongoClientOptions.builder().sslEnabled(true).sslInvalidHostNameAllowed(true).build();
MongoClient client = new MongoClient(uri, options); 
```

## Go
如下为使用 GO 语言，通过 SSL 认证方式连接数据库的代码示例。请您根据实际情况替换证书文件 MongoDB-CA.crt 的路径、URI 中拼接的账号及其密码、IP 信息与端口信息。
```
package main

import (
    "context"
    "crypto/tls"
    "crypto/x509"
    "io/ioutil"

     "go.mongodb.org/mongo-driver/mongo"
     "go.mongodb.org/mongo-driver/mongo/options"
)

func main() {
    ca, err := ioutil.ReadFile("MongoDB-CA.crt")
    if err != nil {
        return
    }
    pool := x509.NewCertPool()
    ok := pool.AppendCertsFromPEM([]byte(ca))
    if !ok {
        return
    }
    tlsConfig := &tls.Config{
        RootCAs:      pool,
        InsecureSkipVerify: true,
    }
    uri := "mongodb://mongouser:password@10.x.x.1:27017/admin?ssl=true"
    clientOpt := options.Client().ApplyURI(uri)
    clientOpt.SetTLSConfig(tlsConfig)

     client, err := mongo.Connect(context.TODO(), clientOpt)
     if err != nil {
         return
     }
    client.Disconnect(context.TODO())
} 
```

## python
如下为使用 Python 语言，通过 SSL 认证方式连接数据库的代码示例。请您根据实际情况替换证书文件 MongoDB-CA.crt 的路径、URI 中拼接的账号及其密码、IP 信息与端口信息。
```
uri = "mongodb://mongouser:password@10.x.x.1:27017/admin"
client = MongoClient(uri,
           ssl=True,
           ssl_ca_certs='MongoDB-CA.crt',
           ssl_match_hostname=False) 
```

