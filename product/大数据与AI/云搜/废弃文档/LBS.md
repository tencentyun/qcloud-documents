## 1 简介

LBS定制可以提供给基于地理位置距离进行优先的搜索业务，例如查找距离用户（经度：113.959633，纬度：22.54138）最近的川菜馆，这样即要考虑商户的经纬度信息和用户自身经纬度的球面距离（单位为米）作为返回结果的一个重要权重信息，同时，云搜提供distance字段作为LBS值的排序字段（精细排序）。

## 2 配置

第一步：在“应用结构修改”数值域字段添加”经纬度“两个字段（字段类型为浮点型），用于存储商户的经纬度信息。如下图

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunsousuobangzhuwendang-55.png)

第二步：在高级组件定制”LBS“里设置经纬度字段，并保存开启LBS距离优先策略。

![](//mccdn.qcloud.com/img5698f6224f42f.png)

## 3 使用

在检索过程中，需要传入用户所在的经（参数名为longitude）纬（参数名为latitude）度值，用来计算两点的距离，如下图所示：

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunsousuobangzhuwendang-57.png)
