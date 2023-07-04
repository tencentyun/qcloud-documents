一个组件的事件由触发条件以及执行动作两部分构成，执行动作又分为 [平台方法](https://cloud.tencent.com/document/product/1301/61120) 和自定义方法，本文章主要对触发条件及对应 event 对象进行介绍说明。


## 什么是 event 对象
在微搭中，当一个组件的触发条件被触发时则会返回该触发条件的 event 对象，触发条件不同，返回的 event 对象中存储的值也不同，我们可以通过获取 event 对象中的值来实现一些常见功能。
我们可以通过自定义 JS 方法来打印 event，查看其结构，下文为打印 event 的示例：
1. 通过左下角的代码区添加一个自定义 Javascript 方法，代码内容如下，保存后命名为 eventLog，示例如下：
```
export default function({event, data}) {
  console.log(event);
}
```
2. 在编辑区拖入任意一个组件，如单行输入组件，然后在按钮绑定一个点击事件，事件动作选择 **Javascript 代码方法**节点，然后下拉方法列表中选择刚刚新建的 eventLog 方法。
3. 在输入框中进行输入改变的操作，查看下方开发调试工具（**面板** > **开发调试工具**）控制台中的查看打印信息。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/339109084f9a972cbeddaaae88cf39e3.png" />
4. 根据上图所示，我们便可以在编辑器中通过使用 `event.detail.value` 来调用当前触发条件所返回的值。


## 不同组件的事件触发时返回的 event 对象

### 单行输入
<table>
<thead>
<tr><th style = "width:50%">事件</th>
<th>event.detail</th>
</tr>
</thead>
<tbody>
<tr><td>change（输入改变）</td>
<td>{ value: string }， value 为输入的新值</td>
</tr>
<tr>
<td>focus（聚焦）</td>
<td>{ value: string }，value 为当前输入框的值</td>
</tr>
<tr>
<td>blur（失焦）</td>
<td>{ value: string }，value 为当前输入框的值</td>
</tr>
<tr>
<td>confirm（确认）</td>
<td>{ value: string }，value 为当前输入框的值</td>
</tr>
<tr>
<td>clear（清除内容）</td>
<td>{ originValue: string }，originValue 为清除前输入框的值</td>
</tr>
</tbody>
</table>


###  多选
<table>
<thead>
<tr>
<th style = "width:50%">事件</th>
<th>event.detail</th>
</tr>
</thead>
<tbody>
<tr>
<td>change（选中状态改变）</td>
<td>{ value: string[] }，value 为当前选中状态的值的集合</td>
</tr>
</tbody>
</table>

### 单选
<table>
<thead>
<tr><th style = "width:50%">事件</th>
<th>event.detail</th>
</tr>
</thead>
<tbody>
<tr>
<td>change（选中状态改变）</td>
<td>{ value: boolean }，value 为当前选中状态</td>
</tr>
</tbody>
</table>

### 下拉选择
<table>
<thead>
<tr><th style = "width:50%">事件</th>
<th>event.detail</th>
</tr>
</thead>
<tbody>
<tr>
<td>change（值改变）</td>
<td>{ value: string }，value 为当前选中的值</td>
</tr>
</tbody>
</table>

### 更多组件
其余更多组件对应的触发条件以及返回的 event 对象结构，请参见 [组件列表](https://docs.cloudbase.net/lowcode/components/) 中的**事件**部分，例如查看 [开关组件](https://docs.cloudbase.net/lowcode/components/wedaUI/src/docs/compsdocs/form/WdSwitch#%E4%BA%8B%E4%BB%B6) 的事件介绍。
