在数据库中注册一个扩展名。

## 概要
```sql
CREATE EXTENSION [ IF NOT EXISTS ] extension_name
  [ WITH ] [ SCHEMA schema_name ]
           [ VERSION version ]
           [ FROM old_version ]
           [ CASCADE ]
```

## 描述
CREATE EXTENSION 将新的扩展加载到当前数据库中。不得加载的同名的扩展名。

加载扩展本质上等于运行扩展脚本文件。脚本通常创建新的 SQL 对象，例如函数、数据类型、操作符和索引支持方法。CREATE EXTENSION 命令还记录所有创建的对象的身份，如果 DROP EXTENSION 执行时可以再次删除它们。

加载扩展需要创建组件扩展对象所需的相同权限。对于大多数扩展，这意味着需要超级用户或数据库所有者权限。运行 CREATE EXTENSION 的用户成为后续特权检查目的的扩展的所有者，以及由扩展脚本创建的任何对象的所有者。

## 参数
IF NOT EXISTS
如果具有相同名称的扩展名已经存在，请勿抛出错误。在这种情况下发出通知，现在的扩展程序不能保证与已安装的扩展名相似。

extension_name
要安装的扩展名。该名称在数据库中必须是唯一的。扩展名是根据扩展控制文件中的细节创建 SHAREDIR/extension/extension_name.control。

SHAREDIR 是安装共享数据目录，例如`/usr/local/greenplum-db/share/postgresql`。命令 pg_config --sharedir 显示目录。

SCHEMA schema_name
要在其中安装扩展对象的方案名称。这假设扩展允许其内容被重新定位。指定的方案必须已经存在。如果未指定，并且扩展控制文件未指定方案，则使用当前的默认对象创建方案。

如果扩展名在其控制文件中指定了方案参数，则该方案无法用 SCHEMA 子句覆盖。通常，如果给出了 SCHEMA 子句与扩展参数冲突，则会引发错误。但是，如果还给出了 CASCADE 子句，那么当发生冲突的时候`schema_name`会被忽略。给定的`schema_name`用于安装任何必要的但未在其控制文件中指定方案的扩展。

扩展本身不在任何方案中：扩展的未限定名称在数据库中必须是唯一的。但属于该扩展的对象可以在一个方案中。

VERSION version
要安装的扩展版本。这可以写成标识符或字符串文字。默认版本是在扩展控制文件中指定的值。

FROM old_version
指定`FROM *old_version*`当用户尝试安装一个扩展名来替换`*旧样式*`模板，该模块是未打包到扩展中的对象的集合。如果指定，CREATE EXTENSION 运行一个替代安装脚本，将现有对象吸收到扩展中，而不是创建新对象。确保 SCHEMA 子句指定包含这些预先存在的对象的模式。

用于`*旧版本*`的值由扩展名作者确定，如果有多个版本的旧式模块可以升级到扩展名，则可能会有所不同。对于9.1之前的 PostgreSQL 提供的标准附加模块，指定 unpackaged 为`*old_version*`将模块更新为扩展样式时。

CASCADE
自动安装依赖尚未安装的扩展名。递归检查依赖扩展名，并且这些依赖关系也自动安装。如果指定了 SCHEMA 子句，则该模式适用于所安装的扩展名和所有依赖扩展。指定的其他选项不适用于自动安装的从属扩展。特别是，安装从属扩展时，始终选择默认版本。

## 注解
目前可用于加载的扩展可以从 pg_available_extensions 或 pg_available_extension_versions 系统视图中识别。

在用户使用 CREATE EXTENSION 将扩展加载到数据库中之前，必须安装支持扩展文件，其中包括扩展控制文件和至少一个 SQL 脚本文件。支持文件必须安装在所有数据库主机的相同位置。

## 兼容性
CREATE EXTENSION 是数据库扩展。

## 另见
ALTER EXTENSION、DROP EXTENSION
