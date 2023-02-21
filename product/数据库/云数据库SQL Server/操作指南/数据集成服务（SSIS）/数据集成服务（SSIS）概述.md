
## 功能简介
SSIS、SSAS、SSRS 是 SQL Server 实现商业智能（BI）的三个重要组件。
- SQL Server Integration Services（SSIS）提供了企业级数据集成和数据转换解决方案，可以用于各种数据源的提取、转换、加载（ETL）等操作。
- SQL Server Analysis Services（SSAS）是一种数据分析引擎，可用于建立 Cube 多维数据模型。
- SQL Server Reporting Services (SSRS) 是一种报表工具，用于创建、部署和管理移动和分页报表。

腾讯云数据库 SQL Server 发布商业智能服务器，提供集数据存储、抽取、转换、装载、可视化分析一体的全套商业智能解决方案，目前已支持 SSIS 数据集成服务。使用 Integration Services 可解决复杂的业务场景，例如合并来自异构数据存储区的数据、数据清洗和数据标准化、填充数据仓库和数据集、处理复杂商业逻辑的数据转换、支持管理功能和数据加载自动化等，帮助客户全链路解决商业智能分析、高价值数据挖掘、主数据管理体系建设等场景的问题。

Integration Services 支持从各种数据源中提取和转换数据，然后将数据加载到一个或多个目标。腾讯云云上 Integration Services 能力当前支持云数据库 SQL Server 及平面文件（要求为 txt、csv、xlsx、xls 后缀）。

云数据库 SQL Server 使用 SSIS 能力，需要通过商业智能服务器中 Integration Services 引擎部署项目。

## 应用场景
### 合并来自异构数据存储区的数据
数据通常被存储在很多个不同的数据存储系统中，很多时候我们需要从这些数据源中提取数据并将其合并到单个一致的数据集中。这个过程面临早期系统繁多、数据存储格式复杂多样、合并可能需要复杂多样的预处理等问题。

SSIS 可以使用 .NET 和 OLE DB 访问接口连接到云数据库，还可以使用 ODBC 驱动程序连接到多个早期数据库，还可以连接到平面文件、Excel 文件等。同时 SSIS 也包含一些源组件，可以从不同的数据源中提取数据。SSIS 提供转换功能对数据进行转换。数据转换为兼容格式后，就可以将其物理合并到一个目标数据库。数据在合并成功且应用转换后，SSIS 可以将数据加载到平面文件、SQL Server 数据库中。

### 数据清洗和数据标准化
由于众多的数据源使用不同的约定和标准，加载中需要执行不同的业务处理，无论数据是加载到联机事务处理、联机分析处理数据库、Excel 电子表格还是加载到文件，都需要在加载前将数据进行清理和标准化。

SSIS 包含一些内置转换，可将其添加到包中以进行数据清洗和数据标准化、更改数据的大小写、将数据转换为不同类型/格式或者根据表达式创建新的列值。例如，包可将姓列和名列连接成单个全名列，然后将字符更改为大写。Integration Services 还可以使用精确查找或模糊查找来找到引用表中的值，通过将列中的值替换为引用表中的值来清理数据。

### 数据转换过程支持复杂商业逻辑处理
数据转换过程需要内置逻辑来动态响应其访问和处理的数据。需要根据数据值对数据进行汇总、转换和分发，根据对列值的评估，该过程甚至可能需要拒绝数据。SSIS 提供了很多相关类型的任务：
- 合并来自多个数据源的数据。
- 计算数据并应用数据转换。
- 根据数据值将一个数据集拆分为多个数据集。
- 将不同的聚合应用到一个数据集的不同子集。
- 将数据的子集加载到不同目标或多个目标。

### 支持管理功能和数据加载自动化
SSIS 提供了相关的组件实现管理的自动化，例如复制 SQL Server 数据库及其包含的对象、复制 SQL Server 对象和加载数据、设置 SSIS 任务作业的调度周期频率等。

## 客户价值
### 高质量数据价值挖掘
将企业中分散、非完全结构化、标准不统一的各种数据，通过数据清洗加工，整合到一起，挖掘数据价值，形成企业级统一数据库，为企业的分析决策提供有质量保证的数据源。

### 主数据管理体系建设
业务早期系统可能面临数据繁多、数据存储格式复杂多样、合并可能需要复杂多样的预处理等问题，SSIS 可将存储在多个不同数据存储系统中的数据进行数据抽取转换装载合并到一个目标数据库，建设业务的主数据库，便于企业内部对数据的维护与管理，同时也可降低纷繁多杂数据库的存储与维护成本。

### 商业智能分析
与 BI 结合， 提供集数据存储、抽取、装载、转换、可视化分析一体的全套商业智能分析解决方案，可让业务人员能一站式完成从数据源的存储到数据可视化分析，全链路的轻松实现数据实时自助可视化分析，也可助力客户搭建企业数据中台，实现数据指导业务精细化运营。

