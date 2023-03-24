# NodesRef

用于获取 WXML 节点信息的对象

#### 方法

##### [NodesRef.fields(Object fields)](#fields)

获取节点的相关信息。需要获取的字段在fields中指定。返回值是 `nodesRef` 对应的 `selectorQuery`

##### [SelectorQuery NodesRef.boundingClientRect(NodesRef.boundingClientRectCallback callback)](#boundingClientRect)

添加节点的布局位置的查询请求。相对于显示区域，以像素为单位。其功能类似于 DOM 的 `getBoundingClientRect`。返回 [`NodesRef`](#nodesref) 对应的 [`SelectorQuery`](./SelectorQuery.md#exec)。

##### [SelectorQuery NodesRef.scrollOffset(NodesRef.scrollOffsetCallback callback)](#scrollOffset)

添加节点的滚动位置查询请求。以像素为单位。节点必须是 `scroll-view` 或者 `viewport`，返回 [`NodesRef`](#nodesref) 对应的 [`SelectorQuery`](./SelectorQuery.md#exec)。

##### [SelectorQuery NodesRef.context(NodesRef.contextCallback callback)](#context)

添加节点的 Context 对象查询请求。目前支持[`MapContext`](../media/map/map.md#wx.createmapcontext) 的获取。

<!-- 目前支持 [`VideoContext`](/develop/miniprogram/API/media/video.html#videocontext-2)、[`CanvasContext`](/develop/miniprogram/API/canvas/canvasContext.html#setlinecap)、[`LivePlayerContext`](/develop/miniprogram/API/media/realtimeAudioVideo.html#liveplayercontext-2) 和 [`MapContext`](/develop/miniprogram/API/media/map.html#qq-createmapcontext) 的获取。 -->

##### [SelectorQuery NodesRef.node(NodesRef.nodeCallback callback)](#node)

获取 Node 节点实例。目前支持[ScrollViewContext](../interface/scroll/ScrollViewContext.md) 的获取。
目前支持 [Canvas](/develop/API/canvas/canvas.md) 的获取。

## boundingClientRect

### [SelectorQuery](./SelectorQuery.md#exec) NodesRef.boundingClientRect(function callback)

添加节点的布局位置的查询请求。相对于显示区域，以像素为单位。其功能类似于 DOM 的 `getBoundingClientRect`。返回 [`NodesRef`](#nodesref) 对应的 [`SelectorQuery`](./SelectorQuery.md#exec)。

#### 参数

##### function callback

回调函数，在执行 [`SelectorQuery.exec`](./SelectorQuery.md#exec) 方法后，节点信息会在 `callback` 中返回。

###### 参数

**Object res**

属性      | 类型     | 说明         
------- | ------ | -----------
id      | string | 节点的 ID     
dataset | Object | 节点的 dataset
left    | number | 节点的左边界坐标   
right   | number | 节点的右边界坐标   
top     | number | 节点的上边界坐标   
bottom  | number | 节点的下边界坐标   
width   | number | 节点的宽度      
height  | number | 节点的高度      

#### 返回值

##### [SelectorQuery](./SelectorQuery.md#exec)

#### 示例代码

```js
Page({
  getRect() {
    wx.createSelectorQuery().select('#the-id').boundingClientRect(function (rect) {
      rect.id // 节点的ID
      rect.dataset // 节点的dataset
      rect.left // 节点的左边界坐标
      rect.right // 节点的右边界坐标
      rect.top // 节点的上边界坐标
      rect.bottom // 节点的下边界坐标
      rect.width // 节点的宽度
      rect.height // 节点的高度
    }).exec()
  },
  getAllRects() {
    wx.createSelectorQuery().selectAll('.a-class').boundingClientRect(function (rects) {
      rects.forEach(function (rect) {
        rect.id // 节点的ID
        rect.dataset // 节点的dataset
        rect.left // 节点的左边界坐标
        rect.right // 节点的右边界坐标
        rect.top // 节点的上边界坐标
        rect.bottom // 节点的下边界坐标
        rect.width // 节点的宽度
        rect.height // 节点的高度
      })
    }).exec()
  }
})
```

## context
### [SelectorQuery](./SelectorQuery.md#exec) NodesRef.context(function callback)


添加节点的 Context 对象查询请求。目前支持[`MapContext`](../media/map/map.md#wx.createmapcontext) 的获取。

<!-- 目前支持 [`VideoContext`](/develop/miniprogram/API/media/video.html#videocontext-2)、[`CanvasContext`](/develop/miniprogram/API/canvas/canvasContext.html#setlinecap)、[`LivePlayerContext`](/develop/miniprogram/API/media/realtimeAudioVideo.html#liveplayercontext-2) 和 [`MapContext`](/develop/miniprogram/API/media/map.html#qq-createmapcontext) 的获取。 -->

#### 参数

##### function callback

回调函数，在执行 [`SelectorQuery.exec`](./SelectorQuery.md#exec) 方法后，返回节点信息。

###### 参数

**Object res**

属性      | 类型     | 说明              
------- | ------ | ----------------
context | Object | 节点对应的 Context 对象

#### 返回值

##### [SelectorQuery](./SelectorQuery.md#exec)

#### 示例代码

```js
Page({
  getContext() {
    wx.createSelectorQuery().select('.the-video-class').context(function (res) {
      console.log(res.context) // 节点对应的 Context 对象。如：选中的节点是 <video> 组件，那么此处即返回 VideoContext 对象
    }).exec()
  }
})
```

## fields
### NodesRef.fields(Object fields)

获取节点的相关信息。需要获取的字段在fields中指定。返回值是 `nodesRef` 对应的 `selectorQuery`

#### 参数

##### Object fields

属性            | 类型             | 默认值   | 必填 | 说明                                                                      | 最低版本                                                                                                              
------------- | -------------- | ----- | -- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------
id            | boolean        | false | 否  | 是否返回节点 id                                                               |                                                                                                                   
dataset       | boolean        | false | 否  | 是否返回节点 dataset                                                          |                                                                                                                   
rect          | boolean        | false | 否  | 是否返回节点布局位置（`left` `right` `top` `bottom`）                               |                                                                                                                   
size          | boolean        | false | 否  | 是否返回节点尺寸（`width` `height`）                                              |                                                                                                                   
scrollOffset  | boolean        | false | 否  | 否 是否返回节点的 `scrollLeft` `scrollTop`，节点必须是 `scroll-view` 或者 `viewport`    |                                                                                                                   
properties    | Array.\<string\> | []    | 否  | 指定属性名列表，返回节点对应属性名的当前属性值（只能获得组件文档中标注的常规属性值，id class style 和事件绑定的属性值不可获取） |                                                                                                                   
computedStyle | Array.\<string\> | []    | 否  | 指定样式名列表，返回节点对应样式名的当前值                                                   | 
context       | boolean        | false | 否  | 是否返回节点对应的 Context 对象                                                    | 

#### 注意

computedStyle 的优先级高于 size，当同时在 computedStyle 里指定了 width/height 和传入了 size: true，则优先返回 computedStyle 获取到的 width/height。

#### 示例代码

```js
Page({
  getFields() {
    wx.createSelectorQuery().select('#the-id').fields({
      dataset: true,
      size: true,
      scrollOffset: true,
      properties: ['scrollX', 'scrollY'],
      computedStyle: ['margin', 'backgroundColor'],
      context: true,
    }, function (res) {
      res.dataset // 节点的dataset
      res.width // 节点的宽度
      res.height // 节点的高度
      res.scrollLeft // 节点的水平滚动位置
      res.scrollTop // 节点的竖直滚动位置
      res.scrollX // 节点 scroll-x 属性的当前值
      res.scrollY // 节点 scroll-y 属性的当前值
      // 此处返回指定要返回的样式名
      res.margin
      res.backgroundColor
      res.context // 节点对应的 Context 对象
    }).exec()
  }
})
```

### Node

### [SelectorQuery](./SelectorQuery.md#exec) NodesRef.Node(function callback)

获取 Node 节点实例。目前支持[ScrollViewContext](../interface/scroll/ScrollViewContext.md) 的获取。
目前支持 [Canvas](/develop/API/canvas/canvas.md) 的获取。

#### 参数

##### function callback

回调函数，在执行 `SelectorQuery.exec` 方法后，返回节点信息。

###### 参数

##### Object res

| 属性 | 类型   | 说明                 |
| :--- | :----- | :------------------- |
| node | Object | 节点对应的 Node 实例 |

#### 返回值

##### [SelectorQuery](./SelectorQuery.md)

#### 示例代码

```js
Page({
  getNode() {
    wx.createSelectorQuery().select('.canvas').node(function(res){
      console.log(res.node) // 节点对应的 Canvas 实例。
    }).exec()
  }
})
```

## scrollOffset

### [SelectorQuery](./SelectorQuery.md#exec) NodesRef.scrollOffset(function callback)

添加节点的滚动位置查询请求。以像素为单位。节点必须是 `scroll-view` 或者 `viewport`，返回 [`NodesRef`](#nodesref) 对应的 [`SelectorQuery`](./SelectorQuery.md#exec)。

#### 参数

##### function callback

回调函数，在执行 [`SelectorQuery.exec`](./SelectorQuery.md#exec) 方法后，节点信息会在 `callback` 中返回。

###### 参数

**Object res**

属性         | 类型     | 说明         
---------- | ------ | -----------
id         | string | 节点的 ID     
dataset    | Object | 节点的 dataset
scrollLeft | number | 节点的水平滚动位置  
scrollTop  | number | 节点的竖直滚动位置  

#### 返回值

##### [SelectorQuery](./SelectorQuery.md)

#### 示例代码

```js
Page({
  getScrollOffset() {
    wx.createSelectorQuery().selectViewport().scrollOffset(function (res) {
      res.id // 节点的ID
      res.dataset // 节点的dataset
      res.scrollLeft // 节点的水平滚动位置
      res.scrollTop // 节点的竖直滚动位置
    }).exec()
  }
})
```