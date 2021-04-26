DCDB (MySQL 5.7 kernel) supports JSON. For more information, please see MySQL's official JSON documentation [https://dev.mysql.com/doc/refman/5.7/en/json-function-reference.html](https://dev.mysql.com/doc/refman/5.7/en/json-function-reference.html).

## Notes for JSON Used in DCDB
1. The JSON field cannot serve as shardkey (table partition key).
2. The JSON-based integration operations (such as orderby and groupby) do not support the mixed-type sorting, for example, comparison or sorting for fields of string type and int type cannot be achieved. Furthermore, only numeric fields can be sorted, but string and other types cannot be sorted.

## Comparison of JSON in DCDB and MongoDB
### Syntax for Table Creation
**DCDB**
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
     <span style="font-size:14px;">DCDB</span><br>
    </td>
   </tr>
   <tr>
    <td >
     <span style="font-size:14px;">Insert a single file</span><br>
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
     <span style="font-size:14px;">Insert multiple files</span><br>
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
     <span style="font-size:14px;">Update a single file</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.updateOne(<br>&emsp;
   { item: "paper" },<br>&emsp;
   {<br>&emsp;
     $set: { "size.uom": "cm", status: "P" },<br>&emsp;
   }<br>
)<br><br>If shardkey is not carried, an error will be reported; otherwise, it can be executed correctly.</span>
    </td>
    <td>
     <span style="font-size:14px;">update inventory set value=json_set(value, <br>
    "$.size.uom", "cm", <br>
    "$.status", "P") <br>
where value->"$.item"="paper" limit 1;<br>
<br>The statement without shardkey can be executed on multiple nodes and multiple pieces of data may be modified; while the statement with shardkey can modify data precisely.
</span><br>
    </td>
   </tr>
   <tr>  
    <td>
     <span style="font-size:14px;">Update multiple files</span><br>
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
     <span style="font-size:14px;">Replace a file</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.replaceOne(<br>
   { item: "paper" },<br>
   { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 40 } ] }
)<br>
)<br><br>If shardkey is not carried, an error will be reported; otherwise, it can be executed correctly.
</span><br>
    </td>
    <td>
     <span style="font-size:14px;">update inventory set value= '{ "item": "paper", "instock":<br> [ { "warehouse": "A", "qty": 60 }, <br>{ "warehouse": "B", "qty": 40 }]}'<br>
where value->"$.item"="paper" limit 1
)
<br><br>The statement without shardkey can be executed on multiple nodes and multiple pieces of data may be modified; while the statement with shardkey can surely be executed on the correct node and only one piece of data is modified.
</span><br>
    </td>
   </tr>
 <tr>  
    <td>
     <span style="font-size:14px;">Delete only one file meeting the conditions</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.deleteOne( { status: "A" } )
		 <br>If shardkey is not carried, an error will be reported; otherwise, it can be executed correctly.</span><br>
    </td>
    <td>
     <span style="font-size:14px;">delete from inventory where value->"$.status"="A" limit 1;<br>
