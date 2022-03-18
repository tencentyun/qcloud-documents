DLC 权限包括数据权限和计算资源权限。拥有管理权限的用户可以登录 DLC 控制台或者使用 API， 将数据和计算资源权限授权给子用户。任何子用户的权限都需要被授予，否则无法执行数据和引擎的使用、修改、删除等操作。
## 数据权限
DLC 的数据权限包括对数据目录、数据库和数据表的操作权限。为方便您的管理及配置，我们提供了两种权限授予模式：常规权限设置、高级权限设置。
- 常规权限设置模式下，您可以直接给用户授予角色（角色与权限对应参见 [子账号权限管理](https://cloud.tencent.com/document/product/1342/61976)），而无需关注具体的权限配置。授权粒度覆盖数据目录、数据库、数据表。适合快速授权、无需复杂权限管理场景。
- 高级权限设置模式下，您可以对单个数据库及数据库内的数据表、视图、函数进行全面授权，适合需要精细权限管理场景。

操作权限对应的 SQL 操作如下：

| Action | CREATE | ALTER |	DROP	 |	SELECT	 |	INSERT |		DELETE	 |	Target |	
|---------|---------|---------|---------|---------|---------|---------|---------|
| CREATE DATABASE| 	Y| -| - | - | - | -|  	Cataglog| 
| ALTER DATABASE| -| 	Y| -| -| -| -| 					Database| 
| DROP DATABASE| 	-| 	-	| Y| -| 	-| -| 			Database| 
| CREATE TABLE|  	Y| -| - | - | - | -|  	Database| 
| CREATE TABLE AS SELECT| Y| -| - | Y | Y | -|  	Database/Table| 
| DROP TABLE| -| 	-	| Y| -| 	-| -| 	Table|
| ALTER TABLE LOCATION	|  -| 	Y| -| -| -| -| 				Table| 		
| ALTER PARTITION LOCATION| 	 -| 	Y| -| -| -| -| 					Table| 		
| ALTER TABLE ADD PARTITION| 	 -| 	Y| -| -| -| -| 					Table| 		
| ALTER TABLE DROP PARTITION	| -| 	Y| -| -| -| -| 							Table| 		
| ALTER TABLE| 	 -| 	Y| -| -| -| -| 						Table| 		
| CREATE VIEW| Y| -| - | - | - | -|  				Database| 		
| ALTER VIEW PROPERTIES	|  -| 	Y| -| -| -| -| 	View|
| ALTER VIEW RENAME	|  -| 	Y| -| -| -| -| 			View|
| DROP VIEW PROPERTIES| 	 -| 	Y| Y| -| -| -| 			View|  
| DROP VIEW| 		 	-| 	-	| Y| -| 	-| -| 			View|  
| SELECT TABLE| 		 	-| 	-	| -| Y| 	-| -| 	Table|  
| INSERT	| 			 	-| 	-	| -| -| 	Y| -| 	Table|  
| INSERT OVERWRITE	| 		 	-| 	-	| -| -| 	Y| Y| 	Table|  
| CREATE FUNCTION| 		Y| -| - | - | - | -|  			Database|  
| DROP FUNCTION| 	-| -| Y | - | - | -|  	Function|  
| SELECT VIEW		| 		-| -| - | Y | - | -|  	View|  
| SELECT FUNCTION		| 	-| -| - | Y | - | -|			Function|  

## 计算资源权限
DLC 的计算资源操作权限包括对计算引擎的使用、修改、操作、监控、删除权限。具体权限如下：
- 使用：选择使用该引擎进行计算的权限。
- 修改：可以修改引擎的配置信息修改：修改引擎配置信息权限（需要CAM财务权限）。
- 操作：对引擎进行挂起、重启操作的权限。
- 监控：查看引擎的运行任务与监控信息的权限。
- 删除：对引擎进行退费处理权限。

## 权限授予
单个用户可被授予多组权限，授权详细操作参见 [子账号权限管理](https://cloud.tencent.com/document/product/1342/61976)。

