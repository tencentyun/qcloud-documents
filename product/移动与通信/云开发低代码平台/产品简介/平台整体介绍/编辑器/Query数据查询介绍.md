## Query 介绍
Query 是一个静态 JS 对象，主要作用于后端相关的数据获取和更新等操作，支持关联主流数据库 MySQL 以及任何第三方的 HTTP API。其可以通过与变量类似的方式在组件配置的表达式中进行引用，例如 `query1.data`，可以很方便的让组件从各种数据源读取或写入数据，具备与变量一致的生命周期以及作用域。
>? Query 的作用域：分为页面级别作用域的 Query 和应用全局作用域的 Query，开发者可按需声明。当选择定义**全局作用域**的 Query 时，应注意避免引用**页面作用域**的局部变量作为入参，以避免入参值为空时导致 Query 执行异常。

### Query 触发方式介绍
<img style="width:50%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/a96679a37e9955efad7c8a80be32b0a5.png" />

- 手动触发更新 
手动触发需要用户主动通过单击某按钮或者类型前端行为，查询 Query 才会触发执行。手动触发适用于由事件触发时的按需更新场景（例如单击某个按钮触发查询）。
- 入参变化时自动执行
对于读取类请求的 Query，可在入参更新时自动刷新。适合根据查询条件的输入变化，实时响应查询结果（例如列表的筛选条件变化等）的场景。
而对于写请求（包括增/删/改）的 Query 查询类型，并不建议使用入参变化时自动执行的触发方式，一般是用户执行某个行为或者完成输入后才触发写操作，这种写请求的场景一般选择手动触发方式。
> !针对写入数据（增/删/改）的 Query 数据查询，不建议选择入参变化自动更新方式，以避免反复操作导致的脏数据。

### Query 的引用
可以直接在表达式、自定义代码以及事件节点中使用：

- 例如在表达式中引入 Query 的返回结果，输入：`$w.query1.data`。
- 例如在自定义 JS 代码手动触发查询某个 Query，输入：`$w.query1.trigger()`，或引用 Query 的返回数据：`userList = $w.query1.data`。
- 例如在用户的某个点击行为时，手动触发调用 Query。

<img style="width:50%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/d5c2909dde18cb2cad6d8d24063c783b.png" />

### Query 执行成功/失败的回调

在完成 Query 运行后，如果还希望触发其他的行为动作（例如显示加载成功或失败的 toast 提示），则可通过事件回调来完成对应事件流的调用（可复用已定义的事件流或者新建事件流）。
<img style="width:50%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/fbcc94d395a0832340bf802be64f9f4d.png" />

如上图，在定义 Query 查询时，在下方选择执行成功或失败时的回调，然后关联对应的事件流（没有可新建），则在查询成功或失败时做出相应的交互行为。

## Query 的内置属性和方法

### 可访问属性有
<table>
   <tr>
      <th width="0%" >参数名称</td>
      <th width="0%" >参数类型</td>
<th width="0%" >参数描述</td>
   </tr>
   <tr>
      <td>$w.query1.data</td>
       <td>Any</td>
 <td>数据请求成功时，返回的数据结果，默认值：null。</td>
   </tr>
   <tr>
      <td>$w.query1.error</td>
       <td>Error</td>
 <td>数据请求失败时，返回的 Error 错误对象，默认值：null。</td>
   </tr>
   <tr>
      <td>$w.query1.isFetching</td>
       <td>Boolean</td>
 <td>数据请求状态，是否在请求加载中，默认值：false。</td>
   </tr>
</table>


### 可访问方法有
<table>
   <tr>
      <th width="20%" >参数名称</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>$w.query1.reset()</td>
      <td>重置 Query 对象的 data 和 error 值 为 null。</td>
   </tr>
   <tr>
      <td>$w.query1.trigger()</td>
      <td>在代码中手动触发 Query 的执行。如果需要触发 Query 时进行传参，可以通过类似 `$w.query1.trigger({aaa:10})` 的方式传入额外数据，然后在 Query 的配置中通过绑定表达式 `params.aaa` 来获取到传入的数据10（进行手动触发时传参）。</td>
   </tr>