The statement without shardkey can be executed on multiple nodes and multiple pieces of data may be modified; while the statement with shardkey can surely be executed on the correct node and only one piece of data is modified.
</span><br>
    </td>
		   </tr>    
	<tr>  
    <td>
     <span style="font-size:14px;">Delete all the files meeting the conditions</span><br>
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
|| MongoDB |	DCDB |
|---- |-----| ----|
| Pre-insert Data	|db.inventory.insertMany([ <br>&emsp;{ item: "canvas", qty: 100, size: { h: 28, w: 35.5, uom: "cm" }, status: "A" , tags: ["blank", "red"], dim_cm: [ 14, 21 ] , instock: [ { warehouse: "A", qty:, 5 }, { warehouse: "C", qty: 15 } ] } ,<br>&emsp;{ item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" , tags: ["red", "blank"], dim_cm: [ 14, 21 ] , instock: [ { warehouse: "C", qty: 5 } ] }, <br>&emsp;{ item: "mat", qty: 85, size: { h: 27.9, w: 35.5, uom: "cm" }, status: "D" , tags: ["red", "blank", "plain"], dim_cm: [ 14, 21 ] , instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 15 } ] },<br>&emsp;{ item: "mousepad", qty: 25, size: { h: 19, w: 22.85, uom: "cm" }, status: "P" , tags: ["blank", "red"], dim_cm: [ 22.85, 30 ] , instock: [ { warehouse: "A", qty: 40 }, { warehouse: "B", qty: 5 } ] },<br>&emsp;{ item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "P" , tags: ["blue"], dim_cm: [ 10, 15.25 ] , instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }]); |	insert into inventory(value) values<br>('{ "item": "canvas", "qty": 100, "size": { "h": 28, "w": 35.5, "uom": "cm" }, "status": "A" , "tags": ["blank", "red"], "dim_cm": [ 14, 21 ] , "instock": [ { "warehouse": "A", "qty": 5 }, { "warehouse": "C", "qty": 15 } ] }'),<br>&emsp;('{ "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" , "tags": ["red", "blank"], "dim_cm": [ 14, 21 ] , "instock": [ { "warehouse": "C", "qty": 5 } ] }'),<br>&emsp;('{ "item": "mat", "qty": 85, "size": { "h": 27.9, "w": 35.5, "uom": "cm" }, "status": "D" , "tags": ["red", "blank", "plain"], "dim_cm": [ 14, 21 ] , "instock": [ { "warehouse": "A", "qty": 60 }, { "warehouse": "B", "qty": 15 } ] }'),<br>&emsp;('{ "item": "mousepad", "qty": 25, "size": { "h": 19, "w": 22.85, "uom": "cm" }, "status": "P" , "tags": ["blank", "red"], "dim_cm": [ 22.85, 30 ] , "instock": [ { "warehouse": "A", "qty": 40 }, { "warehouse": "B", "qty": 5 } ] }'),<br>&emsp;('{ "item": "notebook", "qty": 50, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "P" , "tags": ["blue"], "dim_cm": [ 10, 15.25 ] , "instock": [ { "warehouse": "B", "qty": 15 }, { "warehouse": "C", "qty": 35 } ] }') |
| Access any member in JSON via path syntax | 	Support | 	Support |
| Query a file | db.inventory.find( { status: "D" } ) |	SELECT * FROM inventory WHERE value->"$.status" = "D";
|| db.inventory.find( { status: { $in: [ "A", "D" ] } } )	 | SELECT * FROM inventory WHERE cast(value->"$.status" as char(4)) in ('"A"', '"D"');<br><br> value->"$.status" is JSON type. MySQL does not support the IN comparison of JSON type, please pay attention to type conversion, and "A" must be quoted with the single quotation marks.
| Query embedded/nested files | db.inventory.find( { size: { h: 14, w: 21, uom: "cm" } } )<br><br>When filtering according to the matching conditions in MongoDB, the order of fields may be taken into consideration, for example, no results will be obtained for <br>db.inventory.find(  { size: { w: 21, h: 14, uom: "cm" } }  )<br>.	 | SELECT \* FROM inventory WHERE value->"$.size" = cast('{"h": 14, "w": 21, "uom": "cm"}' as json)<br><br>The order of fields will not be considered for this query in MySQL.<br>SELECT * FROM inventory WHERE value->"$.size" = cast('{"w": 21, "h": 14, "uom": "in"}' as json) <br>The same results will be filtered. |
| Query arrays | db.inventory.find( { tags: ["red", "blank"] } )<br>The order of elements in array should be taken into consideration.	 | select * from inventory where value->"$.tags"=cast('["red", "blank"]' as json);<br>The order of elements in array should be taken into consideration. |
 | Find arrays containing "red" and "blank" elements, regardless of the element order of array or other elements | 	db.inventory.find( { tags: { $all: ["red", "blank"] } } ) | select * from inventory where json_contains(value->"$.tags",cast('["red", "blank"]' as json))=1; |
| Specify multiple conditions for array elements | db.inventory.find( { dim_cm: { $gt: 15, $lt: 20 } } )<br>Select at least one element which is greater than 15, or less than 20, or greater than 15 but less than 20 from the array.	 | Do not support. |
	|| db.inventory.find( { dim_cm: { $elemMatch: { $gt: 22, $lt: 30 } } } ) Select at least one element which is greater than 22 but less than 30 from the array.	 | Do not support. |
| Query elements by the array index location | db.inventory.find( { "dim_cm.1": { $gt: 25 } } )	 | select * from inventory where value->"$.dim_cm[1]" < 25|
|Query arrays by the array length|	db.inventory.find( { "tags": { $size: 3 } } )	|select * from inventory where json_length(value->"$.tags") = 3; |
| Query arrays containing elements | db.inventory.find( { tags: "red" } )	 | select * from inventory where json_contains(value->"$.tags",cast('"red"' as json))=1; |
| Query embedded file arrays | db.inventory.find( { "instock": { warehouse: "A", qty: 5 } } )<br>The order of the fields (warehouse, qty) must be taken into consideration.<br>db.inventory.find( { "instock": { $elemMatch: { qty: 5, warehouse: "A" } } } )<br>The order of the fields (warehouse, qty) does not matter.	 | select * from inventory where json_contains(value->"$.instock", cast('{ "warehouse": "A", "qty": 5 }' as json))=1;<br>The order of the fields (warehouse, qty) does not matter. |
| Specify query conditions on the field of the file array | db.inventory.find( { 'instock.qty': { $lte: 20 } } ) | 	//Not supported (because qty is the field of the array instock, and it can only be accessed through instock[index].qty. The access method of instock.qty is not supported in MySql.) |

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
     <span style="font-size:14px;">DCDB</span><br>
    </td>
   </tr>
   <tr>
    <td >
     <span style="font-size:14px;">Single-column index</span><br>
    </td>
    <td>
     <span style="font-size:14px;">Create indexes on qty.
db.inventory.createIndex( { qty: <br>1 }
)</span><br>
    </td>
    <td>
     <span style="font-size:14px;">MySQL does not support creating indexes directly on JSON fields. Virtual columns must be created for type conversion. For example, use value->"$.qty" as the index.<br>alter table inventory add value_qty int generated always as (value->"$.qty") virtual;
create index idx on inventory(value_qty);</span><br>
    </td>
   </tr>
    <td>
     <span style="font-size:14px;">Composite indexes</span><br>
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
Hash indexes</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.createIndex( { qty: "hashed" } )</span>
    </td>
    <td>
     <span style="font-size:14px;">Innodb does not support this feature.
</span><br>
    </td>
   </tr>
   <tr>  
    <td>
     <span style="font-size:14px;">Multi-key indexes</span><br>
    </td>
    <td>
     <span style="font-size:14px;">The multi-key index will index the fields containing the array values, and MongoDB will create an index key for each element in the array.</span><br>
    </td>
    <td>
     <span style="font-size:14px;">Do not support.
</span><br>
    </td>
  </tr>  
    <td>
     <span style="font-size:14px;">Unique indexes</span><br>
    </td>
    <td>
     <span style="font-size:14px;">db.inventory.createIndex( { "_id":1, "qty": 1 }, {unique:true} )<br>Take shardkey as the prefix.
</span><br>
    </td>
		<td>
     <span style="font-size:14px;">alter table inventory add value_qty int generated always as (value->"$.qty") virtual;<br><br>create unique index idx on inventory(id, value_qty);<br>The index should include shardkey.
</span><br>
    </td>
   </tr>
 <tr>  
    <td>
     <span style="font-size:14px;">Text indexes</span><br>
    </td>
    <td>
     <span style="font-size:14px;">Insert data<br>
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
Create an index<br><br>
db.stores.createIndex( { name: "text", description: "text" } )<br><br>
Execute a query by index<br><br>
db.stores.find( { $text: { $search: "java coffee shop" } } )</span><br>
    </td>
    <td>
     <span style="font-size:14px;">DCDB does not support this feature for now. For MySQL 5.7, the text index can be performed as follows.<br><br>
Insert data<br>
create table stores(id int primary key auto_increment, value json);<br>
insert into stores(value) values('{ "name": "Java Hut", "description": "Coffee and cakes" }'),<br>
('{ "name": "Burger Buns", "description": "Gourmet hamburgers" }'),<br>
('{ "name": "Coffee Shop", "description": "Just coffee" }'),<br>
('{ "name": "Clothes Clothes Clothes", "description": "Discount clothing" }'),<br>
('{ "name": "Java Shopping", "description": "Indonesian goods" }');<br><br>
Create generated column<br><br>
alter table stores add value_name varchar(50) generated always as (value->"$.name") stored;<br><br>
alter table stores add value_description varchar(50) generated always as (value->"$.description") stored;<br><br>

create FULLTEXT index full_idx on stores(value_name, value_description);<br>
(<br>
**If generated column is stored, the performance of insert and update may be affected. For more information, please see**<br>
<a class=n href=http://mysqlserverteam.com/virtual-columns-and-effective-functional-indexes-in-innodb/>http://mysqlserverteam.com/virtual-columns-and-effective-functional-indexes-in-innodb/</a> 
<br>
)
</span><br>
   </td>
		   </tr>    
 
  </tbody>
</table>

### SHARDING

|| MongoDB | 	DCDB |
|---- |-----| ----|
| Ranged sharding	 | Support	 | Do not support
| Hashed sharding	 | db.t1.createIndex({"key1":"hashed"})<br>sh.shardCollection("test.t1", {"key1":"hashed"})<br>db.t1.insertOne({"key1":"value1","key2":"value2"}) | DCDB does not need to create a hashed index in advance.<br><br>create table t1(key1 varchar(20), value json) shardkey=key1;<br>insert into t1(key1, value) values("value1", '{"key2":"value2"}');<br><br>DCDB does not support hashed sharding according to any field in JSON. If necessary, take the field serving as shardkey out as an independent column.
| Modify a non-shard table containing data into a shard table | 	Support	 | Do not support |
Although the shard (distributed) architecture of MongoDB and DCDB is similar, their horizontal expansion and disaster recovery are different. We will not go into details about those topics herein.

### SHARD INDEX
The indexes of MongoDB and DCDB are created on shards, and only the index containing shardkey has the global unique constraint effect. No matter it is Compound Indexes containing shardkey or indexes created on the shardkey itself, shard is found based on shardkey first, and this index is used on the corresponding shard. Without shardkey, the query will be sent to all shards.

### JOIN
MongoDB only supports the left join operation of multiple tables in the non-shard table, and does not support the join operation in the shard table. The following code is the specific implementation method:
```
Insert data:
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

Left join operation:
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
Compared with MongoDB, DCDB can use JSON field to create various join conditions in the non-shard table. DCDB supports join operation in the single shard instead of multiple shard tables (for more information, please see the following codes).
```
Insert data
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

Multiple join operations can be performed on JSON field according to join syntax of MySQL.
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


## Comparison Summary
### Writing Data
Both MongoDB and DCDB can easily write JSON strings and update some fields in JSON. However, MongoDB does not support transactions, and only single-line operations can ensure the atomicity. If multiple-line operations need to ensure the atomicity, two-phase submission must be implemented at the application level. JSON operations of DCDB can completely support the transaction characteristics, and support the distributed transactions in the sharding mode.

### Querying Data
1. Join: DCDB supports the join operation of multiple tables on JSON fields, and MongoDB only supports the left join operation of multiple unsharded tables.
2. Index: Both MongoDB and DCDB support creating indexes on some fields (int, string) of JSON. And MongoDB also supports the multikey index.
3. Access internal elements of JSON: Both MongoDB and DCDB have their own complete syntax to access the various fields in JSON and do not need perform JSON parsing at the application level.
4. Searching conditions: The searching and matching features provided by MongoDB are more complete. In contrast, DCDB is not very friendly to developers. The type conversion of conditions must be performed before any judgment. In addition, due to the poorer filtering feature than MongoDB, DCDB is applicable to applications with simple JSON operations.

### Comprehensive Comparison
In general, compared with the three core features of MongoDB (JSON flexibility, high availability ensured by the replica set and scalability ensured by sharding), DCDB supports all of them as well. MongoDB supports relatively detailed JSON features. Because DCDB is created on the basis of Tencent TDSQL financial-level distributed architecture, the complete solutions regarding its highly consistent data, high availability and scalability are available. Furthermore, DCDB is featured with relational database-related transactions and join operations.

If you desire to use the JSON type and have requirements on the consistent data, transaction, join operation and other capabilities required by the traditional database, DCDB will be a good choice for you.

