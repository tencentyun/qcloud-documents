## 相关说明
云数据库 MongoDB 默认提供 rwuser 和 mongouser 两个用户名，分别支持 MONGODB-CR 和 SCRAM-SHA-1 两种认证方式，对于这两种认证方式，连接 URI 需要做不同的处理，具体请参见 [连接实例](https://cloud.tencent.com/document/product/240/7092)。

[mGo 驱动下载](https://gopkg.in/mgo.v2)、[MongoDB Go 驱动下载](https://github.com/mongodb/mongo-go-driver/)

## mGo 驱动示例代码 
```
func GetMgoURL(ip, user, password string, port int) string {
	urlString := ""
	if user == "" && password == "" {
		urlString = fmt.Sprintf("mongodb://%s:%d/admin", ip, port)
	}else {
		urlString = fmt.Sprintf("mongodb://%s:%s@%s:%d/admin", url.QueryEscape(user), url.QueryEscape(password), ip, port)
	}

	return urlString
}


url := service.GetMgoURL(reqPara.Ip, reqPara.User, reqPara.Password, reqPara.Port)
	session, err := mgo.Dial(url)
```

## MongoDB Go 驱动示例代码
示例代码请参见 [官方文档](https://www.mongodb.com/blog/post/quick-start-golang--mongodb--starting-and-setup)。
