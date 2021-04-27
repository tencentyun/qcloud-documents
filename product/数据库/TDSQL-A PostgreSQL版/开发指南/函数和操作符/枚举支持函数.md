枚举类型支持如下函数：

| **函数**                     | **描述**                                                     |
| ---------------------------- | ------------------------------------------------------------ |
| enum_first(anyenum)          | 返回输入枚举类型的第一个值                                   |
| enum_last(anyenum)           | 返回输入枚举类型的最后一个值                                 |
| enum_range(anyenum)          | 将输入枚举类型的所有值作为一个有序的数组返回                 |
| enum_range(anyenum, anyenum) | 以一个数组返回在给定两个枚举值之间的范围，值必须来自相同的枚举类型。如果第一个参数为空，其结果将从枚举类型的第一个值开始；如果第二参数为空，其结果将以枚举类型的最后一个值结束 |

示例：
```
postgres=# CREATE TYPE rainbow AS ENUM ('red', 'orange', 'yellow', 'green', 'blue', 'purple');
CREATE TYPE
postgres=# SELECT enum_first(null::rainbow);
enum_first
------------
 red
(1 row)
 
postgres=# SELECT enum_last(null::rainbow);
 enum_last 
-----------
 purple
(1 row)

postgres=# SELECT enum_range(null::rainbow);
       enum_range        
---------------------------------------
 {red,orange,yellow,green,blue,purple}
(1 row)
 
postgres=# SELECT enum_range('orange'::rainbow, 'green'::rainbow);
   enum_range    
-----------------------
 {orange,yellow,green}
(1 row)

postgres=# SELECT enum_range(NULL, 'green'::rainbow);
    enum_range     
---------------------------
 {red,orange,yellow,green}
(1 row)
 
postgres=# SELECT enum_range('orange'::rainbow, NULL);
      enum_range       
-----------------------------------
 {orange,yellow,green,blue,purple}
(1 row)
```
