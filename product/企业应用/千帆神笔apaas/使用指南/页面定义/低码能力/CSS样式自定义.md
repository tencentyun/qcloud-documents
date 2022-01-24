## 自定义CSS

### 功能简介

当前已经支持常用样式的可视化设计，需支持用户CSS代码自定义设置样式，包含组件样式和主题样式。

### **源码编辑介绍**

#### **快速通过属性面板设置**

通过属性面板可以快速设置常用样式，同时会生成CSS源码，可以在「源码编辑」里看到具体设置的样式内容；修改「源码编辑」里的CSS样式，如果属性面板存在设置也会即时显示填充上。简单地说，「源码编辑」和属性面板设置是即时同步的。

​                 ![img](https://docimg4.docs.qq.com/image/uMBeUvd9KcLMse9bjvEzJw.png?w=700&h=800)        

展开效果

​                 ![img](https://docimg8.docs.qq.com/image/BSZFxbBf5QD7Cb9UScEghw.png?w=694&h=1608)        

#### **通过自定义样式代码设置**

1. 1. 自定义设置当前组件样式的写法

​                 ![img](https://docimg10.docs.qq.com/image/du3aPRFIzbTsa4d1DiR42A.png?w=1280&h=810.3857008466604)        

其中:root 表示当前组件的样式，预览或发布后会自动替换成className

**例如：:root { font-size: 12px} 替换成.compcode-xxxxxx {font-size: 12px}**

1. 1. 自定义设置当前组件及以下其他嵌套的组件的样式

​                 ![img](https://docimg1.docs.qq.com/image/yZzoWoQ0bcW8rv_eyWaPkg.png?w=1280&h=783.5514018691589)        

1. 1. 全局样式设置（不推荐）

全局样式设置方式，在不加:root情况下写的样式可以设置全局组件的样式，有额可以跨组件设置，**容易造成混乱，不建议使用**。如果非要使用，可以在页面根页面节点设置。

例如：（**当前页面范围**）

​                 ![img](https://docimg9.docs.qq.com/image/RbFJQxBR6JIQHEYwnT8iMw.png?w=1280&h=864.2038216560509)        

如果去掉:root 会在整个应用范围生效，极力不推荐。

### **样式介绍**

#### **1.基本属性**

基本属性中包括状态、页面高度以及宽度、显示方式。

​                 ![img](https://docimg4.docs.qq.com/image/sDGRTzmmh3VlitEQum41TA.png?w=284&h=285)        

状态：默认、:hover、:focus、:active。

:hover：选择器用于选择鼠标指针浮动在上面的元素。

:focus：选择器用于选择具有焦点的元素。

:active：选择器用于选择活动链接。

​                 ![img](https://docimg6.docs.qq.com/image/ZGesscUh0kqULIyKttyXGg.png?w=282&h=290)        

显示：块、内联块、内联、弹性布局。

弹性布局：调整页面方向，支持自动换行。

​                 ![img](https://docimg9.docs.qq.com/image/KzY5u127yi6MF3cLwu3OOw.png?w=290&h=454)        

#### **2.边距**

支持自定义边距，可以通过下拉列表统一调整，也可以在布局图中调整边距大小。

​                 ![img](https://docimg6.docs.qq.com/image/PjW4YG0n9SrqKNMDJrC5lA.png?w=277&h=381)        

​                 ![img](https://docimg1.docs.qq.com/image/nXpsUPGKOwtBpNM5fdoilg.png?w=280&h=389)        

​                 ![img](https://docimg7.docs.qq.com/image/4LJTjfTjrHA_KKv-O7xYog.png?w=317&h=412)        

#### **3.背景**

背景调整包括颜色，背景图、背景定位、填充方式、平铺方式以及固定方式。

用户可根据自己需求选择颜色背景或图片背景，同时支持调整背景图的填充方式以及固定方式等。

​                 ![img](https://docimg4.docs.qq.com/image/rwj0oqRLiq9kjhXvcTwdlA.png?w=284&h=627)        

#### **4.边框**

支持添加边框，边框可自定义线段粗细、类型、以及颜色调整。

​                 ![img](https://docimg3.docs.qq.com/image/B2SmU6LTNH9FCpW95vDNjg.png?w=294&h=391)        

#### **5.圆角**

支持自定义调整圆角半径，包括全局调整以及局部调整。

​                 ![img](https://docimg2.docs.qq.com/image/eXZ3O3bBQanKeC1WvGBu6A.png?w=289&h=318)        

​                 ![img](https://docimg4.docs.qq.com/image/WNB6M1U0QMJKJOWGUKnq_Q.png?w=283&h=361)        

#### **6.阴影**

支持添加页面阴影效果，包括调整阴影颜色、方向、模糊范围、扩展范围。

​                 ![img](https://docimg8.docs.qq.com/image/s6FgVF5MOz3bDarhtM22Pw.png?w=282&h=440)        

#### **7.字体**

调整页面中字体样式、大小、字重、行高、字体颜色、对齐方式、风格。

​                 ![img](https://docimg1.docs.qq.com/image/C_vD-pWFTC3y9tut5FKpyQ.png?w=279&h=593)        
