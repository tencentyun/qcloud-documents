Java MongoDB驱动文档
http://mongodb.github.io/mongo-java-driver/3.2/driver/getting-started/
Java Jar包下载
https://oss.sonatype.org/content/repositories/releases/org/mongodb/mongo-java-driver/
请选择3.2以上版本下载

**Java示例代码:**
```
package mongodbdemo;

import org.bson.*;
import com.mongodb.*;
import com.mongodb.client.*;

public class MongodbDemo {

    public static void main(String[] args) {
        String mongoUri = "mongodb://rwuser:********@10.66.122.28:27017/admin?authMechanism=MONGODB-CR";
        // 或者 String mongoUri = "mongodb://rwuser:********@10.66.122.28:27017?authMechanism=MONGODB-CR&authSource=admin";
        MongoClientURI connStr = new MongoClientURI(mongoUri);
        MongoClient mongoClient = new MongoClient(connStr);
        try {
            // 使用名为 someonedb 的数据库
            MongoDatabase database = mongoClient.getDatabase("someonedb");
            // 取得集合/表 someonetable 句柄
            MongoCollection<Document> collection = database.getCollection("someonetable");

            // 准备写入数据
            Document doc = new Document();
            doc.append("key", "value");
            doc.append("username", "jack");
            doc.append("age", 31);

            // 写入数据
            collection.insertOne(doc);
            System.out.println("insert document: " + doc);

            // 读取数据
            BsonDocument filter = new BsonDocument();
            filter.append("username", new BsonString("username"));
            MongoCursor<Document> cursor = collection.find(filter).iterator();
            while (cursor.hasNext()) {
                System.out.println("find document: " + cursor.next());
            }

        } finally {
            //关闭连接
            mongoClient.close();
        }
    }
}
```

**输出:**

```
INFO: Opened connection [connectionId{localValue:2, serverValue:67621}] to 10.66.122.28:27017
insert document: Document{{key=value, username=jack, age=31, _id=56a6ebb565b33b771f9826dd}}
find document: Document{{_id=56a3189565b33b2e7ca150ba, key=value, username=jack, age=31}}
Jan 26, 2016 11:44:53 AM com.mongodb.diagnostics.logging.JULLogger log
INFO: Closed connection [connectionId{localValue:2, serverValue:67621}] to 10.66.122.28:27017 because the pool has been closed.
```