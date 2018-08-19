## 数据导入

### 数据导入说明
云数据库Redis-CKV引擎提供数据导入工具 [redis-import-rdb](http://121.com)，数据的导入流程步骤分为三步：

- 通过BGSAVE或者SAVE命令生成RDB文件，推进适用BGSAVE命令备份数据，因为SAVE命令会在完成备份前会使整个Redis服务不可用；
- 清空目标实例，可用通过云数据库Redis控制台右上角的【清空实例】按钮清空实例数据，如果不清空目标实例，数据导入会失败；
- 使用redis-import-rdb工具导入RDB文件中的数据，工具参数说明如下：
<code>
    - -dip，云数据Redis的IP地址；
    - -dport，云数据Redis的端口（默认是6379）；
    - -dauth，云数据Redis的密码；
    - -client，导入数据的并发线程数量，根据导入数据决定（默认情况建议设置为10）；
    - -rdb，RDB文件路径；
    - -support_multi_db，该参数为0表示将所有DB的数据导入到DB 0，非0表示将数据导入到原有的DB；
    
- 工具使用示例：

  ./redis-import-rdb  -dip 192.168.1.2 -dport 6379 -dauth 654321 -client 200 -rdb ./dump.rdb
</code>
