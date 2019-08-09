目前，TDSQL（MySQL 5.7内核）已支持 json 能力，更多细节，可以参考 mysql 官方的 json 文档 [https://dev.mysql.com/doc/refman/5.7/en/json-function-reference.html]( https://dev.mysql.com/doc/refman/5.7/en/json-function-reference.html)

## TDSQL 使用 JSON 注意事项
1. json 字段不可以作为 shardkey（分表键）；
2. json 类型的聚合操作( 如 orderby，groupby )不支持混合类型排序，例如，不能将 string 类型和 int 类型做比较或排序。且排序只支持数值类型，string 等类型排序不支持。

## TDSQL 与 MongoDB 的 JSON 能力对比
### 建表语法
**TDSQL**
```
Create table inventory(id int primary key auto_increment, value json) shardkey=id;
```
**MongoDB**
```
sh.shardCollection("test.inventory", {"_id":"hashed"})
```
### **INSERT/UPDATE/DELETE Document**
<table>
  <tbody>
   <tr>
    <td>
     <span style="font-size:14px;"></span><br>
    </td>
    <td>
     <span style="font-size:14px;">MongoDB</span><br>
    </td>
    <td>
     <span style="font-size:14px;">TDSQL</span><br>
    </td>
   </tr>
   <tr>
    <td >
     <span style="font-size:14px;">插入单个文件</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.insertOne(<br>
  &emsp; { item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }<br>
)</span><br>
    </td>
    <td>
     <span style="font-size:14px;">Insert into inventory(value) values(<br>
 &emsp; '{ "item": "canvas", "qty": 100, "tags": ["cotton"], "size": { "h": 28, "w": 35.5, "uom": "cm" } }'<br>
);</span><br>
    </td>
   </tr>
    <td>
     <span style="font-size:14px;">插入多个文件</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.insertMany([<br>&emsp;
   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },<br>&emsp;
   { item: "mat", qty: 35, size: { h: 27.9, w: 35.5, uom: "cm" }, status: "A" },<br>&emsp;
   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" }<br>
]);<br></span><br>
    </td>
    <td>
     <span style="font-size:14px;">insert into inventory(value) values<br>&emsp;
   ('{ "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A"  }'),<br>&emsp;
   ('{ "item": "mat", "qty": 35, "size": { "h": 27.9, "w": 35.5, "uom": "cm" }, "status": "A" }'),<br>&emsp;
   ('{ "item": "paper", "qty": 100, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "D" }') </span><br>
    </td>
   </tr>
   <tr>
      <td>
     <span style="font-size:14px;">更新单个文件</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.updateOne(<br>&emsp;
   { item: "paper" },<br>&emsp;
   {<br>&emsp;
     $set: { "size.uom": "cm", status: "P" },<br>&emsp;
   }<br>
)<br><br>不携带shardkey报错，携带shardkey可以正确执行</span>
    </td>
    <td>
     <span style="font-size:14px;">update inventory set value=json_set(value, <br>
    "$.size.uom", "cm", <br>
    "$.status", "P") <br>
where value->"$.item"="paper" limit 1;<br>
<br>不携带 shardkey 的语句会在多个节点上执行，语法结构可能会修改多条数据，而携带 shardkey 可以确保正确只修改 1 条数据执行
</span><br>
    </td>
   </tr>
   <tr>  
    <td>
     <span style="font-size:14px;">更新多个文件</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.updateMany(<br>
   { "qty": { $lt: 50 } },<br>
   {<br>
     $set: { "size.uom": "in", status: "P" },<br>
   }
)</span><br>
    </td>
    <td>
     <span style="font-size:14px;">update inventory set value=json_set(value, <br>
    "$.size.uom", "in", <br>
    "$.status", "P") <br>
where value->"$.qty"<50 ;
</span><br>
    </td>
		   </tr>  
    <td>
     <span style="font-size:14px;">替换文件</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.replaceOne(<br>
   { item: "paper" },<br>
   { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 40 } ] }
)<br>
)<br><br>不携带 shardkey 报错，携带 shardkey 可以正确执行
</span><br>
    </td>
    <td>
     <span style="font-size:14px;">update inventory set value= '{ "item": "paper", "instock":<br> [ { "warehouse": "A", "qty": 60 }, <br>{ "warehouse": "B", "qty": 40 }]}'<br>
