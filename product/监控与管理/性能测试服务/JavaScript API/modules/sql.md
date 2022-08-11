
### Interfaces（接口）
- [Result](https://cloud.tencent.com/document/product/1484/77618)



## Variables
[](id:default)
### Const default
default: { Database: (new (driverName: string, dataSourceName: string) => { exec: any; query: any }); MySQL: "mysql"}

#### Type declaration
- ##### Database: (new (driverName: *string*, dataSourceName: *string*) => { exec: *any*; query: *any* })
 - new (driverName: *string*, dataSourceName: *string*): { exec: *any*; query: *any* }
  - Database 新建数据库实例。

  #### Parameters
 - ##### driverName: *string*
     驱动名，支持 mysql。
 - ##### dataSourceName: *string*
     数据源。

 #### Returns { exec: *any*; query: *any* }
- ##### exec:function
 - exec(query: *string*, ...args: *any*[]): [Result](https://cloud.tencent.com/document/product/1484/77618)
执行查询而不返回任何行。
  ```js
          import sql from 'pts/sql';
          
          const db = new sql.Database("mysql", "user:passwd@tcp(ip:port)/database")
          
          export default function () {
              let result = db.exec("UPDATE user SET age=? WHERE name='zhangsan'", Math.floor(Math.random() * 100));
              console.log(JSON.stringify(result)); // {"lastInsertId":0,"rowsAffected":1}
} 
```			
   #### Parameters
   - ##### query: *string*
查询语句。
   - ##### Rest ...args: *any*[]
用于查询中的占位符参数。
   - #### Returns [Result](https://cloud.tencent.com/document/product/1484/77618)
查询结果。

- #### query:function
 - query(query: *string*, ...args: *any*[]): *Record*<*string*, *any*>[]
执行返回行的查询，通常是 SELECT。
```js
       import sql from 'pts/sql';
          
       const db = new sql.Database("mysql", "user:passwd@tcp(ip:port)/database")
          
       export default function () {
        let rows = db.query("SELECT * FROM user");
         console.log(JSON.stringify(rows)); // [{"id":1,"name":"zhangsan","age":23},{"id":2,"name":"lisi","age":2}]
          }
     ```
#### Parameters
 - ##### query: *string*
查询语句。
 - ##### Rest ...args: *any*[]
用于查询中的占位符参数。

 - #### Returns *Record*<*string*, *any*>[]
查询结果。
- ##### MySQL: *"mysql"*
  MySQL 数据库。
