更改一个函数的定义。

## 概要
```sql
ALTER FUNCTION name ( [ [argmode] [argname] argtype [, ...] ] ) 
   action [, ... ] [RESTRICT]
 
ALTER FUNCTION name ( [ [argmode] [argname] argtype [, ...] ] )
   RENAME TO new_name
 
ALTER FUNCTION name ( [ [argmode] [argname] argtype [, ...] ] ) 
   OWNER TO new_owner
 
ALTER FUNCTION name ( [ [argmode] [argname] argtype [, ...] ] ) 
   SET SCHEMA new_schema
```

其中 action 是下列之一：

```sql
{CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT}
{IMMUTABLE | STABLE | VOLATILE}
{[EXTERNAL] SECURITY INVOKER | [EXTERNAL] SECURITY DEFINER}
COST execution_cost
SET configuration_parameter { TO | = } { value | DEFAULT }
SET configuration_parameter FROM CURRENT
RESET configuration_parameter
RESET ALL
```

## 描述
ALTER FUNCTION 更改一个函数的定义。

用户必须拥有该函数以使用 ALTER FUNCTION。要更改函数的模式，用户还必须对新模式具有 CREATE 特权。要更改所有者，用户还必须是新拥有角色的直接或间接成员，并且该角色必须对该函数的模式具有 CREATE 特权（这些限制强制修改拥有者不能做一些通过删除和重建该函数做不到的事情。但是，超级用户有可以改变任何功能的所有权）。

## 参数
name
现有函数的名称（可选方案限定）。

argmode
参数的模式： IN、OUT、INOUT、VARIADIC。如果省略，默认值为 IN。请注意 ALTER FUNCTION 实际上并不关 OUT 参数，因为只需要输入参数来确定函数的身份。因此已经足够了对于只列出 IN、INOUT、VARIADIC 参数。

argname
参数的名称。请注意，ALTER FUNCTION 实际上并不关心参数名称，因为只需要参数数据类型来确定函数的身份。

argtype
函数参数（如果有）的数据类型（可以是方案限定）。

new_name
函数的新名称。

new_owner
函数的新拥有者。请注意，如果函数被标记为 SECURITY DEFINER，随后它将作为新的所有者执行。

new_schema
该函数的新模式。

CALLED ON NULL INPUT
RETURNS NULL ON NULL INPUT
STRICT
CALLED ON NULL INPUT 将该函数改为在某些或者全部参数为空值时可以被调用。 
RETURNS NULL ON NULL INPUT 或者 STRICT 更改函数，以便如果其任何参数为空，则不会调用该函数；而是自动假设一个空的结果。参阅 CREATE FUNCTION 获取更多信息。

IMMUTABLE
STABLE
VOLATILE
将函数的波动性改为指定的设置。参阅 CREATE FUNCTION 以便问题得以解决。

[ EXTERNAL ] SECURITY INVOKER
[ EXTERNAL ] SECURITY DEFINER
更改该函数是否为一个安全性定义者。 关键词 EXTERNAL 为了 SQL 的一致性而被忽略。参阅 CREATE FUNCTION 获取更多有关此功能的信息。

COST execution_cost
更改该函数的估计执行代价。参阅 CREATE FUNCTION 获取更多信息。

configuration_parameter
value
当该函数被调用时，要对一个配置参数做出增加或者更改的赋值。如果 value 是 DEFAULT 或者使用等价的 RESET， 该函数本地的设置将会被移除，这样该函数会使用其环境中存在的值执行。使用 RESET ALL 可以清除所有函数本地的设置。SET FROM CURRENT 应用会话的当前值当函数被输入时。

RESTRICT
忽略 SQL 标准。

## 注意
数据库对某些定义的函数有 STABLE 或者 VOLATILE 这样的限制。参阅 CREATE FUNCTION 获取更多信息。

## 示例
将 integer 类型的函数 sqrt 重命名为 square_root：

```sql
ALTER FUNCTION sqrt(integer) RENAME TO square_root;
```

更改 integer 类型的 sqrt 函数的所有者为 joe：

```sql
ALTER FUNCTION sqrt(integer) OWNER TO joe;
```

更改 integer 类型的函数 sqrt 的模式为 math：

```sql
ALTER FUNCTION sqrt(integer) SET SCHEMA math;
```

要调整一个函数的自动搜索路径：

```sql
ALTER FUNCTION check_password(text) RESET search_path;
```

## 兼容性
这个语句部分兼容 SQL 标准中的 ALTER FUNCTION 语句。该标准允许修改一个函数的更多属性，但是不提供重命名一个函数、标记一个函数为安全性定义者、为一个函数附加配置参数值或者更改一个函数的拥有者、模式或者稳定性等功能。 该标准还需要 RESTRICT 关键字, 它在数据库中是可选的。

## 另见
CREATE FUNCTION、DROP FUNCTION
