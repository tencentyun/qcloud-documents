# Animation

动画对象

#### 方法

##### [Array.\<Object\> Animation.export()](#export)

导出动画队列。**export 方法每次调用后会清掉之前的动画操作。**

##### [Animation Animation.step(Object object)](#step)

表示一组动画完成。可以在一组动画中调用任意多个动画方法，一组动画中的所有动画会同时开始，一组动画完成后才会进行下一组动画。

##### [Animation Animation.matrix()](#matrix)

同 [transform-function matrix](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix)

##### [Animation Animation.matrix3d()](#matrix3d)

同 [transform-function matrix3d](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix3d)

##### [Animation Animation.rotate(number angle)](#rotate)

从原点顺时针旋转一个角度

##### [Animation Animation.rotate3d(number x, number y, number z, number angle)](#rotate3d)

从 X 轴顺时针旋转一个角度

##### [Animation Animation.rotateX(number angle)](#rotateX)

从 X 轴顺时针旋转一个角度

##### [Animation Animation.rotateY(number angle)](#rotateY)

从 Y 轴顺时针旋转一个角度

##### [Animation Animation.rotateZ(number angle)](#rotateZ)

从 Z 轴顺时针旋转一个角度

##### [Animation Animation.scale(number sx, number sy)](#scale)

缩放

##### [Animation Animation.scale3d(number sx, number sy, number sz)](#scale3d)

缩放

##### [Animation Animation.scaleX(number scale)](#scaleX)

缩放 X 轴

##### [Animation Animation.scaleY(number scale)](#scaleY)

缩放 Y 轴

##### [Animation Animation.scaleZ(number scale)](#scaleZ)

缩放 Z 轴

##### [Animation Animation.skew(number ax, number ay)](#skew)

对 X、Y 轴坐标进行倾斜

##### [Animation Animation.skewX(number angle)](#skewX)

对 X 轴坐标进行倾斜

##### [Animation Animation.skewY(number angle)](#skewY)

对 Y 轴坐标进行倾斜

##### [Animation Animation.translate(number tx, number ty)](#translate)

平移变换

##### [Animation Animation.translate3d(number tx, number ty, number tz)](#translate3d)

对 xyz 坐标进行平移变换

##### [Animation Animation.translateX(number translation)](#translateX)

对 X 轴平移

##### [Animation Animation.translateY(number translation)](#translateY)

对 Y 轴平移

##### [Animation Animation.translateZ(number translation)](#translateZ)

对 Z 轴平移

##### [Animation Animation.opacity(number value)](#opacity)

设置透明度

##### [Animation Animation.backgroundColor(string value)](#backgroundColor)

设置背景色

##### [Animation Animation.width(number|string value)](#width)

设置宽度

##### [Animation Animation.height(number|string value)](#height)

设置高度

##### [Animation Animation.left(number|string value)](#left)

设置 left 值

##### [Animation Animation.right(number|string value)](#right)

设置 right 值

##### [Animation Animation.top(number|string value)](#top)

设置 top 值

##### [Animation Animation.bottom(number|string value)](#bottom)

设置 bottom 值

```html
<view
  animation="{{animationData}}"
  style="background:red;height:100rpx;width:100rpx"
></view>
```

```js
Page({
  data: {
    animationData: {}
  },
  onShow() {
    const animation = wx.createAnimation({
      duration: 1000,
      timingFunction: 'ease',
    })

    this.animation = animation

    animation.scale(2, 2).rotate(45).step()

    this.setData({
      animationData: animation.export()
    })

    setTimeout(function () {
      animation.translate(30).step()
      this.setData({
        animationData: animation.export()
      })
    }.bind(this), 1000)
  },
  rotateAndScale() {
    // 旋转同时放大
    this.animation.rotate(45).scale(2, 2).step()
    this.setData({
      animationData: this.animation.export()
    })
  },
  rotateThenScale() {
    // 先旋转后放大
    this.animation.rotate(45).step()
    this.animation.scale(2, 2).step()
    this.setData({
      animationData: this.animation.export()
    })
  },
  rotateAndScaleThenTranslate() {
    // 先旋转同时放大，然后平移
    this.animation.rotate(45).scale(2, 2).step()
    this.animation.translate(100, 100).step({duration: 1000})
    this.setData({
      animationData: this.animation.export()
    })
  }
})
```

#### [Animation](#animation)  Animation.backgroundColor(string value)

设置背景色

#### 参数

##### string value

颜色值

#### 返回值

##### [Animation](#animation)

#### [Animation](#animation)  Animation.bottom(number|string value)

设置 bottom 值

#### 参数

##### number|string value

长度值，如果传入 number 则默认使用 px，可传入其他自定义单位的长度值

