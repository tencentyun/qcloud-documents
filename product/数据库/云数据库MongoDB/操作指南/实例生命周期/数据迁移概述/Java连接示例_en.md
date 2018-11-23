## Notes
Tencent Cloud MongoDB provides two user names "rwuser" and "mongouser" by default to support the "MONGODB-CR" and "SCRAM - SHA - 1" authentication respectively. The connecting URI for the two types of authentication are formed differently. For more information, please see [Connection Examples](https://cloud.tencent.com/doc/product/240/3563).

Java MongoDB Driver Documentation
http://mongodb.github.io/mongo-java-driver/3.2/driver/getting-started/
Download Java Jar packet
https://oss.sonatype.org/content/repositories/releases/org/mongodb/mongo-java-driver/
Please select version 3.2 or above for downloading

## Quick Start
### Example of Java Native Codes
```
package mongodbdemo;

import org.bson.*;
import com.mongodb.*;
import com.mongodb.client.*;

public class MongodbDemo {

    public static void main(String[] args) {
        String mongoUri = "mongodb://mongouser:thepasswordA1@10.66.187.127:27017/admin";
        MongoClientURI connStr = new MongoClientURI(mongoUri);
        MongoClient mongoClient = new MongoClient(connStr);
        try {
            // Use the database named "someonedb"
            MongoDatabase database = mongoClient.getDatabase("someonedb");
            // Get the handle of the collection/table "someonetable"
            MongoCollection<Document> collection = database.getCollection("someonetable");

            // Prepare to write data
            Document doc = new Document();
            doc.append("key", "value");
            doc.append("username", "jack");
            doc.append("age", 31);

            // Write data
            collection.insertOne(doc);
            System.out.println("insert document: " + doc);

            // Read data
            BsonDocument filter = new BsonDocument();
            filter.append("username", new BsonString("username"));
            MongoCursor<Document> cursor = collection.find(filter).iterator();
            while (cursor.hasNext()) {
                System.out.println("find document: " + cursor.next());
            }
        } finally {
            //Close the connection
            mongoClient.close();
        }
    }
}
```

Output

```
INFO: Opened connection [connectionId{localValue:2, serverValue:67621}] to 10.66.122.28:27017
insert document: Document{{key=value, username=jack, age=31, _id=56a6ebb565b33b771f9826dd}}
find document: Document{{_id=56a3189565b33b2e7ca150ba, key=value, username=jack, age=31}}
Jan 26, 2016 11:44:53 AM com.mongodb.diagnostics.logging.JULLogger log
INFO: Closed connection [connectionId{localValue:2, serverValue:67621}] to 10.66.122.28:27017 because the pool has been closed.
```

### Examples for Configuring Spring Data MongoDB
The example is mainly for demonstrating the configuration of [Verification Library admin](https://cloud.tencent.com/document/product/240/3563#.E8.AE.A4.E8.AF.81.E6.95.B0.E6.8D.AE.E5.BA.93), which is actually depended on the version of Spring and Spring Data MongoDB you are using.
```
<bean id="mongoTemplate" class="org.springframework.data.mongodb.core.MongoTemplate">
    <constructor-arg name="mongoDbFactory" ref="mongoDbFactory" />
</bean>
<bean id="mongoDbFactory" class="org.springframework.data.mongodb.core.SimpleMongoDbFactory">
    <constructor-arg name="mongo" ref="mongo" />
    <constructor-arg name="databaseName" value="Your target library" />
    <constructor-arg name="credentials" ref="userCredentials" />
    <constructor-arg name="authenticationDatabaseName" value="admin" />
</bean>
<bean id="userCredentials" class="org.springframework.data.authentication.UserCredentials">
    <constructor-arg name="username" value="Username" />
    <constructor-arg name="password" value="Password" />
</bean>
```

