## 添加 maven 依赖
```xml
<dependency>
      <groupId>org.apache.phoenix</groupId>
      <artifactId>phoenix-core</artifactId>
      <version>4.8.1-HBase-1.2</version>
 </dependency>
```


## 创建 JDBC 连接对象
```c++
Class.forName("org.apache.phoenix.jdbc.PhoenixDriver");
        // Connect to the database
    connection = DriverManager.getConnection("jdbc:phoenix:10.0.0.3:2181,10.0.0.5:2181,10.0.0.8:2181");
```



## 执行查询
```c++
private static void instertPhoenix(Connection connection)throws Exception{
     String sql="upsert into album_subscribe_log(id,album_id,user_id,op_time,sub_flag,is_optimize,type_parent_id,type_id,host_id,is_pay,user_type,identtity_typ)"
     +" values(?,?,?,?,?,?,?,?,?,?,?,?)";
     PreparedStatement ps=connection.prepareStatement(sql);
     ps.setLong(0,1);
     ps.setLong(1,3);
     ps.setLong(2,1);
     ps.setString(3,"2017-09-05 14:00:00");
     ps.setInt(4,1);
     ps.setString(5,"1");
     ps.setInt(6,3);
     ps.setInt(7,5);
     ps.setInt(8,6);
     ps.setInt(9,7);
     ps.setString(10,"1");
     ps.setString(11,"1");
     ps.setString(12,"1");
     ps.executeUpdate();
     ps.close();
     connection.commit();
}
```
    