#### 返回值

##### [Animation](#animation)

#### Array.\<Object\> Animation.export()

导出动画队列。**export 方法每次调用后会清掉之前的动画操作。**

#### 返回值

##### Array.\<Object\>

animationData

#### [Animation](#animation)  Animation.height(number|string value)

设置高度

#### 参数

##### number|string value

长度值，如果传入 number 则默认使用 px，可传入其他自定义单位的长度值

#### 返回值

##### [Animation](#animation)

#### [Animation](#animation)  Animation.left(number|string value)

设置 left 值

#### 参数

##### number|string value

长度值，如果传入 number 则默认使用 px，可传入其他自定义单位的长度值

#### 返回值

##### [Animation](#animation)

#### [Animation](#animation) Animation.matrix()

同 [transform-function matrix](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix)

#### 返回值

##### [Animation](#animation)


### .matrix3d
#### [Animation](#animation) Animation.matrix3d()

同 [transform-function matrix3d](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix3d)

#### 返回值

##### [Animation](#animation)


### .opacity
#### [Animation](#animation) Animation.opacity(number value)

设置透明度

#### 参数

##### number value

透明度，范围 0-1

#### 返回值

##### [Animation](#animation)


### .right
#### [Animation](#animation) Animation.right(number|string value)

设置 right 值

#### 参数

##### number|string value

长度值，如果传入 number 则默认使用 px，可传入其他自定义单位的长度值

#### 返回值

##### [Animation](#animation)



### .rotate
#### [Animation](#animation) Animation.rotate(number angle)

从原点顺时针旋转一个角度

#### 参数

##### number angle

旋转的角度。范围 [-180, 180]

#### 返回值

##### [Animation](#animation)


### .rotate3d
#### [Animation](#animation) Animation.rotate3d(number x, number y, number z, number angle)

从 X 轴顺时针旋转一个角度

#### 参数

##### number x

旋转轴的 x 坐标

##### number y

旋转轴的 y 坐标

##### number z

旋转轴的 z 坐标

##### number angle

旋转的角度。范围 [-180, 180]

#### 返回值

##### [Animation](#animation)


### .rotateX
#### [Animation](#animation) Animation.rotateX(number angle)

从 X 轴顺时针旋转一个角度

#### 参数

##### number angle

旋转的角度。范围 [-180, 180]

#### 返回值

##### [Animation](#animation)



### .rotateY
#### [Animation](#animation) Animation.rotateY(number angle)

从 Y 轴顺时针旋转一个角度

#### 参数

##### number angle

旋转的角度。范围 [-180, 180]

#### 返回值

##### [Animation](#animation)


### .rotateZ
#### [Animation](#animation) Animation.rotateZ(number angle)

从 Z 轴顺时针旋转一个角度

#### 参数

##### number angle

旋转的角度。范围 [-180, 180]

#### 返回值

##### [Animation](#animation)



### .scale
#### [Animation](#animation) Animation.scale(number sx, number sy)

缩放

#### 参数

##### number sx

当仅有 sx 参数时，表示在 X 轴、Y 轴同时缩放sx倍数

##### number sy

在 Y 轴缩放 sy 倍数

#### 返回值

##### [Animation](#animation)


### .scale3d
#### [Animation](#animation) Animation.scale3d(number sx, number sy, number sz)

缩放

#### 参数

##### number sx

x 轴的缩放倍数

##### number sy

y 轴的缩放倍数

##### number sz

z 轴的缩放倍数

#### 返回值

##### [Animation](#animation)


### .scaleX
#### [Animation](#animation) Animation.scaleX(number scale)

缩放 X 轴

#### 参数

##### number scale

X 轴的缩放倍数

#### 返回值

##### [Animation](#animation)


### .scaleY
#### [Animation](#animation) Animation.scaleY(number scale)

缩放 Y 轴

#### 参数

##### number scale

Y 轴的缩放倍数

#### 返回值

##### [Animation](#animation)


### .scaleZ
#### [Animation](#animation) Animation.scaleZ(number scale)

缩放 Z 轴

#### 参数

##### number scale

Z 轴的缩放倍数

#### 返回值

##### [Animation](#animation)



### .skew
#### [Animation](#animation) Animation.skew(number ax, number ay)

对 X、Y 轴坐标进行倾斜

#### 参数

##### number ax

对 X 轴坐标倾斜的角度，范围 [-180, 180]

##### number ay

对 Y 轴坐标倾斜的角度，范围 [-180, 180]

#### 返回值

##### [Animation](#animation)



### .skewX
#### [Animation](#animation) Animation.skewX(number angle)

对 X 轴坐标进行倾斜

#### 参数

##### number angle

