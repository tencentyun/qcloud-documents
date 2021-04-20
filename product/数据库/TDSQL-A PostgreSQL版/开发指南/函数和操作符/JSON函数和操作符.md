## JSON 和 JSONB 操作符
| **操作符** | **描述**                              |
| ---------- | ------------------------------------- |
| ->         | 获得 JSON 数组元素/通过键获得 JSON 对象域 |
| ->>        | 以文本形式获得 JSON 数组元素/对象域     |
| #>         | 获取在指定路径的 JSON 对象              |
| #>>        | 以文本形式获取在指定路径的 JSON 对象    |

示例：
```
postgres=# SELECT '[{"a":"foo"},{"b":"bar"},{"c":"baz"}]'::json->2;
 ?column? 
-------------
 {"c":"baz"}
(1 row)
 
postgres=# SELECT '{"a": {"b":"foo"}}'::json->'a';
 ?column? 
-------------
 {"b":"foo"}
(1 row)
 
postgres=# SELECT '[1,2,3]'::json->>2;
 ?column? 
----------
 3
(1 row)
 
postgres=# SELECT '{"a":1,"b":2}'::json->>'b';
 ?column? 
----------
 2
(1 row)
 
postgres=# SELECT '{"a": {"b":{"c": "foo"}}}'::json#>'{a,b}';
  ?column? 
--------------
 {"c": "foo"}
(1 row)
```

## JSON 创建函数
| **函数**                                                     | **描述**                                                     |
| --------------------------------------------- | --------------------------------------------------- |
| to_json(anyelement)  to_jsonb(anyelement)                    | 把值返回为 json 或者 jsonb。数组和组合被（递归地）转换成数组和对象；否则，如果有从该类型到 json 的投影，将使用该投影函数来执行转换； 否则将产生一个标量值。对任何一个数值、布尔量或空值的标量类型， 将使用其文本表达，以这样一种方式使其成为有效的 json 或者 jsonb 值 |
| array_to_json  (anyarray [, pretty_bool])                    | 把数组作为一个 JSON 数组返回。一个多维数组会成为一个数组 的 JSON 数组。如果 pretty_bool 为真，将在 第1维度的元素之间增加换行 |
| row_to_json  (record [, pretty_bool])                        | 把行作为一个 JSON 对象返回。如果 pretty_bool 为真，将在第1层元素之间增加换行 |
| json_build_array  (VARIADIC  "any")  jsonb_build_array  (VARIADIC  "any") | 从一个可变参数列表构造一个可能包含异质类型的 JSON 数组     |
| json_build_object  (VARIADIC  "any")  jsonb_build_object  (VARIADIC  "any") | 从一个可变参数列表构造一个 JSON 对象。通过转换，该参数列表由交替出现的键和值构成 |
| json_object(text[])  jsonb_object(text[])                    | 从一个文本数组构造一个 JSON 对象。该数组必须可以是具有偶数个成员的一维数组（成员被当做交替出现的键/值对），或者是一个二维数组（每一个 内部数组刚好有2个元素，可以被看做是键/值对） |
| json_object  (keys  text[], values text[])  jsonb_object  (keys  text[], values text[]) | json_object 的这种形式从两个独立的数组得到键/值对，在其他方面和一个参数的形式相同 |

