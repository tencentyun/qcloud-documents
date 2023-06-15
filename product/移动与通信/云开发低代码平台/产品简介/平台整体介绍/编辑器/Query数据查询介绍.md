## Query 介绍

Query 是一个静态JS对象，主要用作与后端相关的数据获取和更新等操作，支持关联主流数据库 MySQL 以及任何第三方的 HTTP API。其可以通过与变量类似的方式在组件配置的表达式中进行引用，例如 `query1.data`，可以很方便的让组件从各种数据源读取或写入数据，其具备与变量一致的生命周期以及作用域。

> ? Query 的作用域：分为页面级别作用域的 Query 和应用全局作用域 Query，可以按需声明。

### Query 触发方式介绍

- 手动触发更新 Query 
  手动触发需要用户主动通过点击某按钮或者类型前端行为，查询 Query 才会触发执行。手动触发适用于由事件触发时的按需更新场景（例如单击某个按钮触发查询）。
- 入参变化时自动更新 Query
  对于读取类请求的 Query，可在入参更新时自动刷新。适合根据查询条件的输入变化，实时响应查询结果（例如列表的筛选条件变化等）的场景。
  而对于写请求（包括增/删/改）的 Query 查询类型，并不建议使用入参变化时自动执行的触发方式，一般是用户执行某个行为或者完成输入后才触发写操作，这种写请求的场景一般选择手动触发方式。

