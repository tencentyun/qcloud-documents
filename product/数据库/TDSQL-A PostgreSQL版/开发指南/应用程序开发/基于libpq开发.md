libpq 是应用程序员使用 TDSQL-A PostgreSQL版 的 C 接口。libpq 是一个库函数的集合，它们允许客户端程序传递查询给TDSQL-A PostgreSQL版 后端服务器并且接收这些查询的结果。

libpq 也是很多其他 TDSQL-A PostgreSQL版 应用接口的底层引擎，包括为 C++、Perl、Python、Tcl 和 ECPG 编写的接口。

使用 libpq 的客户端程序必须包括头文件 libpq-fe.h，并必须与 libpq 库连接在一起。

## 示例代码
### 示例：进行数据库连接
1. 创建 conn_test.cpp 文件。
```
#include <stdio.h>
#include <stdlib.h>
#include "libpq-fe.h"  
int
main(int argc, char **argv){
  const char *conninfo;
  PGconn   *conn;   
  if (argc > 1){
    conninfo = argv[1];
  }else{
    conninfo = "dbname = postgres"; 
  }      
  conn = PQconnectdb(conninfo);
  if (PQstatus(conn) != CONNECTION_OK){
    fprintf(stderr, "连接数据库失败: %s",PQerrorMessage(conn));       
  }else{
    printf("连接数据库成功！\n");
  }
  PQfinish(conn);
  return 0;
}
```
2. 进行编译。
```
gcc -c -I ~/user_1/tdata_02/tbase_v3_1/3.0.16/install/tbase_pgxz/include conn_test.cpp
```
3. 连接成可执行文件。
```
gcc -o conn conn_test.o -L ~/user_1/tdata_02/tbase_v3_1/3.0.16/install/tbase_pgxz/lib/ -lpq
```
4. 进行数据库连接测试。
```
./conn "host=localhost dbname=postgres port=11345"
```
连接数据库成功！

### 示例：创建表
1. 创建文件 createtable.c。
```
#include <stdio.h>
#include <stdlib.h>
#include "libpq-fe.h"  
int
main(int argc, char **argv){
  const char *conninfo;
  PGconn   *conn;   
  PGresult  *res;
  const char *sql = "create table tdapg(id int,nickname text) ";
  if (argc > 1){
    conninfo = argv[1];
  }else{
    conninfo = "dbname = postgres";      
  }    
  conn = PQconnectdb(conninfo);
  if (PQstatus(conn) != CONNECTION_OK){
    fprintf(stderr, "连接数据库失败: %s",PQerrorMessage(conn));       
  }else{
    printf("连接数据库成功！\n");
  }
  res = PQexec(conn,sql);
  if(PQresultStatus(res) != PGRES_COMMAND_OK){
    fprintf(stderr, "建立数据表失败: %s",PQresultErrorMessage(res)); 
  }else{
    printf("建立数据表成功！\n");
  }
  PQclear(res);
  PQfinish(conn);
  return 0;
}
```
2. 进行编译。
```
gcc -c -I ~/user_1/tdata_02/tbase_v3_1/3.0.16/install/tbase_pgxz/include createtable .cpp
```
3. 连接成可执行文件。
```
gcc -o createtable createtable.o -L ~/user_1/tdata_02/tbase_v3_1/3.0.16/install/tbase_pgxz/lib/ -lpq
```
4. 进行数据库连接测试。
```
./createtable "host=localhost dbname=postgres port=11345"
```
![](https://main.qcloudimg.com/raw/bb0cb159049e78d02dded8f3b8803007.png)
 
### 示例：数据插入
1. 创建文件 insert.c。
```
#include <stdio.h>
#include <stdlib.h>
#include "libpq-fe.h"  
int
main(int argc, char **argv){
  const char *conninfo;
  PGconn   *conn;   
  PGresult  *res;
  const char *sql = "INSERT INTO tdapg (id,nickname) values(1,'tdapg'),(2,'pgxz')";
  if (argc > 1){
    conninfo = argv[1];
  }else{
    conninfo = "dbname = postgres";      
  }    
  conn = PQconnectdb(conninfo);
  if (PQstatus(conn) != CONNECTION_OK){
    fprintf(stderr, "连接数据库失败: %s",PQerrorMessage(conn));       
  }else{
    printf("连接数据库成功！\n");
  }
  res = PQexec(conn,sql);
  if(PQresultStatus(res) != PGRES_COMMAND_OK){
    fprintf(stderr, "插入数据失败: %s",PQresultErrorMessage(res)); 
  }else{
    printf("插入数据成功！\n");
  }
  PQclear(res);
  PQfinish(conn);
  return 0;
}
```
2. 进行编译。
```
gcc -c -I ~/user_1/tdata_02/tbase_v3_1/3.0.16/install/tbase_pgxz/include insert.cpp
```
3. 连接成可执行文件。
```
gcc -o insert insert.o -L ~/user_1/tdata_02/tbase_v3_1/3.0.16/install/tbase_pgxz/lib/ -lpq
```
4. 进行数据库连接测试。
```
./insert "host=localhost dbname=postgres port=11345"
```
![](https://main.qcloudimg.com/raw/4e80c5f4712cb438933d6ac6b587927c.png)
 
### 示例：进行数据查询
1. 创建文件 select.c。
```
#include <stdlib.h>
#include "libpq-fe.h"
int
main(int argc, char **argv){
  const char *conninfo;
  PGconn   *conn;
  PGresult  *res;
  const char *sql = "select * from tdapg";
  if (argc > 1){
    conninfo = argv[1];
  }else{
    conninfo = "dbname = postgres";
  }
  conn = PQconnectdb(conninfo);
  if (PQstatus(conn) != CONNECTION_OK){
    fprintf(stderr, "连接数据库失败: %s",PQerrorMessage(conn));
   }else{
    printf("连接数据库成功！\n");
  }
  res = PQexec(conn,sql);
  if(PQresultStatus(res) != PGRES_TUPLES_OK){
    fprintf(stderr, "插入数据失败: %s",PQresultErrorMessage(res));
  }else{
    printf("查询数据成功！\n");
    int rownum = PQntuples(res) ;
    int colnum = PQnfields(res);
    for(int j = 0;j< colnum; ++j){
      printf("%s\t",PQfname(res,j));
    }
    printf("\n");
    for(int i = 0;i< rownum; ++i){
      for(int j = 0;j< colnum; ++j){
        printf("%s\t",PQgetvalue(res,i,j));
      }
      printf("\n");
    }
  }
  PQclear(res);
  PQfinish(conn);
  return 0;
}
```
2. 进行编译。
```
gcc -std=c99 -c -I ~/user_1/tdata_02/tbase_v3_1/3.0.16/install/tbase_pgxz/include select.c
```
3. 连接成可执行文件。
```
gcc -o select select.o -L ~/user_1/tdata_02/tbase_v3_1/3.0.16/install/tbase_pgxz/lib/ -lpq
```
4. 进行数据库连接测试。
```
./select"host=localhost dbname=postgres port=11345"
```
![](https://main.qcloudimg.com/raw/73ffdf332b1e6ac6a2521c0eb224f82a.png)
