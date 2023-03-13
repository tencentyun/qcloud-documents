# IntersectionObserver

IntersectionObserver 对象，用于推断某些节点是否可以被用户看见、有多大比例可以被用户看见。

#### 方法

##### [IntersectionObserver.relativeTo(string selector, Object margins)](#relativeto)

使用选择器指定一个节点，作为参照区域之一。

##### [IntersectionObserver.relativeToViewport(Object margins)](#relativetoviewport)

指定页面显示区域作为参照区域之一

##### [IntersectionObserver.observe(string targetSelector, IntersectionObserver.observeCallback callback)](#observe)

指定目标节点并开始监听相交状态变化情况

##### [IntersectionObserver.disconnect()](#disconnect)

停止监听。回调函数将不再触发

## disconnect
### IntersectionObserver.disconnect()

停止监听。回调函数将不再触发


## observe
### IntersectionObserver.observe(string targetSelector, function callback)

指定目标节点并开始监听相交状态变化情况

#### 参数

##### string targetSelector

选择器

##### function callback

监听相交状态变化的回调函数

###### 参数

**Object res**

属性                 | 类型     | 说明       
------------------ | ------ | ---------
intersectionRatio  | number | 相交比例     
intersectionRect   | Object | 相交区域的边界  
boundingClientRect | Object | 目标边界     
relativeRect       | Object | 参照区域的边界  
time               | number | 相交检测时的时间戳

**res.intersectionRect 的结构**

属性     | 类型     | 说明 
------ | ------ | ---
left   | number | 左边界
right  | number | 右边界
top    | number | 上边界
bottom | number | 下边界

**res.boundingClientRect 的结构**

属性     | 类型     | 说明 
------ | ------ | ---
left   | number | 左边界
right  | number | 右边界
top    | number | 上边界
bottom | number | 下边界

**res.relativeRect 的结构**

属性     | 类型     | 说明 
------ | ------ | ---
left   | number | 左边界
right  | number | 右边界
top    | number | 上边界
bottom | number | 下边界


## relativeTo
### IntersectionObserver.relativeTo(string selector, Object margins)

使用选择器指定一个节点，作为参照区域之一。

#### 参数

##### string selector

选择器

##### Object margins

用来扩展（或收缩）参照节点布局区域的边界

属性     | 类型     | 默认值 | 必填 | 说明        
------ | ------ | --- | -- | ----------
left   | number |     | 否  | 节点布局区域的左边界
right  | number |     | 否  | 节点布局区域的右边界
top    | number |     | 否  | 节点布局区域的上边界
bottom | number |     | 否  | 节点布局区域的下边界

## relativeToViewport
### IntersectionObserver.relativeToViewport(Object margins)

指定页面显示区域作为参照区域之一

#### 参数

##### Object margins

用来扩展（或收缩）参照节点布局区域的边界

属性     | 类型     | 默认值 | 必填 | 说明        
------ | ------ | --- | -- | ----------
left   | number |     | 否  | 节点布局区域的左边界
right  | number |     | 否  | 节点布局区域的右边界
top    | number |     | 否  | 节点布局区域的上边界
bottom | number |     | 否  | 节点布局区域的下边界

#### 示例代码

下面的示例代码中，如果目标节点（用选择器 .target-class 指定）进入显示区域以下 100px 时，就会触发回调函数。

```javascript
Page({
  onLoad() {
    wx.createIntersectionObserver().relativeToViewport({bottom: 100}).observe('.target-class', (res) => {
      res.intersectionRatio // 相交区域占目标节点的布局区域的比例
      res.intersectionRect // 相交区域
      res.intersectionRect.left // 相交区域的左边界坐标
      res.intersectionRect.top // 相交区域的上边界坐标
      res.intersectionRect.width // 相交区域的宽度
      res.intersectionRect.height // 相交区域的高度
    })
  }
})
```