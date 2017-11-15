## What's new

<table class="t">
<tbody><tr>
<th>  High-performance instance name
</th><th>  Capacity configuration (GB)
</th><th>  Total number of rows in table
</th><th>  Number of tables
</th><th>  Testing dataset (GB)
</th><th>  Concurrency level
</th></tr>
<tr>
<td> Large-sized
</td><td> 600
</td><td> 1,560,000,000
</td><td> 39
</td><td> 429
</td><td> 128
</td></tr>
<tr>
<td> Type A
</td><td> 400
</td><td> 1,160,000,000
</td><td> 29
</td><td> 319
</td><td> 96
</td></tr>
<tr>
<td> Type B
</td><td> 200
</td><td> 600,000,000
</td><td> 15
</td><td> 165
</td><td> 64
</td></tr>
<tr>
<td>  Type C
</td><td> 100
</td><td> 320,000,000
</td><td> 8
</td><td> 88
</td><td> 64
</td></tr>
<tr>
<td> Small-sized
</td><td> 50
</td><td> 160,000,000
</td><td> 4
</td><td> 44
</td><td> 64
</td></tr>
<tr>
<td> Micro-sized
</td><td> 25
</td><td> 80,000,000
</td><td> 2
</td><td> 22
</td><td> 64
</td></tr></tbody></table>

High-capacity version is released on September 14th, 2015, which is suitable for scenarios with large data volume but low demand for performance.

## 1. Performance of High-capacity Version

### 1.1 Testing Tool

SysBench0.5 

### 1.2 Testing Method

Run multiple instances simultaneously on the server, according to different instance specifications. Run SysBench on the customer machine and send concurrent requests to the server as stress test. Retrieve stable performance data once the data has been fully prefetched. 

### 1.3 Testing Parameters

<table class="t">
<tbody><tr>
<th> <b>Memory of high-capacity version (MB)</b>
</th><th> <b>Storage space (GB)</b>
</th><th> <b>Number of tables</b>
</th><th> <b>Number of rows in each table</b>
</th><th> <b>Testing dataset (GB)</b>
</th><th> <b>Running time (s)</b>
</th><th> <b>Sampling interval (s)</b>
</th></tr>
<tr>
<td> 20,000
</td><td> 2,000
</td><td> 40
</td><td> 40 million
</td><td> 378
</td><td> 1,800
</td><td> 20
</td></tr>
<tr>
<td> 10,000
</td><td> 1,000
</td><td> 25
</td><td> 40 million
</td><td> 238
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 5,000
</td><td> 500
</td><td> 20
</td><td> 40 million
</td><td> 190
</td><td> 1,800
</td><td> 5
</td></tr></tbody></table>

### 1.4 Test Result

<table class="t">
<tbody><tr>
<th> <b>High-capacity instance configuration</b>
</th><th> <b>Testing dataset (GB)</b>
</th><th> <b>Concurrency level</b>
</th><th> <b>QPS</b>
</th><th> <b>TPS</b>
</th></tr>
<tr>
<td> Memory: 20,000 MB. Storage space: 2,000 GB
</td><td> 1,500
</td><td> 96
</td><td> 7,911
</td><td> 1,130
</td></tr>
<tr>
<td> Memory: 10,000 MB. Storage space: 1,000 GB
</td><td> 750
</td><td> 96
</td><td> 3,351
</td><td> 478
</td></tr>
<tr>
<td> Memory: 5,000 MB. Storage space: 500 GB
</td><td> 410
</td><td> 96
</td><td> 1,257
</td><td> 179
</td></tr></tbody></table>

Description:
1. Row format is Dynamic by default.

2. QPS: Queries per second.

3. Concurrency level: Number of concurrent requests processed by the instance at the same time.

4. Testing dataset: Volume of testing data, that is, volume distribution of access data.

5. During the test, each transaction contains 4 point query statements and 1 update statement. We use Special Distribution, 1% of the data is Special data. Refer to the manual of SysBench for relevant details.

6. During the test, prepare mode is used by default (--db-ps-mode=auto).

## 2. Performance of High-IO Version

### 2.1 Testing Tool

SysBench0.5 

### 2.2 Testing Method

Run multiple instances simultaneously on the server, according to different instance specifications. Run SysBench on the customer machine and send concurrent requests to the server as stress test. Retrieve stable performance data once the data has been fully prefetched. 

### 2.3 Testing Parameters