</table>


**示例：**
手动调用 Query 的传参示例：例如在点击事件中调用 Query 时的入参配置如下：
<img style="width:70%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/df60d71f48f93372697114878d75f100.png" />
然后可在 Query 配置中引用该参数。
<img style="width:70%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/3b5cb4e56773128cc8a3c9edcda51eee.png" />
想了解更多 Query 对象的定义封装，请参见 [Query 实例介绍](https://docs.cloudbase.net/lowcode/api/api-referrence#%E6%95%B0%E6%8D%AE%E6%9F%A5%E8%AF%A2query)。

## Query 的数据来源
微搭数据查询 Query 的数据来源目前主要有以下几种（Query 的数据来源未来会持续增加），可通过编辑器左下角代码区单击 **+** 打开新建面板，来进行不同数据来源 Query 对象的新建。
<img style="width:50%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/f27922107d5e5e9b06f72aaf12962105.png" />

### 内置微搭数据表查询

可用于查询操作微搭平台内置的数据表，适用于简单的数据表 CURD 场景，数据库由微搭维护。
<img style="width:50%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/906884ce385f30de43d02d43f6345f6a.png" />
了解更多数据表/数据模型相关介绍，请参见 [数据表概述](https://cloud.tencent.com/document/product/1301/68441)。

### 外部 HTTP APIs 查询
可用于查询操作 HTTP 协议的外部 API 数据或服务，适用于依赖 HTTP 标准接口做数据对接的场景。
<img style="width:50%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/59d39156710bba4c0e287f2586fa84b6.png" />

了解更多 APIs 相关介绍，请参见 [自定义 API 概述](https://cloud.tencent.com/document/product/1301/68439)。

### 外部 MySQL 数据查询 
可用于查询操作有读写权限的外部 MySQL 数据库，适用于开发者有自主维护 MySQL 数据库的场景，以及相对复杂业务多表关联查询等场景，数据库需自行保障稳定性且确保有外网访问权限。
<img style="width:80%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/ade951df97fbe293f958e24528a1b3a5.png" />

了解更多 MySQL 连接相关介绍，请参见 [MySQL 连接器](https://cloud.tencent.com/document/product/1301/95015)。

#### SQL语句数据查询的使用说明
- SQL 语句中可支持插入前端 JS 表达式，JS 表达式需使用 `{{ }}` 进行包裹，如：`{{$w.input1.value}}`，例如需要根据单行输入组件 `input1` 的输入值进行用户信息的查询，SQL 语句可以写作：`SELECT * FROM users WHERE users.name={{$w.input1.value}}`，再例如使用 SQL 进行模糊查询：`SELECT * FROM users WHERE users.name like {{"%" + $w.input1.value + "%"}}`。
>!在 SQL 中使用 JS 表达式时，如需要字符串拼装，则必须在 JS 表达式中进行，即 `{{"string"+js_expr}}`，SQL 语句中不支持使用 `string{{js_expr}}` 进行拼接。
>
- SQL 的批量操作示例：例如批量查询或批量删除等场景，可通过传入前端数组变量来实现。假设新建了自定义数组变量 `$w.page.dataset.state.array`，默认值为 `[50,51,52]`，那么 SQL 语句可写作：`SELECT * FROM users WHERE users.id IN ({{$w.page.dataset.state.array]}})`。
- SQL 语句中如需条件判断的查询示例：假设场景为查询某个用户列表时，当某个输入框组件（input1）的值不为空时则进行条件查询过滤，否则不过滤查询全量，参考 SQL 可以写作：`SELECT * FROM users WHERE name LIKE {{ $w.input1.value ? ("%" + $w.input1.value + "%") : "%" }}`。
- 在使用 SQL 语句进行数据查询时，如果涉及针对当前登录用户的数据查询，为保障安全性，建议开发者使用服务端保留的占位符 `SERVER.xxx` 作为查询条件代入查询，使用占位符时服务端会校验当前登录用户的合法性。例如，在微信小程序中根据当前用户的 OPENID 进行数据查询，则查询 SQL 条件应该写作：`SELECT * FROM users WHERE users.openid={{SERVER.OPENID}}`。
- 目前保留字 SERVER 对象下有如下字段可使用：
  - `SERVER.USERID`：表示当前用户 USERID，与前端系统变量 `$w.auth.currentUser.userId` 取值一致。
  - `SERVER.OPENID`：表示小程序下当前登录用户的 OPENID，与前端系统变量 `$w.auth.currentUser.openId` 取值一致。



## 使用场景示例

### 示例1：获取微搭内置数据表中的列表数据和单条详情数据

#### 列表页的配置
1. 首先，在代码区单击 **+** 可新建一个查询列表的 Query，选择**新建微搭数据表查询**，并且命名为 `query_list`（也可以使用默认名，例如 Query1）。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/f8f8155b3f17b43e32a7a527cc46eccc.png" />

 相关的配置参考如下：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/3d50e91ec441af2e6615c6a487e4a94a.png" />
>? 其中，截图中的 **AI 产品表**为在微搭自行新建内置数据表，关于如何新建微搭数据表，请参见 [数据源概述](https://cloud.tencent.com/document/product/1301/68507)。
>完成 `query_list` 的配置后，也可以通过单击**运行**，来实时查看 Query 执行的返回结果，如下所示。
><img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/f83604e9e75b0b736a241f259ee0c079.png" />
>
2. 然后，完成 Query 新建之后，就可以在组件中通过表达式直接用 `query_list` 绑定和渲染列表数据了。如下图，我们可以往编辑区拖入多个所需要组件，并且分别对组件属性进行数据绑定。
>? 这里我们使用**循环展示**组件作为列表展示的示例（这里也可以选择**数据列表**或**数据表格**组件进行绑定，尤其列表数据量大需要分页时），参见配置如下：
><img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/8050193d8cafb02e522e3adc33c0cd37.png" />
>
3. 再对循环组件内的其他文本组件进行字段绑定，参见配置如下：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/f1f8a81c4b66a7295ef7655a9b90c591.png" />
4. 分别完成数据绑定后，即可看到如下效果，一个简单的列表渲染就完成了。<br>
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/e5c41b58d891dff3aab4a5a1d20d41d5.png" />

#### 详情页的配置
接下来，我们再新建一个详情页，通过刚搭建的这个列表跳转到这个详情页，展示对应的详情内容，完成一个列表展示到详情展示的闭环，这样的话我们就需要用一个查询单条的 Query。
1. 首先，在新建 Query 之前，先新建一个**内容详情页**页面，并且给这个页面配置一个 URL 参数变量，参考配置如下：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/b0c1282ae2e4161d8bc0e3a9960fc7b8.png" />
2. 完成页面新建之后，我们同样的在代码区单击 **+** 可新建一个查询单条的 Query，选择**新建微搭数据表查询**，并且命名为 `query_one`，相关的配置参见如下：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/dcd56a2dd6e90f54e3ddf5aa109262d2.png" />
3. 然后，我们就可以用 `query_one` 给详情页内的组件进行数据绑定了。例如给文本组件绑定数据的参见配置如下：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/f68131f2ec208caa26c43b2bf1d38b24.png" />

以上，一个详情页就搭建完了，有兴趣也可以继续在此基础上按需扩展。

#### 列表页跳转详情页的配置
最后，切换到之前的列表页，我们给列表页面做一个页面跳转配置，并完成详情页的 URL 参数（id）进行传值，相关配置很简单，参见如下：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7e4cb4ea290ac9d9a636949a5e37d031.png" />

### 示例2：从第三方 HTTP API 中获取用户列表数据

从第三方 HTTP API 中获取数据的配置与上一个示例从微搭数据表获取数据流程大致相同。
1. 首先，在代码区单击 **+** 可新建一个查询列表的 Query，选择**新建外部 APIs 查询**，可重命名为 `query_api` 或使用默认命名。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/870e11c1eb99e92fdd88562d5c4b7fc9.png" />

 相关的配置参考如下：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7db53f28ba863cb8ec4f20e50168ecac.png" />
>? 其中，截图中的 **测试 diy 连接器**为自行新建的数据源 APIs 连接器，关于如何新建数据源 APIs，请参见 [自定义 API 概述](https://cloud.tencent.com/document/product/1301/68439)。
>
2. 然后，完成 Query 的新建之后，就可以在组件中通过表达式直接用 `query_api` 绑定和渲染列表数据了。如下图，我们可以往编辑区拖入多个所需要组件，并且分别对组件属性进行数据绑定。
>? 这里我们使用**循环展示**组件作为列表展示的示例（这里也可以选择**数据列表**或**数据表格**组件进行绑定，尤其列表数据量大需要分页时），参见配置如下：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/95a625883a1707dc182f60a7b4b6b332.png" />
>
3. 最后，再对循环组件内的其他文本组件进行字段绑定，一个简单的通过外部 APIs 请求的数据列表就完成了，此处后续步骤与上一个示例**获取微搭内置数据表中的列表数据和单条详情数据**一致，在此不再赘述。



### 示例3：获取外部 MySQL 的用户列表以及删除某条数据
从外部 MySQL 获取数据之前，我们需要先新建一个 [MySQL 连接器](https://cloud.tencent.com/document/product/1301/95015)，参考步骤如下。
1. 在代码区单击 **+** 可新建一个查询列表的 Query，选择**新建 MySQL 查询**，可重命名为 `query_list` 或使用默认命名。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/e54d7d18ff55dde6938c428057170163.png" />

 填写好需要创建的内容后单击**保存**。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/812cb514c6873c497d7d4881353ca0f7.png" />

 如果是首次新建 MySQL 连接器，则会直接打开 MySQL 连接的配置弹层，如果不是则可在 MySQL 的下拉列表中找到新建入口，如下所示。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/3c28075d141f10d86ba4258445be723c.png" />
2. 完成 MySQL 配置并且测试连接正常之后，即可进行 Query 的配置，编写 SQL 语句，例如输入：`SELECT * FROM users ORDER BY id LIMIT 10`，单击**运行**，即可在结果弹层中看到查询到的数据结果，如下图所示。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/dd100c0c65913cb822b219d97c1af221.png" />
3. 完成 Query 的配置并且运行返回正常之后，即完成了外部 MySQL 数据库的用户列表数据的获取，接下来可以通过在列表中绑定 `query_list.data` 来对获取到的用户列表数据进行渲染展示。后续的数据绑定步骤配置与上一个示例的流程大致相同。如下图，我们可以往编辑区拖入多个所需要组件，并且分别对组件属性进行数据绑定。
>? 这里我们使用**循环展示**组件作为列表展示的示例（这里也可以选择**数据列表**或**数据表格**组件进行绑定，尤其列表数据量大需要分页时），**循环展示**组件参见配置如下：
> <img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/0bd79d5cf3699073ab4a5d1a907e7cc5.png" />
>
4. 再对循环组件内的其他文本组件进行字段绑定，参见配置如下：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c265c7a015bd2ee6c0705d12a6a31790.png" />
5. 分别完成上图所述的数据绑定后，一个简单的从外部 MySQL 获取的用户列表数据渲染就完成了。
6. 接下来我们来实现从列表中删除某条数据。先新建一个自定义变量和一个用于执行删除的 Query。自定义变量用于存储点击某一行时对应的数据 ID，例如变量命名为 `current_row_id`，如下所示：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/1855f3dc2ae6c2688c7b72ccd90ca8b6.png" />

 用于执行删除的 Query 则命名为 `query_del`，SQL语句为：`DELETE FROM users WHERE id={{$w.page.dataset.state.current_row_id}}`，如下所示：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/02851816ac6c4d7502da28bd6030f7da.png" />
7. 完成自定义变量和 Query 新建之后，开始进行组件的配置。这里我们为了达到更好的列表展示效果，可以把前面的**循环展示**组件，换成**数据列表**组件，数据列表与循环展示组件的数据绑定流程类似，在数据列表的数据源中选择表达式，然后绑定第1步中新建的 `query_list` 即可。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/bbcdadbcb80b1036b91ee048f7a6ecd2.png" />
8. 完成数据绑定后，即可看到渲染后的列表效果。然后往数据列表对应的节点拖入一个按钮，按钮标题可修改为删除，具体结构如下图所示：
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/3842b101e70747f018964301763cf52a.png" />
9. 配置删除按钮对应事件：选中**按钮**组件，在组件属性面板右下角配置对应的点击动作。
   1. 首先配置第1个动作节点**变量赋值**，即将单击对应行的数据 ID 复制给前面新建的自定义变量 `current_row_id`，如上图所示。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c033062ad6efafef6c942c01411d60be.png" />
   2. 第2个动作节点选择**调用数据查询**，配置项如上图所示。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/1331f449b10f34c394c61ece3493f0f2.png" />
   3. 上述的第3个动作**刷新数据列表**，和第4个动作**显示消息提示**均为可选配置，主要用作交互提示，具体配置如图所示，可按需参考。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/29adccbb1dde8ad79c8e4fee267a2826.png" />
10. 完成上述配置后，可通过单击编辑器右上角**预览按钮**，打开预览界面来进行操作和查看效果。如下所示，单击页面上的**删除**，即可删除对应的行数据，同时完成删除后的数据列表也会同步刷新。<br>
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/fdded16362740c2e58d660bb9759fddc.png" />



### 示例4：向外部 MySQL 数据库新增一条用户数据
1. 在编辑区拖入一个**单行输入**组件，以及一个**按钮**组件，大纲树结构参考下图所示，将单行输入组件标题修改为“用户名”，按钮标题修改为“提交数据”。同时我们可以看到单行输入的组件 id 为 `input1`，在接下来的 SQL 语句中会用到。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/61f0b98a07aafccb600a3b5f6b08b318.png" />
2. 然后，我们开始新建新增数据的 Query，在代码区单击 **+** 可新建一个查询列表的 Query，选择**新建 MySQL 查询**，可重命名为 `query_insert` 或使用默认命名，在 **MySQL 名称**的下拉列表中，选择之前新建好的 **MySQL 连接器**。
>!前置步骤，提前完成[ MySQL 连接器](https://cloud.tencent.com/document/product/1301/95015)的配置新建，可参考上一个示例。
>
3. 接着在 `query_insert` 配置中编写 SQL 语句，例如输入：`INSERT INTO users (name) VALUES ({{$w.input1.value}})`，表示将输入框的值作为一条新数据，插入到 MySQL 数据库的 `users` 表中的 `name` 字段，单击**运行**，即可在弹层查看 Query 的执行结果（执行成功则表示数据完成了插入，如果是测试效果请注意脏数据的处理），如下图所示。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/41b9aa13a70a49a3e2f9e5d48699c9a1.png" />
>!针对上述新增数据的 Query 数据查询，会默认选择**手动触发执行**，以避免入参变化自动执行导致的反复插入数据。
4. 最后，再选中之前拖入的**按钮**组件，在组件属性区配置点击事件，即通过点击按钮时来触发前面 Query 的执行。具体配置参考下图所示。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/2c106cc9ee52fc7399cf1492ad629bb4.png" />
5. 完成上述配置后，即可通过单击**提交数据**来进行输入框用户名的提交，每次单击都会向外部数据库的 `users` 表插入一条数据。



以上仅为使用 SQL Query 的数据插入示例，实际生产环境请注意提交数据的合法性校验以及脏数据的处理。

