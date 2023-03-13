# SelectorQuery

查询节点信息的对象

#### 方法

##### [SelectorQuery SelectorQuery.in(Component component)](#in)

将选择器的选取范围更改为自定义组件 `component` 内。（初始时，选择器仅选取页面范围的节点，不会选取任何自定义组件中的节点）。

##### [NodesRef SelectorQuery.select(string selector)](#select)

在当前页面下选择第一个匹配选择器 `selector` 的节点。返回一个 [`NodesRef`](./NodesRef.md#boundingclientrect) 对象实例，可以用于获取节点信息。

##### [NodesRef SelectorQuery.selectAll(string selector)](#selectall)

在当前页面下选择匹配选择器 selector 的所有节点。

##### [NodesRef SelectorQuery.selectViewport()](#selectviewport)

选择显示区域。可用于获取显示区域的尺寸、滚动位置等信息。

##### [NodesRef SelectorQuery.exec(function callback)](#exec)

执行所有的请求。请求结果按请求次序构成数组，在callback的第一个参数中返回。

## exec
### [NodesRef](./NodesRef.md#boundingclientrect) SelectorQuery.exec(function callback)

执行所有的请求。请求结果按请求次序构成数组，在callback的第一个参数中返回。

#### 参数

##### function callback

回调函数

#### 返回值

##### [NodesRef](./NodesRef.md#boundingclientrect)


## in
### [SelectorQuery](#selectorquery) SelectorQuery.in(Component component)


将选择器的选取范围更改为自定义组件 `component` 内。（初始时，选择器仅选取页面范围的节点，不会选取任何自定义组件中的节点）。

#### 参数

##### Component component

自定义组件实例

#### 返回值

##### [SelectorQuery](#selectorquery)

#### 示例代码

```js
Component({
  queryMultipleNodes() {
    const query = wx.createSelectorQuery().in(this)
    query.select('#the-id').boundingClientRect(function (res) {
      res.top // 这个组件内 #the-id 节点的上边界坐标
    }).exec()
  }
})
```

## select
### [NodesRef](./NodesRef.md#boundingclientrect) SelectorQuery.select(string selector)

在当前页面下选择第一个匹配选择器 `selector` 的节点。返回一个 [`NodesRef`](./NodesRef.md#boundingclientrect) 对象实例，可以用于获取节点信息。

#### 参数

##### string selector

选择器

#### 返回值

##### [NodesRef](./NodesRef.md#boundingclientrect)

#### selector 语法

selector类似于 CSS 的选择器，但仅支持下列语法。

* ID选择器：#the-id
* class选择器（可以连续指定多个）：.a-class.another-class
* 子元素选择器：.the-parent > .the-child
* 后代选择器：.the-ancestor .the-descendant
* 跨自定义组件的后代选择器：.the-ancestor >>> .the-descendant
* 多选择器的并集：#a-node, .some-other-nodes

## selectAll
### [NodesRef](./NodesRef.md#boundingclientrect) SelectorQuery.selectAll(string selector)

在当前页面下选择匹配选择器 selector 的所有节点。

#### 参数

##### string selector

选择器

#### 返回值

##### [NodesRef](./NodesRef.md#boundingclientrect)

#### selector 语法

selector类似于 CSS 的选择器，但仅支持下列语法。

* ID选择器：#the-id
* class选择器（可以连续指定多个）：.a-class.another-class
* 子元素选择器：.the-parent > .the-child
* 后代选择器：.the-ancestor .the-descendant
* 跨自定义组件的后代选择器：.the-ancestor >>> .the-descendant
* 多选择器的并集：#a-node, .some-other-nodes


## selectViewport
### [NodesRef](./NodesRef.md#boundingclientrect) SelectorQuery.selectViewport()

选择显示区域。可用于获取显示区域的尺寸、滚动位置等信息。

#### 返回值

##### [NodesRef](./NodesRef.md#boundingclientrect)