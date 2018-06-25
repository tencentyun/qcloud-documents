## What's new

<table class="t">
<tbody><tr>
<th>  高性能版实例名称
</th><th>  容量配置(GB)
</th><th>  表总行数
</th><th>  表数
</th><th>  测试数据集(GB)
</th><th>  并发数
</th></tr>
<tr>
<td> 大型
</td><td> 600
</td><td> 1,560,000,000
</td><td> 39
</td><td> 429
</td><td> 128
</td></tr>
<tr>
<td> A型
</td><td> 400
</td><td> 1,160,000,000
</td><td> 29
</td><td> 319
</td><td> 96
</td></tr>
<tr>
<td> B型
</td><td> 200
</td><td> 600,000,000
</td><td> 15
</td><td> 165
</td><td> 64
</td></tr>
<tr>
<td>  C型
</td><td> 100
</td><td> 320,000,000
</td><td> 8
</td><td> 88
</td><td> 64
</td></tr>
<tr>
<td> 小型
</td><td> 50
</td><td> 160,000,000
</td><td> 4
</td><td> 44
</td><td> 64
</td></tr>
<tr>
<td> 微型
</td><td> 25
</td><td> 80,000,000
</td><td> 2
</td><td> 22
</td><td> 64
</td></tr></tbody></table>

2015年9月14日，大容量版发布，适合性能要求不高但数据量较大的场景。

## 1 大容量版性能说明

### 1.1 测试工具

SysBench0.5 

### 1.2 测试方法

根据不同实例规格，在服务器上同时运行多个实例，在客户机上运行SysBench，向服务器发起并发请求，进行压力测试，待数据完全预热后，取出稳定性能数据。 

### 1.3 测试参数

<table class="t">
<tbody><tr>
<th> <b>大容量版内存大小(MB)</b>
</th><th> <b>存储空间(GB)</b>
</th><th> <b>表数</b>
</th><th> <b>每张表的行数</b>
</th><th> <b>测试数据集(GB)</b>
</th><th> <b>运行时间(S)</b>
</th><th> <b>采样间隔(S)</b>
</th></tr>
<tr>
<td> 20000
</td><td> 2000
</td><td> 40
</td><td> 4000万
</td><td> 378
</td><td> 1800
</td><td> 20
</td></tr>
<tr>
<td> 10000
</td><td> 1000
</td><td> 25
</td><td> 4000万
</td><td> 238
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 5000
</td><td> 500
</td><td> 20
</td><td> 4000万
</td><td> 190
</td><td> 1800
</td><td> 5
</td></tr></tbody></table>

### 1.4 测试结果

<table class="t">
<tbody><tr>
<th> <b>大容量版实例配置</b>
</th><th> <b>测试数据集(GB)</b>
</th><th> <b>并发数</b>
</th><th> <b>QPS</b>
</th><th> <b>TPS</b>
</th></tr>
<tr>
<td> 20000MB内存，2000GB存储空间
</td><td> 1500
</td><td> 96
</td><td> 7911
</td><td> 1130
</td></tr>
<tr>
<td> 10000MB内存，1000GB存储空间
</td><td> 750
</td><td> 96
</td><td> 3351
</td><td> 478
</td></tr>
<tr>
<td> 5000MB内存，500GB存储空间
</td><td> 410
</td><td> 96
</td><td> 1257
</td><td> 179
</td></tr></tbody></table>

说明：
1. 默认采用Dynamic行格式。

2. QPS：每秒处理查询数。

3. 并发数：同一时间实例处理的并发请求数。

4. 测试工作集：测试数据规模，即访问数据的分布规模。

6. 测试中，每条事务包含4条点查询语句，以及1条更新语句，测试采用Special分布，Special数据占1%，有关详情请参考SysBench手册。

7. 测试中，默认使用prepare模式，即：--db-ps-mode=auto。

## 2 高IO版性能说明

### 2.1 测试工具

SysBench0.5 

### 2.2 测试方法

根据不同实例规格，在服务器上同时运行多个实例，在客户机上运行SysBench，向服务器发起并发请求，进行压力测试，待数据完全预热后，取出稳定性能数据。 

### 2.3 测试参数

