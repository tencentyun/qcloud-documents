# CanvasContext

canvas 组件的绘图上下文

#### 属性

##### string fillStyle



填充颜色。用法同 CanvasContext.setFillStyle()。

##### string strokeStyle



边框颜色。用法同 CanvasContext.setFillStyle()。

##### number shadowOffsetX



阴影相对于形状在水平方向的偏移

##### number shadowOffsetY



阴影相对于形状在竖直方向的偏移

##### number shadowColor



阴影的颜色

##### number shadowBlur



阴影的模糊级别

##### number lineWidth



线条的宽度。用法同 CanvasContext.setLineWidth()。

##### number lineCap



线条的端点样式。用法同 [CanvasContext.setLineCap()](#setlinecap)。

##### number lineJoin



线条的交点样式。用法同 CanvasContext.setLineJoin()。

##### number miterLimit



最大斜接长度。用法同 CanvasContext.setMiterLimit()。

##### number lineDashOffset



虚线偏移量，初始值为0

##### string font



当前字体样式的属性。符合 [CSS font 语法](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font) 的 DOMString 字符串，至少需要提供字体大小和字体族名。默认值为 10px sans-serif。

##### number globalAlpha

全局画笔透明度。范围 0-1，0 表示完全透明，1 表示完全不透明。

##### string globalCompositeOperation



在绘制新形状时应用的合成操作的类型。目前安卓版本只适用于 `fill` 填充块的合成，用于 `stroke` 线段的合成效果都是 `source-over`。

目前支持的操作有

* 安卓：xor, source-over, source-atop, destination-out, lighter, overlay, darken, lighten, hard-light
* iOS：xor, source-over, source-atop, destination-over, destination-out, lighter, multiply, overlay, darken, lighten, color-dodge, color-burn, hard-light, soft-light, difference, exclusion, saturation, luminosity

#### 方法

##### [CanvasContext.draw(boolean reserve, function callback)](#draw)

将之前在绘图上下文中的描述（路径、变形、样式）画到 canvas 中。

##### [CanvasGradient CanvasContext.createLinearGradient(number x0, number y0, number x1, number y1)](#createlineargradient)

创建一个线性的渐变颜色。返回的[`CanvasGradient`](./canvasGradient.md)对象需要使用 CanvasGradient.addColorStop() 来指定渐变点，至少要两个。

##### [CanvasGradient CanvasContext.createCircularGradient(number x, number y, number r)](#createcirculargradient)

创建一个圆形的渐变颜色。起点在圆心，终点在圆环。返回的[`CanvasGradient`](./canvasGradient.md)对象需要使用 [CanvasGradient.addColorStop()](./canvasGradient.md#addcolorstop) 来指定渐变点，至少要两个。

##### [CanvasContext.createPattern(string image, string repetition)](#createpattern)

对指定的图像创建模式的方法，可在指定的方向上重复元图像

##### [Object CanvasContext.measureText(string text)](#measuretext)

测量文本尺寸信息。目前仅返回文本宽度。同步接口。

##### [CanvasContext.save()](#save)

保存绘图上下文。

##### [CanvasContext.restore()](#restore)

恢复之前保存的绘图上下文。

##### [CanvasContext.beginPath()](#beginpath)

开始创建一个路径。需要调用 `fill` 或者 `stroke` 才会使用路径进行填充或描边

* 在最开始的时候相当于调用了一次 `beginPath`。
* 同一个路径内的多次 `setFillStyle`、`setStrokeStyle`、`setLineWidth`等设置，以最后一次设置为准。

##### [CanvasContext.moveTo(number x, number y)](#moveto)

把路径移动到画布中的指定点，不创建线条。用 `stroke` 方法来画线条

##### [CanvasContext.lineTo(number x, number y)](#lineto)

增加一个新点，然后创建一条从上次指定点到目标点的线。用 `stroke` 方法来画线条

##### [CanvasContext.quadraticCurveTo(number cpx, number cpy, number x, number y)](#quadraticcurveto)

创建二次贝塞尔曲线路径。曲线的起始点为路径中前一个点。

##### [CanvasContext.bezierCurveTo()](#beziercurveto)

创建三次方贝塞尔曲线路径。曲线的起始点为路径中前一个点。

##### [CanvasContext.arc(number x, number y, number r, number sAngle, number eAngle, number counterclockwise)](#arc)

创建一条弧线。

* 创建一个圆可以指定起始弧度为 0，终止弧度为 2 * Math.PI。
* 用 `stroke` 或者 `fill` 方法来在 `canvas` 中画弧线。

##### [CanvasContext.rect(number x, number y, number width, number height)](#rect)

创建一个矩形路径。需要用 [`fill`](#fill) 或者 [`stroke`](#stroke) 方法将矩形真正的画到 `canvas` 中

##### [CanvasContext.arcTo(number x1, number y1, number x2, number y2, number radius)](#arcto)

根据控制点和半径绘制圆弧路径。

##### [CanvasContext.clip()](#clip)

从原始画布中剪切任意形状和尺寸。一旦剪切了某个区域，则所有之后的绘图都会被限制在被剪切的区域内（不能访问画布上的其他区域）。可以在使用 `clip` 方法前通过使用 `save` 方法对当前画布区域进行保存，并在以后的任意时间通过`restore`方法对其进行恢复。

##### [CanvasContext.fillRect(number x, number y, number width, number height)](#fillrect)

填充一个矩形。用 [`setFillStyle`](#setfillstyle) 设置矩形的填充色，如果没设置默认是黑色。

##### [CanvasContext.strokeRect(number x, number y, number width, number height)](#strokerect)

画一个矩形(非填充)。 用 [`setStrokeStyle`](#setstrokestyle) 设置矩形线条的颜色，如果没设置默认是黑色。

##### [CanvasContext.clearRect(number x, number y, number width, number height)](#clearrect)

清除画布上在该矩形区域内的内容

##### [CanvasContext.fill()](#fill)

对当前路径中的内容进行填充。默认的填充色为黑色。

##### [CanvasContext.stroke()](#stroke)

画出当前路径的边框。默认颜色色为黑色。

##### [CanvasContext.closePath()](#closepath)

关闭一个路径。会连接起点和终点。如果关闭路径后没有调用 `fill` 或者 `stroke` 并开启了新的路径，那之前的路径将不会被渲染。

##### [CanvasContext.scale(number scaleWidth, number scaleHeight)](#scale)

在调用后，之后创建的路径其横纵坐标会被缩放。多次调用倍数会相乘。

##### [CanvasContext.rotate(number rotate)](#rotate)

以原点为中心顺时针旋转当前坐标轴。多次调用旋转的角度会叠加。原点可以用 `translate` 方法修改。

##### [CanvasContext.translate(number x, number y)](#translate)

对当前坐标系的原点 (0, 0) 进行变换。默认的坐标系原点为页面左上角。

##### [CanvasContext.drawImage(string imageResource, number sx, number sy, number sWidth, number sHeight, number dx, number dy, number dWidth, number dHeight)](#drawimage)

绘制图像到画布

##### [CanvasContext.strokeText(string text, number x, number y, number maxWidth)](#stroketext)

给定的 (x, y) 位置绘制文本描边的方法

##### [CanvasContext.transform(number scaleX, number scaleY, number skewX, number skewY, number translateX, number translateY)](#transform)

使用矩阵多次叠加当前变换的方法

##### [CanvasContext.setTransform(number scaleX, number scaleY, number skewX, number skewY, number translateX, number translateY)](#settransform)

使用矩阵重新设置（覆盖）当前变换的方法

##### [CanvasContext.setFillStyle(Color color)](#setfillstyle)

设置填充色。

##### [CanvasContext.setStrokeStyle(Color color)](#setstrokestyle)

设置描边颜色。

##### [CanvasContext.setShadow(number offsetX, number offsetY, number blur, string color)](#setshadow)

设定阴影样式。

##### [CanvasContext.setGlobalAlpha(number alpha)](#setglobalalpha)

设置全局画笔透明度。

##### [CanvasContext.setLineWidth(number lineWidth)](#setlinewidth)

设置线条的宽度

##### [CanvasContext.setLineJoin(string lineJoin)](#setlinejoin)

设置线条的交点样式

##### [CanvasContext.setLineCap(string lineCap)](#setlinecap)

设置线条的端点样式

##### [CanvasContext.setLineDash(Array.&lt;number&gt; pattern, number offset)](#setlinedash)

设置虚线样式。

##### [CanvasContext.setMiterLimit(number miterLimit)](#setmiterlimit)

设置最大斜接长度。斜接长度指的是在两条线交汇处内角和外角之间的距离。当 [CanvasContext.setLineJoin()](#setlinejoin) 为 miter 时才有效。超过最大倾斜长度的，连接处将以 lineJoin 为 bevel 来显示。

##### [CanvasContext.fillText(string text, number x, number y, number maxWidth)](#filltext)

在画布上绘制被填充的文本

##### [CanvasContext.setFontSize(number fontSize)](#setfontsize)

设置字体的字号

##### [CanvasContext.setTextAlign(string align)](#settextalign)

设置文字的对齐

##### [CanvasContext.setTextBaseline(string textBaseline)](#settextbaseline)

设置文字的竖直对齐

## setLineCap

#### CanvasContext.setLineCap(string lineCap)


设置线条的端点样式

#### 参数

##### string lineCap

线条的结束端点样式

**lineCap 的合法值**

值      | 说明              
------ | ----------------
butt   | 向线条的每个末端添加平直的边缘。
round  | 向线条的每个末端添加圆形线帽。 
square | 向线条的每个末端添加正方形线帽。

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.beginPath()
ctx.moveTo(10, 10)
ctx.lineTo(150, 10)
ctx.stroke()

ctx.beginPath()
ctx.setLineCap('butt')
ctx.setLineWidth(10)
ctx.moveTo(10, 30)
ctx.lineTo(150, 30)
ctx.stroke()

ctx.beginPath()
ctx.setLineCap('round')
ctx.setLineWidth(10)
ctx.moveTo(10, 50)
ctx.lineTo(150, 50)
ctx.stroke()

ctx.beginPath()
ctx.setLineCap('square')
ctx.setLineWidth(10)
ctx.moveTo(10, 70)
ctx.lineTo(150, 70)
ctx.stroke()

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155252_rc4bz1nT7u.png?t=19022220)

## setTextAlign

#### CanvasContext.setTextAlign(string align)


设置文字的对齐

#### 参数

##### string align

文字的对齐方式

**align 的合法值**

值      | 说明  
------ | ----
left   | 左对齐 
center | 居中对齐
right  | 右对齐 

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.setStrokeStyle('red')
ctx.moveTo(150, 20)
ctx.lineTo(150, 170)
ctx.stroke()

ctx.setFontSize(15)
ctx.setTextAlign('left')
ctx.fillText('textAlign=left', 150, 60)

ctx.setTextAlign('center')
ctx.fillText('textAlign=center', 150, 80)

ctx.setTextAlign('right')
ctx.fillText('textAlign=right', 150, 100)

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426160101_HSgFcwon20.png?t=19022220)

## setTextBaseline

#### CanvasContext.setTextBaseline(string textBaseline)

设置文字的竖直对齐

#### 参数

##### string textBaseline

文字的竖直对齐方式

**textBaseline 的合法值**

值      | 说明  
------ | ----
top    | 顶部对齐
bottom | 底部对齐
middle | 居中对齐
normal |     

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.setStrokeStyle('red')
ctx.moveTo(5, 75)
ctx.lineTo(295, 75)
ctx.stroke()

ctx.setFontSize(20)

ctx.setTextBaseline('top')
ctx.fillText('top', 5, 75)

ctx.setTextBaseline('middle')
ctx.fillText('middle', 50, 75)

ctx.setTextBaseline('bottom')
ctx.fillText('bottom', 120, 75)

ctx.setTextBaseline('normal')
ctx.fillText('normal', 200, 75)

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426160045_t4oB1z0n7Q.png?t=19022220)

## setTransform

#### CanvasContext.setTransform(number scaleX, number scaleY, number skewX, number skewY, number translateX, number translateY)



使用矩阵重新设置（覆盖）当前变换的方法

#### 参数

##### number scaleX

水平缩放

##### number scaleY

垂直缩放

##### number skewX

水平倾斜

##### number skewY

垂直倾斜

##### number translateX

水平移动

##### number translateY

垂直移动

## stroke

#### CanvasContext.stroke()

画出当前路径的边框。默认颜色色为黑色。

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.moveTo(10, 10)
ctx.lineTo(100, 10)
ctx.lineTo(100, 100)
ctx.stroke()
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155939_w00RkYRl3f.png?t=19022220)

stroke() 描绘的路径是从 beginPath() 开始计算，但是不会将 strokeRect() 包含进去。

```javascript
const ctx = wx.createCanvasContext('myCanvas')
// begin path
ctx.rect(10, 10, 100, 30)
ctx.setStrokeStyle('yellow')
ctx.stroke()

// begin another path
ctx.beginPath()
ctx.rect(10, 40, 100, 30)

// only stoke this rect, not in current path
ctx.setStrokeStyle('blue')
ctx.strokeRect(10, 70, 100, 30)

ctx.rect(10, 100, 100, 30)

// it will stroke current path
ctx.setStrokeStyle('red')
ctx.stroke()
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155918_sQsd7PUkEi.png?t=19022220)

## strokeRect

#### CanvasContext.strokeRect(number x, number y, number width, number height)

画一个矩形(非填充)。 用 [`setStrokeStyle`](#setstrokestyle) 设置矩形线条的颜色，如果没设置默认是黑色。

#### 参数

##### number x

矩形路径左上角的横坐标

##### number y

矩形路径左上角的纵坐标

##### number width

矩形路径的宽度

##### number height

矩形路径的高度

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.setStrokeStyle('red')
ctx.strokeRect(10, 10, 150, 75)
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155856_TbK8e2b18y.png?t=19022220)

## strokeText

#### CanvasContext.strokeText(string text, number x, number y, number maxWidth)



给定的 (x, y) 位置绘制文本描边的方法

#### 参数

##### string text

要绘制的文本

##### number x

文本起始点的 x 轴坐标

##### number y

文本起始点的 y 轴坐标

##### number maxWidth

需要绘制的最大宽度，可选

## transform

#### CanvasContext.transform(number scaleX, number scaleY, number skewX, number skewY, number translateX, number translateY)



使用矩阵多次叠加当前变换的方法

#### 参数

##### number scaleX

水平缩放

##### number scaleY

垂直缩放

##### number skewX

水平倾斜

##### number skewY

垂直倾斜

##### number translateX

水平移动

##### number translateY

垂直移动

## translate

#### CanvasContext.translate(number x, number y)

对当前坐标系的原点 (0, 0) 进行变换。默认的坐标系原点为页面左上角。

#### 参数

##### number x

水平坐标平移量

##### number y

竖直坐标平移量

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.strokeRect(10, 10, 150, 100)
ctx.translate(20, 20)
ctx.strokeRect(10, 10, 150, 100)
ctx.translate(20, 20)
ctx.strokeRect(10, 10, 150, 100)

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155809_8N4eejDAJ9.png?t=19022220)

## arc

#### CanvasContext.arc(number x, number y, number r, number sAngle, number eAngle, number counterclockwise)

创建一条弧线。

* 创建一个圆可以指定起始弧度为 0，终止弧度为 2 * Math.PI。
* 用 `stroke` 或者 `fill` 方法来在 `canvas` 中画弧线。

#### 参数

##### number x

圆心的 x 坐标

##### number y

圆心的 y 坐标

##### number r

圆的半径

##### number sAngle

起始弧度，单位弧度（在3点钟方向）

##### number eAngle

终止弧度

##### number counterclockwise

弧度的方向是否是逆时针

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

// Draw coordinates
ctx.arc(100, 75, 50, 0, 2 * Math.PI)
ctx.setFillStyle('#EEEEEE')
ctx.fill()

ctx.beginPath()
ctx.moveTo(40, 75)
ctx.lineTo(160, 75)
ctx.moveTo(100, 15)
ctx.lineTo(100, 135)
ctx.setStrokeStyle('#AAAAAA')
ctx.stroke()

ctx.setFontSize(12)
ctx.setFillStyle('black')
ctx.fillText('0', 165, 78)
ctx.fillText('0.5*PI', 83, 145)
ctx.fillText('1*PI', 15, 78)
ctx.fillText('1.5*PI', 83, 10)

// Draw points
ctx.beginPath()
ctx.arc(100, 75, 2, 0, 2 * Math.PI)
ctx.setFillStyle('lightgreen')
ctx.fill()

ctx.beginPath()
ctx.arc(100, 25, 2, 0, 2 * Math.PI)
ctx.setFillStyle('blue')
ctx.fill()

ctx.beginPath()
ctx.arc(150, 75, 2, 0, 2 * Math.PI)
ctx.setFillStyle('red')
ctx.fill()

// Draw arc
ctx.beginPath()
ctx.arc(100, 75, 50, 0, 1.5 * Math.PI)
ctx.setStrokeStyle('#333333')
ctx.stroke()

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155251_6K0rRHWq6C.png?t=19022220)

针对 arc(100, 75, 50, 0, 1.5 * Math.PI)的三个关键坐标如下：

* 绿色: 圆心 (100, 75)
* 红色: 起始弧度 (0)
* 蓝色: 终止弧度 (1.5 * Math.PI)

## arcTo

#### CanvasContext.arcTo(number x1, number y1, number x2, number y2, number radius)



根据控制点和半径绘制圆弧路径。

#### 参数

##### number x1

第一个控制点的 x 轴坐标

##### number y1

第一个控制点的 y 轴坐标

##### number x2

第二个控制点的 x 轴坐标

##### number y2

第二个控制点的 y 轴坐标

##### number radius

圆弧的半径

## beginPath

#### CanvasContext.beginPath()

开始创建一个路径。需要调用 `fill` 或者 `stroke` 才会使用路径进行填充或描边

* 在最开始的时候相当于调用了一次 `beginPath`。
* 同一个路径内的多次 `setFillStyle`、`setStrokeStyle`、`setLineWidth`等设置，以最后一次设置为准。

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
// begin path
ctx.rect(10, 10, 100, 30)
ctx.setFillStyle('yellow')
ctx.fill()

// begin another path
ctx.beginPath()
ctx.rect(10, 40, 100, 30)

// only fill this rect, not in current path
ctx.setFillStyle('blue')
ctx.fillRect(10, 70, 100, 30)

ctx.rect(10, 100, 100, 30)

// it will fill current path
ctx.setFillStyle('red')
ctx.fill()
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155252_qixt5D1FCO.png?t=19022220)

## bezierCurveTo

#### CanvasContext.bezierCurveTo()

创建三次方贝塞尔曲线路径。曲线的起始点为路径中前一个点。

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

// Draw points
ctx.beginPath()
ctx.arc(20, 20, 2, 0, 2 * Math.PI)
ctx.setFillStyle('red')
ctx.fill()

ctx.beginPath()
ctx.arc(200, 20, 2, 0, 2 * Math.PI)
ctx.setFillStyle('lightgreen')
ctx.fill()

ctx.beginPath()
ctx.arc(20, 100, 2, 0, 2 * Math.PI)
ctx.arc(200, 100, 2, 0, 2 * Math.PI)
ctx.setFillStyle('blue')
ctx.fill()

ctx.setFillStyle('black')
ctx.setFontSize(12)

// Draw guides
ctx.beginPath()
ctx.moveTo(20, 20)
ctx.lineTo(20, 100)
ctx.lineTo(150, 75)

ctx.moveTo(200, 20)
ctx.lineTo(200, 100)
ctx.lineTo(70, 75)
ctx.setStrokeStyle('#AAAAAA')
ctx.stroke()

// Draw quadratic curve
ctx.beginPath()
ctx.moveTo(20, 20)
ctx.bezierCurveTo(20, 100, 200, 100, 200, 20)
ctx.setStrokeStyle('black')
ctx.stroke()

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155251_TVCqdvVdgN.png?t=19022220)

针对 moveTo(20, 20) bezierCurveTo(20, 100, 200, 100, 200, 20) 的三个关键坐标如下：

* 红色：起始点(20, 20)
* 蓝色：两个控制点(20, 100) (200, 100)
* 绿色：终止点(200, 20)

## clearRect

#### CanvasContext.clearRect(number x, number y, number width, number height)

清除画布上在该矩形区域内的内容

#### 参数

##### number x

矩形路径左上角的横坐标

##### number y

矩形路径左上角的纵坐标

##### number width

矩形路径的宽度

##### number height

矩形路径的高度

#### 示例代码

clearRect 并非画一个白色的矩形在地址区域，而是清空，为了有直观感受，对 canvas 加了一层背景色。

```html
<canvas canvas-id="myCanvas" style="border: 1px solid; background: #123456;" />
```

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.setFillStyle('red')
ctx.fillRect(0, 0, 150, 200)
ctx.setFillStyle('blue')
ctx.fillRect(150, 0, 150, 200)
ctx.clearRect(10, 10, 150, 75)
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155251_tSjsl9dk0O.png?t=19022220)

## clip

#### CanvasContext.clip()


从原始画布中剪切任意形状和尺寸。一旦剪切了某个区域，则所有之后的绘图都会被限制在被剪切的区域内（不能访问画布上的其他区域）。可以在使用 `clip` 方法前通过使用 `save` 方法对当前画布区域进行保存，并在以后的任意时间通过`restore`方法对其进行恢复。

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

wx.downloadFile({
  url: 'https://is5.mzstatic.com/image/thumb/Purple128/v4/75/3b/90/753b907c-b7fb-5877-215a-759bd73691a4/source/50x50bb.jpg',
  success(res) {
    ctx.save()
    ctx.beginPath()
    ctx.arc(50, 50, 25, 0, 2 * Math.PI)
    ctx.clip()
    ctx.drawImage(res.tempFilePath, 25, 25)
    ctx.restore()
    ctx.draw()
  }
})
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426161854_sCWX2VK2iy.png?t=19022220)

## closePath

#### CanvasContext.closePath()

关闭一个路径。会连接起点和终点。如果关闭路径后没有调用 `fill` 或者 `stroke` 并开启了新的路径，那之前的路径将不会被渲染。

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.moveTo(10, 10)
ctx.lineTo(100, 10)
ctx.lineTo(100, 100)
ctx.closePath()
ctx.stroke()
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155251_8Yu1TQx63D.png?t=19022220)

```javascript
const ctx = wx.createCanvasContext('myCanvas')
// begin path
ctx.rect(10, 10, 100, 30)
ctx.closePath()

// begin another path
ctx.beginPath()
ctx.rect(10, 40, 100, 30)

// only fill this rect, not in current path
ctx.setFillStyle('blue')
ctx.fillRect(10, 70, 100, 30)

ctx.rect(10, 100, 100, 30)

// it will fill current path
ctx.setFillStyle('red')
ctx.fill()
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155251_LEpr2JZV82.png?t=19022220)

## createCircularGradient

#### [CanvasGradient](./canvasGradient.md) CanvasContext.createCircularGradient(number x, number y, number r)

创建一个圆形的渐变颜色。起点在圆心，终点在圆环。返回的[`CanvasGradient`](./canvasGradient.md)对象需要使用 [CanvasGradient.addColorStop()](./canvasGradient.md#addcolorstop) 来指定渐变点，至少要两个。

#### 参数

##### number x

圆心的 x 坐标

##### number y

圆心的 y 坐标

##### number r

圆的半径

#### 返回值

##### [CanvasGradient](./canvasGradient.md)

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

// Create circular gradient
const grd = ctx.createCircularGradient(75, 50, 50)
grd.addColorStop(0, 'red')
grd.addColorStop(1, 'white')

// Fill with gradient
ctx.setFillStyle(grd)
ctx.fillRect(10, 10, 150, 80)
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155251_735dS5IEGB.png?t=19022220)

## createLinearGradient

#### [CanvasGradient](./canvasGradient.md) CanvasContext.createLinearGradient(number x0, number y0, number x1, number y1)

创建一个线性的渐变颜色。返回的[`CanvasGradient`](./canvasGradient.md)对象需要使用 [CanvasGradient.addColorStop()](./canvasGradient.md#addcolorstop) 来指定渐变点，至少要两个。

#### 参数

##### number x0

起点的 x 坐标

##### number y0

起点的 y 坐标

##### number x1

终点的 x 坐标

##### number y1

终点的 y 坐标

#### 返回值

##### [CanvasGradient](./canvasGradient.md)

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

// Create linear gradient
const grd = ctx.createLinearGradient(0, 0, 200, 0)
grd.addColorStop(0, 'red')
grd.addColorStop(1, 'white')

// Fill with gradient
ctx.setFillStyle(grd)
ctx.fillRect(10, 10, 150, 80)
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155252_IK1kOmUpli.png?t=19022220)

## createPattern

#### CanvasContext.createPattern(string image, string repetition)



对指定的图像创建模式的方法，可在指定的方向上重复元图像

#### 参数

##### string image

重复的图像源，仅支持包内路径和临时路径

##### string repetition

如何重复图像

**repetition 的合法值**

值         | 说明       
--------- | ---------
repeat    | 水平竖直方向都重复
repeat-x  | 水平方向重复   
repeat-y  | 竖直方向重复   
no-repeat | 不重复      

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
const pattern = ctx.createPattern('/path/to/image', 'repeat-x')
ctx.fillStyle = pattern
ctx.fillRect(0, 0, 300, 150)
ctx.draw()
```

## draw

#### CanvasContext.draw(boolean reserve, function callback)

将之前在绘图上下文中的描述（路径、变形、样式）画到 canvas 中。

#### 参数

##### boolean reserve

本次绘制是否接着上一次绘制。即 reserve 参数为 false，则在本次调用绘制之前 native 层会先清空画布再继续绘制；若 reserve 参数为 true，则保留当前画布上的内容，本次调用 drawCanvas 绘制的内容覆盖在上面，默认 false。

##### function callback

绘制完成后执行的回调函数

#### 示例代码

第二次 draw() reserve 为 true。所以保留了上一次的绘制结果，在上下文设置的 fillStyle 'red' 也变成了默认的 'black'。

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.setFillStyle('red')
ctx.fillRect(10, 10, 150, 100)
ctx.draw()
ctx.fillRect(50, 50, 150, 100)
ctx.draw(true)
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426160211_ICNGloZalb.png?t=19022220)

#### 示例代码

第二次 draw() reserve 为 false。所以没有保留了上一次的绘制结果和在上下文设置的 fillStyle 'red'。

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.setFillStyle('red')
ctx.fillRect(10, 10, 150, 100)
ctx.draw()
ctx.fillRect(50, 50, 150, 100)
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155730_KOLw7ZHl6W.png?t=19022220)

## drawImage

#### CanvasContext.drawImage(string imageResource, number sx, number sy, number sWidth, number sHeight, number dx, number dy, number dWidth, number dHeight)

绘制图像到画布

#### 参数

##### string imageResource

所要绘制的图片资源

##### number sx

源图像的矩形选择框的左上角 x 坐标

##### number sy

源图像的矩形选择框的左上角 y 坐标

##### number sWidth

源图像的矩形选择框的宽度

##### number sHeight

源图像的矩形选择框的高度

##### number dx

图像的左上角在目标 canvas 上 x 轴的位置

##### number dy

图像的左上角在目标 canvas 上 y 轴的位置

##### number dWidth

在目标画布上绘制图像的宽度，允许对绘制的图像进行缩放

##### number dHeight

在目标画布上绘制图像的高度，允许对绘制的图像进行缩放

#### 示例代码

有三个版本的写法：

* drawImage(imageResource, dx, dy)
* drawImage(imageResource, dx, dy, dWidth, dHeight)
* drawImage(imageResource, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight) 

```javascript
const ctx = wx.createCanvasContext('myCanvas')

wx.chooseImage({
  success(res) {
    ctx.drawImage(res.tempFilePaths[0], 0, 0, 150, 100)
    ctx.draw()
  }
})
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155252_5haIPTLDll.png?t=19022220)

