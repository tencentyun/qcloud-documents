

本章节主要介绍微服务引擎 TSE 注册配置中心 Apollo 的计费项目和费用。微服务引擎 TSE 于2022年6月X日正式进行商业化。

>!
>- 自2022年6月*日起，微服务引擎 TSE 注册配置中心中的 apollo 将结束免费公测，正式开始计费。其他组件继续在内测/公测免费阶段。
>- todo :是否有优惠活动

## 计费模式

注册配置中心 apollo 按量计费（后付费）和包年包月（预付费）两种购买方式。

- 按量计费模式：您可以随时开通/销毁实例，按实例的实际使用时长付费。计费时间粒度精确到小时，不需要提前支付费用，每天进行结算，可以有效避免资源浪费。
- 包年包月模式：即在新建实例时支付费用。适用于长期稳定的业务场景，费用较按量计费模式更为低廉。

## 计费项与费用说明

注册配置中心 apollo 费用包括**apollo实例计算资源**、**数据存储计算资源**、**数据存储空间**、**环境配置费用**四部分组成
<table>
    <tr>
        <th>计费项</th><th>计费项说明</th>
    </tr>
    <tr>
        <td rowspan="2">apollo实例计算资源</td><td>环境计算资源</td>
    </tr>
    <tr>
        <td>控制台计算资源</td>
    </tr>
    <tr>
        <td>数据存储计算资源</td><td rowspan="2">数据库资源</td>
    </tr>
    <tr>
        <td>数据存储空间</td>
    </tr>
    <tr>
        <td>环境配置费用</td><td>网络资源</td>
    </tr>
  
</table>



### 按量计费模式（后付费）

<table>
    <tr>
        <th>计费项</th><th>规格</th><th>单价(元/小时)</th>
    </tr>
    <tr>
        <td rowspan="5">apollo实例计算资源</td><td>1核2GB</td><td>0.314</td>
    </tr>
    <tr>
        <td>2核4GB</td><td>0.594</td>
    </tr>
    <tr>
        <td>4核8GB</td><td>1.156</td>
    </tr>
    <tr>
        <td>8核16GB</td><td>2.278</td>
    </tr>
    <tr>
        <td>16核32GB</td><td>4.525</td>
    </tr>
    <tr>
        <td rowspan="4">数据存储计算资源</td><td>1核1GB</td><td>0.45</td>
    </tr>
    <tr>
        <td>1核2GB</td><td>0.91</td>
    </tr>
    <tr>
        <td>2核4GB</td><td>1.81</td>
    </tr>
    <tr>
        <td>4核8GB</td><td>3.63</td>
    </tr>
    <tr>
        <td >数据存储空间</td><td>1GB</td><td>0.0032</td>
    </tr>
    <tr>
        <td >环境配置</td><td>每环境</td><td>0.14</td>
    </tr>
</table>

**计费公式**：总费用 = （环境套数 × apollo实例计算资源单价 + 控制台apollo实例个数 × apollo实例计算资源单价 + 数据存储计算资源单价 + 存储空间总数 × 存储空间单价 + 环境套数 × 环境配置单价）× 总小时数。

**计费示例**：假如您选了以下规格，总费用为0.314 + 0.594 × 2 + 0.31389 + 0.91 + 25 × 0.0032 + 2 × 0.14 = 3.08589元/小时。

<table>
    <tr>
        <th>计费项</th><th>规格</th><th>数量</th><th>单价(元/小时)</th>
    </tr>
    <tr>
        <td rowspan="3">apollo实例计算资源</td><td>测试环境 1核2GB</td><td>1套</td><td>0.314</td>
    </tr>
    <tr>
        <td>生产环境 2核4GB</td><td>2套</td><td>0.594</td>
    </tr>
    <tr>
        <td>控制台 1核2GB</td><td>1个</td><td>0.31389</td>
    </tr>
    <tr>
        <td>数据存储计算资源</td><td>mysql 1核2GB</td><td>1个</td><td>0.91</td>
    </tr>
    <tr>
        <td>数据存储空间</td><td></td><td>25GB</td><td>0.0032</td>
    </tr>
    <tr>
        <td>环境配置</td><td></td><td>2个环境</td><td>0.14</td>
    </tr>
</table>


### 包年包月（预付费）模式


<table>
    <tr>
        <th>计费项</th><th>规格</th><th colspan="2">单价</th>
    </tr>
    <tr>
        <td rowspan="5">apollo实例计算资源</td><td>1核2GB</td><td>113 </td><td rowspan="9">元/节点/月</td>
    </tr>
    <tr>
        <td>2核4GB</td><td>214</td>
    </tr>
    <tr>
        <td>4核8GB</td><td>416</td>
    </tr>
    <tr>
        <td>8核16GB</td><td>820</td>
    </tr>
    <tr>
        <td>16核32GB</td><td>1629</td>
    </tr>
    <tr>
        <td rowspan="4">数据存储计算资源</td><td>1核1GB</td><td>163</td>
    </tr>
    <tr>
        <td>1核2GB</td><td>327</td>
    </tr>
    <tr>
        <td>2核4GB</td><td>652</td>
    </tr>
    <tr>
        <td>4核8GB</td><td>1306</td>
    </tr>
    <tr>
        <td >数据存储空间</td><td>1GB</td><td>1.152</td><td>元/G/月</td>
    </tr>
    <tr>
        <td >环境配置</td><td>每环境</td><td>50</td><td>元/每环境/月</td>
    </tr>
</table>

**计费公式**：总费用 = （环境套数 × apollo实例计算资源单价 + 控制台apollo实例个数 × apollo实例计算资源单价 + 数据存储计算资源单价 + 存储空间总数 × 存储空间单价 + 环境套数 × 环境配置单价）× 总月数。

**计费示例**：加入您选了以下规格，总费用为113 + 2 × 214 + 112.32 + 327 + 25 × 1.152 + 2 × 50 = 1109.12元/月  

<table>
    <tr>
        <th>计费项</th><th>规格</th><th>数量</th><th colspan="2">单价</th>
    </tr>
    <tr>
        <td rowspan="3">apollo实例计算资源</td><td>测试环境 1核2GB</td><td>1套</td><td>113</td rowspan=""><td rowspan="4">元/节点/月</td>
    </tr>
    <tr>
        <td>生产环境 2核4GB</td><td>2套</td><td>214</td>
    </tr>
    <tr>
        <td>控制台 1核2GB</td><td>1个</td><td>112.32</td>
    </tr>
    <tr>
        <td>数据存储计算资源</td><td>mysql 1核2GB</td><td>1个</td><td>327</td>
    </tr>
    <tr>
        <td>数据存储空间</td><td></td><td>25GB</td><td>1.152</td><td>元/GB/月</td>
    </tr>
    <tr>
        <td>环境配置</td><td></td><td>2个环境</td><td>50</td><td>元/环境/月</td>
    </tr>
</table>



