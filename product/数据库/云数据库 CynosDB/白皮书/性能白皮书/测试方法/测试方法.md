
本文为您介绍 TDSQL-C MySQL 版性能测试的方法。

## 场景一：全缓存
全缓存测试场景下的单表数据量和表总数列表：

<table>
<tr><th rowspan = "1"  width="33%">规格</th>
<th rowspan = "1"  width="33%">单表数据量（table_size）</th>
<th rowspan = "1"  width="33%">表总数（tables）</th></tr>
<tr><td>2核16GB</td><td>25000</td><td>250</td></tr>
<tr><td>4核16GB</td><td>25000</td><td>250</td></tr>
<tr><td>4核32GB</td><td>25000</td><td>250</td></tr>
<tr><td>8核32GB</td><td>25000</td><td>250</td></tr>
<tr><td>8核64GB</td><td>25000</td><td>250</td></tr>
<tr><td>16核64GB</td><td>25000</td><td>250</td></tr>
<tr><td>16核96GB</td><td>25000</td><td>250</td></tr>
<tr><td>16核128GB</td><td>25000</td><td>250</td></tr>
<tr><td>32核128GB</td><td>25000</td><td>250</td></tr>
<tr><td>32核256GB</td><td>25000</td><td>250</td></tr>
<tr><td>64核256GB</td><td>25000</td><td>250</td></tr>
</table>

### 执行命令
>?请将以下命令中的 XXX 替换为 TDSQL-C MySQL 版测试集群的内网地址、端口号、用户名、用户密码、数据库名，以及对应测试场景的单表数据量和表总数，具体参数说明如下：
>- -host：测试实例的内网地址
>- -port：端口号
>- -user：用户名
>- -password：上述用户名对应的密码
>- -table_size：单表数据量
>- -tables：表总数
>- -mysql-db：数据库名 

**1. 只写**
```
sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX oltp_write_only run
##准备数据

sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX --events=0 --time=600   --threads=192 --percentile=95 --report-interval=1 oltp_write_only run
##运行 workload

sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX oltp_write_only cleanup
##清理数据
```

**2. 只读（point select）**
```
sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX oltp_read_only prepare
##准备数据

sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX --events=0 --time=600   --threads=512 --percentile=95 --range_selects=0 --skip-trx=1 --report-interval=1 oltp_read_only run
##运行 workload

sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX oltp_read_only cleanup
##清理数据
```

**3.只读（range select）**
```
sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX oltp_read_only prepare
##准备数据

sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX --events=0 --time=600   --threads=512 --percentile=95 --skip-trx=1 --report-interval=1 oltp_read_only run
##运行 workload

sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX oltp_read_only cleanup
##清理数据
```

**4. 混合读写（point select）**
```
sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX oltp_read_write run
##准备数据

sysbench --db-driver=mysql  --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX --events=0 --time=600  --range_selects=0 --threads=XXX --percentile=95 --report-interval=1 oltp_read_write run
##运行 workload

sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX oltp_read_write cleanup
##清理数据
```

**5. 混合读写（range select）**
```
sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX oltp_read_write run
##准备数据

sysbench --db-driver=mysql  --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX --events=0 --time=600   --threads=XXX --percentile=95 --report-interval=1 oltp_read_write run
##运行 workload

sysbench --db-driver=mysql --mysql-host=XXX --mysql-port=XXX --mysql-user=XXX --mysql-password=XXX --mysql-db=XXX --table_size=XXX --tables=XXX oltp_read_write cleanup
##清理数据
```

## 场景二：大数据集
大数据集测试场景下的单表数据量和表总数列表：
<table>
<tr><th rowspan = "1"  width="33%">规格</th>
<th rowspan = "1"  width="33%">单表数据量（table_size）</th>
<th rowspan = "1"  width="33%">表总数（tables）</th></tr>
<tr><td>2核16GB</td><td>800000</td><td>150</td></tr>
<tr><td>4核16GB</td><td>800000</td><td>300</td></tr>
<tr><td>4核32GB</td><td>800000</td><td>300</td></tr>
<tr><td>8核32GB</td><td>800000</td><td>300</td></tr>
<tr><td>8核64GB</td><td>800000</td><td>450</td></tr>
<tr><td>16核64GB</td><td>800000</td><td>450</td></tr>
<tr><td>16核96GB</td><td>800000</td><td>600</td></tr>
<tr><td>16核128GB</td><td>5000000</td><td>300</td></tr>
<tr><td>32核128GB</td><td>5000000</td><td>300</td></tr>
<tr><td>32核256GB</td><td>5000000</td><td>400</td></tr>
<tr><td>64核256GB</td><td>6000000</td><td>450</td></tr>
</table>

### 执行命令
与全缓存各个测试场景下执行命令操作一致，只需替换命令中的单表数据量（table_size）和表总数（tables）。

## 场景三：单表1T
单表1T测试场景下的单表数据量和表总数列表：
<table>
<tr><th rowspan = "1"  width="33%">规格</th>
<th rowspan = "1"  width="33%">单表数据量（table_size）</th>
<th rowspan = "1"  width="33%">表总数（tables）</th></tr>
<tr><td>2核16GB</td><td>4000000000</td><td>1</td></tr>
<tr><td>4核16GB</td><td>4000000000</td><td>1</td></tr>
<tr><td>4核32GB</td><td>4000000000</td><td>1</td></tr>
<tr><td>8核32GB</td><td>4000000000</td><td>1</td></tr>
<tr><td>8核64GB</td><td>4000000000</td><td>1</td></tr>
<tr><td>16核64GB</td><td>4000000000</td><td>1</td></tr>
<tr><td>16核96GB</td><td>4000000000</td><td>1</td></tr>
<tr><td>16核128GB</td><td>4000000000</td><td>1</td></tr>
<tr><td>32核128GB</td><td>4000000000</td><td>1</td></tr>
<tr><td>32核256GB</td><td>4000000000</td><td>1</td></tr>
<tr><td>64核256GB</td><td>4000000000</td><td>1</td></tr>
</table>

### 执行命令
与全缓存各个测试场景下执行命令操作一致，只需替换命令中的单表数据量（table_size）和表总数（tables）。

