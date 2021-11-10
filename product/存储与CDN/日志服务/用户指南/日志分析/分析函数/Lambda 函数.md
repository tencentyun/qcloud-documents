本文介绍 Lambda 函数对日志数据进行分析处理的语法及示例。

日志服务支持您在 SQL 分析语句中定义 Lambda 表达式，并将该表达式传递给指定函数，丰富函数的表达。

### 语法

Lambda 表达式需与函数一起使用，例如 [filter 函数](https://cloud.tencent.com/document/product/614/63800#filter)、[reduce 函数](https://cloud.tencent.com/document/product/614/63800#reduce)、[transform 函数](https://cloud.tencent.com/document/product/614/63800#transform)、[zip_with 函数](https://cloud.tencent.com/document/product/614/63800#zip_with)。Lambda 表达式的语法如下：
```
parameter -> expression
```

<table>
	<tr><th>参数</th><th>说明</th></tr>
	<tr><td>parameter</td><td>用于传递参数的标识符。</td></tr>
	<tr><td>expression</td><td>表达式，大多数的 Mysql 表达式都可以在 Lambda 表达式使用。例如：</br>
	<pre><code>x -> x + 1 <br/>(x, y) -> x + y <br/>x -> regexp_like(x, 'a+') <br/>x -> x[1] / x[2] <br/>x -> if(x > 0, x, -x) <br/>x -> coalesce(x, 0) <br/>x -> cast(x AS JSON) <br/>x -> x + try(1 / 0)</code></pre></td></tr>
</table>


### 示例

#### 示例1：使用 Lambda 表达式 x-> x is not null

返回数组[5，null，7，null]中非 null 的元素。

- 查询和分析语句
```
* | SELECT filter(array[5, null, 7, null], x -> x is not null)
```
- 查询和分析结果
![image-20211101031735763](https://qcloudimg.tencent-cloud.cn/raw/3d737dee14bb0cd89dd9f3e160366c18.png)

#### 示例2：使用 Lambda 表达式0，(s, x) -> s + x, s -> s

返回数组[5，20，50]中各个元素相加的结果。

- 查询和分析语句
```
* | SELECT reduce(array[5, 20, 50], 0, (s, x) -> s + x, s -> s)
```
- 查询和分析结果
![image-20211101031923093](https://qcloudimg.tencent-cloud.cn/raw/fdb8f1b749c0e104274835585104be64.png)


#### 示例3：使用 Lambda 表达式(k, v) -> v> 10

将两个数组映射为一个 Map 且 Map 中的键值大于10。

- 查询和分析语句
```
* | SELECT map_filter(map(array['class01', 'class02', 'class03'], array[11, 10, 9]), (k,v) -> v > 10)
```
- 查询和分析结果
![image-20211101032008892](https://qcloudimg.tencent-cloud.cn/raw/ac904e623c19d617c91f6038245a7036.png)

#### 示例4：使用 Lambda 表达式(x, y) -> (y, x)

将对换两个数组的元素位置，并提取数组中索引相同的元素组成一个新的二维数组。

- 查询和分析语句
```
* | SELECT zip_with(array['a', 'b', 'c'], array['d', 'e', 'f'], (x, y) -> concat(x, y))
```
- 查询和分析结果
![image-20211101033556418](https://qcloudimg.tencent-cloud.cn/raw/251495f2e8a57b345d88bd61462ba1fe.png)

#### 示例5：使用 Lambda 表达式 x -> coalesce（x, 0）+1

将数组[5, null, 6]的各个元素加1，然后返回。如果数组中包含 null 元素，则转换为0，再加1。

- 查询和分析语句
```
* | SELECT transform(array[5, NULL, 6], x -> coalesce(x, 0) + 1)
```
- 查询和分析结果
![image-20211101032336484](https://qcloudimg.tencent-cloud.cn/raw/26ad9725c211a7ee5b98f48490a8e5cc.png)

#### 其他示例

```
* | SELECT filter(array[], x -> true)
* | SELECT map_filter(map(array[],array[]), (k, v) -> true)
* | SELECT reduce(array[5, 6, 10, 20], -- calculates arithmetic average: 10.25
              cast(row(0.0, 0) AS row(sum double, count integer)),
              (s, x) -> cast(row(x + s.sum, s.count + 1) AS row(sum double, count integer)),
              s -> if(s.count = 0, null, s.sum / s.count))
* | SELECT reduce(array[2147483647, 1], cast(0 AS bigint), (s, x) -> s + x, s -> s)
* | SELECT reduce(array[5, 20, null, 50], 0, (s, x) -> s + x, s -> s)
* | SELECT transform(array[array[1, null, 2], array[3, null]], a -> filter(a, x -> x is not null))
```

