
云数据库 PostgreSQL 提供 pg_roaringbitmap 插件，可以使用位图计算功能，提高查询性能。

## 前提条件
实例为云数据库 PostgreSQL 10、11、12、13 全新版本。

## 背景信息
Roaring Bitmap 算法是将32位的 INT 类型数据划分为216个数据块（Chunk），每一个数据块对应整数的高16位，并使用一个容器（Container）来存放一个数值的低16位。
Roaring Bitmap 将这些容器保存在一个动态数组中，作为一级索引。容器使用两种不同的结构：数组容器（Array Container）和位图容器（Bitmap Container）。数组容器存放稀疏的数据，位图容器存放稠密的数据。如果一个容器里面的整数数量小于4096，就用数组容器来存储值。若大于4096，就用位图容器来存储值。
采用这种存储结构，Roaring Bitmap可以快速检索一个特定的值。在做位图计算（AND、OR、XOR）时，Roaring Bitmap提供了相应的算法来高效地实现在两种容器之间的运算。使得Roaring Bitmap无论在存储和计算性能上都表现优秀。

## 操作步骤
1. 创建插件。示例如下：
```
CREATE EXTENSION roaringbitmap;
```
2. 创建带有 RoaringBitmap 数据类型的表。示例如下：
```
CREATE TABLE t1 (id integer, bitmap roaringbitmap);
```
3. 使用 rb_build 函数插入 roaringbitmap 的数据。示例如下：
```
--数组位置对应的 BIT 值为1
INSERT INTO t1 SELECT 1,RB_BUILD(ARRAY[1,2,3,4,5,6,7,8,9,200]);
--将输入的多条记录的值对应位置的 BIT 值设置为1，最后聚合为一个 roaringbitmap  
INSERT INTO t1 SELECT 2,RB_BUILD_AGG(e) FROM GENERATE_SERIES(1,100) e;
```
4. 进行 Bitmap 计算（OR、AND、XOR、ANDNOT）。示例如下：
```
--数组位置对应的 BIT 值为1
SELECT RB_OR(a.bitmap,b.bitmap) FROM (SELECT bitmap FROM t1 WHERE id = 1) AS a,(SELECT bitmap FROM t1 WHERE id = 2) AS b;
```
5. 进行 Bitmap 聚合计算（OR、AND、XOR、BUILD），并生成新的 roaringbitmap 类型。示例如下：
```
SELECT RB_OR_AGG(bitmap) FROM t1;
SELECT RB_AND_AGG(bitmap) FROM t1;
SELECT RB_XOR_AGG(bitmap) FROM t1;
SELECT RB_BUILD_AGG(e) FROM GENERATE_SERIES(1,100) e;
```
6. 统计基数（Cardinality），即统计 roaringbitmap 中包含多少个位置为1的 BIT 位。示例如下：
```
SELECT RB_CARDINALITY(bitmap) FROM t1;
```
7. 从 roaringbitmap 中返回位置为1的 BIT 下标（即位置值）。示例如下：
```
SELECT RB_ITERATE(bitmap) FROM t1 WHERE id = 1;
```

## 功能函数列表