## fill

#### CanvasContext.fill()

对当前路径中的内容进行填充。默认的填充色为黑色。

#### 示例代码

如果当前路径没有闭合，fill() 方法会将起点和终点进行连接，然后填充。

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.moveTo(10, 10)
ctx.lineTo(100, 10)
ctx.lineTo(100, 100)
ctx.fill()
ctx.draw()
```

fill() 填充的路径是从 beginPath() 开始计算，但是不会将 fillRect() 包含进去。

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155251_Rb0JHP3Mro.png?t=19022220)

```javascript
const ctx = wx.createCanvasContext('myCanvas')
// begin path
ctx.rect(10, 10, 100, 30)
ctx.setFillStyle('yellow')
ctx.fill()

// begin another path
ctx.beginPath()
ctx.rect(10, 40, 100, 30)

// only fill this rect, not in current path
ctx.setFillStyle('blue')
ctx.fillRect(10, 70, 100, 30)

ctx.rect(10, 100, 100, 30)

// it will fill current path
ctx.setFillStyle('red')
ctx.fill()
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155252_qixt5D1FCO.png?t=19022220)

## fillRect

#### CanvasContext.fillRect(number x, number y, number width, number height)

填充一个矩形。用 [`setFillStyle`](#setfillstyle) 设置矩形的填充色，如果没设置默认是黑色。

#### 参数

##### number x

矩形路径左上角的横坐标

##### number y

矩形路径左上角的纵坐标

##### number width

矩形路径的宽度

##### number height

矩形路径的高度

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.setFillStyle('red')
ctx.fillRect(10, 10, 150, 75)
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155252_6R9DZVEXrS.png?t=19022220)