<table class="t">
<tbody><tr>
<th>  Memory of high-IO version (MB)
</th><th>  Storage space (GB)
</th><th>  Number of tables
</th><th>  Number of rows in each table
</th><th>  Testing dataset (GB)
</th><th>  Running time (s)
</th><th>  Sampling interval (s)
</th></tr>
<tr>
<td> 48,000
</td><td> 1,000
</td><td> 40
</td><td> 40 million
</td><td> 378
</td><td> 1,800
</td><td> 20
</td></tr>
<tr>
<td> 24,000
</td><td> 500
</td><td> 25
</td><td> 40 million
</td><td> 238
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 16,000
</td><td> 400
</td><td> 20
</td><td> 40 million
</td><td> 190
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 12,000
</td><td> 250
</td><td> 15
</td><td> 40 million
</td><td> 142
</td><td> 1,800
</td><td> 20
</td></tr>
<tr>
<td> 8,000
</td><td> 200
</td><td> 12
</td><td> 40 million
</td><td> 114
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 4,000
</td><td> 100
</td><td> 8
</td><td> 40 million
</td><td> 76
</td><td> 1,800
</td><td> 20
</td></tr>
<tr>
<td> 2,000
</td><td> 50
</td><td> 6
</td><td> 20 million
</td><td> 29
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 1,000
</td><td> 25
</td><td> 6
</td><td> 10 million
</td><td> 14
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 360
</td><td> 10
</td><td> 4
</td><td> 5 million
</td><td> 4.6
</td><td> 1,800
</td><td> 5
</td></tr></tbody></table>

### 2.4 Test Result

<table class="t">

<tbody><tr>
<th> <b>High-IO instance configuration</b>
</th><th > <b>Testing dataset (GB)</b>
</th><th> <b>Concurrency level</b>
</th><th> <b>QPS</b>
</th><th> <b>TPS</b>
</th></tr>
<tr>
<td> Memory: 48,000 MB. Storage space: 1,000 GB
</td><td> 378
</td><td> 256
</td><td> 40,856
</td><td> 8,208
</td></tr>
<tr>
<td> Memory: 24,000 MB. Storage space: 500 GB
</td><td> 238
</td><td> 256
</td><td> 24,979
</td><td> 4,995
</td></tr>
<tr>
<td> Memory: 16,000 MB. Storage space: 400 GB
</td><td> 190
</td><td> 256
</td><td> 24,953
</td><td> 4,991
</td></tr>
<tr>
<td> Memory: 12,000 MB. Storage space: 250 GB
</td><td> 142
</td><td> 64
</td><td> 15,700
</td><td> 3,139
</td></tr>
<tr>
<td> Memory: 8,000 MB. Storage space: 200 GB
</td><td> 114
</td><td> 64
</td><td> 14,085
</td><td> 2,817
</td></tr>
<tr>
<td> Memory: 4,000 MB. Storage space: 100 GB
</td><td> 76
</td><td> 64
</td><td> 4,852
</td><td> 970
</td></tr>
<tr>
<td> Memory: 2,000 MB. Storage space: 50 GB
</td><td> 29
</td><td> 64
</td><td> 2,667
</td><td> 533
</td></tr>
<tr>
<td> Memory: 1,000 MB. Storage space: 25 GB
</td><td> 14
</td><td> 64
</td><td> 1,103
</td><td> 220
</td></tr>
<tr>
<td> Memory: 360 MB. Storage space: 10 GB
</td><td> 4.6
</td><td> 64
</td><td> 133
</td><td> 26
</td></tr></tbody></table>

Description:

1. Row format is Dynamic by default.

2. QPS: Queries per second.

3. Concurrency level: Number of concurrent requests processed by the instance at the same time.

4. Testing dataset: Volume of testing data, that is, volume distribution of access data.

5. During the test, each transaction contains 4 point query statements and 1 update statement. We use Special Distribution, 1% of the data is Special data. Refer to the manual of SysBench for relevant details.

6. During the test, prepare mode is used by default (--db-ps-mode=auto).

## 3. Performance of High-performance Version

### 3.1 Testing Tool

SysBench0.5 

### 3.2 Testing Method

Run multiple instances simultaneously on the server, according to different instance specifications. Run SysBench on the customer machine and send concurrent requests to the server as stress test. Retrieve stable performance data once the data has been fully prefetched. 

### 3.3 Testing Data
<table class="t">
<tbody><tr>
<th>  High-performance instance name
</th><th>  Capacity configuration (GB)
</th><th>  Total number of rows in table
</th><th>  Number of tables
</th><th>  Testing dataset (GB)
</th><th>  Concurrency level
</th></tr>
<tr>
<td> Large-sized
</td><td> 600
</td><td> 1,560,000,000
</td><td> 39
</td><td> 429
</td><td> 128
</td></tr>
<tr>
<td> Type A
</td><td> 400
</td><td> 1,160,000,000
</td><td> 29
</td><td> 319
</td><td> 96
</td></tr>
<tr>
<td> Type B
</td><td> 200
</td><td> 600,000,000
</td><td> 15
</td><td> 165
</td><td> 64
</td></tr>
<tr>
<td>  Type C
</td><td> 100
</td><td> 320,000,000
</td><td> 8
</td><td> 88
</td><td> 64
</td></tr>
<tr>
<td> Small-sized
</td><td> 50
</td><td> 160,000,000
</td><td> 4
</td><td> 44
</td><td> 64
</td></tr>
<tr>
<td> Micro-sized
</td><td> 25
</td><td> 80,000,000
</td><td> 2
</td><td> 22
</td><td> 64
</td></tr></tbody></table>

### 3.4 Test Result

