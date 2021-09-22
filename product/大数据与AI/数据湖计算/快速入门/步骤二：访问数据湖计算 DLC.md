可通过数据湖计算 DLC 控制台、DLC API 和 JDBC 三种方式访问数据湖计算 DLC 。

## DLC 控制台
您可以使用数据湖计算 DLC 控制台执行以下操作：
- 创建、查看和删除数据库。
- 创建、查看和删除表。
- 显示表属性。
- 预览数据，自动生成查询 SQL，预览10条数据。
- 自动生成建表语句。
- 对表运行查询、保存查询脚本，以及查看查询历史记录。
- 显示和保存查询结果。
- 查看和更改查询结果位置。

## 使用 API
用户可以使用 API 访问数据湖计算 DLC，具体可参见 [API 文档](https://cloud.tencent.com/document/product/1342/53658)。

## 使用 JDBC
1. 依赖：JDK 1.8
2. JDBC 下载：[点击下载 JDBC 驱动]()
3. 连接 DLC
 - 加载 DLC JDBC 驱动
```
Class.forName("com.tencent.cloud.dlc.jdbc.DlcDriver");
```
 - 通过 DriverManager 创建 Connection
```
Connection cnct = DriverManager.getConnection(url, secretId, secretKey);
```
 - url 的格式
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
 - 执行查询
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
4. 语法支持
目前 jdbc 可以使用的语法与 DLC 标准语法保持一致。
5. 实例代码
 - 库表操作
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
 - 数据查询
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
6. 数据库客户端 
您可以将 DLC 的 JDBC 驱动包加载到 SQL 客户端，连接到 DLC 服务进行查询。