示例：
```
postgres=# SELECT '{"a": {"b":{"c": "foo"}}}'::json#>'{a,b}';
  ?column? 
--------------
 {"c": "foo"}
(1 row)
 
postgres=# SELECT to_json('Fred said "Hi."'::text);
    to_json    
---------------------
 "Fred said \"Hi.\""
(1 row)
 
postgres=# SELECT array_to_json('{{1,5},{99,100}}'::int[]);
 array_to_json  
------------------
 [[1,5],[99,100]]
(1 row)
 
postgres=# SELECT row_to_json(row(1,'foo'));
   row_to_json   
---------------------
 {"f1":1,"f2":"foo"}
(1 row)
 
postgres=# SELECT json_build_array(1,2,'3',4,5);
 json_build_array 
-------------------
 [1, 2, "3", 4, 5]
(1 row) 

postgres=# SELECT json_build_object('foo',1,'bar',2);
  json_build_object  
------------------------
 {"foo" : 1, "bar" : 2}
(1 row) 

postgres=# SELECT json_object('{a, 1, b, "def", c, 3.5}');
       json_object       
---------------------------------------
 {"a" : "1", "b" : "def", "c" : "3.5"}
(1 row) 

postgres=# SELECT json_object('{{a, 1},{b, "def"},{c, 3.5}}');
       json_object       
---------------------------------------
 {"a" : "1", "b" : "def", "c" : "3.5"}
(1 row)
 
postgres=# SELECT json_object('{a, b}', '{1,2}');
   json_object    
------------------------
 {"a" : "1", "b" : "2"}
(1 row)
```

## JSON 处理函数
| **函数**                                                     | **描述**                                                     |
| -------------------------------------------- | ----------------------------------------------------- |
| json_array_length(json)  jsonb_array_length(jsonb)      | 返回最外层 JSON 数组中的元素数量                          |
| json_each(json)  jsonb_each(jsonb)                           | 扩展最外层的 JSON 对象成为一组键/值对                      |
| json_each_text(json)  jsonb_each_text(jsonb)                 | 扩展最外层的 JSON 对象成为一组键/值对。返回值将是`文本`类型 |
| json_object_keys(json)  jsonb_object_keys(jsonb)             | 返回最外层 JSON 对象中的键集合                             |
| json_array_elements(json)  jsonb_array_elements(jsonb)       | 把一个 JSON 数组扩展成一个 JSON 值的集合           |
| json_array_elements_text(json)  jsonb_array_elements_text(jsonb) | 把一个 JSON 数组扩展成一个 text 值集合       |
| json_typeof(json)  jsonb_typeof(jsonb)                       | 把最外层的 JSON 值的类型作为一个文本字符串返回。可能的类型是：`object`、`array`、`string`、`number`、`boolean`以及`null` |
| jsonb_insert(target jsonb,   path text[],   new_value jsonb,  [insert_after boolean]) | 返回被插入了 new_value 的 target。 <br>如果 path 指定的 target 节在一个 JSONB 数组中，new_value 将被插入到目标之前（insert_after 为 false，默认情况） 或者之后（insert_after 为真）。<br>如果 path 指定的 target 节在一个 JSONB 对象内，则只有当 target 不存在时才插入 new_value。 对于面向路径的操作符来说，出现在 path 中的负整数表示从 JSON 数组的末尾开始计数。 |

示例：
```
postgres=# SELECT jsonb_insert('{"a": [0,1,2]}', '{a, 1}', '"new_value"');
     jsonb_insert     
-------------------------------
 {"a": [0, "new_value", 1, 2]}
(1 row)
 
postgres=# SELECT json_array_length('[1,2,3,{"f1":1,"f2":[5,6]},4]');
 json_array_length 
-------------------
         5
(1 row)
 
postgres=# SELECT * FROM json_each('{"a":"foo", "b":"bar"}');
key | value
-----+-------
 a  | "foo"
 b  | "bar"
(2 rows)

postgres=# SELECT * FROM json_each_text('{"a":"foo", "b":"bar"}');
 key | value 
-----+-------
 a  | foo
 b  | bar
(2 rows)
 
postgres=# SELECT json_object_keys('{"f1":"abc","f2":{"f3":"a", "f4":"b"}}');
 json_object_keys 
------------------
 f1
 f2
(2 rows)
 
postgres=# SELECT * FROM json_array_elements('[1,true, [2,false]]');
  value 
-----------
 1
 true
 [2,false]
(3 rows)
 
postgres=# SELECT * FROM json_array_elements_text('["foo", "bar"]');
 value 
-------
 foo
 bar
(2 rows)
```
示例展示了部分 JSON 操作函数，更多可参考 [官网](http://www.postgres.cn/docs/10/functions-json.html)。
