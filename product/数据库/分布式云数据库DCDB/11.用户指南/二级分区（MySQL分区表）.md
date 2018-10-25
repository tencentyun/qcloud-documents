# DCDB二级分区（MySQL分区表）

## 概述

DCDB在使用了两级分区来实现类似于MySQL（单机版）分区表的功能，MySQL分区表主要用于均衡数据分布和访问、快速扩容、快速删除流水数据等能力，目前MySQL（单机版）分区表支持RANGE,LIST,HASH,KEY四种类型。DCDB目前已经基于二级分区的方案，支持类似于MySQL分区表RANGE分区（后续支持LIST等算法）的方案，其原理如下：

 - DCDB的第一级分区即我们常说的水平拆分（分表），目前使用HASH算法分区，目的是使得数据能均匀的分散到后端的所有物理节点

 - DCDB的第二级分区使用RANGE算法，即在水平拆分的基础上，再加上一层逻辑上的分区方法，使得相关的数据能够落在一个逻辑分区。（如下图）

## 使用方法

	目前二级分区的具体语法如下，例子中以id作为水平拆分的分表键（shardkey），hired作为二级分区的RANGE字段：

```
	CREATE TABLE employees (
	    id INT NOT NULL,
	    fname VARCHAR(30),
	    lname VARCHAR(30),
	    hired DATE NOT NULL DEFAULT '1970-01-01',
	    separated DATE NOT NULL DEFAULT '9999-12-31',
	    job_code INT,
	    store_id INT
	)
	shardkey=id 
	PARTITION BY RANGE ( YEAR(hired) ) (
	    PARTITION p0 VALUES LESS THAN (1991),
	    PARTITION p1 VALUES LESS THAN (1996),
	    PARTITION p2 VALUES LESS THAN (2001)
	);
```

注意：DCDB对有如下限制：

	Shardkey，类型必须是int,bigint,smallint/char/varchar
	二级分区字段，类型必须是DATE，DATETIME，支持的模式为RANGE，函数类型为YEAR，MONTH，DAY