<table class="t">
<tbody><tr>
<th>  高IO版内存大小(MB)
</th><th>  存储空间(GB)
</th><th>  表数
</th><th>  每张表的行数
</th><th>  测试数据集(GB)
</th><th>  运行时间(S)
</th><th>  采样间隔(S)
</th></tr>
<tr>
<td> 48000
</td><td> 1000
</td><td> 40
</td><td> 4000万
</td><td> 378
</td><td> 1800
</td><td> 20
</td></tr>
<tr>
<td> 24000
</td><td> 500
</td><td> 25
</td><td> 4000万
</td><td> 238
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 16000
</td><td> 400
</td><td> 20
</td><td> 4000万
</td><td> 190
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 12000
</td><td> 250
</td><td> 15
</td><td> 4000万
</td><td> 142
</td><td> 1800
</td><td> 20
</td></tr>
<tr>
<td> 8000
</td><td> 200
</td><td> 12
</td><td> 4000万
</td><td> 114
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 4000
</td><td> 100
</td><td> 8
</td><td> 4000万
</td><td> 76
</td><td> 1800
</td><td> 20
</td></tr>
<tr>
<td> 2000
</td><td> 50
</td><td> 6
</td><td> 2000万
</td><td> 29
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 1000
</td><td> 25
</td><td> 6
</td><td> 1000万
</td><td> 14
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 360
</td><td> 10
</td><td> 4
</td><td> 500万
</td><td> 4.6
</td><td> 1800
</td><td> 5
</td></tr></tbody></table>

### 2.4 测试结果

<table class="t">

<tbody><tr>
<th> <b>高IO版实例配置</b>
</th><th > <b>测试数据集(GB)</b>
</th><th> <b>并发数</b>
</th><th> <b>QPS</b>
</th><th> <b>TPS</b>
</th></tr>
<tr>
<td> 48000MB内存，1000GB存储空间
</td><td> 378
</td><td> 256
</td><td> 40856
</td><td> 8208
</td></tr>
<tr>
<td> 24000MB内存，500GB存储空间
</td><td> 238
</td><td> 256
</td><td> 24979
</td><td> 4995
</td></tr>
<tr>
<td> 16000 MB内存，400GB存储空间
</td><td> 190
</td><td> 256
</td><td> 24953
</td><td> 4991
</td></tr>
<tr>
<td> 12000MB内存，250GB存储空间
</td><td> 142
</td><td> 64
</td><td> 15700
</td><td> 3139
</td></tr>
<tr>
<td> 8000 MB内存，200GB存储空间
</td><td> 114
</td><td> 64
</td><td> 14085
</td><td> 2817
</td></tr>
<tr>
<td> 4000MB内存，100GB存储空间
</td><td> 76
</td><td> 64
</td><td> 4852
</td><td> 970
</td></tr>
<tr>
<td> 2000MB内存，50GB存储空间
</td><td> 29
</td><td> 64
</td><td> 2667
</td><td> 533
</td></tr>
<tr>
<td> 1000MB内存，25GB存储空间
</td><td> 14
</td><td> 64
</td><td> 1103
</td><td> 220
</td></tr>
<tr>
<td> 360MB内存，10GB存储空间
</td><td> 4.6
</td><td> 64
</td><td> 133
</td><td> 26
</td></tr></tbody></table>

说明：

1. 默认采用Dynamic行格式。

2. QPS：每秒处理查询数。

3. 并发数：同一时间实例处理的并发请求数。

4. 测试工作集：测试数据规模，即访问数据的分布规模。

6. 测试中，每条事务包含4条点查询语句，以及1条更新语句，测试采用Special分布，Special数据占1%，有关详情请参考SysBench手册。

7. 测试中，默认使用prepare模式，即：--db-ps-mode=auto。

## 3 高性能版性能说明

### 3.1 测试工具

SysBench0.5 

### 3.2 测试方法

根据不同实例规格，在服务器上同时运行多个实例，在客户机上运行SysBench，向服务器发起并发请求，进行压力测试，待数据完全预热后，取出稳定性能数据。 

### 3.3 测试数据
<table class="t">
<tbody><tr>
<th>  高性能版实例名称
</th><th>  容量配置(GB)
</th><th>  表总行数
</th><th>  表数
</th><th>  测试数据集(GB)
</th><th>  并发数
</th></tr>
<tr>
<td> 大型
</td><td> 600
</td><td> 1,560,000,000
</td><td> 39
</td><td> 429
</td><td> 128
</td></tr>
<tr>
<td> A型
</td><td> 400
</td><td> 1,160,000,000
</td><td> 29
</td><td> 319
</td><td> 96
</td></tr>
<tr>
<td> B型
</td><td> 200
</td><td> 600,000,000
</td><td> 15
</td><td> 165
</td><td> 64
</td></tr>
<tr>
<td>  C型
</td><td> 100
</td><td> 320,000,000
</td><td> 8
</td><td> 88
</td><td> 64
</td></tr>
<tr>
<td> 小型
</td><td> 50
</td><td> 160,000,000
</td><td> 4
</td><td> 44
</td><td> 64
</td></tr>
<tr>
<td> 微型
</td><td> 25
</td><td> 80,000,000
</td><td> 2
</td><td> 22
</td><td> 64
</td></tr></tbody></table>

### 3.4 测试结果

