# 腾讯云对外发布文档规范

本文档旨在规范腾讯云所有对外文档（包括但不限于产品文档、API文档、SDK文档、白皮书文档等）的基本格式及风格。腾讯云文档书写语法为Markdown，关于Markdown的更多信息，可参考http://wowubuntu.com/markdown/

注：本标准参考[AWS文档惯例](http://docs.aws.amazon.com/zh_cn/general/latest/gr/docconventions.html) 及 [DaoCloud写作规范和格式规范](http://docs.daocloud.io/write-docs/format)

<table><tbody>
<tr>
<td>
总体方针</td>
<td>	以解决用户问题为目标，注重场景化。<br>遵循5W1H分析法：<br>
（What）这是什么产品？<br>
（Who）针对哪些客户群体？<br>
（Why）我为什么要使用这个产品？这个产品解决什么问题？<br>
（When+Where）使用产品的具体场景是什么？<br>
（How）怎么使用这个产品？<br><br>

* 分清读者对象，按不同的类型、不同层次的读者，决定怎样适应他们的需要。
</td>
</tr>
<tr>
<td>
流程
</td>
<td>
参考《腾讯云文档发布流程》
</td>
</tr>
<tr>
<td>
文档结构	
</td><td>根据统一的内容框架（请参考《产品介绍页基本规范》、《产品文档页基本规范》、《API文档基本规范》）进行内容补充
</td>
</tr>
<tr >
<td rowspan="2">基本方法论</td>
<td>关注一致性、准确性（上下文、文字、标点符号与图片）<br><br>
把可能使用的名词、缩略语都在文首列出，避免文档中出现从未见过的名词。注意标点的正确使用，截图中出现的文字与说明需保持强一致性。<br><br>
例子：云服务器（又称CVM、CVM实例、云服务器实例、云主机）
</td>
<tr><td>清晰、易读<br><br>
关注文档结构，构建易读的索引。<br><br>
多使用图、表，增强易懂性。同时注意图表的清晰度，规范统一的图表风格
</td></tr>
</tbody>
</table>


## 1. 字体、颜色规范

腾讯云对外在线文档均由磐石统一编辑发布，采用Markdown编写方式。当前CSS渲染出的默认字体字号如下：

> 注意：除代码块内文字可更改颜色（请使用html标准颜色如red\blue等），其余规范均不可更改。

<table><tbody>
<tr>
<td rowspan="4">
正文	</td><td>中文字体</td><td>	微软雅黑（PC） 苹方（Mac）</td></tr>
<tr><td>	英文字体</td><td>	PingFangSC-Light字集（苹方）</td></tr>
	<tr><td>字体颜色</td><td>	#666</td></tr>
	<tr><td>字号</td><td>		14px（五号）</td></tr>
<tr>
<td rowspan="4">
代码块/文本中的代码</td><td>	英文字体</td><td>	Consolas字集</td></tr>
<tr><td>	默认字体颜色</td><td>	#666（可更改）</td></tr>
<tr><td>	字号</td><td>	14px（五号）</td></tr>
<tr><td>    背景颜色	</td><td>#F7F7F7</td></tr>
<tr>
<td rowspan="4">
标题</td><td>	中文字体</td><td>	微软雅黑（PC） 苹方（Mac）</td></tr>
<tr><td>	英文字体	</td><td>	PingFangSC-Light字集（苹方）</td></tr>
<tr><td>	字体颜色	</td><td>	#000</td></tr>
<tr><td>	字号	</td><td>不等，见下文“标题/列表规范”。</td></tr>
</tbody>
</table>

腾讯云对外离线文档统一为PDF格式，请使用Markdown编辑器编写，有形如以上的规范。

## 2. 标题/列表规范
文档标题有形如下的格式规范，目录从一级开始，最多可到第三级。（三级以上的标题不符合常规阅读需求，请拆分或使用标题内的列表进行相应处理）
<table>
  <tbody>
  <tr>
    <th> 标题层级</th>
    <th> 显示样式</th>
    <th> Markdown语法</th>
  </tr>
  <tr>
    <td> 第一级标题</td>
    <td> ## 第一级标题</td>
    <td> Markdown请注意采用二级‘##’语法，对应Word字号为22.5</td>
  </tr>
  <tr>
    <td> 第二级标题</td>
    <td> ### 第二级标题</td>
    <td> Markdown请注意采用三级‘###’语法，对应Word字号为17.5</td>
  </tr>
  <tr>
    <td> 第三级标题</td>
    <td> #### 第三级标题</td>
    <td> Markdown请注意采用四级‘####’语法，对应Word字号为13</td>
  </tr>
  </tbody>
</table>

内容列表有形如下的格式规范：
<table>
  <tbody>
  <tr>
    <th> 列表层级</th>
    <th> 显示样式</th>
  </tr>
  <tr>
    <td> 正文第一级列表</td>
    <td> 1. 列表项一<br>2. 列表项二	</td>
   
  </tr>
  <tr>
    <td> 列表中的第二级列表</td>
    <td> 1. 列表项一<br><br>这是一段说明<br><br>1) 二级列表项一<br>  2) 二级列表项二	</td>
  </tr>
  <tr>
    <td> 二级列表中的第三级列表</td>
    <td> 1. 列表项一<br><br>这是一段说明<br><br>1) 二级列表项一<br><br>这是另一段说明<br><br>A. 三级列表项1<br>B.  三级列表项2<br><br>2) 二级列表项二</td>
  </tr>
  </tbody>
</table>