<table class="t">
<tbody><tr>
<th>  Memory of high-IO version (MB)
</th><th>  Storage space (GB)
</th><th>  Number of tables
</th><th>  Number of rows in each table
</th><th>  Testing dataset (GB)
</th><th>  Running time (s)
</th><th>  Sampling interval (s)
</th></tr>
<tr>
<td> 48,000
</td><td> 1,000
</td><td> 40
</td><td> 40 million
</td><td> 378
</td><td> 1,800
</td><td> 20
</td></tr>
<tr>
<td> 24,000
</td><td> 500
</td><td> 25
</td><td> 40 million
</td><td> 238
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 16,000
</td><td> 400
</td><td> 20
</td><td> 40 million
</td><td> 190
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 12,000
</td><td> 250
</td><td> 15
</td><td> 40 million
</td><td> 142
</td><td> 1,800
</td><td> 20
</td></tr>
<tr>
<td> 8,000
</td><td> 200
</td><td> 12
</td><td> 40 million
</td><td> 114
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 4,000
</td><td> 100
</td><td> 8
</td><td> 40 million
</td><td> 76
</td><td> 1,800
</td><td> 20
</td></tr>
<tr>
<td> 2,000
</td><td> 50
</td><td> 6
</td><td> 20 million
</td><td> 29
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 1,000
</td><td> 25
</td><td> 6
</td><td> 10 million
</td><td> 14
</td><td> 1,800
</td><td> 5
</td></tr>
<tr>
<td> 360
</td><td> 10
</td><td> 4
</td><td> 5 million
</td><td> 4.6
</td><td> 1,800
</td><td> 5
</td></tr></tbody></table>

Description:

1. Row format is Dynamic by default. Capacity for a single table is 11 GB.

2. QPS: Queries per second.

3. Concurrency level: Number of concurrent requests processed by the instance at the same time.

4. Testing dataset: Volume of testing data, that is, volume distribution of access data.

5. During the test, each transaction contains 4 point query statements and 1 update statement. We use Special Distribution, 1% of the data is Special data. Refer to the manual of SysBench for relevant details.

6. During the test, prepare mode is used by default (--db-ps-mode=auto).

7. With the same instance specification, the performances of standard version and standalone version are the same 

### 3.5 Performance Curve
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-4.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-5.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-6.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-7.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-8.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-9.png)

## 4. Performance of Standard Version
### 4.1 Testing Tool

SysBench0.5 

### 4.2 Testing Method

Run multiple instances simultaneously on the server, according to different instance specifications. Run SysBench on the customer machine and send concurrent requests to the server as stress test. Retrieve stable performance data once the data has been fully prefetched. 

### 4.3 Testing Data

<table class="t">
<tbody><tr>
<th>  Standard instance name
</th><th>  Capacity configuration (GB)
</th><th>  Total number of rows in table
</th><th>  Number of tables
</th><th>  Testing dataset (GB)
</th><th>  Concurrency level
</th></tr>
<tr>
<td> Large-sized
</td><td> 700
</td><td> 1,440,000,000
</td><td> 36
</td><td> 345.6
</td><td> 128
</td></tr>
<tr>
<td> Medium-sized
</td><td> 230
</td><td> 480,000,000
</td><td> 12
</td><td> 115.2
</td><td> 64
</td></tr>
<tr>
<td> Small-sized
</td><td> 100
</td><td> 240,000,000
</td><td> 6
</td><td> 57.6
</td><td> 64
</td></tr>
<tr>
<td> Micro-sized
</td><td> 20
</td><td> 75,000,000
</td><td> 2
</td><td> 18
</td><td> 64
</td></tr></tbody></table>

### 4.4 Test Result

<table class="t">
<tbody><tr>
<th width="80"><b>Standard instance name</b>
</th><th width="136"><b>Testing dataset (GB)</b>
</th><th width="66"> <b>Concurrency level</b>
</th><th width="66"> <b>Peak QPS</b>
</th></tr>
<tr>
<td> Large-sized
</td><td> 345.6
</td><td> 128
</td><td> 2,932
</td></tr>
<tr>
<td> Standard Server
</td><td> 115.2
</td><td> 64
</td><td> 1,088
</td></tr>
<tr>
<td> Small-sized
</td><td> 57.6
</td><td> 64
</td><td> 556
</td></tr>
<tr>
<td> Micro-sized
</td><td> 18
</td><td> 64
</td><td> 108
</td></tr></tbody></table>

Description:

1. Data volume of a single table is about 9.6 GB.

2. QPS: Queries per second.

3. Concurrency level: Number of concurrent requests processed by the instance at the same time.

4. Testing dataset: Volume of testing data, that is, volume distribution of access data.

5. During the test, each transaction contains 4 point query statements and 1 update statement. We use Special Distribution, 1% of the data is Special data. Refer to the manual of SysBench for relevant details.

6. During the test, prepare mode is used by default (--db-ps-mode=auto).

7. With the same instance specification, the performances of standard version and standalone version are the same 

### 4.5 Performance Curve
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-1.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-2.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukugebanbenxingnengshuoming-3.png)

