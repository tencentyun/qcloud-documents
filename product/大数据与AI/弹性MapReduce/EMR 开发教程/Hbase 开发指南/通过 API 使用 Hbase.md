HBase 是一个高可靠性、高性能、面向列、可伸缩的分布式存储系统。本章开发指南将从技术人员的角度帮助用户使用 EMR 集群开发。

考虑用户数据安全，EMR 中当前只支持 VPC 网络访问

- 添加maven 依赖

    ``` xml
    <dependency>
      <groupId>org.apache.hbase</groupId>
      <artifactId>hbase-client</artifactId>
      <version>1.2.4</version>
    </dependency>
    ```

- 获取 Hbase 集群 zookeeper 地址  

    登录EMR 任意一台 master 节点或者 core 节点，进入 /usr/local/service/hbase/conf 目录，查看 base-site.xml 的 hbase.zookeeper.quorum 配置获得 zookeeper 的 IP，hbase.zookeeper.property.clientPort 配置获得 zookeeper 的端口号。
    
- 访问样例代码

    ``` c++
    TTransport transport = new TSocket(host, port, timeout);
        if (framed) {
            transport = new TFramedTransport(transport);
        }
        TProtocol protocol = new TBinaryProtocol(transport);
        // This is our thrift client.
        THBaseService.Iface client = new THBaseService.Client(protocol);
        // open the transport
        transport.open();
        ByteBuffer table = ByteBuffer.wrap("blog".getBytes());
        TPut put = new TPut();
        put.setRow("103".getBytes());
        TColumnValue columnValue = new TColumnValue();
        columnValue.setFamily("article".getBytes());
        columnValue.setQualifier("title,".getBytes());
        columnValue.setValue("change thirft".getBytes());
        List<TColumnValue> columnValues = new ArrayList<TColumnValue>();
        columnValues.add(columnValue);
        put.setColumnValues(columnValues);
        client.put(table, put);
        TGet get = new TGet();
        get.setRow("102".getBytes());
        TResult result = client.get(table, get);
        System.out.print("row = " + new String(result.getRow()));
        for (TColumnValue resultColumnValue : result.getColumnValues()) {
            System.out.print(",family = " + new String(resultColumnValue.getFamily()));
            System.out.print(",qualifier = " + new String(resultColumnValue.getFamily()));
            System.out.print(",value = " + new String(resultColumnValue.getValue()));
            System.out.print(",timestamp = " + resultColumnValue.getTimestamp());
        }
        transport.close();
    ```