### 内部业务系统数据集成
使用云上 SSIS，可提升数据采集和清洗的效率、准确性和系统性能大幅提高，同时简化了整个数据汇总分析的过程，设置 SSIS 自动调度作业，自动化地进行数据抽取转换装载，方便与企业内部业务系统进行数据集成。

## 使用限制
- 目前商业智能服务器处于公测阶段，公测期免费使用，期间每个地域限购1台，每个主账号最多限购3台，仅支持2核4GB规格。公测期结束后将启动计费，计费方式为按量计费。
- 商业智能服务器目前仅支持 SQL Server Integration Services（SSIS）引擎，支持三个版本，分别为 SQL Server 2016 Integration Services 、SQL Server 2017 Integration Services、SQL Server 2019 Integration Services。
- 云数据库 SQL Server 的单节点（原基础版）、双节点（原高可用版/集群版）均可以通过商业智能服务器使用 SSIS 能力，只读实例不支持 SSIS 能力。
- 商业智能服务器目前仅支持广州、上海、北京、香港这四个地域。

## 注意事项
- SSIS 能力当前支持云数据库 SQL Server 及平面文件（要求为txt、csv、xlsx、xls 后缀）。
- 商业智能服务器的所属地域需要与源 SQL Server 数据库实例及目标 SQL Server 数据库实例的地域保持一致。同一地域的不同可用区之间的 SQL Server 数据库实例与商业智能服务器之间内网可互通。
- 同一个商业智能服务器可接入的数据库实例的个数不限，即可通过同一个商业智能服务器同时连接多个源实例及目标实例，运行多个 SSIS 项目任务。
- 商业智能服务器的 CPU 和内存规格大小的占用与 SSIS 项目的任务复杂度有关，商业智能服务器的磁盘大小的占用与所添加的平面文件大小有关。
- 平面文件需要上传到对象存储 COS上，才可获取要上传的 COS 源文件链接，将平面文件部署至商业智能服务器中，注意对象存储的对象访问权限需要设置为公有读私有写。平面文件只支持 txt,csv,xlsx,xls 后缀。文件名必须是字母开头且只支持数字，字母，下划线和中划线。
- 通过控制台创建的商业智能服务器的 Windows 鉴权账号，会自动在您创建的账号前添加域前缀，该前缀您无需关注。例如：您在控制台创建的账号为 act1，则列表中的账号名显示为 xx_x_xx_xxxx/act1。
- SSIS 项目涉及的相关源数据库实例、目标数据库实例及商业智能服务器需要互通，以此才可保证各实例间可以互相访问，进而进行 SSIS 项目的部署。因此在部署 SSIS 项目前，需要将 SSIS 项目相关的源、目标数据库实例与商业智能服务器实例加入至同一互通组中且每个实例均需要开启商业智能服务互通 IP。
- 数据库实例及商业智能服务器实例，在加入互通组后，均有两个 IP 地址，一个为内网 IP，一个为商业智能服务互通 IP，两个 IP 地址各有所用，请在操作步骤中注意区分。
- SSIS 项目仅支持项目部署模式。
- 支持使用 SQL Server Agent 运行 SSIS 程序包。
- 请不要手动创建或者恢复 SSISDB 数据库，否则可能造成实例 SSIS 无法正常使用。

