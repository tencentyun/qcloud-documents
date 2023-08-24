本文将针对审批页面中各个具体模块进行关于 UI 构建方面的介绍。

> ? 这一环节是在审批详情页面数据初始化完毕的基础上进行。如果不了解这个过程，可参见 **审批详情模板介绍** 下的**审批详情页面数据初始化**。
## 基本信息

这个模块主要使用了**网格布局**组件和**文本**组件，主要呈现流程的基本信息，包含**发起人**、**发起时间**、**结束时间**、**流程状态**。

### 组件布局描述

模块主体是一个**网格布局**组件，其中设置**4**行。每一行有**2**列。每一行的第一列为**信息标题**。第二列为具体信息字段的值。
![](https://qcloudimg.tencent-cloud.cn/raw/fd836ecf94d9cef31ba43c1c1f1ed118.jpg)

### 具体信息字段取值

#### 发起人
在基础属性 > 文本内容中，绑定 `$page.dataset.state?.processInstance` 变量中的 StartedBy 这个值。

```js
$page.dataset.state?.processInstance?.StartedBy || "-";
```

#### 发起时间

在基础属性 > 文本内容中，绑定 `$page.dataset.state?.processInstance` 变量中的 StartTime 这个值， 其中在表达式中需要通过 DateText 这个公式进行时间转换，并且做空值判断。

```js
$page.dataset.state?.processInstance?.StartTime
  ? DateText(
      $page.dataset.state.processInstance?.StartTime,
      "YYYY-MM-DD HH:mm:ss"
    )
  : "-";
```

#### 结束时间

逻辑与发起时间相同，取值为 EndTime。

#### 流程状态

流程状态这个信息在 `$page.dataset.state?.processInstance` 这个变量中并未直接返回，需要通过 `$page.dataset.state?.processInstance` 这个变量中几个字段进行计算而来。计算方法为 **getProcessStatusInfo**，此方法返回 text（状态名称）和 color（状态字段颜色）。最终的文本内容绑定表达式如下：

```js
$page.handler?.getProcessStatusInfo?.($page.dataset.state.processInstance)
  ?.text || "-";
```

然后给在流程状态文本组件中的**样式** > **高级** > **style 绑定**中进行如下样式绑定。

```js
({
  color:
    $page.handler?.getProcessStatusInfo?.($page.dataset.state.processInstance)
      ?.color || "#000",
});
```

### 涉及到的方法

<table>
   <tr>
      <th width="0%" >方法</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>getProcessStatusInfo</td>
      <td>计算当前流程的状态信息，入参为当前流程实例，出参为状态文本（text）和文本颜色（color）</td>
   </tr>
</table>

### 涉及到的变量

<table>
   <tr>
      <th width="0%" >变量</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>processInstance</td>
      <td>流程实例信息</td>
   </tr>
</table>

## 流程记录

### 组件布局描述

流程记录的布局主要由以下几块构成：
- 标题
- 空状态显示文本
- 循环展示组件

循环展示组件中结构如下：
- 普通容器
  - 记录顶部容器，其中包含审批节点的标题，节点审批状态以及操作时间。
  - 网格布局，包含记录信息。有审批人、加签信息、审批意见、回退信息、抄送信息。 其中针对待审批的节点还有审批策略信息。

![](https://qcloudimg.tencent-cloud.cn/raw/ee10f99180c2818ac4c593bb7f3eece1.jpg)

### 具体信息字段取值

这个模块使用到的数据都在 elementInfos 这个变量中。在 initApprovalPage 中，这个变量来源于 getProcessMetaData 返回的 elementInfos，经由 transElementInfos 处理得到。具体转换逻辑可见 transElementInfos 这个方法，方法内包含详尽的转换逻辑的注释信息。

在获取到 elementInfos 这个变量后，将此变量跟循环对象进行绑定，利用变量中的循环对象，对循环展示内网格布局中的文本组件进行赋值。

```js
// 转换流程记录容器所需要显示的数据，并将结果赋值给流程记录变量
$page.dataset.state.elementInfos =
  $page.handler.transElementInfos(elementInfos);
```

最终得到以下的绑定对应关系：

#### 审批节点标题

绑定循环对象的 title。

```js
$w.item_listView1.title;
```

#### 审批节点状态

绑定循环对象的 status。

```js
$w.item_listView1.status.text;
```

针对此字段颜色设置，在状态文本组件中的**样式** > **高级** > **style 绑定**中进行如下样式绑定：

```js
({
  display: "inline-block",
  color: $w.item_listView1.status.color,
  background: $w.item_listView1.status.backgroundColor,
});
```

#### 操作时间

绑定循环对象的 createTime。

```js
$w.item_listView1.createTime;
```

#### 发起人/审批人

绑定循环对象的 operaName.value。

```js
$w.item_listView1.operaName.value;
```

针对**字段标题**的设置，operaName 中包含一个 label 字段，决定这个字段名称显示发起人还是审批人。故给字段标题进行如下绑定。

```js
$w.item_listView1.operaName.label;
```

#### 审批策略

这个字段的值绑定为：
```js
$w.item_listView1.approvalStrategy;
```

另外此字段有值说明该审批节点是待审批状态，待审批状态才显示审批策略。

#### 加签

绑定循环对象的 addAssignee.value。

```js
$w.item_listView1.addAssignee.value || "-";
```

#### 回退到指定节点

绑定循环对象的 rollback.value。

```js
$w.item_listView1.rollback.value || "-";
```

#### 抄送

绑定循环对象的 cc.value。

```js
$w.item_listView1.cc.value || "-";
```

#### 审批意见

绑定循环对象的 comment.value。

```js
$w.item_listView1.comment.value || "-";
```

### 涉及到的方法

<table>
   <tr>
      <th width="0%" >方法</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>transElementInfos</td>
      <td>转换批办过程数据</td>
   </tr>
</table>

### 涉及到的变量

<table>
   <tr>
      <th width="0%" >变量</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>elementInfos</td>
      <td>批办过程数据</td>
   </tr>
</table>

## 流程图示

流程图示目前使用的是微搭平台中内置的流程图组件。该组件并未开放出来，仅供生成审批详情模板时使用。属性目前也很简约只有一个数据属性。
![](https://qcloudimg.tencent-cloud.cn/raw/bd1556e67e7afc3aa455ff3f0688aaa1.jpg)

### 数据取值

这里用到的数据是在初始化数据请求的时候得到的**流程画布详情**。

```js
/** initApprovalPage **/
// 将流程画布详情数据赋值给 流程画布详情变量
$page.dataset.state.processCanvasInfo = processCanvasInfo;
```

将这个 processCanvasInfo 流程画布变量直接绑定到流程图组件上，即可显示图示内容。

> ? 这里的图示也可以自己实现。具体的画布数据格式可以参见 [流程画布详情](https://cloud.tencent.com/document/product/1301/94470#.E6.9F.A5.E8.AF.A2.E6.B5.81.E7.A8.8B.E7.94.BB.E5.B8.83.E8.AF.A6.E6.83.85) 这个接口。根据这个接口返回的数据，并借助其他第三方图表库，实现一个自定义组件，并应用到此模板中。

### 涉及到的变量

<table>
   <tr>
      <th width="0%" >变量</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>processCanvasInfo</td>
      <td>流程画布数据</td>
   </tr>
</table>

## 流程操作

### 组件布局描述

操作区域主要的布局是网格布局，在一行之中放置了 11 列。在每一列放置相应的交互按钮或其他交互组件。
每一个操作项都会有显隐控制，具体体现在列的**条件展示** > **条件渲染**中。
<img style="width:30%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/b9f539da48e2675fa95c984c1a88bdac.jpg" />

以下是各个操作内容的构成、条件渲染逻辑。如果需要重新实现这一套流程操作渲染，可以参考这些内容进行个性化的搭建。

#### 流程操作区域的条件渲染规则

如果用户针对自己的审批进行了**回退**操作的话，在回退成功后，用户操作的这条审批任务将被销毁，用户不能再进行任何审批操作。
所以单击回退之后，整个流程操作区域将不再显示。这个条件渲染应用在流程操作所在的网格布局，在**配置** > **条件展示** > **是否渲染**进行如下的表达式绑定：

```js
!$page.dataset.state.hasRollback;
```

`hasRollback` 的赋值过程在请求回退成功之后。具体逻辑见下一章审批阶段 > 回退中。

#### 各操作的 UI 组件组成以及渲染条件表格

<table>
  <tr>
    <th width="5%">操作名称</td>
    <th width="15%">UI组件组成</td>
    <th width="40%">条件渲染规则</td>
    <th width="40%">条件渲染表达式</td>
  </tr>
  <tr>
    <td>抄送</td>
    <td>
      抄送这一列放置了一个普通容器。其中包含一个按钮，一个成员选择组件。成员选择组件通过样式定位，覆盖在按钮之上。点击按钮其实是触发了成员选择弹窗。
    </td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 DRAFT（草稿）、CREATEFLOW（创建）、TODO（待办）中的一个。</li>
        <li>审批页面详情（变量 approvalPageDetail）中的 Show、ShowSubmitApp、ShowCarbonCopy 的值都为 <strong>true</strong>。</li>
      </ul>
    </td>
<td>
```js
["DRAFT", "CREATEFLOW", "TODO"].includes(
  $page.dataset.state.internalPageType
) &&
  $page.dataset.state.approvalPageDetail?.Show &&
  $page.dataset.state.approvalPageDetail?.ShowSubmitApp &&
  $page.dataset.state.approvalPageDetail?.ShowCarbonCopy;
```

</td>
  </tr>
  <tr>
    <td>保存草稿</td>
    <td>按钮</td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 DRAFT（草稿）、CREATEFLOW（创建）中的一个。</li>
        <li>审批页面详情（变量 approvalPageDetail）中的 Show、ShowSubmitApp 的值都为 <strong>true</strong>。</li>
        <li>审批实例（变量 processInstance） 中的 CanDelete 的值为 <strong>true</strong>。</li>
      </ul>
    </td>
<td>

```js
["DRAFT", "CREATEFLOW"].includes($page.dataset.state.internalPageType) &&
  $page.dataset.state.approvalPageDetail?.Show &&
  $page.dataset.state.approvalPageDetail?.ShowSubmitApp &&
  $page.dataset.state.processInstance?.CanDelete;
```

</td>
  </tr>
  <tr>
    <td>取消</td>
    <td>按钮</td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 DRAFT（草稿）、CREATEFLOW（创建）中的一个。</li>
        <li>审批页面详情（变量 approvalPageDetail）中的 Show、ShowSubmitApp 的值都为 <strong>true</strong>。</li>
        <li>审批实例（变量 processInstance）中的 CanDelete 的值为 <strong>true</strong>。</li>
      </ul>
    </td>
<td>

```js
["DRAFT", "CREATEFLOW"].includes($page.dataset.state.internalPageType) &&
  $page.dataset.state.approvalPageDetail?.Show &&
  $page.dataset.state.approvalPageDetail?.ShowSubmitApp &&
  $page.dataset.state.processInstance?.CanDelete;
```

</td>
  </tr>
  <!-- 提交申请 -->
  <tr>
    <td>提交申请</td>
    <td>按钮</td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 DRAFT（草稿）、CREATEFLOW（创建）、TODO（待办）中的一个。</li>
        <li>审批页面详情（变量 approvalPageDetail）中的 Show、ShowSubmitApp 的值都为 <strong>true</strong>。</li>
      </ul>
    </td>
<td>

```js
["DRAFT", "CREATEFLOW", "TODO"].includes(
  $page.dataset.state.internalPageType
) &&
  $page.dataset.state.approvalPageDetail?.Show &&
  $page.dataset.state.approvalPageDetail?.ShowSubmitApp;
```

</td>
  </tr>
  <!-- 回退 -->
  <tr>
    <td>回退</td>
    <td>按钮</td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 TODO（待办）。</li>
        <li>审批页面详情（变量 approvalPageDetail）中的 ShowRollBack 的值都为 <strong>true</strong>，ShowSubmitApp 为 <strong>false</strong>。</li>
        <li>变量 taskHasEnd 的值为 <strong>false</strong>。</li>
      </ul>
    </td>
<td>

```js
$page.dataset.state.internalPageType === "TODO" &&
  !$page.dataset.state.approvalPageDetail?.ShowSubmitApp &&
  $page.dataset.state.approvalPageDetail?.ShowRollBack &&
  !$page.dataset.state.taskHasEnd;
```

</td>
  </tr>
  <tr>
    <td>加签</td>
    <td>加签的操作布局构成同抄送</td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 TODO（待办）。</li>
        <li>审批页面详情（变量 approvalPageDetail）中的 ShowAddAssignee 的值都为 <strong>true</strong>，ShowSubmitApp 为 <strong>false</strong>。</li>
        <li>变量 taskHasEnd 的值为 <strong>false</strong>。</li>
      </ul>
    </td>
<td>

```js
$page.dataset.state.internalPageType === "TODO" &&
  !$page.dataset.state.approvalPageDetail?.ShowSubmitApp &&
  $page.dataset.state.approvalPageDetail?.ShowAddAssignee &&
  !$page.dataset.state.taskHasEnd;
```

</td>
  </tr>
  <tr>
    <td>转办</td>
    <td>转办的操作布局构成同抄送</td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 TODO（待办）。</li>
        <li>审批页面详情（变量 approvalPageDetail）中 ShowTurnToPerson 的值都为 <strong>true</strong>，ShowSubmitApp 为 <strong>false</strong>。</li>
        <li>变量 taskHasEnd 的值为 <strong>false</strong>。</li>
      </ul>
    </td>
<td>

```js
$page.dataset.state.internalPageType === "TODO" &&
  !$page.dataset.state.approvalPageDetail?.ShowSubmitApp &&
  $page.dataset.state.approvalPageDetail?.ShowTurnToPerson &&
  !$page.dataset.state.taskHasEnd;
```

</td>
  </tr>
  <!-- 拒绝 -->
  <tr>
    <td>拒绝</td>
    <td>按钮</td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 TODO（待办）。</li>
        <li>审批页面详情（变量 approvalPageDetail）中的 ShowSubmitApp 的值都为 <strong>false</strong>。</li>
        <li>审批实例（变量 processInstance）中的 UserTaskType 的值<strong>不为 2</strong>。</li>
        <li>变量 taskHasEnd 的值为 <strong>false</strong>。</li>
      </ul>
    </td>
<td>

```js
$page.dataset.state.internalPageType === "TODO" &&
  !$page.dataset.state.approvalPageDetail?.ShowSubmitApp &&
  $page.dataset.state.processInstance?.UserTaskType !== 2 &&
  !$page.dataset.state.taskHasEnd;
```

</td>
  </tr>
  <!-- 同意 -->
  <tr>
    <td>同意</td>
    <td>按钮</td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 TODO（待办）。</li>
        <li>审批页面详情（变量 approvalPageDetail）中的 ShowSubmitApp 的值都为 <strong>false</strong>。</li>
        <li>审批实例（变量 processInstance）中的 UserTaskType 的值<strong>不为 2</strong>。</li>
        <li>变量 taskHasEnd</code> 的值为 <strong>false</strong>。</li>
      </ul>
    </td>
<td>

```js
$page.dataset.state.internalPageType === "TODO" &&
  !$page.dataset.state.approvalPageDetail?.ShowSubmitApp &&
  $page.dataset.state.processInstance?.UserTaskType !== 2 &&
  !$page.dataset.state.taskHasEnd;
```

</td>
  </tr>
  <tr>
    <td>处理</td>
    <td>按钮</td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 TODO（待办）。</li>
        <li>审批页面详情（变量 approvalPageDetail）中的 ShowSubmitApp 的值都为 <strong>false</strong>。</li>
        <li>审批实例（变量 processInstance）中的 UserTaskType 的值<strong>为 2</strong>。</li>
        <li>变量 taskHasEnd 的值为 <strong>false</strong>。</li>
      </ul>
    </td>
<td>

```js
$page.dataset.state.internalPageType === "TODO" &&
  !$page.dataset.state.approvalPageDetail?.ShowSubmitApp &&
  $page.dataset.state.processInstance?.UserTaskType === 2 &&
  !$page.dataset.state.taskHasEnd;
```

</td>
  </tr>
  <!-- 撤销 -->
  <tr>
    <td>撤销</td>
    <td>按钮</td>
    <td>
      <ul>
        <li>当前的页面类型（变量 internalPageType）是 CREATE（创建）、DONE（已办）中的一个。</li>
        <li>审批页面详情（变量 approvalPageDetail）中的 ShowRevoke 的值都为 <strong>true</strong>。</li>
      </ul>
    </td>
<td>

```js
["CREATE", "DONE"].includes($page.dataset.state.internalPageType) &&
  $page.dataset.state.approvalPageDetail?.ShowRevoke;
```

</td>
  </tr>
</table>

### 涉及到的变量

<table>
   <tr>
      <th width="0%" >变量</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>internalPageType</td>
      <td>页面类型。</td>
   </tr>
    <tr>
      <td>processInstance</td>
      <td>流程实例。</td>
   </tr>
    <tr>
      <td>approvalPageDetail</td>
      <td>审批详情。</td>
   </tr>
    <tr>
      <td>taskHasEnd</td>
      <td>审批任务是否已完成。</td>
   </tr>
</table>

## 审批弹窗
审批弹窗部分的包含两个组件，一个是弹窗，一个是表单。 其中**当前节点**、**审批人**这两个表单项为只读。
<img style="width:40%; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/ecb07807253523b65051eff63a35d33b.png" />

### 具体信息字段取值

#### 当前节点

```js
$page.dataset.state.processInstance?.CurrentNodeName;
```

#### 当前审批人/处理人
- 标题内容绑定
```js
$page.dataset.state.processInstance?.UserTaskType === 2 ? "处理人" : "审批人";
```
- 输入值绑定
```js
$page.dataset.state.processInstance?.CurrentApproverName || "-";
```

### 可交互表单项显隐逻辑

- 审批意见
这里会用到一个变量，currentOperation 为当前操作，其中包含操作标识字段 operationName，当 operationName 不为 transfer 时进行显示。
```js
$page.dataset.state.currentOperation.operationName !== "transfer";
```
- 抄送
抄送的显示首先要保证 approvalPageDetail（审批页面详情）这个变量中 ShowCarbonCopy 显示抄送字段为 **true**，然后 currentOperation 变量中 operationName 字段值为 agree 和 handle 中的一个。
```js
$page.dataset.state.approvalPageDetail.ShowCarbonCopy &&
  ["agree", "handle"].includes(
    $page.dataset.state.currentOperation.operationName
  );
```
- 通知人选择
这个表单项未设置隐藏逻辑，在审批弹窗中的表单中总是显示的。

### 涉及到的变量

<table>
   <tr>
      <th width="0%" >变量</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>processInstance</td>
      <td>流程实例</td>
   </tr>
    <tr>
      <td>approvalPageDetail</td>
      <td>审批页面详情</td>
   </tr>
    <tr>
      <td>currentOperation</td>
      <td>当前审批操作</td>
   </tr>
</table>

## 回退弹窗

回退弹窗中的弹窗内容是一个单选框。这里的单选框列表渲染是由变量 preElementList 生成。这部分的数据交互建下一章**审批详情页操作交互逻辑**。

### 涉及到的变量

<table>
   <tr>
      <th width="0%" >变量</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>preElementList</td>
      <td>可回退节点列表</td>
   </tr>
</table>

## 下一节点审批人弹窗

下一节点审批人弹窗中的弹窗内容是一个多选框。这里的单选框列表渲染是由变量 flowTaskInfoList 生成。这部分的数据交互建下一章**审批详情页操作交互逻辑**。

### 涉及到的变量

<table>
   <tr>
      <th width="0%" >变量</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>flowTaskInfoList</td>
      <td>下一节点审批人列表</td>
   </tr>
</table>

## 审批表单

审批表单是在创建的时候，由编辑器创建。
表单创建依赖审批节点配置的变量背后的数据模型。取审批节点上出参和入参的数据模型的并集，然后生成一个或多个数据模型对应的表单。

### 表单值的设置

关于设置表单值，这里通过模板预置的 setFormValue 这个方法来实现，并在 initApprovalPage 中调用。这个方法主要有两个逻辑。

#### 获取审批详情页面中的变量值

```js
// 转换流程变量中的业务数据
const { objectMap } = transVariableInfos(approvalPageDetail);
```

其中 transVariableInfos 这个值在 setFormValue 文件中，主要就做一个事情，针对审批页面详情中 ObjectMap 进行转化。
转化前：
```js
{
  ObjectMap: [
    {
      EntityCode: "foo",
      FieldValueMap: {
        name: "hello",
      },
    },
    {
      EntityCode: "bar",
      FieldValueMap: {
        name: "world",
      },
    },
  ];
}
```

转化后：
```js
{
  foo: {
     name: "hello",
  }
  bar: {
     name: "world",
  }
}
```

#### 表单赋值
遍历当前页面的所有组件判定当前组件是不是表单的逻辑为：如果当前组件存在数据源标识并且流程业务数据中包含此数据源标识对应的数据，说明当前组件是表单再将上一步转化后的数据，赋值给当前表单。具体逻辑可参见 setFormValue 方法内的注释。

### 表单读写设置

在生成表单的同时，表单的**表单场景**也会被设置成一个表达式。来控制表单在不同场景下的可读可写的权限。

具体的读写性由两个变量决定 taskHasEnd 和 internalPageType。这两个变量在 initApprovalPage 中已赋值。并且在复制之后作为入参传给 setFormType 方法进行进一步的计算，并在 initApprovalPage 中调用 setFormType 方法。

具体计算逻辑可参见 setFormType 这个方法内的注释。

### 涉及到的变量

<table>
   <tr>
      <th width="0%" >变量</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>taskHasEnd</td>
      <td>当前审批任务是否结束</td>
   </tr>
   <tr>
      <td>internalPageType</td>
      <td>页面类型</td>
   </tr>
</table>

### 涉及到的方法

<table>
   <tr>
      <th width="0%" >方法</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>setFormValue</td>
      <td>将流程中的业务数据回显到表单中</td>
   </tr>
   <tr>
      <td>setFormType</td>
      <td>设置表单场景</td>
   </tr>
</table>
