本文为您介绍使用4.1.1版本的 BenchmarkSQL 对 TBase 数据库进行 TPC-C 测试的过程，下载地址请参见 [BenchmarkSQL 官网](https://sourceforge.net/projects/benchmarksql/)。

## TPC-C 简介
TPC-C 是针对联机交易处理系统（OLTP）进行测试的规范。使用一个商品销售模型对 OLTP 系统进行测试，其中包含五类事务：
- NewOrder：新订单的生成
- Payment：订单付款
- OrderStatus：最近订单查询
- Delivery：配送
- StockLevel：库存缺货状态分析

TPC-C 使用 tpmC 值（Transactions per Minute）来衡量系统最大有效吞吐量（Max Qualified Throughput，MQTh），其中 Transactions 以 NewOrder Transaction 为准，即最终衡量单位为每分钟处理的新订单数。

## 前提条件
已下载 BenchMarkSQL，并安装好 java 和 ant。

## 测试步骤
TPC-C 的测试结果与 prop.pg 中的配置参数有关，请您基于业务场景来进行调整参数测试。

### 步骤1：修改prop.pg
```
driver=org.postgresql.Driver
conn=jdbc:postgresql://localhost:5866/benchdb
user=bench
password=bench

warehouses=10
terminals=1
//To run specified transactions per terminal- runMins must equal zero
runTxnsPerTerminal=0
//To run for specified minutes- runTxnsPerTerminal must equal zero
runMins=5
//Number of total transactions per minute
limitTxnsPerMin=300
```

### 步骤2：创建测试表
`./runSQL.sh props.pg sqlTableCreates`

### 步骤3：导入数据
`./runLoader.sh props.pg numWarehouses 10`

### 步骤4：创建索引
`./runSQL.sh props.pg sqlIndexCreates`

### 步骤5：执行压测
`./runBenchmark.sh props.pg`
