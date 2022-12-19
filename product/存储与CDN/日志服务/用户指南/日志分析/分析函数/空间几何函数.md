本文将为您介绍空间几何函数。

## 基本概念

空间几何函数支持 Well-Known Text（WKT）及 Well-Known Binary（WKB）格式描述的几何实体，相关概念可参考 [Well-known text representation of geometry - Wikipedia](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)。

| 几何实体     | Well-Known Text（WKT）格式                                   |
| ------------ | ------------------------------------------------------------ |
| 点           | POINT (0 0)                                                  |
| 线段         | LINESTRING (0 0, 1 1, 1 2)                                   |
| 多边形       | POLYGON ((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 2 1, 2 2, 1 2, 1 1)) |
| 多点         | MULTIPOINT (0 0, 1 2)                                        |
| 多线段       | MULTILINESTRING ((0 0, 1 1, 1 2), (2 3, 3 2, 5 4))           |
| 多个多边形   | MULTIPOLYGON (((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 2 1, 2 2, 1 2, 1 1)), ((-1 -1, -1 -2, -2 -2, -2 -1, -1 -1))) |
| 几何实体集合 | GEOMETRYCOLLECTION (POINT(2 3), LINESTRING (2 3, 3 4))       |

几何实体默认采用平面几何，在平面几何中两点之间的最短距离为直线。几何实体也支持球面几何，球面中两点之间的最短距离为大圆弧。使用 to_spherical_geography() 可将平面几何实体转换为球面几何实体。
例如：
`ST_Distance(ST_Point(-71.0882, 42.3607), ST_Point(-74.1197, 40.6976))` 计算平面上的两个点的距离，值为3.4577。
`ST_Distance(to_spherical_geography(ST_Point(-71.0882, 42.3607)), to_spherical_geography(ST_Point(-74.1197, 40.6976)))` 计算球面上两个点的距离，值为312822.179。

计算长度时（例如：ST_Distance()和ST_Length() ），单位为米，计算面积时（例如：ST_Area()），单位为平方米。



## 构造几何实体

| 函数                             | 返回值类型         | 说明                                |
| -------------------------------- | ------------------ | ----------------------------------- |
| ST_Point(double, double)         | Point              | 构造一个点。                        |
| ST_LineFromText(varchar)         | LineString         | 从 WKT 格式的文本中构造一个线段。   |
| ST_Polygon(varchar)              | Polygon            | 从 WKT 格式的文本中构造一个多边形。 |
| ST_GeometryFromText(varchar)     | Geometry           | 从 WKT 文本中构造一个几何实体。     |
| ST_GeomFromBinary(varbinary)     | Geometry           | 从 WKB 中构造一个几何实体。         |
| ST_AsText(Geometry)              | varchar            | 把一个空间几何实体转变成 WKT 格式。 |
| to_spherical_geography(Geometry) | SphericalGeography | 将平面几何实体转换为球面几何实体。  |
| to_geometry(SphericalGeography)  | Geometry           | 将球面几何实体转换为平面几何实体。  |



## 空间关系判断

| 函数                              | 返回值类型 | 说明                                                         |
| --------------------------------- | ---------- | ------------------------------------------------------------ |
| ST_Contains(Geometry, Geometry)   | boolean    | 当第二个实体的所有点都不在第一个实体外部，并且第一个实体至少有一个内部点在第二个实体内部时，返回 true。如果第二个实体正好在第一个实体的边上，返回 false。 |
| ST_Crosses(Geometry, Geometry)    | boolean    | 当两个实体有共同内部点时，返回 true。                        |
| ST_Disjoint(Geometry, Geometry)   | boolean    | 当两个实体没有任何交集时，返回 true。                        |
| ST_Equals(Geometry, Geometry)     | boolean    | 当两个实体完全相同时，返回 true。                            |
| ST_Intersects(Geometry, Geometry) | boolean    | 当两个实体在两个空间上共享时，返回 true。                    |
| ST_Overlaps(Geometry, Geometry)   | boolean    | 当两个实体维度相同，并且不是包含关系时，返回 true。          |
| ST_Relate(Geometry, Geometry)     | boolean    | 当两个实体相关时，返回 true。                                |
| ST_Touches(Geometry, Geometry)    | boolean    | 当两个实体仅仅边界有联系，没有共同内部点时，返回 true。      |
| ST_Within(Geometry, Geometry)     | boolean    | 当第一个实体完全在第二个实体内部时，返回 true。如果边界有交集，返回 false。 |