## 操作流程
**前提条件**
准备好已构建的 SSIS 的项目文件，为 “.ispac” 后缀格式。
**1. [购买商业智能服务器](https://cloud.tencent.com/document/product/238/75224)**
云数据库 SQL Server 使用 Integration Services（SSIS）数据集成服务能力，需要通过商业智能服务器中 Integration Services 引擎进行项目部署。如果您的 SSIS 项目相关的源及目标云数据库 SQL Server 实例已存在同地域的商业智能服务器，则可跳过此步骤，直接通过已存在的商业智能服务器进行**步骤2**。如果您第一次使用 SSIS 功能，则需购买商业智能服务器。

**2. [创建 Windows 鉴权账号](https://cloud.tencent.com/document/product/238/75225)**
商业智能服务器实例需要创建 Windows 鉴权账号，后续才可用该账号登录商业智能服务器实例部署 SSIS 项目。故在部署 SSIS 项目前，您需要先在商业智能服务器中创建 Windows 鉴权账号。
>?商业智能服务器中创建的账号均是具有 Windows 鉴权的账号，商业智能服务器仅允许使用 Windows 鉴权账号，且账号权限不支持修改。

**3. [添加平面文件](https://cloud.tencent.com/document/product/238/75226)**
在 SSIS 项目部署之前，需要确定 SSIS 项目中是否有涉及平面文件，如果有涉及平面文件，则需要在 SSIS 项目部署之前，将平面文件添加于商业智能服务器中。如果 SSIS 项目的源和目标不涉及平面文件，则该步骤无需操作，直接进行**步骤4**。

**4. [互通源、目标实例及商业智能服务器](https://cloud.tencent.com/document/product/238/75227)**
在 SSIS 项目部署之前，还需要将 SSIS 项目涉及的相关源数据库实例、目标数据库实例及商业智能服务器互通，以此保证各实例间可以互相访问。互通组管理功能用于承载实例间的互通访问，因此同一账号同一地域下，SSIS 项目相关的所有数据库实例与商业智能服务器实例需要加入至同一互通组中且每个实例均需要开启商业智能服务互通 IP，加入至互通组中的多个实例之间可便以互相访问。

**5. [部署 SSIS 项目](https://cloud.tencent.com/document/product/238/75228)**
在 SSIS 项目部署之前，首先需要连接商业智能服务器。需要进行以下步骤：
5.1 在 Windows 云服务器 CVM 创建与商业智能服务器中同名同密码的 Windows 系统鉴权账号。
5.2 使用5.1步骤中在 Windows 云服务器 CVM 上创建的 Windows 系统鉴权账号来登录 Windows 云服务器 CVM。
5.3 使用 Windows 系统鉴权账号登录商业智能服务器实例。
5.4 部署 SSIS 项目。
5.5 配置 SSIS 服务，包括平面文件连接配置及源和目标 SQL Server 数据库实例连接配置。
5.6 运行 SSIS 服务，执行 package 包。
5.7 配置 agent 作业，包括新建作业步骤、新建作业执行计划等。

## 云数据库 SQL Server 数据集成服务（SSIS）功能相关操作
<table>
<thead><tr><th>功能页</th><th>功能项</th><th>操作说明、参考步骤</th></tr></thead>
<tbody>
<tr>
<td rowspan="6">实例列表</td>
<td>购买商业智能服务器</td><td>新建/购买商业智能服务器请参见 <a href="https://cloud.tencent.com/document/product/238/75224" target="_blank">购买商业智能服务器</a>。</td></tr>
<td>修改实例名称</td><td> 与 SQL Server 数据库实例操作方法相同，请参见 <a href="https://cloud.tencent.com/document/product/238/70169" target="_blank">修改实例名称</a>。</td></tr>
<td>重启</td><td>与 SQL Server 数据库实例操作方法相同，请参见 <a href="https://cloud.tencent.com/document/product/238/70918" target="_blank">重启实例</a>。</td></tr>
<td>销毁实例</td><td>与 SQL Server 数据库实例操作方法相同，请参见 <a href="https://cloud.tencent.com/document/product/238/43225" target="_blank">销毁实例</a>。</td></tr>
<td>回收站</td><td>商业智能服务器 实例销毁或误删除后，在回收站的操作方法与 SQL Server 数据库实例相同，请参见 <a href="https://cloud.tencent.com/document/product/238/70915" target="_blank">回收站</a>。</td></tr>
<td>编辑标签</td><td>与 SQL Server 数据库实例相同，请参见 <a href="https://cloud.tencent.com/document/product/238/70916" target="_blank">设置实例标签</a>。</td></tr>
<tr>
<td rowspan="8">实例管理</td>
<td>设置实例备注</td><td>与 SQL Server 数据库实例相同，请参见 <a href="https://cloud.tencent.com/document/product/238/70170" target="_blank">设置实例备注</a>。</td></tr>
<td>更改网络</td><td> 与 SQL Server 数据库实例操作方法相同，请参见 <a href="https://cloud.tencent.com/document/product/238/68270" target="_blank">更改网络（VPC 转 VPC）</a>。</td></tr>
<td>修改项目</td><td>与 SQL Server 数据库实例操作方法相同，请参见 <a href="https://cloud.tencent.com/document/product/238/43219" target="_blank">设置实例所属项目</a>。</td></tr>
<td>设置实例维护信息</td><td>与 SQL Server 数据库实例操作方法相同，请参见 <a href="https://cloud.tencent.com/document/product/238/43218" target="_blank">设置实例维护信息</a>。</td></tr>
<td>查看监控图表</td><td>商业智能服务器 实例监控项与 SQL Server 数据库实例的监控项不完全一致，详细监控项以实际监控页面显示为准，操作请参考 <a href="https://cloud.tencent.com/document/product/238/70272" target="_blank">查看监控图表</a>。</td></tr>
<td>配置安全组</td><td>商业智能服务器 实例也需要配置安全组，请参见 <a href="https://cloud.tencent.com/document/product/238/43287" target="_blank">配置安全组</a>。</td></tr>
<td>账号管理</td><td>创建、删除账号登操作请参见 <a href="https://cloud.tencent.com/document/product/238/75225" target="_blank">创建 Windows 鉴权账号</a>。</td></tr>
<td>SSIS 管理</td><td>SSIS 管理添加文件操作请参见 <a href="https://cloud.tencent.com/document/product/238/75226" target="_blank">添加平面文件</a>。</td></tr>
<tr>
<td rowspan="1">互通组管理</td>
<td>互通源、目标实例及商业智能服务器</td><td>开启商业智能服务互通 IP 、添加互通实例，请参见 <a href="https://cloud.tencent.com/document/product/238/75227" target="_blank">互通源目标实例及商业智能服务器</a>。</td></tr>
</tbody></table>
