腾讯云 Elasticsearch Service 支持使用 SQL 代替 DSL 查询语言。对于从事产品运营、数据分析等工作以及初次接触 ES 的人，使用 SQL 语言进行查询，将会降低他们使用 ES 的学习成本。

ES 提供了两种 SQL 解析器。ES 所有的开源版本，均预装了开源社区提供的 SQL 解析插件。ES 6.4.3及以上版本，包括基础版和白金版，支持使用 ES 原生的 SQL 解析器。

### 原生 SQL 解析器
使用 SQL 的 API 进行简单的查询。
```
POST /_xpack/sql?format=txt
{
    "query": "SELECT * FROM my_index"
}
```
更多原生 SQL 解析器的 API 及使用方法请参见 [官方文档](https://www.elastic.co/guide/en/elasticsearch/reference/6.4/sql-rest.html)。
 
### 开源 SQL 解析插件
- 7.5.1及以上版本：
```
POST /_nlpcn/sql 
{
		"sql":"select * from test_index"
}
```
- 其他版本：
```
POST /_sql 
{
		"sql":"select * from test_index"
}
```

更多 SQL 插件的 API 及使用方法请参见 [文档](https://github.com/NLPchina/elasticsearch-sql/blob/master/README.md)。

### SQL JDBC 访问
ES 6.4.3及以上的白金版中，支持通过 JDBC 访问 ES 集群。您首先需要下载 JDBC 驱动，JDBC 驱动可以在 [官网下载](https://www.elastic.co/downloads/jdbc-client)，或在 Maven 中添加依赖来下载：
```
<dependency>
  <groupId>org.elasticsearch.plugin</groupId>
  <artifactId>x-pack-sql-jdbc</artifactId>
  <version>6.4.3</version>
</dependency>
```
SQL JDBC 访问示例代码：
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
