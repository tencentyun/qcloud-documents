# wx.createAnimation
#### [Animation](./Animation.md) wx.createAnimation(Object object)

创建一个动画实例 [animation](./Animation.md)。调用实例的方法来描述动画。最后通过动画实例的 export 方法导出动画数据传递给组件的 animation 属性。

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

##### [Animation](./Animation.md)

