## Properties（属性）

### Optional lastInsertId
**lastInsertId?:** number

lastInsertId 返回数据库为响应命令而生成的整数。通常，这将来自插入新行时的“自动增量”列。并非所有数据库都支持此功能，并且此类语句的语法各不相同。



### Optional rowsAffected
**rowsAffected?:** number

rowsAffected 返回受更新、插入或删除影响的行数并非每个数据库或数据库驱动程序都支持这一点。