## 3. 特殊表达及标点规范
<table>
  <tbody>
  <tr>
    <th> 特殊表达</th>
    <th> 表达方式</th>
    <th> 说明</th>
  </tr>
  <tr>
    <td>强调</td>
    <td>	粗体+斜体+前后空格	</td>
    <td>非普通文字和短语或重要文字和短语的特殊标记。<br><br><img src="https://mccdn.qcloud.com/static/img/b979c0180a367bd3203f9f443f243671/image.png">

    </td>
  </tr>
  <tr>
    <td>正文中的参数、表达式或代码</td>
    <td>	内联代码	</td>
    <td>必须使用内联代码标识正文中的参数、表达式或代码。Markdown语法为 ``<br><br><img src="https://mccdn.qcloud.com/static/img/f9dbb700441f7a407727eb9c6d20a4e8/image.png"></td>
  </tr>
  <tr>
    <td>代码块</td>
    <td>	文档中出现的完整代码	</td>
    <td>与正文分开，使用代码块标识。Markdown语法为``` ```<br><br><img src="https://mccdn.qcloud.com/static/img/05b2ea78c32e165af2922b3a9da54464/image.png"></td>
  </tr>
  <tr>
    <td>界面标志</td>
    <td>	【中文方括号】	</td>
    <td>标识 UI 上的指定内容以便识别。<br><br>在【云服务器】选项卡中，点击【新建】按钮。</td>
  </tr>
  <tr>
    <td>交叉引用/外链</td>
    <td>	超链接</td>
    <td>多使用超链接进行文档间关系的建立。<br><br>产品文档中引用的链接地址请统一直接拷贝磐石产品文档中的相对路径，/document/product/ +数字路径，例如/document/product/213/6090。</td>
  </tr>
  <tr>
    <td>互斥参数</td>
    <td>	(圆括号 | 和 | 竖 | 线)</td>
    <td>代码中，分割线表示必须从中选择一个选项的选项集。<br><br>% data = hdfread (start | stride | edge)</td>
  </tr>
  <tr>
    <td>可选参数</td>
    <td>	[英文方括号]</td>
    <td>代码中，方括号表示完全可选的命令或参数。<br><br>ssh [-l, -q] root@10.10.10.10</td>
  </tr>
  <tr>
    <td>变量</td>
    <td>	<箭头括号></td>
    <td>代码中，箭头括号表示必须替换为有效值的变量。<br><br>mount /dev/vdb1 %<%your-mountpoint></td>
  </tr>
</tbody>
</table>


## 4. 文档风格规范
### 文案风格
1. 一定多检查，确保没有错别字。即使是流行语中的谐音错别字也不要使用，比如”墙裂”、”童鞋”、“程序猿”等。
2. 段落之间使用一个空行隔开。段落开头 ***不要*** 留出空白字符。
3. 请把对表达意思没有明显作用的字、词、句删除，在不影响表达效果的前提下把文案长度减到最短。
4. 避免口语，使用规范的书面语。例子：避免使用“么”、“喔”、“挂掉”等口语词汇。
5. 尽量避免中英文混杂。
6. 请一定注意“的”、“地”、“得”的用法。
7. 第一人称：推荐使用“腾讯云”、“我们”，不推荐使用“小编”、“笔者”。
8. 避免多介词的复合长句。注意句子成分要齐全。


> 例如：
改前：对于apt-get下载源，不需要添加软件源，可以直接安装软件包。为了加速软件安装，目前系统已经在内网预先配置了Ubuntu的mirror，这个mirror是官网x86_64的完全镜像，与官网源一致。

> 改后：对于apt-get下载源，不需添加软件源则可直接安装软件包。为了加速软件安装，腾讯云已在内网预先配置了Ubuntu的x86_64完全镜像，与官方源一致。


### 中文、英文、数字混排时空格的使用
1. 英文与非标点的中文之间需要有一个空格。如“使用 CVM 构建和部署应用环境”而不是“使用CVM构建和部署应用环境”。
2. 尽可能使用中文数词，特别是当前后都是中文时。例如：“我们发布了五个产品”。

### 标点相关
1. 只有中文或中英文混排中，一律使用中文 / 全角标点
2. 中英文混排中如果出现整句英文，则在这句英文中使用英文 / 半角标点。
3. 省略号：请使用”……“标准用法，不要使用”。。。“。
4. 感叹号：请勿使用”！！“。尽量避免使用”！“。请先冷静下来再坐电脑前敲键盘。
5. 波浪号：请勿在文章内使用“~”，活泼地卖萌有很多其他的表达方式。

### 一些常用名词的正确用法

<table>
<tbody>
<tr><td>正确使用</td><td>错误使用</td></tr>
<tr><td>腾讯云数据中心高速互联网</td><td>腾讯骨干网</td></tr><tr><td>App / 应用</td><td>APP、软件、程序</td></tr><tr><td>Android</td><td>android、安卓</td></tr><tr><td>iOS</td><td>ios、IOS</td></tr><tr><td>iPhone</td><td>IPHONE、iphone</td></tr>
<tr><td>App Store</td><td>AppStore、app store</td></tr>
<tr><td>WiFi</td><td>wifi、Wifi、Wi-fi</td></tr>
<tr><td>email</td><td>E-mail、Email</td></tr>
<tr><td>IP</td><td>Ip、ip</td></tr>
</tbody>
</table>

## 5. 示例
*本示例仅供参考此规范中部分条款的使用说明，不保证其对客观事实的描述正确性。
![](https://mc.qcloudimg.com/static/img/c3ab304e29ec3c2ce3655184438261b0/image.png)
