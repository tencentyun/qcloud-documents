拥有数据管理权限的用户可以登录 DLC 控制台或者使用 API， 将数据访问权限授权给子用户。任何子用户的数据权限都需要被授予，否则无法执行数据的新建、查询、删除等操作。
- DLC 的数据资源包括：数据连接、数据库和数据表。
- DLC 的操作权限包括：CREATE、ALTER、DROP、SELECT、INSERT、UPADATE、DELETE。操作权限对应的 SQL 操作如下：


  | Action                     | CREATE | ALTER | DROP | SELECT | INSERT | DELETE | Target         |
  | -------------------------- | ------ | ----- | ---- | ------ | ------ | ------ | -------------- |
  | CREATE DATABASE            | &#10003      |     -  |   -   |    -    |   -     | -       | Cataglog       |
  | ALTER DATABASE             |  -      | &#10003     |   -   |    -    |     -   |  -      | Database       |
  | DROP DATABASE              |  -      | -      | &#10003    |  -      |    -    |      -  | Database       |
  | CREATE TABLE               | &#10003      | -      |     - |     -   |   -     |   -     | Database       |
  | CREATE TABLE AS SELECT     | &#10003      |    -   |   -   | &#10003      | &#10003      |  -      | Database/Table |
  | DROP TABLE                 |     -   | -      | &#10003    |     -   |    -    |   -     | Table          |
  | ALTER TABLE LOCATION       |      -  | &#10003     |    -  |    -    |   -     |  -      | Table          |
  | ALTER PARTITION LOCATION   |    -    | &#10003     |  -    |    -    |     -   |   -     | Table          |
  | ALTER TABLE ADD PARTITION  |    -    | &#10003     |   -   |    -    |     -   |    -    | Table          |
  | ALTER TABLE DROP PARTITION |    -    | &#10003     |   -   |   -     |    -    |  -      | Table          |
  | ALTER TABLE                |   -     | &#10003     |   -   |     -   |     -   |       - | Table          |
  | CREATE VIEW                | &#10003      |  -     |    -  |    -    |     -   |     -   | Database       |
  | ALTER VIEW PROPERTIES      |   -     | &#10003     |   -   |  -      |    -    |  -      | Table          |
  | ALTER VIEW RENAME          |     -   | &#10003     |  -    |     -   |  -      |     -   | Table          |
  | DROP VIEW PROPERTIES       |    -    | &#10003     | &#10003    |  -      |   -     |     -   | Table          |
  | DROP VIEW                  |     -   |   -    | &#10003    |     -   |  -      |     -   | Table          |
  | SELECT                     |   -     |  -     |   -   | &#10003      |    -    |    -    | Table          |
  | INSERT                     |      -  |    -   |   -   |    -    | &#10003      |      -  | Table          |
  | INSERT OVERWRITE           |    -    |  -     |   -   | -       | &#10003      | &#10003      | Table          |