where value->"$.item"="paper" limit 1
)
<br><br>不携带 shardkey 的语句会在多个节点上执行，语法结构可能会修改多条数据，而携带 shardkey 可以确保正确只修改 1 条数据执行
</span><br>
    </td>
   </tr>
 <tr>  
    <td>
     <span style="font-size:14px;">只删除一个符合条件的文件</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.deleteOne( { status: "A" } )
		 <br>不携带 shardkey 报错，携带 shardkey 可以正确执行</span><br>
    </td>
    <td>
     <span style="font-size:14px;">delete from inventory where value->"$.status"="A" limit 1;<br>
不携带 shardkey 的语句会在多个节点上执行，语法结构可能会修改多条数据，而携带 shardkey 可以确保正确只修改 1 条数据执行
</span><br>
    </td>
		   </tr>    
	<tr>  
    <td>
     <span style="font-size:14px;">删除所有符合条件的文档</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.deleteMany({ status : "A" })
)</span><br>
    </td>
    <td>
     <span style="font-size:14px;">delete from inventory where value->"$.status"="A";
</span><br>
    </td>
		   </tr>  
  </tbody>
</table>

### QUERY Document
||MongoDB|	TDSQL|
|---- |-----| ----|
|预先插入数据	|db.inventory.insertMany([ <br>&emsp;{ item: "canvas", qty: 100, size: { h: 28, w: 35.5, uom: "cm" }, status: "A" , tags: ["blank", "red"], dim_cm: [ 14, 21 ] , instock: [ { warehouse: "A", qty:, 5 }, { warehouse: "C", qty: 15 } ] } ,<br>&emsp;{ item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" , tags: ["red", "blank"], dim_cm: [ 14, 21 ] , instock: [ { warehouse: "C", qty: 5 } ] }, <br>&emsp;{ item: "mat", qty: 85, size: { h: 27.9, w: 35.5, uom: "cm" }, status: "D" , tags: ["red", "blank", "plain"], dim_cm: [ 14, 21 ] , instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 15 } ] },<br>&emsp;{ item: "mousepad", qty: 25, size: { h: 19, w: 22.85, uom: "cm" }, status: "P" , tags: ["blank", "red"], dim_cm: [ 22.85, 30 ] , instock: [ { warehouse: "A", qty: 40 }, { warehouse: "B", qty: 5 } ] },<br>&emsp;{ item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "P" , tags: ["blue"], dim_cm: [ 10, 15.25 ] , instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }]); |	insert into inventory(value) values<br>('{ "item": "canvas", "qty": 100, "size": { "h": 28, "w": 35.5, "uom": "cm" }, "status": "A" , "tags": ["blank", "red"], "dim_cm": [ 14, 21 ] , "instock": [ { "warehouse": "A", "qty": 5 }, { "warehouse": "C", "qty": 15 } ] }'),<br>&emsp;('{ "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" , "tags": ["red", "blank"], "dim_cm": [ 14, 21 ] , "instock": [ { "warehouse": "C", "qty": 5 } ] }'),<br>&emsp;('{ "item": "mat", "qty": 85, "size": { "h": 27.9, "w": 35.5, "uom": "cm" }, "status": "D" , "tags": ["red", "blank", "plain"], "dim_cm": [ 14, 21 ] , "instock": [ { "warehouse": "A", "qty": 60 }, { "warehouse": "B", "qty": 15 } ] }'),<br>&emsp;('{ "item": "mousepad", "qty": 25, "size": { "h": 19, "w": 22.85, "uom": "cm" }, "status": "P" , "tags": ["blank", "red"], "dim_cm": [ 22.85, 30 ] , "instock": [ { "warehouse": "A", "qty": 40 }, { "warehouse": "B", "qty": 5 } ] }'),<br>&emsp;('{ "item": "notebook", "qty": 50, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "P" , "tags": ["blue"], "dim_cm": [ 10, 15.25 ] , "instock": [ { "warehouse": "B", "qty": 15 }, { "warehouse": "C", "qty": 35 } ] }') |
|通过路径语法实现对json内任意成员的访问|	支持	|支持|
|查询文件|db.inventory.find( { status: "D" } )|	SELECT * FROM inventory WHERE value->"$.status" = "D";
||db.inventory.find( { status: { $in: [ "A", "D" ] } } )	|SELECT * FROM inventory WHERE cast(value->"$.status" as char(4)) in ('"A"', '"D"');<br><br> value->"$.status"是json类型，mysql对于json类型目前不支持in比较操作，需要注意类型转换，并且"A"一定要用单引号引起来
|查询嵌入式/嵌套文档|db.inventory.find( { size: { h: 14, w: 21, uom: "cm" } } )<br><br>MongoDB在筛选匹配条件的时候也会考虑字段的顺序，例如<br>db.inventory.find(  { size: { w: 21, h: 14, uom: "cm" } }  )<br>将不会查询到任何结果	|SELECT \* FROM inventory WHERE value->"$.size" = cast('{"h": 14, "w": 21, "uom": "cm"}' as json)<br><br>Mysql这种查找方式不会考虑字段顺序<br>SELECT * FROM inventory WHERE value->"$.size" = cast('{"w": 21, "h": 14, "uom": "in"}' as json) <br>将会筛选出同样的结果|
|查询数组 | db.inventory.find( { tags: ["red", "blank"] } )<br>需要考虑数组中的顺序	|select * from inventory where value->"$.tags"=cast('["red", "blank"]' as json);<br>需要考虑数组中的顺序|
 |查找包含“红色”和“空白”元素的数组，而不考虑数组中的顺序或其他元素|	db.inventory.find( { tags: { $all: ["red", "blank"] } } )|select * from inventory where json_contains(value->"$.tags",cast('["red", "blank"]' as json))=1;|
|为数组元素指定多个条件 | db.inventory.find( { dim_cm: { $gt: 15, $lt: 20 } } )<br>选出数组中至少有一个元素满足大于15或者小于20或同时满足	|不支持|
	||db.inventory.find( { dim_cm: { $elemMatch: { $gt: 22, $lt: 30 } } } )选出数组中至少有一个元素同时满足大于22和小于30	|不支持|
|按数组索引位置查询元素|db.inventory.find( { "dim_cm.1": { $gt: 25 } } )	|select * from inventory where value->"$.dim_cm[1]" < 25|
|按数组长度查询数组|	db.inventory.find( { "tags": { $size: 3 } } )	|select * from inventory where json_length(value->"$.tags") = 3;|
|查询元素的数组|db.inventory.find( { tags: "red" } )	|select * from inventory where json_contains(value->"$.tags",cast('"red"' as json))=1;|
|查询嵌入式文档数组|db.inventory.find( { "instock": { warehouse: "A", qty: 5 } } )<br>需要考虑字段(warehouse, qty)的顺序<br>db.inventory.find( { "instock": { $elemMatch: { qty: 5, warehouse: "A" } } } )<br>不需要考虑字段(warehouse, qty)的顺序	|select * from inventory where json_contains(value->"$.instock", cast('{ "warehouse": "A", "qty": 5 }' as json))=1;<br>不需要考虑字段(warehouse, qty)的顺序|
|在嵌入文档数组的字段中指定查询条件|db.inventory.find( { 'instock.qty': { $lte: 20 } } )|	//不支持（qty 是数组 instock内的 field， 只能通过 instock[index].qty 访问，instock.qty 这种访问方式mysql均不支持）|

### INDEXES
<table>
  <tbody>
   <tr>
    <td>
     <span style="font-size:14px;"></span><br>
    </td>
    <td>
     <span style="font-size:14px;">MongoDB</span><br>
    </td>
    <td>
     <span style="font-size:14px;">TDSQL</span><br>
    </td>
   </tr>
   <tr>
    <td >
     <span style="font-size:14px;">单场索引</span><br>
    </td>
    <td>
     <span style="font-size:14px;">对qty建立索引
db.inventory.createIndex( { qty: <br>1 }
)</span><br>
    </td>
    <td>
     <span style="font-size:14px;">Mysql不支持直接针对json字段创建index，需要先创建虚拟列并进行类型转换，如将value->"$.qty"作为索引<br>alter table inventory add value_qty int generated always as (value->"$.qty") virtual;
create index idx on inventory(value_qty);</span><br>
    </td>
   </tr>
    <td>
     <span style="font-size:14px;">复合索引</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.createIndex( { "item": 1, "qty": 1 } )<br></span><br>
    </td>
    <td>
     <span style="font-size:14px;">alter table inventory add value_item varchar(50) generated always as (value->"$.item") virtual;<br><br>alter table inventory add value_qty int generated always as (value->"$.qty") virtual;<br><br>create index idx_1 on inventory(value_item, value_qty);
</span><br>
    </td>
   <tr>
    <td>
     <span style="font-size:14px;">
哈希索引</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.createIndex( { qty: "hashed" } )</span>
    </td>
    <td>
     <span style="font-size:14px;">Innodb不支持
</span><br>
    </td>
   </tr>
   <tr>  
    <td>
     <span style="font-size:14px;">多键索引</span><br>
    </td>
    <td>
     <span style="font-size:14px;">多键索引要索引包含数组值的字段，MongoDB 会为数组中的每个元素创建一个索引键</span><br>
    </td>
    <td>
     <span style="font-size:14px;">不支持
</span><br>
    </td>
  </tr>  
    <td>
     <span style="font-size:14px;">唯一索引</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.createIndex( { "_id":1, "qty": 1 }, {unique:true} )<br>需要shardkey做前缀
</span><br>
    </td>
		<td>
     <span style="font-size:14px;">alter table inventory add value_qty int generated always as (value->"$.qty") virtual;<br><br>create unique index idx on inventory(id, value_qty);<br>索引中需要包含shardkey
</span><br>
    </td>
   </tr>
 <tr>  
    <td>
     <span style="font-size:14px;">文本索引</span><br>
    </td>
    <td>
     <span style="font-size:14px;">插入数据<br>
sh.shardCollection("test.stores", {"_id":"hashed"}}<br><br>
db.stores.insertMany(<br>
   [<br>
     { _id: 1, name: "Java Hut", description: "Coffee and cakes" },<br>
     { _id: 2, name: "Burger Buns", description: "Gourmet hamburgers" },<br>
     { _id: 3, name: "Coffee Shop", description: "Just coffee" },<br>
     { _id: 4, name: "Clothes Clothes Clothes", description: "Discount clothing" },<br>
     { _id: 5, name: "Java Shopping", description: "Indonesian goods" }<br>
   ]
)
<br><br>
创建索引<br><br>
db.stores.createIndex( { name: "text", description: "text" } )<br><br>
根据索引查找<br><br>
db.stores.find( { $text: { $search: "java coffee shop" } } )</span><br>
    </td>
    <td>
     <span style="font-size:14px;">TDSQL暂时不支持，mysql5.7可以按照如下方法进行<br><br>
插入数据<br>
create table stores(id int primary key auto_increment, value json);<br>
insert into stores(value) values('{ "name": "Java Hut", "description": "Coffee and cakes" }'),<br>
('{ "name": "Burger Buns", "description": "Gourmet hamburgers" }'),<br>
('{ "name": "Coffee Shop", "description": "Just coffee" }'),<br>
('{ "name": "Clothes Clothes Clothes", "description": "Discount clothing" }'),<br>
('{ "name": "Java Shopping", "description": "Indonesian goods" }');<br><br>
创建generated column<br><br>
alter table stores add value_name varchar(50) generated always as (value->"$.name") stored;<br><br>
alter table stores add value_description varchar(50) generated always as (value->"$.description") stored;<br><br>

create FULLTEXT index full_idx on stores(value_name, value_description);<br>
(<br>
**generated column 为stored会影响insert，update性能，详见** <br>
<a class=n href=http://mysqlserverteam.com/virtual-columns-and-effective-functional-indexes-in-innodb/>http://mysqlserverteam.com/virtual-columns-and-effective-functional-indexes-in-innodb/</a> 
<br>
)
</span><br>
   </td>
		   </tr>    
 
  </tbody>
</table>

### SHARDING

||MongoDB|	TDSQL|
|---- |-----| ----|
|Ranged sharding	|支持	|不支持
|Hashed sharding	|db.t1.createIndex({"key1":"hashed"})<br>sh.shardCollection("test.t1", {"key1":"hashed"})<br>db.t1.insertOne({"key1":"value1","key2":"value2"})|TDSQL不需要事先创建hashed index<br><br>create table t1(key1 varchar(20), value json) shardkey=key1;<br>insert into t1(key1, value) values("value1", '{"key2":"value2"}');<br><br>TDSQL目前不支持按照json内的任意字段进行hashed sharding，如有需要，需要将作为shardkey的字段单独提出作为一列。
|将含有数据的非shard表修改为shard表|	支持	|不支持|
MongoDB和TDSQL的shard（分布式）架构相似，因此在水平扩容、容灾等方面各有千秋，此处不做展开。

### SHARD INDEX
MongoDB 和 TDSQL 的 index 都是建立在各个 shard 上的，并且只有包含 shardkey 的 index 才可以有全局 unique 的约束条件。无论是包含  shardkey 的 Compound Indexes 还是将对 shardkey 本身建立 index，两者都是先通过 shardkey 确定相关 shard，再在相关的各个  shard 上利用该索引，在没有 shardkey 的情况下，查询会发送到所有的 shard。

### JOIN
MongoDB 在非 shard 表下只能支持多表 left join，而在 shard 表下不支持 join；具体实现方法如下代码所示
```
插入数据：
db.users.insertMany([{
		"email" : "admin@gmail.com",
		"userId" : "AD",
		"userName" : "admin"
	},
	
	{ 
		"email" : "admin1@gmail.com",
		"userId" : "AD",
		"userName" : "admin1"
	}
]);

db.userinfo.insertMany([{
		"userId" : "AD",
		"phone" : "0000000000"
	},
	{
		"userId" : "AD",
		"phone" : "0000000000"
	}
]);

db.userrole.insertMany([{
		"userId" : "AD",
		"role": "admin"
	},
	{
		"userId" : "AC",
		"role" : "admin"
	}
]);

左连接操作：
db.users.aggregate([{
// Join with user_info table
		lookup:{
					from: "userinfo", // other tablename
					localField: "userId", // name of users table field
					foreignField: "userId", // name of userinfo table field
					as: "user_info" // alias for userinfo table
				}
	},
		{ $unwind:"$user_info" },
		// $unwind used for getting data in object or for one record only
		
		// Join with user_role table
	{
		$lookup:{
					from: "userrole", 
					localField: "userId", 
					foreignField: "userId",
					as: "user_role"
					
		{ $unwind:"$user_role" },
		
		// define some conditions here 
	{
		$match:{$and:[{"userName" : "admin"}]}
	},
	
	// define which fields are you want to fetch
	{
		$project:
					_id : 1,
					email : 1,
					userName : 1,
					userPhone : "$user_info.phone",
					role : "$user_role.role",
	} 
}
]);

```
相对 MongoDB，而 TDSQL 在非 shard 表下可以运用 json 的字段做各种条件 join，当在单个 shard 表下 TDSQL 允许 Join 操作，但是不支持在多个 shard 表。（详细操作见见下面代码）
```
插入数据
create table users(id int primary key auto_increment, value json);
create table userinfo(id int primary key auto_increment, value json);
create table userrole(id int primary key auto_increment, value json);

insert into users(value) values('{ 
									"email" : "admin@gmail.com",
									"userId" : "AD",
									"userName" : "admin"}'),
								('{
									"email" : "admin1@gmail.com",
									"userId" : "AD",
									"userName" : "admin1"}');
									
insert into userinfo(value) values('{
										"userId" : "AD",
										"phone" : "0000000000"}'),
								('{
										"userId" : "AD",
										"phone" : "0000000000"}');
										
insert into userrole(value) values('{
										"userId" : "AD",
										"role" : "admin"}'),
								('{
										"userId" : "AC",
										"role" : "admin"}');

可以按照mysql的join语法根据json字段进行多种join操作
select * from users left join userinfo on users.value
					->"$.userId" = userinfo.value
					->"$.userId" left join userrole on users.value
					->"$.userId" = userrole.value
					->"$.userId" where users.value
					->"$.userName"="admin";

select * from users left join userinfo on users.value
					->"$.userId" = userinfo.value
					->"$.userId" right join userrole on users.value
					->"$.userId" = userrole.value
					->"$.userId" where userrole.value
					->"$.role"="admin";
```


## 对比总结
### 写入数据
两者都可以以方便的写入 json 串和更新 json 内部的某些字段，但 MongoDB 不支持事务，只有单行操作可保证原子性，多行操作如果需要原子性需要应用层实现两阶段提交。而 TDSQL 的 json 操作可以完整的支持事务特性，sharding 模式下也支持分布式事务。

### 查询数据
1. Join： TDSQL 支持多表根据 json 字段进行 join 操作，MongoDB 只支持多个 unsharded 表 left join
2. Index：两者都支持根据 json 的某些（int,string）字段建立索引，MongoDB 还额外支持 multikey index 等索引
3. 访问j son 内部元素：两者都有各自完善的语法可以访问到json内部的各个字段，无需应用层进行json解析
4. 搜索条件：MongoDB 提供的搜索和匹配方面的功能更完善，相比之下，TDSQL 需要时刻注意对选择条件进行类型转换后再进行判断，对开发人员来说不是很友好，并且筛选的功能方面也较 MongoDB 稍弱，适用于对json操作相对简单的应用。

### 综合对比
综合来看，对比于 MongoDB 目前的三大核心功能：json 的灵活性，复制集保证高可用，sharding 保证可扩展，TDSQL 均可以支持。而在 json 细节的支持，MongoDB 提供的功能更加丰富一些。但是，TDSQL 是基于腾讯 TDSQL 金融级分布式架构的，其自身数据强一致、高可用和可扩展也有着完善的解决方案，且能够关系型数据库的事务，join等功能。

如果您既希望使用json类型，又对数据一致性，事务，join 等传统数据库具备的能力也有一定要求的话，TDSQL 将是一个很好的选择。