## Operations

| 函数                                        | 返回值类型        | 说明                                                         |
| ------------------------------------------- | ----------------- | ------------------------------------------------------------ |
| geometry_nearest_points(Geometry, Geometry) | row(Point, Point) | 返回两个几何实体之间最相近的两个点。                         |
| geometry_union(array(Geometry))             | Geometry          | 将多个几何实体合并为一个几何实体。                           |
| ST_Boundary(Geometry)                       | Geometry          | 返回几何实体的闭包。                                         |
| ST_Buffer(Geometry, distance)               | Geometry          | 返回一个多边形，该多边形距离输入参数 Geometry 的距离是 distance。 |
| ST_Difference(Geometry, Geometry)           | Geometry          | 返回两个空间实体的不同的点的集合。                           |
| ST_Envelope(Geometry)                       | Geometry          | 返回空间实体的边界多边形。                                   |
| ST_ExteriorRing(Geometry)                   | Geometry          | 返回多边形的外部环。                                         |
| ST_Intersection(Geometry, Geometry)         | Geometry          | 返回两个空间实体的交集点。                                   |
| ST_SymDifference(Geometry, Geometry)        | Geometry          | 返回两个空间实体不同的点，组成的新的空间实体。获取两个几何对象不相交的部分。 |



## Accessors

| 函数                                                | 返回值类型 | 说明                                                        |
| --------------------------------------------------- | ---------- | ----------------------------------------------------------- |
| ST_Area(Geometry)                                   | double     | 在平面几何中计算多边形面积。                                |
| ST_Area(SphericalGeography)                         | double     | 在球面几何中计算多边形面积。                                |
| ST_Centroid(Geometry)                               | Geometry   | 返回几何实体的中心点。                                      |
| ST_CoordDim(Geometry)                               | bigint     | 返回几何实体的坐标维度。                                    |
| ST_Dimension(Geometry)                              | bigint     | 返回几何实体的固有维度，必须小于或等于坐标维度。            |
| ST_Distance(Geometry, Geometry)                     | double     | 计算平面几何中两个实体之间的最小距离。                      |
| ST_Distance(SphericalGeography, SphericalGeography) | double     | 计算球面几何中两个实体之间的最小距离。                      |
| ST_IsClosed(Geometry)                               | boolean    | 当实体是一个闭合空间时，返回 true。                         |
| ST_IsEmpty(Geometry)                                | boolean    | 当参数是一个空的几何实体集合或者多边形或者点时，返回 true。 |
| ST_IsRing(Geometry)                                 | boolean    | 当参数是一条线，并且是闭合的简单的线时，返回 true。         |
| ST_Length(Geometry)                                 | double     | 在平面几何中，计算一个线段或者多条线段的长度。              |
| ST_Length(SphericalGeography)                       | double     | 在球面几何中，计算一个线段或者多条线段的长度。              |
| ST_XMax(Geometry)                                   | double     | 返回几何体边框的 X 最大值。                                 |
| ST_YMax(Geometry)                                   | double     | 返回几何体边框的 Y 最大值。                                 |
| ST_XMin(Geometry)                                   | double     | 返回几何体边框的 X 最小值。                                 |
| ST_YMin(Geometry)                                   | double     | 返回几何体边框的 Y 最小值。                                 |
| ST_StartPoint(Geometry)                             | point      | 返回线段类型几何体的第一个点。                              |
| ST_EndPoint(Geometry)                               | point      | 返回线段类型几何体的最后一个点。                            |
| ST_X(Point)                                         | double     | 返回点类型的 X 轴。                                         |
| ST_Y(Point)                                         | double     | 返回点类型的 Y 轴。                                         |
| ST_NumPoints(Geometry)                              | bigint     | 计算几何实体的点的个数。                                    |
| ST_NumInteriorRing(Geometry)                        | bigint     | 返回多边形内部的环的个数。                                  |