<table class="t">
<tbody><tr>
<th>  高IO版内存大小(MB)
</th><th>  存储空间(GB)
</th><th>  表数
</th><th>  每张表的行数
</th><th>  测试数据集(GB)
</th><th>  运行时间(S)
</th><th>  采样间隔(S)
</th></tr>
<tr>
<td> 48000
</td><td> 1000
</td><td> 40
</td><td> 4000万
</td><td> 378
</td><td> 1800
</td><td> 20
</td></tr>
<tr>
<td> 24000
</td><td> 500
</td><td> 25
</td><td> 4000万
</td><td> 238
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 16000
</td><td> 400
</td><td> 20
</td><td> 4000万
</td><td> 190
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 12000
</td><td> 250
</td><td> 15
</td><td> 4000万
</td><td> 142
</td><td> 1800
</td><td> 20
</td></tr>
<tr>
<td> 8000
</td><td> 200
</td><td> 12
</td><td> 4000万
</td><td> 114
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 4000
</td><td> 100
</td><td> 8
</td><td> 4000万
</td><td> 76
</td><td> 1800
</td><td> 20
</td></tr>
<tr>
<td> 2000
</td><td> 50
</td><td> 6
</td><td> 2000万
</td><td> 29
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 1000
</td><td> 25
</td><td> 6
</td><td> 1000万
</td><td> 14
</td><td> 1800
</td><td> 5
</td></tr>
<tr>
<td> 360
</td><td> 10
</td><td> 4
</td><td> 500万
</td><td> 4.6
</td><td> 1800
</td><td> 5
</td></tr></tbody></table>

说明：

1.默认采用Dynamic行格式，单表容量11GB。

2. QPS：每秒处理查询数。

3. 并发数：同一时间实例处理的并发请求数。

4. 测试工作集：测试数据规模，即访问数据的分布规模。

6. 测试中，每条事务包含4条点查询语句，以及1条更新语句，测试采用Special分布，Special数据占1%，有关详情请参考SysBench手册。

7. 测试中，默认使用prepare模式，即：--db-ps-mode=auto。

8. 标准版和单机版在相同的实例规格下，性能表现一致 

### 3.5 性能曲线
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-4.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-5.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-6.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-7.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-8.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-9.png)

## 4标准版性能说明
### 4.1 测试工具

SysBench0.5 

### 4.2 测试方法

根据不同实例规格，在服务器上同时运行多个实例，在客户机上运行SysBench，向服务器发起并发请求，进行压力测试，待数据完全预热后，取出稳定性能数据。 

### 4.3 测试数据

<table class="t">
<tbody><tr>
<th>  标准版实例名称
</th><th>  容量配置(GB)
</th><th>  表总行数
</th><th>  表数
</th><th>  测试数据集(GB)
</th><th>  并发数
</th></tr>
<tr>
<td> 大型
</td><td> 700
</td><td> 1,440,000,000
</td><td> 36
</td><td> 345.6
</td><td> 128
</td></tr>
<tr>
<td> 中型
</td><td> 230
</td><td> 480,000,000
</td><td> 12
</td><td> 115.2
</td><td> 64
</td></tr>
<tr>
<td> 小型
</td><td> 100
</td><td> 240,000,000
</td><td> 6
</td><td> 57.6
</td><td> 64
</td></tr>
<tr>
<td> 微型
</td><td> 20
</td><td> 75,000,000
</td><td> 2
</td><td> 18
</td><td> 64
</td></tr></tbody></table>

### 4.4 测试结果

<table class="t">
<tbody><tr>
<th width="80"><b>标准版实例名称</b>
</th><th width="136"><b>测试数据集(GB)</b>
</th><th width="66"> <b>并发数</b>
</th><th width="66"> <b>极限QPS</b>
</th></tr>
<tr>
<td> 大型
</td><td> 345.6
</td><td> 128
</td><td> 2932
</td></tr>
<tr>
<td> 标准型
</td><td> 115.2
</td><td> 64
</td><td> 1088
</td></tr>
<tr>
<td> 小型
</td><td> 57.6
</td><td> 64
</td><td> 556
</td></tr>
<tr>
<td> 微型
</td><td> 18
</td><td> 64
</td><td> 108
</td></tr></tbody></table>

说明：

1. 单表数据量约9.6GB。

2. QPS：每秒处理查询数。

3. 并发数：同一时间实例处理的并发请求数。

4. 测试工作集：测试数据规模，即访问数据的分布规模。

6. 测试中，每条事务包含4条点查询语句，以及1条更新语句，测试采用Special分布，Special数据占1%，有关详情请参考SysBench手册。

7. 测试中，默认使用prepare模式，即：--db-ps-mode=auto。

8. 标准版和单机版在相同的实例规格下，性能表现一致 

### 4.5 性能曲线
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-1.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-2.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-3.png)