![](https://qcloudimg.tencent-cloud.cn/raw/a96679a37e9955efad7c8a80be32b0a5.png)

> !针对写入数据的 Query 查询，不建议选择入参变化自动更新方式，避免反复插入冗余数据。

### Query 的引用

可以直接在表达式、自定义代码以及事件节点中使用：

- 如在表达式中引入 Query 的返回结果，输入：`$w.query1.data`。
- 如在自定义 JS 代码手动触发查询某个 Query，输入：`$w.query1.trigger()`，或引用 Query 的返回数据：`userList = $w.query1.data`。
- 如在用户的某个点击行为时，手动触发调用 Query。

![](https://qcloudimg.tencent-cloud.cn/raw/d5c2909dde18cb2cad6d8d24063c783b.png)

### Query 执行成功/失败的回调

在完成 Query 运行后，如果还希望触发其他的行为动作（例如显示加载成功或失败的 toast 提示），则可通过事件回调来完成对应事件流的调用（可复用已定义的事件流或者新建事件流）。
![](https://qcloudimg.tencent-cloud.cn/raw/fbcc94d395a0832340bf802be64f9f4d.png)
如上图，在定义 Query 查询时，在下方选择执行成功或失败时的回调，然后关联对应的事件流（没有可新建），则在查询成功或失败时做出相应的交互行为。

## Query 的内置属性和方法

### 可访问属性有

- `$w.query1.data`：`<any>`    请求成功数据对象，为接口返回值。
- `$w.query1.error`：`<Error>`    请求失败时错误对象。



### 可访问方法有

- `$w.query1.trigger()`：在代码中手动触发 Query 执行。
- `$w.query1.reset()`：重置 Query 对象的 data 和 error 属性值。

## Query 的数据来源

### 微搭内置数据表查询

可用于查询操作微搭平台内置的数据表，适用于简单的数据表 CURD 场景，数据库由微搭维护。
![](https://qcloudimg.tencent-cloud.cn/raw/906884ce385f30de43d02d43f6345f6a.png)


### 外部 HTTP APIs 查询

可用于查询操作HTTP协议的外部API数据或服务，适用于依赖HTTP标准接口做数据对接的场景。
![](https://qcloudimg.tencent-cloud.cn/raw/59d39156710bba4c0e287f2586fa84b6.png)

## 使用场景示例

### 获取微搭内置数据表中的列表数据和单条详情数据

#### 列表页的配置

1. 首先，在代码区单击 **+** 可新建一个查询列表的 Query，选择**新建微搭数据表查询**，并且命名为 `query_list`（也可以使用默认名，例如 Query1）。
![](https://qcloudimg.tencent-cloud.cn/raw/f8f8155b3f17b43e32a7a527cc46eccc.png)
相关的配置参考如下：
![](https://qcloudimg.tencent-cloud.cn/raw/3d50e91ec441af2e6615c6a487e4a94a.png) 
>? 其中，截图中的 **AI 产品表**为在微搭自行新建内置数据表，关于如何新建微搭数据表，请参见 [数据源概述](https://cloud.tencent.com/document/product/1301/68507)。
2. 然后，完成 Query 新建之后，就可以在组件中通过表达式直接用 `query_list` 绑定和渲染列表数据了。如下图，我们可以往编辑区拖入多个所需要组件，并且分别对组件属性进行数据绑定。
>? 这里我们使用**循环展示**组件作为列表展示的示例（这里也可以选择**数据列表**或**数据表格**组件进行绑定，尤其列表数据量大需要分页时），参见配置如下：
> ![](https://qcloudimg.tencent-cloud.cn/raw/8050193d8cafb02e522e3adc33c0cd37.png)
3. 再对循环组件内的其他文本组件进行字段绑定，参见配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/f1f8a81c4b66a7295ef7655a9b90c591.png)
4. 分别完成数据绑定后，即可看到如下效果，一个简单的列表渲染就完成了。
![](https://qcloudimg.tencent-cloud.cn/raw/e5c41b58d891dff3aab4a5a1d20d41d5.png)

#### 详情页的配置

接下来，我们再新建一个详情页，通过刚搭建的这个列表跳转到这个详情页，展示对应的详情内容，完成一个列表展示到详情展示的闭环，这样的话我们就需要用一个查询单条的 Query。
首先，在新建 Query 之前，先新建一个**内容详情页**页面，并且给这个页面配置一个 URL 参数变量，参考配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/b0c1282ae2e4161d8bc0e3a9960fc7b8.png)
完成页面新建之后，我们同样的在代码区单击 **+** 可新建一个查询单条的 Query，选择**新建微搭数据表查询**，并且命名为 `query_one`，相关的配置参见如下：
![](https://qcloudimg.tencent-cloud.cn/raw/dcd56a2dd6e90f54e3ddf5aa109262d2.png)
然后，我们就可以用 `query_one` 给详情页内的组件进行数据绑定了。例如给文本组件绑定数据的参见配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/f68131f2ec208caa26c43b2bf1d38b24.png)
以上，一个详情页就搭建完了，有兴趣也可以继续在此基础上按需扩展。

#### 列表页跳转详情页的配置

最后，切换到之前的列表页，我们给列表页面做一个页面跳转配置，并完成详情页的 URL 参数（ID）进行传值，相关配置很简单，参见如下：
![](https://qcloudimg.tencent-cloud.cn/raw/7e4cb4ea290ac9d9a636949a5e37d031.png)

### 从第三方 HTTP API 中获取用户列表数据

从第三方 HTTP API 中获取数据的配置与上一步从微搭数据表获取数据流程大致相同。
首先，在代码区单击 **+** 可新建一个查询列表的 Query，选择**新建外部 APIs 查询**，可重命名为 `query_api` 或使用默认命名。
![](https://qcloudimg.tencent-cloud.cn/raw/870e11c1eb99e92fdd88562d5c4b7fc9.png)
相关的配置参考如下：
![](https://qcloudimg.tencent-cloud.cn/raw/7db53f28ba863cb8ec4f20e50168ecac.png)
>? 其中，截图中的 **测试 diy 连接器**为自行新建的数据源 APIs 连接器，关于如何新建数据源 APIs，请参见 [自定义 API 概述](https://cloud.tencent.com/document/product/1301/68439)。

然后，完成 Query 的新建之后，就可以在组件中通过表达式直接用 `query_api` 绑定和渲染列表数据了。如下图，我们可以往编辑区拖入多个所需要组件，并且分别对组件属性进行数据绑定。
>? 这里我们使用**循环展示**组件作为列表展示的示例（这里也可以选择**数据列表**或**数据表格**组件进行绑定，尤其列表数据量大需要分页时），参见配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/95a625883a1707dc182f60a7b4b6b332.png)

最后，再对循环组件内的其他文本组件进行字段绑定，一个简单的通过外部 APIs 请求的数据列表就完成了，此处后续步骤与**获取微搭内置数据表中的列表数据和单条详情数据**一致，在此不再赘述。
