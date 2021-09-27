拥有数据管理权限的用户可以登录 DLC 控制台或者使用 API， 将数据访问权限授权给子用户。任何子用户的数据权限都需要被授予，否则无法执行数据的新建、查询、删除等操作。
- DLC 的数据资源包括：数据连接、数据库和数据表。
- DLC 的操作权限包括：CREATE、ALTER、DROP、SELECT、INSERT、UPADATE、DELETE。操作权限对应的 SQL 操作如下：


  | Action                     | CREATE | ALTER | DROP | SELECT | INSERT | DELETE | Target         |
  | -------------------------- | ------ | ----- | ---- | ------ | ------ | ------ | -------------- |
  | CREATE DATABASE            | Y      |     -  |   -   |    -    |   -     | -       | Cataglog       |
  | ALTER DATABASE             |  -      | Y     |   -   |    -    |     -   |  -      | Database       |
  | DROP DATABASE              |  -      | -      | Y    |  -      |    -    |      -  | Database       |
  | CREATE TABLE               | Y      | -      |     - |     -   |   -     |   -     | Database       |
  | CREATE TABLE AS SELECT     | Y      |    -   |   -   | Y      | Y      |  -      | Database/Table |
  | DROP TABLE                 |     -   | -      | Y    |     -   |    -    |   -     | Table          |
  | ALTER TABLE LOCATION       |      -  | Y     |    -  |    -    |   -     |  -      | Table          |
  | ALTER PARTITION LOCATION   |    -    | Y     |  -    |    -    |     -   |   -     | Table          |
  | ALTER TABLE ADD PARTITION  |    -    | Y     |   -   |    -    |     -   |    -    | Table          |
  | ALTER TABLE DROP PARTITION |    -    | Y     |   -   |   -     |    -    |  -      | Table          |
  | ALTER TABLE                |   -     | Y     |   -   |     -   |     -   |       - | Table          |
  | CREATE VIEW                | Y      |  -     |    -  |    -    |     -   |     -   | Database       |
  | ALTER VIEW PROPERTIES      |   -     | Y     |   -   |  -      |    -    |  -      | Table          |
  | ALTER VIEW RENAME          |     -   | Y     |  -    |     -   |  -      |     -   | Table          |
  | DROP VIEW PROPERTIES       |    -    | Y     | Y    |  -      |   -     |     -   | Table          |
  | DROP VIEW                  |     -   |   -    | Y    |     -   |  -      |     -   | Table          |
  | SELECT                     |   -     |  -     |   -   | Y      |    -    |    -    | Table          |
  | INSERT                     |      -  |    -   |   -   |    -    | Y      |      -  | Table          |
  | INSERT OVERWRITE           |    -    |  -     |   -   | -       | Y      | Y      | Table          |

