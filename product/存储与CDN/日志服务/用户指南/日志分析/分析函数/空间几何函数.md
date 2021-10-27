本文介绍空间几何函数。

## 空间几何概念

空间几何函数支持 Well-Known Text（WKT）格式描述的几何实体。

| 几何实体     | Well-Known Text（WKT）格式                                   |
| ------------ | ------------------------------------------------------------ |
| 点           | POINT (0 0)                                                  |
| 线段         | LINESTRING (0 0, 1 1, 1 2)                                   |
| 多边形       | POLYGON ((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 2 1, 2 2, 1 2, 1 1)) |
| 多点         | MULTIPOINT (0 0, 1 2)                                        |
| 多线段       | MULTILINESTRING ((0 0, 1 1, 1 2), (2 3, 3 2, 5 4))           |
| 多个多边形   | MULTIPOLYGON (((0 0, 4 0, 4 4, 0 4, 0 0), (1 1, 2 1, 2 2, 1 2, 1 1)), ((-1 -1, -1 -2, -2 -2, -2 -1, -1 -1))) |
| 空间实体集合 | GEOMETRYCOLLECTION (POINT(2 3), LINESTRING (2 3, 3 4))       |



## 构造空间实体

| 函数                                    | 说明                              |
| --------------------------------------- | --------------------------------- |
| ST_Point(double, double) → Point        | 构造一个点。                      |
| ST_LineFromText(varchar) → LineString   | 从 WKT 格式的文本中构造一个线段。   |
| ST_Polygon(varchar) → Polygon           | 从 WKT 格式的文本中构造一个多边形。 |
| ST_GeometryFromText(varchar) → Geometry | 从 WKT 文本中构造一个空间几何实体。 |
| ST_AsText(Geometry) → varchar           | 把一个空间几何实体转变成 WKT 格式。 |



## 运算符

| 函数                                            | 说明                                                         |
| ----------------------------------------------- | ------------------------------------------------------------ |
| ST_Boundary(Geometry) → Geometry                | 计算几何实体的闭包。                                         |
| ST_Buffer(Geometry, distance) → Geometry        | 返回一个多边形，该多边形距离输入参数 Geometry 的距离是 distance。 |
| ST_Difference(Geometry, Geometry) → Geometry    | 返回两个空间实体的不同的点的集合。                           |
| ST_Envelope(Geometry) → Geometry                | 返回空间实体的边界多边形。                                   |
| ST_ExteriorRing(Geometry) → Geometry            | 返回多边形的外部环。                                         |
| ST_Intersection(Geometry, Geometry) → Geometry  | 返回两个空间实体的交集点。                                   |
| ST_SymDifference(Geometry, Geometry) → Geometry | 返回两个空间实体不同的点，组成的新的空间实体。获取两个几何对象不相交的部分。 |



### 空间关系判断

| 函数                                        | 说明                                                         |
| ------------------------------------------- | ------------------------------------------------------------ |
| ST_Contains(Geometry, Geometry) → boolean   | 当第二个实体的所有点都不在第一个实体外部，并且第一个实体至少有一个内部点在第二个实体内部时，返回 true。如果第二个实体正好在第一个实体的边上，那么是 false。 |
| ST_Crosses(Geometry, Geometry) → boolean    | 当两个实体有共同内部点时，返回 true。                         |
| ST_Disjoint(Geometry, Geometry) → boolean   | 当两个实体没有任何交集时，返回 true。                         |
| ST_Equals(Geometry, Geometry) → boolean     | 当两个实体完全相同时，返回 true。                             |
| ST_Intersects(Geometry, Geometry) → boolean | 当两个实体在两个空间上共享时，返回 true。                     |
| ST_Overlaps(Geometry, Geometry) → boolean   | 当两个实体维度相同，并且不是包含关系时，返回 true。           |
| ST_Relate(Geometry, Geometry) → boolean     | 当两个实体相关时，返回 true。                                 |
| ST_Touches(Geometry, Geometry) → boolean    | 当两个实体仅仅边界有联系，没有共同内部点时，返回 true。       |
| ST_Within(Geometry, Geometry) → boolean     | 当第一个实体完全在第二个实体内部时，返回 true。如果边界有交集，返回 false。 |



### Accessors

| 函数                                     | 说明                                                         |
| ---------------------------------------- | ------------------------------------------------------------ |
| ST_Area(Geometry) → double               | 使用欧几里得测量法，计算多边形在二维平面上的投影面积。       |
| ST_Centroid(Geometry) → Geometry         | 返回几何实体的中心点。                                       |
| ST_CoordDim(Geometry) → bigint           | 返回几何实体的坐标维度。                                     |
| ST_Dimension(Geometry) → bigint          | 返回几何实体的固有维度，必须小于或等于坐标维度。             |
| ST_Distance(Geometry, Geometry) → double | 计算两个实体之间的最小距离。                                 |
| ST_IsClosed(Geometry) → boolean          | 当实体是一个闭合空间时，返回 true。                           |
| ST_IsEmpty(Geometry) → boolean           | 当参数是一个空的几何实体集合或者多边形或者点时，返回 true。   |
| ST_IsRing(Geometry) → boolean            | 当参数是一条线，并且时闭合的简单的线时，返回 true。           |
| ST_Length(Geometry) → double             | 在二维投影平面上，使用欧几里得测量法计算一个线段或者多条线段的长度。返回一个行字符串或多行字符串的长度。该长度是采用欧几里得测量法基于空间参考对二维平面的预测。 |
| ST_XMax(Geometry) → double               | 返回几何体边框的 X 最大值。                                    |
| ST_YMax(Geometry) → double               | 返回几何体边框的 Y 最大值。                                    |
| T_XMin(Geometry) → double                | 返回几何体边框的 X 最小值。                                    |
| ST_YMin(Geometry) → double               | 返回结合体边框的 Y 最小值。                                    |
| ST_StartPoint(Geometry) → point          | 返回线段类型几何体的第一个点。                               |
| ST_EndPoint(Geometry) → point            | 返回线段类型几何体的最后一个点。                             |
| ST_X(Point) → double                     | 返回点类型的 X 轴。                                            |
| ST_Y(Point) → double                     | 返回点类型的 Y 轴。                                            |
| ST_NumPoints(Geometry) → bigint          | 计算几何实体的点的个数。                                     |
| ST_NumInteriorRing(Geometry) → bigint    | 返回多边形内部的环的个数。                                   |

