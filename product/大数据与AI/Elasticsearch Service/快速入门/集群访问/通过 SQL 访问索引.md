Elasticsearch 商业特性中提供了SQL访问索引的方式，用户可以在Kibana的【Dev Tools】中编写SQL，也可用使用SQL JDBC访问索引。

1. 通过Kibana【Dev Tools】编写SQL

```
POST _xpack/sql?format=txt
{
  "query": "select FlightNum from kibana_sample_data_flights limit 10"
}
```

2. 通过SQL JDBC访问索引（以Java客户端为例）

### 下载JDBC驱动

JDBC驱动可以通过在[官网下载](https://www.elastic.co/downloads/jdbc-client)，或在Maven中添加依赖来下载

```
<dependency>
  <groupId>org.elasticsearch.plugin</groupId>
  <artifactId>x-pack-sql-jdbc</artifactId>
  <version>6.4.3</version>
</dependency>

<repositories>
  <repository>
    <id>elastic.co</id>
    <url>https://artifacts.elastic.co/maven</url>
  </repository>
</repositories>
```

### 示例代码

```
import java.sql.*;
import java.util.Properties;

public class Main {

    public static void main(String[] args) {
        try {
            Class.forName("org.elasticsearch.xpack.sql.jdbc.jdbc.JdbcDriver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            return;
        }
        String address = "jdbc:es://http://YOUR_ES_VIP:9200";
        Properties properties = new Properties();
        properties.put("user", "elastic");
        properties.put("password", "YOUR_PASS");

        Connection connection = null;
        try {
            connection = DriverManager.getConnection(address, properties);
            Statement statement = connection.createStatement();
            ResultSet results = statement.executeQuery("select FlightNum from kibana_sample_data_flights limit 10");
            while (results.next()) {
                System.out.println(results.getString(1));
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (connection != null && !connection.isClosed()) {
                    connection.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```