倾斜的角度，范围 [-180, 180]

#### 返回值

##### [Animation](#animation)


### .skewY
#### [Animation](#animation) Animation.skewY(number angle)

对 Y 轴坐标进行倾斜

#### 参数

##### number angle

倾斜的角度，范围 [-180, 180]

#### 返回值

##### [Animation](#animation)


### .step
#### [Animation](#animation) Animation.step(Object object)

表示一组动画完成。可以在一组动画中调用任意多个动画方法，一组动画中的所有动画会同时开始，一组动画完成后才会进行下一组动画。

#### 参数

##### Object object

属性              | 类型     | 默认值         | 必填 | 说明          
--------------- | ------ | ----------- | -- | ------------
duration        | number | 400         | 否  | 动画持续时间，单位 ms
timingFunction  | string | 'linear'    | 否  | 动画的效果       
delay           | number | 0           | 否  | 动画延迟时间，单位 ms
transformOrigin | string | '50% 50% 0' | 否  |             

**timingFunction 的合法值**

值             | 说明                   
------------- | ---------------------
'linear'      | 动画从头到尾的速度是相同的        
'ease'        | 动画以低速开始，然后加快，在结束前变慢  
'ease-in'     | 动画以低速开始              
'ease-in-out' | 动画以低速开始和结束           
'ease-out'    | 动画以低速结束              
'step-start'  | 动画第一帧就跳至结束状态直到结束     
'step-end'    | 动画一直保持开始状态，最后一帧跳到结束状态

#### 返回值

##### [Animation](#animation)

animation


### .top
#### [Animation](#animation) Animation.top(number|string value)

设置 top 值

#### 参数

##### number|string value

长度值，如果传入 number 则默认使用 px，可传入其他自定义单位的长度值

#### 返回值

##### [Animation](#animation)


### .translate
#### [Animation](#animation) Animation.translate(number tx, number ty)

平移变换

#### 参数

##### number tx

当仅有该参数时表示在 X 轴偏移 tx，单位 px

##### number ty

在 Y 轴平移的距离，单位为 px

#### 返回值

##### [Animation](#animation)


### .translate3d
#### [Animation](#animation) Animation.translate3d(number tx, number ty, number tz)

对 xyz 坐标进行平移变换

#### 参数

##### number tx

在 X 轴平移的距离，单位为 px

##### number ty

在 Y 轴平移的距离，单位为 px

##### number tz

在 Z 轴平移的距离，单位为 px

#### 返回值

##### [Animation](#animation)


### .translateX
#### [Animation](#animation) Animation.translateX(number translation)

对 X 轴平移

#### 参数

##### number translation

在 X 轴平移的距离，单位为 px

#### 返回值

##### [Animation](#animation)


### .translateY
#### [Animation](#animation) Animation.translateY(number translation)

对 Y 轴平移

#### 参数

##### number translation

在 Y 轴平移的距离，单位为 px

#### 返回值

##### [Animation](#animation)


### .translateZ
#### [Animation](#animation) Animation.translateZ(number translation)

对 Z 轴平移

#### 参数

##### number translation

在 Z 轴平移的距离，单位为 px

#### 返回值

##### [Animation](#animation)


### .width
#### [Animation](#animation) Animation.width(number|string value)

设置宽度

#### 参数

##### number|string value

长度值，如果传入 number 则默认使用 px，可传入其他自定义单位的长度值

#### 返回值

##### [Animation](#animation)


### .backgroundColor
#### [Animation](#animation) Animation.backgroundColor(string value)

设置背景色

#### 参数

##### string value

颜色值

#### 返回值

##### [Animation](#animation)

### .bottom
#### [Animation](#animation) Animation.bottom(number|string value)

设置 bottom 值

#### 参数

##### number|string value

长度值，如果传入 number 则默认使用 px，可传入其他自定义单位的长度值

#### 返回值

##### [Animation](#animation)

### .export
#### Array.\<Object\> Animation.export()

导出动画队列。**export 方法每次调用后会清掉之前的动画操作。**

#### 返回值

##### Array.\<Object\>

animationData

### .height
#### [Animation](#animation) Animation.height(number|string value)

设置高度

#### 参数

##### number|string value

长度值，如果传入 number 则默认使用 px，可传入其他自定义单位的长度值

#### 返回值

##### [Animation](#animation)

### .left
#### [Animation](#animation) Animation.left(number|string value)

设置 left 值

#### 参数

##### number|string value

长度值，如果传入 number 则默认使用 px，可传入其他自定义单位的长度值

#### 返回值

##### [Animation](#animation)

### .matrix
#### [Animation](#animation) Animation.matrix()

同 [transform-function matrix](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix)

#### 返回值

##### [Animation](#animation)