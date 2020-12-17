开发一个连接器最简单的方式，就是通过 XML 来编写，一个 Connector 就是一个 XML 文件。通过 XML 编写的 **Connector** 和普通的 **module** 模块以同样的方式被使用。

Connector XML 的根节点为"**module**"，需要在根节点引入必要的 namespace，同时指明 **Connector** 使用的 API 类型（**apiType**）、API 版本（**apiVersion**）、表达式语言类型（**expressionType**）和表达式版本（**expressionVersion**），其中 **apiType** 固定为 "**XML**"，**apiVersion** 在当前版本为"1.0"， **expressionType** 在 iPaaS 规范中默认定义了 "**dataway**"，基于 Python 3，并针对部分功能做了裁剪，入口函数名为 **dw_process**，**selector** 函数以下标操作符"[...]"重载的方式提供，详细的定义可参考 iPaaS 中相关标准的定义。

在 "**module**" 节点下，需要通过"**name**"、"**version**"、"**display-name**" 和 "**description**" 标签来描述模块的英文名、版本、展示名和描述，通过“**declaration**”标签来描述 **connector** 对外提供的接口，包括 **property**、**trigger** 和 **operation** 的定义。通过 “**body**” 标签来描述 **trigger** 和 **operation** 在**connector** 内部的实现逻辑。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<module apiType="XML" apiVersion="1.0" expressionType="dataway" expressionVersion="1.0"
xmlns="http://ipaas.cloud.tencent.com/schema/core"
xmlns:http="http://ipaas.cloud.tencent.com/schema/http"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://ipaas.cloud.tencent.com/schema/core http://ipaas.cloud.tencent.com/schema/core/1.0/core.xsd
http://ipaas.cloud.tencent.com/schema/http http://ipaas.cloud.tencent.com/schema/http/1.0/http.xsd">
 
    <name>tencent-meeting</name>
    <version>1.0</version>
    <display-name>腾讯会议</display-name>
    <description>腾讯会议的连接器</description>
 
    <declaration>
        <properties>
            <!-- property list -->
        </properties>
 
        <triggers>
            <!-- trigger list -->
        </triggers>
 
        <operations>
            <!-- operation list -->
        </operations>
    </declaration>
 
    <body>
        <!-- 实现 -->
    </body>
</module>
```

其中，**name** 为 **module** 在 **iPaaS app** 中的唯一标识，只能包含小写字母、数字和横杠，且以小写字母开头。

## property 定义

在 “**declaration**” 节点下的 **properties** 节点中，可以定义 **connector** 的公共配置，一个配置项的定义节点如下：

```xml
<property name="..." type="..." defaultValue="..." expressionMode="..." .../>
```

- **name** 指定配置名，必填。
- **type** 指定配置类型，必填。
- **defaultValue** 指定默认值，选填，当没有默认值时，此项配置为必填配置。
- **expressionMode** 指定表达式模式，选填，默认 **NOT_SUPPORTED**。

除此之外，还可以在 **property** 的定义中指定配置项在界面上如何渲染，相关属性如下：

- **displayName** 指定配置项的展示名，如果未设置则默认为配置名。
- **displayExample** 为配置案例，在界面通过输入框的 placeholder 展示。
- **displayPageTab** 为配置项的tab，在界面上配置界面左右分栏，按 Tab 进行组织，默认 Tab 为“通用”。
- **description** 为配置项的详细介绍，在界面上通过气泡提示。
- **password** 表示该项在界面上展示为密码输入框。

## trigger 定义

"**trigger**" 节点在 “**declaration**” 节点下的 **triggers** 节点中，可以定义 **connector** 封装的触发器，一个 **trigger** 的定义节点如下：

```xml
<trigger name="..." flowRef="...">
    <parameters>
        <!-- parameter list -->
    </parameters>
    <output>
        <payload/>
        <attributes/>
    </output>
</trigger>
```

"**trigger**" 节点的属性有：
- **name** 指定触发器名，必填。
- **flowRef** 指定实现的 **flow** 名，必填，在下面的实现章节中详细介绍。

除此之外，还可以在 **trigger** 的定义中指定触发器在界面上如何渲染，相关属性如下：

- **displayName** 指定触发器的展示名，如果未设置则默认为触发器名。
- **displayGroup** 指定在下拉列表中所在的分组，默认是“默认”。
- **description** 指定触发器的介绍，会通过气泡提示。

"**trigger**" 节点的子节点有：

- "**parameters**" 指定参数表，每个参数的定义节点为 "**parameter**"，属性同 "**property**" 一致。
- "**output**" 指定输出格式，可选。如果没指定，则输出空消息，有两个子节点：
  - **payload** 节点，用于指定输出的 **payload**，如果没指定，则 **payload** 为空。
  - **attributes** 节点，用于指定输出的 **attributes**，如果没指定，则 **attributes** 为空。

## operation 定义

"**operation**" 节点在 “**declaration**” 节点下的 **operations** 节点中，可以定义 **connector** 封装的触发器，一个 **operation** 的定义节点如下：

```xml
<operation name="..." flowRef="...">
    <parameters>
        <!-- parameter list -->
    </parameters>
    <output>
        <payload/>
        <attributes/>
    </output>
