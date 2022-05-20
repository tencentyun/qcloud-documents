PostGIS 是关系型数据库 PostgreSQL 的一个扩展，PostGIS 提供如下空间信息服务功能：空间对象、空间索引、空间操作函数和空间操作符。同时，PostGIS 遵循 OpenGIS 的规范。

PostGIS 支持所有的空间数据类型，这些类型包括：点（POINT）、线（LINESTRING）、多边形（POLYGON）、多点（MULTIPOINT）、多线（MULTILINESTRING）、多多边形（MULTIPOLYGON）和集合对象集（GEOMETRYCOLLECTION）等。

PostGIS 也是业界功能较全面，能力强大的空间地理数据库引擎。现如今很多业务开发中，我们经常会遇到诸如“附近的某某”的需求，如何能快速实现，通过 PostGIS+ 关系型数据库 PostgreSQL 可以帮到您。

本文为您介绍，如何通过 PostGIS 实现“附近的对象”功能。

## 前提条件
- 已有一个 PostgreSQL 实例。
- 该实例支持 PostGIS 插件。

## 步骤1：创建插件
登录到数据库实例中，在业务数据库执行如下命令，登录方法您可参考 [连接 PostgreSQL 实例](https://cloud.tencent.com/document/product/409/40429)。
```
\c test
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
```

## 步骤2：创建测试表与索引
在业务数据库执行如下命令，TABLE 后的表名可自定义设置。
```
CREATE TABLE t_user(uid int PRIMARY KEY,name varchar(20),location geometry);
CREATE INDEX t_user_location on t_user USING GIST(location);
```

## 步骤3：插入测试数据
```
## 创建一个自动名字生成函数：
create or replace function random_string(length integer) returns text as
$$
declare
chars text[] := '{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}';
result text := '';
i integer := 0;
length2 integer := (select trunc(random() * length + 1));
begin
if length2 < 0 then
raise exception 'Given length cannot be less than 0';
end if;
for i in 1..length2 loop
result := result || chars[1+random()*(array_length(chars, 1)-1)];
end loop;
return result;
end;
$$ language plpgsql;

## 插入一千万条测试数据
insert into t_user select generate_series(1,10000000), random_string(20),st_setsrid(st_makepoint(150-random()*100, 90-random()*100), 4326);
```

## 步骤4：查询附近的人
1. 首先在 [拾取坐标系统](http://api.map.baidu.com/lbsapi/getpoint/) 中随便找一个坐标。 此处用天安门广场的坐标作为示例：116.404177,39.909652。
2. 确定好后，以此作为要查询的坐标，然后在数据库中找到距离这个坐标最近的5个对象，并输出这五个对象离此地的距离，此处单位是：百公里。
>?WGS84 是目前最流行的地理坐标系统。在国际上，每个坐标系统都会被分配一个 EPSG 代码，EPSG:4326 就是 WGS84 的代码。GPS 是基于 WGS84 的，所以通常我们得到的坐标数据都是 WGS84 的。一般我们在存储数据时，仍然按 WGS84 存储。
>
执行命令：
```
select uid, name, ST_AsText(location), ST_Distance(ST_GeomFromText('POINT(116.404177 39.909652)',4326), location) from t_user order by location <-> 'SRID=4326;POINT(116.404177 39.909652)'::geometry limit 5;
```
3. 查看距离此坐标对象1000米以内的所有对象与距离。
```
select uid, name, ST_AsText(location),ST_Distance(ST_GeomFromText('POINT(116.404177 39.909652)',4326), location) from t_user where ST_DWithin(location::geography, ST_GeographyFromText('POINT(116.404177 39.909652)'), 1000.0);
```
