Tab 组件是多个图表的集合，通过 tab 的标签切换来查看不同的标签下的内容。



## 场景示例

通过切换标签查看不同部门的产品售卖情况。

## 图例效果
![](https://qcloudimg.tencent-cloud.cn/raw/57b3d224fd8e56e3dbbbea1281eae1e0.png)

## 使用方式

1. 从组件列表中拖入 Tab 组件到画布。
![](https://qcloudimg.tencent-cloud.cn/raw/eadaf7337f53eef5da9d8eec4b4d767d.png)
2. 添加标签并设置标签项（详见组件设置）；
3. 单击组件中的标签，切换到当前激活的标签项：
![](https://qcloudimg.tencent-cloud.cn/raw/d38e94b5cb12d38475743160d449a9ed.png)
4. 拖动图表组件到对应的标签项内容区。
![](https://qcloudimg.tencent-cloud.cn/raw/2b1e82273deea33d58d5c5cb15908dca.png)
5. 编辑图表内容（详见各图表组件操作指南）
![](https://qcloudimg.tencent-cloud.cn/raw/a3c5f42d47b66c0a8dc433a1cb7ec48b.png)

## 组件设置

Tab 组件支持以下设置：

<table>
<thead>
<tr>
<th>设置分类</th>
<th>设置项</th>
<th>设置说明</th>
</tr>
</thead>
<tbody><tr>
<td rowspan="4">标签项</td>
<td>标签项名称</td>
<td>可设置标签项显示的名称</td>
</tr>
<tr> 
<td>标签项排序</td>
<td>点击左侧上下箭头进行标签项的排序</td>
</tr>
<tr> 
<td>添加标签</td>
<td>单击可新增一个标签项，最多支持10个标签项</td>
</tr>
<tr> 
<td>删除标签</td>
<td>单击右侧删除图标，可删除一个标签项，最少保留1个标签项</td>
</tr>
<tr>
<td rowspan="3">标签样式</td>
<td>标签对齐</td>
<td>设置标签的对齐方式，提供三种类型供选择：<br>1. 居左<br>2. 居中<br>3. 居右</td>
</tr>
<tr> 
<td>标签形式</td>
<td>设置标签的展现形态，提供两种类型供选择：<br>1. 文字型<br>2. 按钮型</td>
</tr>
<tr> 
<td>保留小数位</td>
<td>设置数值小数位的位数，如“1211.2334”，设置保留小数位为“2”，则展示“1211.23”</td>
</tr>
<tr>
<td rowspan="2"> 标题</td>
<td>显示</td>
<td>开启/关闭显示 tab 标题</td>
</tr>
<tr> 
<td>标题名称</td>
<td>展示 tab 组件的标题名称</td>
</tr>
</tbody></table>


>! 
>1. Tab 组件只支持图表类的组件，不可放置非图表类组件，如文本等。
>2. 每个标签页下只支持放置1个图表组件。