</operation>
```

"**operation**" 节点的属性有：

- **name** 指定操作名，必填。
- **flowRef** 指定实现的 **flow** 名，必填，在下面的实现章节中详细介绍。
- **scope** 指定操作的使用范围，可选，默认为 **PUBLIC**，表示公开。可以设置为 **PRIVATE**，此时该 **operation** 只能在当前**connector**的内部实现中被引用。

除此之外，还可以在 **operation** 的定义中指定操作在界面上如何渲染，相关属性如下：

- **displayName** 指定操作的展示名，如果未设置则默认为操作名。
- **displayGroup** 指定在下拉列表中所在的分组，默认是“默认”。
- **description** 指定操作的介绍，会通过气泡提示。

"**operation**" 节点的子节点有：

- "**parameters**" 指定参数表，每个参数的定义节点为 "**parameter**"，属性同 "**property**"一致。
- "**output**" 指定输出格式，可选。如果没指定，则输出空消息，有两个子节点：
  - **payload** 节点，用于指定输出的 **payload**，如果没指定，则 **payload** 为空。
  - **attributes** 节点，用于指定输出的 **attributes**，如果没指定，则 **attributes** 为空。

## connector 实现

在 **xml connector 的**实现中，**trigger** 和 **operation** 都是通过设计 **flow**，基于已有的 **component** 来编排实现的。每个在 **declaration** 中声明的 **trigger** 或 **operation** 都对应一个实现它的 **flow**，通过**flowRef** 属性可以将声明与实现 **flow** 进行关联。

#### operation 实现

**operation** 在集成流中的角色是 **processor**，它在收到事件时，进行一定的逻辑处理，并在完成时产生一个新的事件返回给下一个 **processor**。在 **xml connector** 的实现中，当 **operation** 实例在收到事件时：

- 构造一个空的 **message**
- 将该 **operation** 实例的参数经过表达式求值后设置到变量表中，变量名为参数
- 将该 **operation** 实例引用的配置集实例中的配置项经过表达式求值后，构造为一个字典，放入变量表中的**properties**变量
- 将构造好的 **message** 传递给 **connector 的 xml** 实现中对应的 **flow** 的第一个 **processor** 进行流转
- 流转完成时，构造一个新的**message**，根据 **operation** 声明中的 **output** 定义的输出项，将最后的 **payload** 和 **attributes** 复制到新的**message**中，作为 **operation** 的输出传递给下一个 **processor**。
- 流转失败时，**operation** 抛出错误，错误内容为**xml flow**中执行出错的**processor**所抛出的错误。

####  trigger 实现

**trigger** 在集成流中的角色是**source**，它在一定条件下主动产生事件并传递给第一个 **processor**。通过设计 **flow** 来实现 **trigger** 有两个要求：

- **flow** 的第一个组件需要为一个其它模块的 **source**，用于在一定条件下触发 **flow** 的运行。对于轮询的场景，通常使用 **scheduler** 作为 **source**。对于回调的场景，通常使用 **http:listener** 作为 **source**。
- **flow** 中通过 "**emit"** 组件来对外产生事件，单次流的执行可以对外触发0次或若干次事件。"**emit**"组件不接受参数，会按照 **trigger** 声明中定义的 **output** 规则来构造 **message**，构造规则同 **operation**。

**trigger** 实例被构造后，实现该 **trigger** 的 **flow** 中的 **source** 会同时被构造，该 **source** 在一定条件下产生事件并在该 **flow** 中流转，当遇到 "**emit**" 组件时，会将新构造的 **message** 传递给外面引用该 **trigger** 实例的 **flow** 中的第一个 **processor**，实现触发逻辑，并在流转完成后得到的 **message** 传递给 **emit** 的下一个 **processor**。

在实现 **trigger** 的 **flow** 中，**trigger** 实例参数和公共配置项会按照 operation 的模式放入到变量表中。在 **source** 的参数及后续的 processor 参数中均可以引用。

#### xml 定义

**connector** 的实现逻辑在根节点 "**module**" 下的 "**body**" 子节点中描述。

"**body**" 的结构如下：

```xml
<body>
    <configs>
        <!-- config list -->
    </configs>
 
    <flows>
        <!-- flow list -->
    </flows>
</body>
```

在 "**body**" 节点下的 "**flows**" 节点中，通过 **"flow**" 标签来定义集成流，并在 **operation** 或 **trigger** 标签的 **flowRef** 中对定义的 **flow** 进行引用即可。**flow** 的定义节点如下：

```xml
<flow name="...">
    <!-- component list -->
</flow>
```

**flow** 只有一个属性：

- **name** 表示集成流名，在 **connector** 内唯一，在 **declaration** 中的 **operation** 或 **trigger** 的 **flowRef** 中使用。

**flow** 的子节点是组件列表，描述了这个的流的结构。根据组件所属模块，每个子节点的标签分为两种：

对于核心模块（**core**）的组件，结构如下：

```xml
<componentName parameterA="..." parameterB="..." ... />
```

标签名为组件名，属性为组件参数。

对于非核心模块的组件，结构如下：

```xml
<moduleName:componentName configRef="..." parameterA="..." parameterB="..." ... />
```

标签名为"模块名:组件名"，例如"<http:request .../>"。"**configRef**" 属性用于指定公共配置集实例的引用，由于第三方模块都需要指定公共配置集，因此需要先在 "**body**" 中定义配置集，然后通过 "**configRef**" 属性进行关联。其它属性为组件参数。

配置集在 "**body**" 节点下的 "**configs**" 节点下定义，每个配置集的定义结构如下：

```xml
<moduleName:propertiesName name="..." parameterA="..." parameterB="..." ... />
```

标签名为"模块名:公共配置集名"，例如"<http:request-config .../>"，“**name”** 属性指定了配置集实例的名称，用于在 **component** 的 **configRef** 中引用，其它属性为该公共配置集中的各配置项。
