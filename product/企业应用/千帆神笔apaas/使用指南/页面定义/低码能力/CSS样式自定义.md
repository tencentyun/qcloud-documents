## 自定义CSS

### 功能简介

当前已经支持常用样式的可视化设计，需支持用户CSS代码自定义设置样式，包含组件样式和主题样式。

### **源码编辑介绍**

#### **快速通过属性面板设置**

通过属性面板可以快速设置常用样式，同时会生成CSS源码，可以在「源码编辑」里看到具体设置的样式内容；修改「源码编辑」里的CSS样式，如果属性面板存在设置也会即时显示填充上。简单地说，「源码编辑」和属性面板设置是即时同步的。

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/14b5037b1203e632d724e4e8d13635a1.png)        

展开效果

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/7b6dad272cc7d2ec1f349cbd2bffc7ec.png)        

#### **通过自定义样式代码设置**

1. 1. 自定义设置当前组件样式的写法

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/860de99c54b17ba1c1f9c9de1be341e8.png)        

其中:root 表示当前组件的样式，预览或发布后会自动替换成className

**例如：:root { font-size: 12px} 替换成.compcode-xxxxxx {font-size: 12px}**

1. 1. 自定义设置当前组件及以下其他嵌套的组件的样式

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/9abcfc5e628da5a4027c9fe9552ac340.png)        

1. 1. 全局样式设置（不推荐）

全局样式设置方式，在不加:root情况下写的样式可以设置全局组件的样式，有额可以跨组件设置，**容易造成混乱，不建议使用**。如果非要使用，可以在页面根页面节点设置。

例如：（**当前页面范围**）

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/28373958daa0c4a1936e598bd1253778.png)        

如果去掉:root 会在整个应用范围生效，极力不推荐。

### **样式介绍**

#### **1.基本属性**

基本属性中包括状态、页面高度以及宽度、显示方式。

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/124a51f797749c96bd1926b62f8b5caf.png)        

状态：默认、:hover、:focus、:active。

:hover：选择器用于选择鼠标指针浮动在上面的元素。

:focus：选择器用于选择具有焦点的元素。

:active：选择器用于选择活动链接。

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/af02884ca60a6b2e938c34f9e2508e35.png)        

显示：块、内联块、内联、弹性布局。

弹性布局：调整页面方向，支持自动换行。

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/edd1c4d30ebb0f70c175074be8dd683b.png)        

#### **2.边距**

支持自定义边距，可以通过下拉列表统一调整，也可以在布局图中调整边距大小。

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/7020119a60398c3952ab719b682cc1b1.png)        

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/f7332b3bd16c1fe2b4a93946d27890d7.png)        

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/12c7fd05586ebe5fe0d8cc39141e0441.png)        

#### **3.背景**

背景调整包括颜色，背景图、背景定位、填充方式、平铺方式以及固定方式。

用户可根据自己需求选择颜色背景或图片背景，同时支持调整背景图的填充方式以及固定方式等。

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/9967fe18a2e4508b1f0382a00ce7924b.png)        

#### **4.边框**

支持添加边框，边框可自定义线段粗细、类型、以及颜色调整。

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/0b9cb1ebb0b7bbcf0ab99cfca80c423b.png)        

#### **5.圆角**

支持自定义调整圆角半径，包括全局调整以及局部调整。

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/f22868bb3642c290a9b3608743f2fbf7.png)        

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/8b5ce4c197c7ba654d79996141fe9150.png)        

#### **6.阴影**

支持添加页面阴影效果，包括调整阴影颜色、方向、模糊范围、扩展范围。

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/f55577f6f6d46db9f7f493f824bb76b4.png)        

#### **7.字体**

调整页面中字体样式、大小、字重、行高、字体颜色、对齐方式、风格。

​                 ![img](https://qcloudimg.tencent-cloud.cn/raw/3cc37e100a8ab00d4d9222e07e785cec.png)        
