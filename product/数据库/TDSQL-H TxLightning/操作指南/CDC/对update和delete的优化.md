## 对update和delete的优化

- 众所周知，ClickHouse的实时update和delete性能较弱。因此CDC为每个表新增字段\_sign和\_version，使用insert代替update和delete。

- 查询时，需带上条件_sign=1

- 具体转换逻辑如下：
  - 新增字段含义
    - _version是单调递增的版本数据。下文以初始值1举例。
    - \_sign=1代表有效数据，\_sign=-1为删除的数据。
  - INSERT
    - 插入新的一行数据
    - 其他数据不变，\_sign=1, \_version=1
  - DELETE
    - 插入新的一行数据 
    - 其他数据不变，\_sign=-1，\_version=\_version+1
  - UPDATE
    - 对于修改的列中，不包含排序键的情况
      - 插入新的一行数据
      - 使用后镜像，\_sign=1, \_version=\_version+1
    - 对于修改的列中，包含了排序键的情况
      - 插入两行数据
      - 第一行，使用前镜像，\_sign=-1, \_version=\_version+1
      - 第二行，使用新镜像，\_sign=1, \_version=\_version+1

  