| 函数名 | 	输入 | 输出 | 描述 | 示例 | 结果 |
|---------|---------|---------|---------|---------|---------|
| rb_build | integer[] | roaringbitmap | Create roaringbitmap from integer array | ```rb_build('{1,2,3,4,5}')``` | {1,2,3,4,5}|
| rb_index | roaringbitmap,integer | bigint | Return the 0-based index of element in this roaringbitmap, or -1 if do not exsits | ```rb_index('{1,2,3}',3)``` | 2 |
| rb_cardinality | roaringbitmap | bigint | Return cardinality of the roaringbitmap | ```rb_cardinality('{1,2,3,4,5}')``` | 5 |
| rb_and_cardinality | roaringbitmap,roaringbitmap | bigint | Return cardinality of the AND of two roaringbitmaps | ```rb_or_cardinality('{1,2,3}','{3,4,5}')``` | 1 |
| rb_xor_cardinality | roaringbitmap,roaringbitmap | bigint | Return cardinality of the XOR of two roaringbitmaps | ```rb_xor_cardinality('{1,2,3}','{3,4,5}')``` | 4 |
| rb_andnot_cardinality | roaringbitmap,roaringbitmap | bigint | Return cardinality of the ANDNOT of two roaringbitmaps | ```rb_andnot_cardinality('{1,2,3}','{3,4,5}')``` | 2 |
| rb_is_empty | roaringbitmap | boolean | Check if roaringbitmap is empty. | ```rb_is_empty('{1,2,3,4,5}')``` | t |
| rb_fill | roaringbitmap,range_start bigint,range_end bigint | roaringbitmap | Fill the specified range (not include the range_end) | ```rb_fill('{1,2,3}',5,7)``` | {1,2,3,5,6} |
| rb_clear | roaringbitmap,range_start bigint,range_end bigint | roaringbitmap | Clear the specified range (not include the range_end) | ```rb_clear('{1,2,3}',2,3)``` | {1,3} |
| rb_flip | roaringbitmap,range_start bigint,range_end bigint | roaringbitmap | Negative the specified range (not include the range_end) | ```rb_flip('{1,2,3}',2,10)``` | {1,4,5,6,7,8,9} |
| rb_range | roaringbitmap,range_start bigint,range_end bigint | roaringbitmap | Return new set with specified range (not include the range_end) | ```rb_range('{1,2,3}',2,3)``` | {2} |
| rb_range_cardinality | roaringbitmap,range_start bigint,range_end bigint | bigint | Return the cardinality of specified range (not include the range_end) | ```rb_range_cardinality('{1,2,3}',2,3)``` | 1 |
| rb_min | roaringbitmap | integer | Return the smallest offset in roaringbitmap. Return NULL if the bitmap is empty | ```rb_min('{1,2,3}')``` | 1 |
| rb_max | roaringbitmap | integer | Return the greatest offset in roaringbitmap. Return NULL if the bitmap is empty | ```rb_max('{1,2,3}')``` | 3 |
| rb_rank | roaringbitmap,integer | bigint | Return the number of elements that are smaller or equal to the specified offset | ```rb_rank('{1,2,3}',3)``` | 3 |
| rb_jaccard_dist | roaringbitmap,roaringbitmap | double precision | Return the jaccard distance(or the Jaccard similarity coefficient) of two bitmaps | ```rb_jaccard_dist('{1,2,3}','{3,4}')``` | 0.25 |
| rb_select | roaringbitmap,bitset_limit bigint,bitset_offset bigint=0,reverse boolean=false,range_start bigint=0,range_end bigint=4294967296 | roaringbitmap | Return subset [bitset_offset,bitset_offset+bitset_limit) of bitmap between range [range_start,range_end) | ```rb_select('{1,2,3,4,5,6,7,8,9}',5,2)``` | {3,4,5,6,7} |
| rb_to_array | roaringbitmap | integer[] | Convert roaringbitmap to integer array | ```rb_to_array(roaringbitmap('{1,2,3}'))``` | {1,2,3} |
| rb_iterate | roaringbitmap | SET of integer | Return set of integer from a roaringbitmap data. | ```SELECT rb_iterate(rb_build('{1,2,3}'))``` | 1<br>2<br>3 |

## 聚合函数列表
| 聚合函数名 | 	输入 | 输出 | 描述 | 示例 | 结果 |
|---------|---------|---------|---------|---------|---------|
| rb_build_agg | 	integer | 	roaringbitmap | Build a roaringbitmap from a integer set | ```select rb_build_agg(id)
    from (values (1),(2),(3)) t(id)``` | {1,2,3} |
| rb_or_agg | roaringbitmap | roaringbitmap | 	AND Aggregate calculations from a roaringbitmap set | ```select rb_or_agg(bitmap) 
    from (values (roaringbitmap('{1,2,3}')),
                 (roaringbitmap('{2,3,4}'))
          ) t(bitmap)``` | {1,2,3,4} |
| rb_and_agg | roaringbitmap | roaringbitmap | 	AND Aggregate calculations from a roaringbitmap set | ```select rb_and_agg(bitmap) 
    from (values (roaringbitmap('{1,2,3}')),
                 (roaringbitmap('{2,3,4}'))
          ) t(bitmap)``` | {2,3} |
| rb_xor_agg | roaringbitmap | roaringbitmap | XOR Aggregate calculations from a roaringbitmap set | ```select rb_xor_agg(bitmap) 
    from (values (roaringbitmap('{1,2,3}')),
                 (roaringbitmap('{2,3,4}'))
          ) t(bitmap)``` | {1,4} |
| rb_or_cardinality_agg | roaringbitmap | bigint | 	OR Aggregate calculations from a roaringbitmap set, return cardinality. | ```select rb_or_cardinality_agg(bitmap) 
    from (values (roaringbitmap('{1,2,3}')),
                 (roaringbitmap('{2,3,4}'))
          ) t(bitmap)``` | 4 |
| rb_and_cardinality_agg | roaringbitmap | bigint | AND Aggregate calculations from a roaringbitmap set, return cardinality | ```select rb_and_cardinality_agg(bitmap) 
    from (values (roaringbitmap('{1,2,3}')),
                 (roaringbitmap('{2,3,4}'))
          ) t(bitmap)``` | 2 |
| rb_xor_cardinality_agg | roaringbitmap | bigint | XOR Aggregate calculations from a roaringbitmap set, return cardinality | ```select rb_xor_cardinality_agg(bitmap) 
    from (values (roaringbitmap('{1,2,3}')),
                 (roaringbitmap('{2,3,4}'))
          ) t(bitmap)``` | 2 |


