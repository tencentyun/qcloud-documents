数据湖计算 DLC 在 [统一函数](https://cloud.tencent.com/document/product/1342/76992) 之外，同时支持 Presto 的内置函数。
## 如何开启 Presto 内置函数应用
### 途径一：在数据探索对数据引擎进行函数配置
1. 登录[ 数据湖计算 DLC 控制台](https://console.cloud.tencent.com/dlc)，选择服务地域。
2. 进入数据探索，选择数据引擎，当引擎内核为 Presto 时，可在高级配置中选择参数 **USEHIVEFUNCTION**，将该参数配置为 **false** 即可在使用该数据引擎进行 SQL 任务时使用 Presto 内置函数。
![](https://qcloudimg.tencent-cloud.cn/raw/a0b6390a7c2b4fffcaa0bdb3fb9420c6.png)

>! 在当前查询 session，所有使用该数据引擎的查询任务皆可使用 Presto 内置函数。

### 途径二：在 SQL 语句中添加参数
如您希望某个 SQL 任务调用 Presto 内置函数，可通过在 SQL 任务中添加配置信息实现。
示例：
```
SELECT/*+OPTIONS('useHiveFunction'='false')*/prestofunc(xx)
```

### 途径三：使用 API 时增加配置参数
在 task 结构体中 config 中设置 kv，useHiveFunction=false。
![](https://qcloudimg.tencent-cloud.cn/raw/9d561fd2b5aeb27851cff7bdf15065f8.png)
示例：
```
Stringstatement="SELECTdate_add('week',3,TIMESTAMP'2001-08-2203:04:05.321')";
TasksInfotask=newTasksInfo();
task.setTaskType("SQLTask");
task.setSQL(Base64.getEncoder().encodeToString(statement.getBytes()));
//添加以下参数配置
KVPairpair=newKVPair();
pair.setKey("useHiveFunction");
pair.setValue("false");
task.setConfig(newKVPair[]{pair});

CreateTasksRequestrequest=newCreateTasksRequest();
request.setDatabaseName("");
request.setDataEngineName(PRESTO_ENGINE);
request.setTasks(task);
```
参考 API 文档：[任务创建](https://cloud.tencent.com/document/product/1342/53775)。

### 途径四：使用 JDBC 进行任务创建时添加参数
- 在 JDBCURL 路径中添加 `&presto.USEHIVEFUNCTION=true` 参数或 `info.setProperty("presto.USEHIVEFUNCTION","false");`。
```
Connectionconnection=
DriverManager.getConnection("jdbc:dlc:dlc.tencentcloudapi.com?task_type=SQLTask&x省略中间参数xx&presto.USEHIVEFUNCTION=true",info);
或者
info.setProperty("presto.USEHIVEFUNCTION","false");
info.setPropertv("user","");
info.setProperty("password","");
```

## 支持的 Presto 内置函数列表

| 函数 | 出参 | 
|---------|---------|
| greatest(value1,value2,...,valueN)	| 与入参一致| 
| least(value1,value2,...,valueN)	| 与入参一致| 
| if(condition,true_value)	| -| 
| if(condition,true_value,false_value)| 	-| 
| coalesce(value1,value2[,...])	| -| 
| nullif(value1,value2)| 	-| 
| try(expression)| 	-| 
| cast(valueAStype)| 	type| 
| abs(x)	| 与入参一致| 
| cbrt(x)	| double| 
| ceil(x)	| 与入参一致| 
| ceiling(x)	| 与入参一致| 
| cosine_similarity(x,y)	| double| 
| degrees(x)| 	double| 
| e()	| double| 
| exp(x)	| double| 
| floor(x)	| 与入参一致| 
| from_base(string,radix)| 	bigint| 
| inverse_normal_cdf(mean,sd,p)	| double| 
| normal_cdf(mean,sd,v)	| double| 
| inverse_beta_cdf(a,b,p)	| double| 
| beta_cdf(a,b,v)| 	double| 
| ln(x)| 	double| 
| log2(x)	| double| 
| log10(x)	| double| 
| mod(n,m)	| 与入参一致| 
| pi()	| double| 
| pow(x,p)	| double| 
| power(x,p)	| double| 
| radians(x)| 	double| 
| rand()	| double| 
| random()| 	double| 
| random(n)	| 与入参一致| 
| round(x)	| 与入参一致| 
| round(x,d)	| 与入参一致| 
| sign(x)	| 与入参一致| 
| sqrt(x)	| double| 
| to_base(x,radix)	| varchar| 
| truncate(x)| double| 
| width_bucket(x,bound1,bound2,n)	| bigint| 
| width_bucket(x,bins)	| bigint| 
| wilson_interval_lower(successes,trials,z)	| double| 
| wilson_interval_upper(successes,trials,z)	| double| 
| acos(x)	| double| 
| asin(x)| 	double| 
| atan(x)| 	double| 
| atan2(y,x)	| double| 
| cos(x)	| double| 
| cosh(x)| 	double| 
| sin(x)	| double| 
| tan(x)	| double| 
| tanh(x)| 	double| 
| infinity()	| double| 
| is_finite(x)	| boolean| 
| is_infinite(x)	| boolean| 
| is_nan(x)| 	boolean| 
| nan()| 	double| 
| bit_count(x,bits)| 	bigint| 
| bitwise_and(x,y)	| bigint| 
| bitwise_not(x)	| bigint| 
| bitwise_or(x,y)	| bigint| 
| bitwise_xor(x,y)	| bigint| 
| bitwise_shift_left(x,shift,bits)| 	bigint| 
| bitwise_logical_shift_right(x,shift,bits)	| bigint| 
| bitwise_arithmetic_shift_right(x,shift)| bigint| 
| chr(n)	| varchar| 
| codepoint(string)	| integer| 
| concat(string1,...,stringN)	| varchar| 
| hamming_distance(string1,string2)| 	bigint| 
| length(string)	| bigint| 
| levenshtein_distance(string1,string2)	| bigint| 
| lower(string)	| varchar| 
| lpad(string,size,padstring)	| varchar| 
| ltrim(string)	| varchar| 
| replace(string,search)	| varchar| 
| replace(string,search,replace)| 	varchar| 
| reverse(string)	| varchar| 
| rpad(string,size,padstring)	| varchar| 
| rtrim(string)	| varchar| 
| split(string,delimiter)	| array(varchar)| 
| split(string,delimiter,limit)	| array(varchar)| 
| split_part(string,delimiter,index)	| varchar| 
| split_to_map(string,entryDelimiter,keyValueDelimiter)	| map(varchar,varchar)| 
| split_to_multimap(string,entryDelimiter,keyValueDelimiter)	| map(varchar,array(varchar))| 
|strpos(string,substring)	|bigint|
|strpos(string,substring,instance)|	bigint|
|strrpos(string,substring)|	bigint|
|strrpos(string,substring,instance)	|bigint|
|position(substringINstring)	|bigint|
|substr(string,start)	|varchar|
|substr(string,start,length)	|varchar|
|trim(string)	|varchar|
|upper(string)|	varchar|
|word_stem(word)	|varchar|
|word_stem(word,lang)|	varchar|
|normalize(string)	|varchar|
|to_utf8(string)	|varbinary|
|from_utf8(binary)	|varchar|
|from_utf8(binary,replace)|	varchar|
|regexp_extract_all(string,pattern)	|array(varchar)|
|regexp_extract_all(string,pattern,group)	|array(varchar)|
|regexp_extract(string,pattern)	|varchar|
|regexp_extract(string,pattern,group)	|varchar|
|regexp_like(string,pattern)|	boolean|
|regexp_replace(string,pattern)|	varchar|
|regexp_replace(string,pattern,replacement)	|varchar|
|regexp_split(string,pattern)	|array(varchar)|
|length(binary)	|bigint|
|concat(binary1,...,binaryN)|	varbinary|
|substr(binary,start)	|varbinary|
|substr(binary,start,length)	|varbinary|
|to_base64(binary)	|varchar|
|from_base64(string)	|varbinary|
|to_base64url(binary)	|varchar|
|from_base64url(string)	|varbinary|
|to_hex(binary)	|varchar|
|from_hex(string)|	varbinary|
|to_big_endian_64(bigint)	|varbinary|
|from_big_endian_64(binary)	|bigint|
|to_big_endian_32(integer)	|varbinary|
|from_big_endian_32(binary)	|integer|
|to_ieee754_32(real)|	varbinary|
|from_ieee754_32(binary)	|real|
|to_ieee754_64(double)	|varbinary|
|from_ieee754_64(binary)	|double|
|lpad(binary,size,padbinary)	|varbinary|
|rpad(binary,size,padbinary)	|varbinary|
|crc32(binary)|	bigint|
|md5(binary)	|varbinary|
|sha1(binary)	|varbinary|
|sha256(binary)	|varbinary|
|sha512(binary)	|varbinary|
|xxhash64(binary)	|varbinary|
|spooky_hash_v2_32(binary)	|varbinary|
|spooky_hash_v2_64(binary)	|varbinary|
|hmac_md5(binary,key)|	varbinary|
|hmac_sha1(binary,key)|	varbinary|
|hmac_sha256(binary,key)|	varbinary|
|hmac_sha512(binary,key)	|varbinary|
|current_date	|date|
|current_timestamp	|timestamp|
|current_timezone()	|varchar|
| date(x)	| date| 
| from_iso8601_timestamp(string)	| timestamp| 
| from_iso8601_date(string)	| date| 
| from_unixtime(unixtime)	| timestamp| 
| from_unixtime(unixtime,string)	| timestamp| 
| from_unixtime(unixtime,hours,minutes)| 	timestamp| 
| localtimestamp	| timestamp| 
| now()	| timestamp| 
| to_iso8601(x)| 	varchar| 
| to_milliseconds(interval)	| bigint| 
| to_unixtime(timestamp)	| double| 
| date_trunc(unit,x)	| 与入参一致| 
| date_add(unit,value,timestamp)	| 与入参一致| 
| date_diff(unit,timestamp1,timestamp2)	| bigint| 
| date_format(timestamp,format)| 	varchar| 
| date_parse(string,format)	| timestamp| 
| format_datetime(timestamp,format)| 	varchar| 
| parse_datetime(string,format)| 	timestamp| 
| day(x)	| bigint| 
| day_of_month(x)	| bigint| 
| day_of_week(x)| 	bigint| 
| day_of_year(x)| 	bigint| 
| dow(x)	| bigint| 
| doy(x)	| bigint| 
| hour(x)	| bigint| 
| millisecond(x)	| bigint| 
| minute(x)| 	bigint| 
| month(x)	| bigint| 
| quarter(x)	| bigint| 
| second(x)	| bigint| 
| timezone_hour(timestamp)	| bigint| 
| timezone_minute(timestamp)	| bigint| 
| week(x)	| bigint| 
| week_of_year(x)	| bigint| 
| year(x)| 	bigint| 
| year_of_week(x)| 	bigint| 
| yow(x)	| bigint| 
| arbitrary(x)	| 与入参一致| 
| array_agg(x)	| array(与入参一致)| 
| avg(x)	| double| 
| bool_and(boolean)	| boolean| 
| bool_or(boolean)	| boolean| 
| checksum(x)	| varbinary| 
| count(*)	| bigint| 
| count(x)	| bigint| 
| count_if(x)	| bigint| 
| every(boolean)	| boolean| 
| geometric_mean(x)	| double| 
| max_by(x,y)	| [same as x]| 
| max_by(x,y,n)	| array([same as x])| 
| min_by(x,y)	| [same as x]| 
| min_by(x,y,n)	| array([same as x])| 
| max(x)	| 与入参一致| 
| max(x,n)	| array([same as x])| 
| min(x)	| 与入参一致| 
| min(x,n)	| array([same as x])| 
| set_agg(x)	| array(与入参一致)| 
| set_union(array(T))	| array(T)| 
| sum(x)	| 与入参一致| 
| bitwise_and_agg(x)	| bigint| 
| bitwise_or_agg(x)	| bigint| 
| histogram(x)| 	map(K,bigint)| 
| map_agg(key,value)	| map(K,V)| 
| map_union(x(K,V))	| map(K,V)| 
| multimap_agg(key,value)	| map(K,array(V))| 
| approx_distinct(x)	| bigint| 
| approx_distinct(x,e)| 	bigint| 
| approx_percentile(x,percentage)| 	[same as x]| 
| approx_percentile(x,percentage,accuracy)	| [same as x]| 
| approx_percentile(x,percentages)	| array([same as x])| 
| approx_percentile(x,percentages,accuracy)	| array([same as x])| 
| approx_percentile(x,w,percentage)| 	[same as x]| 
| approx_percentile(x,w,percentage,accuracy)| 	[same as x]| 
| approx_percentile(x,w,percentages)	| array([same as x])| 
| approx_percentile(x,w,percentages,accuracy)	| array([same as x])| 
| numeric_histogram(buckets,value,weight)	| map(double,double)| 
| numeric_histogram(buckets,value)	| map(double,double)| 
| corr(y,x)	| double| 
| covar_pop(y,x)	| double| 
| covar_samp(y,x)| 	double| 
| entropy(c)	| double| 
| kurtosis(x)| 	double| 
| regr_intercept(y,x)	| double| 
| regr_slope(y,x)	| double| 
| skewness(x)	| double| 
| stddev(x)	| double| 
| stddev_pop(x)	| double| 
| stddev_samp(x)| 	double| 
| variance(x)| 	double| 
| var_pop(x)	| double| 
| var_samp(x)	| double
| classification_miss_rate(buckets,y,x,weight)	| array(double)| 
| classification_miss_rate(buckets,y,x)| 	array(double)| 
| classification_fall_out(buckets,y,x,weight)| 	array(double)| 
| classification_fall_out(buckets,y,x)	| array(double)| 
| classification_precision(buckets,y,x,weight)	| array(double)| 
| classification_precision(buckets,y,x)	| array(double)| 
| classification_recall(buckets,y,x,weight)	| array(double)| 
| classification_recall(buckets,y,x)	| array(double)| 
| classification_thresholds(buckets,y,x)	|-|
| differential_entropy(sample_size,x)	|-|
| differential_entropy(sample_size,x,weight)	|-|
| differential_entropy(bucket_count,x,weight,method,min,max)	|double|
|cume_dist()	|bigint|
|dense_rank()	|bigint|
|ntile(n)	|bigint|
|percent_rank()	|double|
|rank()	|bigint|
|row_number()	|bigint|
|first_value(x)	|与入参一致|
|last_value(x)	|与入参一致|
|nth_value(x,offset)	|与入参一致|
|lead(x[,offset[,default_value]])	|与入参一致|
|lag(x[,offset[,default_value]])	|与入参一致|
|array_average(array(double))	|double|
|array_distinct(x)	|array|
|array_except(x,y)|	array|
|array_join(x,delimiter,null_replacement)	|varchar|
|array_max(x)	|x|
|array_min(x)	|x|
|array_remove(x,element)	|array|
|array_sort(x)	|array|
|array_sum(array(T))	|bigint/double|
|arrays_overlap(x,y)	|boolean|
|array_union(x,y)	|array|
|cardinality(x)|	bigint|
|concat(array1,array2,...,arrayN)	|array|
|combinations(array(T),n)	|array(array(T))|
|contains(x,element)	|boolean|
|element_at(array(E),index)	|E|
|flatten(x)	|array|
|ngrams(array(T),n)	|array(array(T))|
|repeat(element,count)	|array|
|reverse(x)	|array|
|sequence(start,stop)	|array(bigint)|
|sequence(start,stop,step)|	array(bigint)|
|sequence(start,stop)	|array(date)|
|sequence(start,stop,step)	|array(date)|
|sequence(start,stop,step)|	array(timestamp)|
|shuffle(x)	|array|
|slice(x,start,length)	|array|
|cardinality(x)|	bigint|
|element_at(map(K,V),key)	|V|
|map(array(K),array(V))	|map(K,V)|
|map_from_entries(array(row(K,V)))	|map(K,V)|
|multimap_from_entries(array(row(K,V)))|	map(K,array(V))|
|map_concat(map1(K,V),map2(K,V),...,mapN(K,V))|	map(K,V)|
|map_keys(x(K,V))	|array(K)|
|map_normalize(x(varchar,double))	|array(varchar,double)|
|map_values(x(K,V))	|array(V)|
|url_extract_fragment(url)|	varchar|
|url_extract_host(url)|	varchar|
|url_extract_parameter(url,name)|	varchar|
|url_extract_path(url)	|varchar|
|url_extract_port(url)|	bigint|
|url_extract_protocol(url)	|varchar|
|url_extract_query(url)	|varchar|
|url_encode(value)	|varchar|
|url_decode(value)	|varchar|
|try_cast(value AS type)	|type|
|current_user 	|varchar|
|typeof(expr) 	|varchar|
|parse_presto_data_size(string)	|decimal(38)|
|split_to_map(string,entryDelimiter,keyValueDelimiter,function(K,V1,V2,R))	 |map&lt;string,string>|
|regexp_replace(string,pattern,function)	|string|
|reduce_agg(inputValueT,initialStateS,inputFunction(S,T,S),combineFunction(S,S,S))	|S|
|all_match(array(T),function(T,boolean))	|boolean|
|any_match(array(T),function(T,boolean))	|boolean|
|array_sort(array(T),function(T,T,int))	|array(T)|
|filter(array(T),function(T,boolean))	|array(T)|
|none_match(array(T),function(T,boolean))	|boolean|
|reduce(array(T),initialStateS,inputFunction(S,T,S),outputFunction(S,R))	|R|
|transform(array(T),function(T,U))	|array(U)|
|zip_with(array(T),array(U),function(T,U,R))	|array(R)|
|map_filter(map(K,V),function(K,V,boolean))	|map(K,V)|
|map_zip_with(map(K,V1),map(K,V2),function(K,V1,V2,V3))	|map(K,V3)|
|transform_keys(map(K1,V),function(K1,V,K2))	|map(K2,V)|
|transform_values(map(K,V1),function(K,V1,V2))	|map(K,V2)|
