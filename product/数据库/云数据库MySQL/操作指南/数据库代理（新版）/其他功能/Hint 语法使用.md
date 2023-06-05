本文主要介绍在数据库代理上如何使用 Hint 语法。

使用 Hint 语法可以强制 SQL 请求在指定的实例上执行，Hint 的路由优先级最高，例如，Hint 不受一致性、事务的约束，使用前请合理评估业务场景是否需要。
>!
>- 使用 MySQL 命令行进行连接并使用 Hint 语句时，需要在命令中增加 -c 选项，否则 Hint 会被 MySQL 命令行工具过滤。
>- 通过数据库代理使用 Hint 语法时，数据库代理内核小版本大于等于 1.1.3 的版本，支持 prepare。

目前支持三种 Hint：

- 指定到主实例执行：
```
/* to master */
或
/*FORCE_MASTER*/   
``` 
- 指定到只读实例执行：
```
/* to slave */
或
/*FORCE_SLAVE*/  
```  
- 指定某个具体实例执行：
```
/* to server server_name*/
```
server_name 可以为短 id，如 `/* to server test_ro_1 */`。