## fillText

#### CanvasContext.fillText(string text, number x, number y, number maxWidth)

在画布上绘制被填充的文本

#### 参数

##### string text

在画布上输出的文本

##### number x

绘制文本的左上角 x 坐标位置

##### number y

绘制文本的左上角 y 坐标位置

##### number maxWidth

需要绘制的最大宽度，可选

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.setFontSize(20)
ctx.fillText('Hello', 20, 20)
ctx.fillText('MINA', 100, 100)

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155834_Y6ZX0Wi2B0.png?t=19022220)

## lineTo

#### CanvasContext.lineTo(number x, number y)

增加一个新点，然后创建一条从上次指定点到目标点的线。用 `stroke` 方法来画线条

#### 参数

##### number x

目标位置的 x 坐标

##### number y

目标位置的 y 坐标

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.moveTo(10, 10)
ctx.rect(10, 10, 100, 50)
ctx.lineTo(110, 60)
ctx.stroke()
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155252_H0qTCV4PC0.png?t=19022220)

## measureText

#### Object CanvasContext.measureText(string text)



测量文本尺寸信息。目前仅返回文本宽度。同步接口。

#### 参数

##### string text

要测量的文本

#### 返回值

##### Object

属性    | 类型     | 说明   
----- | ------ | -----
width | number | 文本的宽度

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.font = 'italic bold 20px cursive'
const metrics = ctx.measureText('Hello World')
console.log(metrics.width)
```

## moveTo

#### CanvasContext.moveTo(number x, number y)

把路径移动到画布中的指定点，不创建线条。用 `stroke` 方法来画线条

#### 参数

##### number x

目标位置的 x 坐标

##### number y

目标位置的 y 坐标

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.moveTo(10, 10)
ctx.lineTo(100, 10)

ctx.moveTo(10, 50)
ctx.lineTo(100, 50)
ctx.stroke()
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426160316_lEtVjF2q0U.png?t=19022220)

## quadraticCurveTo

#### CanvasContext.quadraticCurveTo(number cpx, number cpy, number x, number y)

创建二次贝塞尔曲线路径。曲线的起始点为路径中前一个点。

#### 参数

##### number cpx

贝塞尔控制点的 x 坐标

##### number cpy

贝塞尔控制点的 y 坐标

##### number x

结束点的 x 坐标

##### number y

结束点的 y 坐标

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

// Draw points
ctx.beginPath()
ctx.arc(20, 20, 2, 0, 2 * Math.PI)
ctx.setFillStyle('red')
ctx.fill()

ctx.beginPath()
ctx.arc(200, 20, 2, 0, 2 * Math.PI)
ctx.setFillStyle('lightgreen')
ctx.fill()

ctx.beginPath()
ctx.arc(20, 100, 2, 0, 2 * Math.PI)
ctx.setFillStyle('blue')
ctx.fill()

ctx.setFillStyle('black')
ctx.setFontSize(12)

// Draw guides
ctx.beginPath()
ctx.moveTo(20, 20)
ctx.lineTo(20, 100)
ctx.lineTo(200, 20)
ctx.setStrokeStyle('#AAAAAA')
ctx.stroke()

// Draw quadratic curve
ctx.beginPath()
ctx.moveTo(20, 20)
ctx.quadraticCurveTo(20, 100, 200, 20)
ctx.setStrokeStyle('black')
ctx.stroke()

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426160253_RbdDDG7VmY.png?t=19022220)

针对 moveTo(20, 20) quadraticCurveTo(20, 100, 200, 20) 的三个关键坐标如下：

* 红色：起始点(20, 20)
* 蓝色：控制点(20, 100)
* 绿色：终止点(200, 20)

## rect

#### CanvasContext.rect(number x, number y, number width, number height)

创建一个矩形路径。需要用 [`fill`](#fill) 或者 [`stroke`](#stroke) 方法将矩形真正的画到 `canvas` 中

#### 参数

##### number x

矩形路径左上角的横坐标

##### number y

矩形路径左上角的纵坐标

##### number width

矩形路径的宽度

##### number height

矩形路径的高度

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')
ctx.rect(10, 10, 150, 75)
ctx.setFillStyle('red')
ctx.fill()
ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426155252_6R9DZVEXrS.png?t=19022220)

## restore

#### CanvasContext.restore()

恢复之前保存的绘图上下文。

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

// save the default fill style
ctx.save()
ctx.setFillStyle('red')
ctx.fillRect(10, 10, 150, 100)

// restore to the previous saved state
ctx.restore()
ctx.fillRect(50, 50, 150, 100)

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426162056_uSkWImYTJQ.png?t=19022220)

## rotate

#### CanvasContext.rotate(number rotate)

以原点为中心顺时针旋转当前坐标轴。多次调用旋转的角度会叠加。原点可以用 `translate` 方法修改。

#### 参数

##### number rotate

旋转角度，以弧度计 degrees * Math.PI/180；degrees 范围为 0-360

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.strokeRect(100, 10, 150, 100)
ctx.rotate(20 * Math.PI / 180)
ctx.strokeRect(100, 10, 150, 100)
ctx.rotate(20 * Math.PI / 180)
ctx.strokeRect(100, 10, 150, 100)

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426160142_RW22eMOj0X.png?t=19022220)

## save

#### CanvasContext.save()

保存绘图上下文。

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

// save the default fill style
ctx.save()
ctx.setFillStyle('red')
ctx.fillRect(10, 10, 150, 100)

// restore to the previous saved state
ctx.restore()
ctx.fillRect(50, 50, 150, 100)

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426162056_uSkWImYTJQ.png?t=19022220)

## scale

#### CanvasContext.scale(number scaleWidth, number scaleHeight)

在调用后，之后创建的路径其横纵坐标会被缩放。多次调用倍数会相乘。

#### 参数

##### number scaleWidth

横坐标缩放的倍数 (1 = 100%，0.5 = 50%，2 = 200%)

##### number scaleHeight

纵坐标轴缩放的倍数 (1 = 100%，0.5 = 50%，2 = 200%)

#### 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.strokeRect(10, 10, 25, 15)
ctx.scale(2, 2)
ctx.strokeRect(10, 10, 25, 15)
ctx.scale(2, 2)
ctx.strokeRect(10, 10, 25, 15)

ctx.draw()
```

![](https://qzonestyle.gtimg.cn/aoi/sola/20190426160124_sUxPFB7D17.png?t=19022220)
