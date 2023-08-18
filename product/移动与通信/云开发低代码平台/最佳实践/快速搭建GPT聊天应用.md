本教程将向您展示如何使用微搭低代码，快速搭建一个基于 GPT 的聊天 Web 应用或小程序，跟朋友分享搭建的 AI 应用一起体验 GPT 技术带来的便捷。

## 1. 准备工作
在开始搭建聊天机器人之前，您需要做以下准备：
- 一个 GPT 服务的 API 接口：可以使用腾讯 AI、文心一言、科大讯飞等 AI 服务提供商均可。本教程为方便演示，使用了一个模拟的 API 接口，可按需替换为上述正式的 GPT 接口。
- 开通微信小程序（可选）：如果没有微信小程序账号，可在微搭控制台直接 [申请注册](https://console.cloud.tencent.com/lowcode/auth/applet/register)，或者也可以直接发布为 H5 网页应用。


## 2. 搭建 ChatBot 聊天应用
首先，一个常见的聊天对话机器人应用预览界面，如下图所示：
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c0523d0c2be2acfb83ca94927ba4c64c.png" />

通过应用界面可以看到，它主要由如下几个部分组成：
- 一个对话聊天界面
- 一个 API 数据查询接口
- 界面 UI 与后端数据的联动渲染

现在，就参照上面的几个模块，分5个步骤来依次拆解和搭建：


### 步骤1：对应用界面进行组件和样式配置
1. 我们先拖入一个滚动容器和一个普通容器，一个用来展示聊天的上下文对话，一个用来展示输入框和发送按钮。然后依次拖入图中大纲树所示的组件，组件相应的层级关系可以参考下图中的大纲树结构。
![](https://qcloudimg.tencent-cloud.cn/raw/828ca974c588741701cce5419ff09be5.png)
2. 接下来针对上述组件分别进行样式的配置，我们默认使用样式面板的弹性（Flex）布局，包含接收消息和发送消息两个普通容器，可以分别选择样式面板中的弹性布局中的左对齐（接收消息）和右对齐（发送消息），如上图所示。
3. 接着可以分别配置图片和文本两个组件的高度和宽度大小以及内外间距，以达到想要的视觉效果，文本组件的参考样式配置如下。
![](https://qcloudimg.tencent-cloud.cn/raw/bc24ea2ebc5e5af5bad4379587e3221d.png)
图片组件的参考样式配置如下。
![](https://qcloudimg.tencent-cloud.cn/raw/ac345ae0768a8d3c3e1b68732a565d54.png)
4. 完成聊天上下文对话框的样式配置之后，可以进行底部的**输入框和按钮容器**的样式配置，样式配置方式与发送消息容器类似，可使用弹性布局并选择**左对齐**的方式布局，由于底部容器是固定位置的，故需要额外配置一下定位属性，参考如下：
![](https://qcloudimg.tencent-cloud.cn/raw/4e125cfaa5f66cd49c7a4e4a6604bad0.png)
5. 对容器内的多行输入组件和按钮组件分别进行配置，两个组件的宽度可分别设置为70%和30%，参考如下：
![](https://qcloudimg.tencent-cloud.cn/raw/24fb1cdf0a09354d049ae370a18df245.png)
6. 最后，如果针对小程序希望设置其顶部导航栏的背景和标题颜色等，可在大纲树中选中页面根节点，在右侧属性区进行配置，参考如下：
![](https://qcloudimg.tencent-cloud.cn/raw/3daba9786b68e35ece6d4a26071934f2.png)


以上，通过进一步按需微调一些样式细节如组件背景色以及间距等后，即可达到上文提到的应用界面效果。整体页面配置过程完全可视化操作，不需要了解代码。如果对样式配置不是很熟悉的朋友，请参见微搭的基础 [视频教程](https://cloud.tencent.com/edu/paths/series/weda) 来学习。


### 步骤2：配置数据变量和数据源 API
下面开始进行数据的绑定和数据源的配置：
#### 数据绑定
1. 新建一个数组对象的自定义变量 chatList，用于存储聊天记录。
![](https://qcloudimg.tencent-cloud.cn/raw/32098fb9ee959608880ec9b80ccae921.png)
2. 配置一个变量，如命名为 chatList 聊天记录这么一个变量，一个对象数组，默认值为如下所示，当然您也可以基于这个结构任意修改。
```json
[
    {
        "res": "你好，欢迎体验ChatGPT聊天机器人，你可以直接输入你感兴趣的任何问题向我提问",
        "req": "红孩儿是牛魔王的亲儿子吗？",
        "index": 1
    },
    {
        "res": "不是，红孩儿是牛魔王的养子。据西游记中的记载，牛魔王是一个孤独的怪物，他在深山里住了很久，没有子女，却有一个养子——红孩儿，红孩儿的父母去世时，牛魔王便收养了他。",
        "req": "那谁教他的三味真火",
        "index": 2
    }
]

```
2. 接着把这个数组变量的初始值跟我们的这个页面的内容分别进行绑定。首先我们选择大纲树中的**循环展示**组件，在循环展示组件的数据属性配置为刚刚新建的数组变量`$w.page.dataset.state.chatList`。
![](https://qcloudimg.tencent-cloud.cn/raw/7e54834b551472c5bec59232455933d2.png)
然后继续选择该组件内的子节点，例如文本组件，分别绑定这个数组中的对象属性值，例如发送消息容器下的文本组件，则绑定循环对象下的 req 属性即 `$w.item_repeater1.req`，对应接收消息下的文本组件则绑定属性 `$w.item_repeater1.res`，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a919fd2097711c60e509fe53d6412f68.png)
这一步数据绑定完成之后，接下来就可以去配置请求远程数据的数据源 API 了。

#### 配置一个数据源 APIs（用于请求 GPT 接口）
API 的配置相对比较简单，主要参考 AI 服务商的 API 文档。此处为方便演示，我们使用 Postman 提供的 echo 测试接口，该 API 接口对应的参数配置参考如下：
![](https://qcloudimg.tencent-cloud.cn/raw/64c51432419f6677d62cf6ec12b52bc7.png)
通过单击上图数据源中的**方法测试**，得到 API 的返回结果如下，单击**出参映射**即可完成出参结构的配置：
![](https://qcloudimg.tencent-cloud.cn/raw/f1c72cb822b15453b8359779b52ee989.png)
```json
{
  "args":  {
  },
  "data":  {
    "text":"AI回复: 这里是示例 ",
  },
  "form":  {
  },
  "files":  {
  },
  "url":"https://xxxx-echo.com/post",
}
```



### 步骤3：给发送按钮绑定请求事件
我们在步骤1中已经在页面中放置了多行输入框、按钮和文本展示等组件。接下来，我们需要给输入框配置相关的事件响应逻辑，来获取用户输入的消息内容，首先新建一个自定义变量`$page.dataset.state.text`。
![](https://qcloudimg.tencent-cloud.cn/raw/a3f5373f8226fc1a8b22cc5999f7f1c6.png)
再将多行输入框的值通过绑定值改变事件，来赋值给该变量 `$page.dataset.state.text`，参考的配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/187e1e95b6b2c5bb34c22e30500cb308.png)
同时，给发送按钮组件绑定一个点击事件，将发送的文本信息加入到聊天列表中。即点击发送按钮时，将发送的文本数据插入到之前定义的聊天记录数组变量 `$page.dataset.state.chatList` 中，如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2815b0dbe5f65d2a76c686f78ef61462.png)
图中表达式参考如下：
```javascript
[...$page.dataset.state.chatList, {req: $page.dataset.state.text}]
```
然后，给按钮组件绑定事件来处理输入框中用户发送的消息，选择按钮组件，在右侧事件面板中配置如下逻辑，即点击按钮时触发 API 请求，并将获取到的 API 返回结果渲染在页面中，参考配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/31cb5f3b2a911a2934a6f7d59df6feb4.png)




### 步骤4：将API返回数据与在页面中进行渲染展示
将调用 API 成功返回值用**变量赋值**方法加入到 chatList 数组中。
![](https://qcloudimg.tencent-cloud.cn/raw/4cbae28f29f44054f23c17de76cf69c3.png)
这里我们需要在数据中增加一条新的消息，采用表达式绑定的方式进行原有的 `ChatList` 变量进行解构后再赋值，图中表达式参考如下：
```javascript
[...$page.dataset.state.chatList, {res: event.detail.data.text }]
```
除了上述 API 返回成功后的变量赋值事件配置外，还可以配置更多控制状态的 [事件动作](https://cloud.tencent.com/document/product/1301/86578)，例如：
- 通过新建一个 `$w.page.dataset.state.loading` 变量来控制 API 的加载状态。
![](https://qcloudimg.tencent-cloud.cn/raw/05b5869b34f28c1673b86874c26fec52.png)
- 通过新建一个 `$w.page.dataset.state.scrollTop` 变量，每次消息接收/发送成功时赋值一个较大随机数如下图所示，来控制滚动容器确保在每次有新消息时，滚动容器能自动滑动到页面底部。
![](https://qcloudimg.tencent-cloud.cn/raw/fb5c083c79758ddc5ce05119c911ac9d.png)

别忘了将变量 `$w.page.dataset.state.scrollTop` 绑定到滚动容器组件的**竖向滚动条位置**的属性值上，如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/1322703a692f5559d5ccd2698e87dba3.png)
以上是几个控制发送状态的事件配置示例，开发者还可以按需自行扩展，如增加请求接口的异常时提示等，或者参考文末的应用模板链接来安装查看。


### 步骤5：完成开发，进行应用发布
前端界面和后端数据逻辑都配置开发完成后，可在应用编辑器的右上角单击**发布**，可以选择发布到已绑定的小程序，或者直接发布移动端的 H5 应用，如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1a81a5aba2636cec692807410da14a54.png)
至此，一个基础的 AI 聊天应用搭建就完成了。上述教程所搭建的应用已经上架到微搭模板中心，可以在微搭控制台打开 [GPT 聊天应用模板](https://console.cloud.tencent.com/lowcode/create/index?templateId=tpl-1peulFtVPaFgMI) 安装体验。


## 3. 进一步完善：记录历史聊天记录
基于上述步骤搭建完聊天机器人应用后，您还可以进一步完善它的功能。例如，可以在应用中添加聊天记录功能，让用户可以查看历史的聊天记录。这个过程相对比较简单，步骤如下：
1. 在数据源中配置一个 **GPT 聊天记录**数据模型，参考模型配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/db30847f308af6d8569de1a46e9b65ba.png)
2. 接着将数据存储到数据表中，可在请求 GPT 接口返回成功时回调事件中，选择**调用数据源方法**，然后选择上一步新建的数据表模型的创建单条方法，在入参中填入对应的数据即可，如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/685583d8c2661ab10aeecc9b9db1e6db.png)
3. 然后，将之前声明的聊天记录变量 `$w.page.dataset.state.chatList` 的静态示例数据，换成从数据表模型中动态获取聊天历史数据。如下所示，可以先新建一个数据表的 [Query 数据查询](https://cloud.tencent.com/document/product/1301/93144) 变量 `$w.query_chats`，用来存储动态获取的历史数据，对应的配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/1ef75b6aa8ae0d208ee213aa63de2b68.png)
数据查询 `$w.query_chats` 对应的配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/cbf6abc492902fca0d88ab7ce0fa69bc.png)
4. 最后，由于上一步的 Query 选择的手动触发，所以在页面加载时触发一次 Query，如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/4c1d6d03ec1f6adf5ac2371633f084d4.png)
然后将 Query 返回值 `$w.query_chats.data.records` 赋值给 `$w.page.dataset.state.chatList` 即可。
![](https://qcloudimg.tencent-cloud.cn/raw/17b0f429d2f60a3826ab171d892362a7.png)


至此，一个带历史记录存储功能的聊天 ChatBot 应用搭建完成了。

