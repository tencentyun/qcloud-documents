腾讯云Elasticsearch支持使用SQL代替DSL查询语言。对于从事产品运营、数据分析等工作以及初次接触Elasticsearch的人，使用SQL语言进行查询，将会降低他们使用Elasticsearch的学习成本。

腾讯云Elasticsearch提供两种SQL解析器供选择。腾讯云Elasticsearch所有的开源版本，均预装了开源社区提供的SQL解析插件。6.4.3及以上版本，包括基础版和白金版，支持使用Elasticsearch原生的SQL解析器。

### 原生SQL解析器

使用SQL的API进行简单的查询

```
POST /_xpack/sql?format=txt
{
    "query": "SELECT * FROM my_index"
}
```

更多原生SQL解析器的API及使用方法请参见官方[文档](https://www.elastic.co/guide/en/elasticsearch/reference/6.4/sql-rest.html)

### 开源SQL解析插件

```
POST /_sql
"select * from my_index"
```
更多SQL插件的API及使用方法请参见[文档](https://github.com/NLPchina/elasticsearch-sql/blob/master/README.md)

### SQL JDBC访问

Elasticsearch 6.4.3及以上的白金版中，支持通过JDBC访问。你首先需要下载JDBC驱动，JDBC驱动可以通过在[官网下载](https://www.elastic.co/downloads/jdbc-client)，或在Maven中添加依赖来下载：

```
<dependency>
  <groupId>org.elasticsearch.plugin</groupId>
  <artifactId>x-pack-sql-jdbc</artifactId>
  <version>6.4.3</version>
</dependency>
```

SQL JDBC访问示例代码

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
