## GET_JSON_OBJECT
- 函数语法：
```
GET_JSON_OBJECT(<json> string, <path> string)
```
- 支持引擎：SparkSQL、Presto。
- 使用说明：提取 json 对象。
- 返回类型：string。
- 示例：
```
> SELECT get_json_object('{"a":"b"}', '$.a');
 b
```

## JSON_TUPLE
- 函数语法：
```
JSON_TUPLE(<json> string, <p1> string, ..., <pn> string)
```
- 支持引擎：SparkSQL。
- 使用说明：返回一个类似于函数 get_json_object 的元组，但它需要输入多个名称。所有输入参数和输出列类型都是字符串。
- 返回类型：struct&lt;string, ..., string>。
- 示例：
```
> SELECT json_tuple('{"a":1, "b":2}', 'a', 'b');
 1  2
```

## TO_JSON
- 函数语法：
```
TO_JSON(<expr> struct|map|array[, <option> map])
```
- 支持引擎：SparkSQL、Presto。
- 使用说明：返回具有给定结构值的 JSON 字符串。
- 返回类型：string。
- 示例：
```
> SELECT to_json(named_struct('a', 1, 'b', 2));
 {"a":1,"b":2}
> SELECT to_json(named_struct('time', to_timestamp('2015-08-26', 'yyyy-MM-dd')), map('timestampFormat', 'dd/MM/yyyy'));
 {"time":"26/08/2015"}
> SELECT to_json(array(named_struct('a', 1, 'b', 2)));
 [{"a":1,"b":2}]
> SELECT to_json(map('a', named_struct('b', 1)));
 {"a":{"b":1}}
> SELECT to_json(map(named_struct('a', 1),named_struct('b', 2)));
 {"[1]":{"b":2}}
> SELECT to_json(map('a', 1));
 {"a":1}
> SELECT to_json(array((map('a', 1))));
 [{"a":1}]
```

## FROM_JSON
- 函数语法：
```
FROM_JSON(<json> string, <schema> string[, <options> map<string, string>])
```
- 支持引擎：SparkSQL、Presto。
- 使用说明：返回具有给定 jsonStr 和模式的结构值。
- 返回类型：struct。
- 示例：
```
> SELECT from_json('{"a":1, "b":0.8}', 'a INT, b DOUBLE');
 {"a":1,"b":0.8}
> SELECT from_json('{"time":"26/08/2015"}', 'time Timestamp', map('timestampFormat', 'dd/MM/yyyy'));
 {"time":2015-08-26 00:00:00}
```


## SCHEMA_OF_JSON
- 函数语法：
```
SCHEMA_OF_JSON(<json> string[, <options> map<string, string>])
```
- 支持引擎：SparkSQL。
- 使用说明：返回 JSON 字符串的 DDL 格式的结构。
- 返回类型：string。
- 示例：
```
> SELECT schema_of_json('[{"col":0}]');
 ARRAY<STRUCT<`col`: BIGINT>>
> SELECT schema_of_json('[{"col":01}]', map('allowNumericLeadingZeros', 'true'));
 ARRAY<STRUCT<`col`: BIGINT>>
```


## JSON_ARRAY_LENGTH
- 函数语法：
```
JSON_ARRAY_LENGTH(<jsonArray> string)
```
- 支持引擎：SparkSQL、Presto。
- 使用说明：返回最外层 JSON 数组中的元素数。
- 返回类型：integer。
- 示例：
```
> SELECT json_array_length('[1,2,3,4]');
  4
> SELECT json_array_length('[1,2,3,{"f1":1,"f2":[5,6]},4]');
  5
> SELECT json_array_length('[1,2');
  NULL
```


## JSON_OBJECT_KEYS
- 函数语法：
```
JSON_OBJECT_KEYS(<json> string)
```
- 支持引擎：SparkSQL、Presto。
- 使用说明：以数组形式返回最外层 JSON 对象的所有键。
- 返回类型：array&lt;string>。
- 示例：
```
> SELECT json_object_keys('{}');
  []
> SELECT json_object_keys('{"key": "value"}');
  ["key"]
> SELECT json_object_keys('{"f1":"abc","f2":{"f3":"a", "f4":"b"}}');
  ["f1","f2"]
```
