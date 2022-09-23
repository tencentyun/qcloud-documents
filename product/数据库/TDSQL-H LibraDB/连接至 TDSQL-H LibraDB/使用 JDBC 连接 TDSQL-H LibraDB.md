TDSQL-H LibraDB JDBC 驱动是 TDSQL-H LibraDB 提供的 Java 数据库连接接口。本文为您介绍如何使用 JDBC 连接 TDSQL-H LibraDB，并提供示例代码。

## 背景信息

本文以使用 IntelliJ IDEA 工具为例，介绍如何使用 JDBC 连接 TDSQL-H LibraDB。

## 前提条件

- 已 [创建 TDSQL-H LibraDB 实例](https://cloud.tencent.com/document/product/1488/63546)。
- 已获取访问 TDSQL-H LibraDB 实例的帐号和密码。
- 获取 JDBC 连接 TDSQL-H LibraDB 实例时的主机地址。访问 TDSQL-H LibraDB 实例方式不同，获取的主机地址不同，请根据实际选择。
  - 若通过搭建代理使用外网访问 TDSQL-H LibraDB 实例，请获取搭建代理时使用的 **CVM 云服务器的公网 IP**，并确保外网连接使用的 CVM 安全组已添加 TCP:8123、TCP:9000 协议端口。本文中的操作以此方式为例。
    搭建代理的具体操作，请参见 [连接实例分析引擎](https://cloud.tencent.com/document/product/1488/63547) 中的外网连接相关内容。
  - 若使用镜像为 Windows 的 CVM，安装 DBeaver 并连接 TDSQL-H LibraDB 实例，请获取 **TDSQL-H LibraDB 实例的内网 IP**。
    镜像为 Windows 的 CVM 与 TDSQL-H LibraDB 实例必须为相同的 VPC，并确保 CVM 安全组已添加 TCP:8123、TCP:9000 协议端口。
- 已下载并安装 [IntelliJ IDEA](https://www.jetbrains.com.cn/idea/)。
  推荐使用 IntelliJ IDEA 版本 IntelliJ IDEA 2021.3.1，其他版本可能存在兼容性问题。本文中的 IntelliJ IDEA 示例版本为 IntelliJ IDEA 2021.3.1。

## JDBC下载

使用 IntelliJ IDEA 工具，创建 Maven 项目在对象模型 POM（Project Object Model）引入 ClickHouse 驱动依赖包。

```java
<dependency>
   <groupId>ru.yandex.clickhouse</groupId>
   <artifactId>clickhouse-jdbc</artifactId>
   <version>0.3.2</version>
</dependency>
```

## 连接 TDSQL-H LibraDB

1. 加载 TDSQL-H LibraDB JDBC 驱动。
```java
Class.forName("ru.yandex.clickhouse.ClickHouseDriver");
```
2. 通过 DriverManager 创建 Connection。
```java
Connection connection = DriverManager.getConnection(connectionStr, username, password);
```
  - connectionStr：格式为 `jdbc:clickhouse://" + url + ":8123`。其中，url 为前提条件获取的 JDBC 连接 TDSQL-H LibraDB 实例时的主机地址。
  - username：访问 TDSQL-H LibraDB 实例的帐号。
  - password：访问 TDSQL-H LibraDB 实例帐号对应的密码。
3. 执行查询。
```java
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery("SELECT foo FROM bar");
       
while (rs.next()) {
     // process the results
}
   
rs.close();
stmt.close();
connection.close();
```

#### 示例代码

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Test {
    private static final String DATE_FORMAT = "yyyy-MM-dd HH:mm:ss";
    private static final SimpleDateFormat SIMPLE_DATE_FORMAT = new SimpleDateFormat(DATE_FORMAT);

    public static void main(String[] args) throws ClassNotFoundException, SQLException, InterruptedException, ParseException {
        String url = "your url";
        String username = "your username";
        String password = "your password";

        Class.forName("ru.yandex.clickhouse.ClickHouseDriver");
        String connectionStr = "jdbc:clickhouse://" + url + ":8123";

        try (Connection connection = DriverManager.getConnection(connectionStr, username, password);
             Statement stmt = connection.createStatement()) {

            {
                String createTableDDL = "create table test_table_local on cluster default_cluster " +
                        "(id UInt32, " +
                        "dt_str String, " +
                        "dt_col DateTime) " +
                        "engine=ReplicatedMergeTree('/clickhouse/tables/{database}/{table}/{shard}', '{replica}')" +
                        "partition by toYYYYMM(dt_col)" +
                        "order by (id)" +
                        "primary key (id)" +
                        "sample by (id)" +
                        "settings index_granularity = 8192;";
                stmt.execute(createTableDDL);
                System.out.println("create local table done.");
            }
            {
                String createTableDDL = "create table test_table on cluster default_cluster " +
                        "as default.test_table_local " +
                        "engine=Distributed(default_cluster, default, test_table_local, rand());";
                stmt.execute(createTableDDL);
                System.out.println("create distributed table done");
            }

            System.out.println("write 100000 rows...");
            long startTime = System.currentTimeMillis();

            // Write 10 batch
            for (int batch = 0; batch < 10; batch++) {
                StringBuilder sb = new StringBuilder();

                // Build one batch
                sb.append("insert into test_table values(" + (batch * 10000) + ", '2020-02-19 16:00:00', '2020-02-19 16:00:00')");
                for (int row = 1; row < 10000; row++) {
                    sb.append(", (" + (batch * 10000 + row) + ", '2020-02-19 16:00:00', '2020-02-19 16:00:00')");
                }

                // Write one batch: 10000 rows
                stmt.execute(sb.toString());
            }

            long endTime = System.currentTimeMillis();
            System.out.println("total time cost to write 10W rows: " + (endTime - startTime) + "ms");

            Thread.sleep(2 * 1000);

            System.out.println("Select count(id)...");
            try (ResultSet rs = stmt.executeQuery("select count(id) from test_table");) {
                while (rs.next()) {
                    int count = rs.getInt(1);
                    System.out.println("id count: " + count);
                }
            }

            try (ResultSet rs = stmt.executeQuery("select id, dt_str, dt_col from test_table limit 10");) {
                while (rs.next()) {
                    int id = rs.getInt(1);
                    String dateStr = rs.getString(2);
                    Timestamp time = rs.getTimestamp(3);

                    String defaultDate = SIMPLE_DATE_FORMAT.format(new Date(time.getTime()));
                    System.out.println("id: " + id
                            + ", date_str:" + dateStr
                            + ", date_col:" + defaultDate);
                }
            }
        }
    }
}
```

