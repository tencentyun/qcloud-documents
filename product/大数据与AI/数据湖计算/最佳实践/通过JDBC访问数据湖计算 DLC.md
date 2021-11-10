## 环境准备
- 依赖：JDK 1.8
- JDBC 下载：[点击下载 JDBC 驱动](https://dlc-jdbc-1304028854.cos.ap-beijing.myqcloud.com/dlc-jdbc-1.3.0-jar-with-dependencies.jar)

## 连接 DLC
1. 加载 DLC JDBC 驱动
```
Class.forName("com.tencent.cloud.dlc.jdbc.DlcDriver");
```
2. 通过 DriverManager 创建 Connection
```
Connection cnct = DriverManager.getConnection(url, secretId, secretKey);
```

## url 格式
```
jdbc:dlc:<dlc_endpoint>?task_type=SQLTask&database_name=abc&datasource_connection_name=CosDataCatalog&region=ap-nanjing
```
<table>
<tr>
<th>参数</th>
<th>必填</th>
<th>说明</th> 
</tr>
<tr>
<td>dlc_endpoint</td>
<td>是</td>
<td>dlc.tencentcloudapi.com，dlc 服务的 Endpoint，Endpoint 服务的详细说明请参见 Endpoint</td>
</tr>
<tr>
<td>datasource_connection_name</td>
<td>是</td>
<td>数据源连接</td>
</tr>
<tr>
<td>task_type</td>
<td>是</td>
<td>SQLTask、SparkSQLTask</td>
</tr>
<tr>
<td>database_name</td>
<td>是</td>
<td>数据库</td>
</tr>
<tr>
<td>region</td>
<td>是</td>
<td>地域，目前 dlc 服务支持 ap-nanjing、ap-beijing、ap-guangzhou</td>
</tr>
<tr>
<td>secretId</td>
<td>是</td>
<td>腾讯云 API 密钥管理中的 SecretId</td>
</tr>
<tr>
<td>secretKey</td>
<td>是</td>
<td>腾讯云 API 密钥管理中的 Secretkey</td>
</tr>
</table>

## 执行查询
```Java
Statement stmt = cnct.createStatement();
ResultSet rset = stmt.executeQuery("SELECT * FROM dlc");

while (rset.next()) {
    // process the results
}

rset.close();
stmt.close();
conn.close();
```

## 语法支持
目前 jdbc 可以使用的语法与 DLC 标准语法保持一致。

## 实例代码
### 库表操作
```Java
import java.sql.*;

public class MetaTest {

  public static void main(String[] args) throws SQLException {

    try {
      Class.forName("com.tencent.cloud.dlc.jdbc.DlcDriver");
    } catch (ClassNotFoundException e) {
      e.printStackTrace();
      return;
    }
    Connection connection = DriverManager.getConnection(
            "jdbc:dlc:<dlc_endpoint>?task_type=<task_type>&database_name=<database_name>&datasource_connection_name=CosDataCatalog&region=<region>",
            "<secret_id>",
            "secret_key");
    Statement statement = connection.createStatement();

    String dbName = "dlc_db1";
    String createDatabaseSql = String.format("CREATE DATABASE IF NOT EXISTS %s", dbName);
    statement.execute(createDatabaseSql);

    String tableName = "dlc_t1";
    String wholeTableName = String.format("%s.%s", dbName, tableName);
    String createTableSql =
            String.format(
                    "CREATE TABLE %s (\n"
                            + "  id string , \n"
                            + "  name string , \n"
                            + "  status string , \n"
                            + "  type string )\n"
                            + "ROW FORMAT SERDE \n"
                            + "  'org.apache.hadoop.hive.ql.io.orc.OrcSerde' \n"
                            + "STORED AS INPUTFORMAT \n"
                            + "  'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat' \n"
                            + "OUTPUTFORMAT \n"
                            + "  'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'\n"
                            + "LOCATION\n"
                            + "  'cosn://<bucket_name>/<path>'\n",
                    wholeTableName);
    statement.execute(createTableSql);

    // get meta data
    DatabaseMetaData metaData = connection.getMetaData();
    System.out.println("product = " + metaData.getDatabaseProductName());
    System.out.println("jdbc version = "
            + metaData.getDriverMajorVersion() + ", "
            + metaData.getDriverMinorVersion());
    ResultSet tables = metaData.getTables(null, dbName, tableName, null);
    while (tables.next()) {
      String name = tables.getString("TABLE_NAME");
      System.out.println("table: " + name);
      ResultSet columns = metaData.getColumns(null, dbName, name, null);
      while (columns.next()) {
        System.out.println(
                columns.getString("COLUMN_NAME") + "\t" +
                        columns.getString("TYPE_NAME") + "\t" +
                        columns.getInt("DATA_TYPE"));
      }
      columns.close();
    }
    tables.close();
    statement.close();
    connection.close();
  }
}
```

### 数据查询
```Java
import java.sql.*;

public class DataTest {
  public static void main(String[] args) throws SQLException {
    try {
      Class.forName("com.tencent.cloud.dlc.jdbc.DlcDriver");
    } catch (ClassNotFoundException e) {
      e.printStackTrace();
      return;
    }
    Connection connection = DriverManager.getConnection(
            "jdbc:dlc:<dlc_endpoint>?task_type=<task_type>&database_name=<database_name>&datasource_connection_name=CosDataCatalog&region=<region>",
            "<secret_id>",
            "secret_key");
    Statement statement = connection.createStatement();
    String sql = "select * from dlc_test";
    statement.execute(sql);
    ResultSet rs = statement.getResultSet();
    while (rs.next()) {
      System.out.println(rs.getInt(1) + ":" + rs.getString(2));
    }
    rs.close();
    statement.close();
    connection.close();
  }
}
```


## 数据库客户端 
您可以将 DLC 的 JDBC 驱动包加载到 SQL 客户端，连接到 DLC 服务进行查询。

### 前置条件
1. 已开通数据湖计算 Data Lake Compute 服务。
2. 已下载上文中的 jdbc 驱动包。
3. 已下载并安装 **SQL Workbench/J**。

### 操作步骤
1. 通过 jdbc 驱动包创建 DLC Driver。
![](https://main.qcloudimg.com/raw/afc6df5b900eb933aaf431d529b4241a.png)
2. 连接 DLC，填入如下参数，单击 **test**，测试通过后，完成与 DLC 的连接。
 - Name：连接名称，用于标识与 DLC 的连接。
 - Username：对应于腾讯云用户的 secret_id。
 - Password：对应于腾讯云用户的 secret_key。
 - URL：用于连接 DLC 的 URL。格式和上文中通过 jdbc 创建连接的 URL 一致。
![](https://main.qcloudimg.com/raw/abda4b50672f4c70b4d81e80a2c2158c.png)
1. 查看库表信息。
![](https://main.qcloudimg.com/raw/5ecbf80953f8589821eb008375f0bbff.png)
1. 查询数据。
![](https://main.qcloudimg.com/raw/7090e6adac000b263cfc41bbcf25695f.png)
