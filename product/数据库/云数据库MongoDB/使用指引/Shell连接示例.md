## shell方式连接MongoDB

### mongouser以及在控制台创建的用户名连接
```
./mongo IP:27017/admin -u mongouser --password=***
```
或者
```
./mongo IP:27017 -u mongouser --password=*** --authenticationDatabase admin
```

### rwuser连接
```
./mongo IP:27017/admin -u rwuser --password=*** --authenticationMechanism=MONGODB-CR
```
或者
```
./mongo IP:27017 -u rwuser --password=*** --authenticationMechanism=MONGODB-CR --authenticationDatabase admin
```

示例：

![](//mc.qcloudimg.com/static/img/43e051246f159a8cc894259a44924d3d/image.png)
