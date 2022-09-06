## 功能简介
API 流量分析功能支持自动发现并梳理已接入 Web 应用防火墙（WAF）防护的业务中开放的 API 、API 参数资产，并提供相关攻击防护指引及相关异常业务调查方案，通过对异常的 API 事件及流量分析，提供详细的风险处理建议和 API 生命周期管理参考数据，帮助您实现 API 安全防护。


## 前提条件
已开通中国大陆版的 [WAF 包年包月实例](https://cloud.tencent.com/document/product/627/11730)，并购买 API 安全实例。
>?API 流量分析功能当前处于公测中，暂时支持试用该功能，公测期间仅支持开启3个域名。


## 开启 API 流量分析
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-overview)，支持通过如下两种方式开启 API 流量分析功能。
  - 在[ 域名列表页面](https://console.cloud.tencent.com/guanjia/tea-domain)，支持查看当前有哪些域名开启了 API 分析功能，并且可以在对应的 WAF 开关列中单击![](https://qcloudimg.tencent-cloud.cn/raw/bd4ed4cc49def692d37b93f06a3a9bf6.png)，经二次确认后，即可开启 API 分析开关。
![](https://qcloudimg.tencent-cloud.cn/raw/f69470dee19af38f7b385756247345d0.png)
 - 在 [API 资产列表页面](https://console.cloud.tencent.com/guanjia/tea-apianalysis)，选择所需域名，单击 API 防护概览中的开关![](https://qcloudimg.tencent-cloud.cn/raw/fc00324752a7231a4524eefaff6a6116.png)，API 防护概况会变为 API 资产识别中。
![](https://qcloudimg.tencent-cloud.cn/raw/d97d40364e7992e717acda2ff771afea.png)
2. 开启对应域名的 API 流量分析开关后，即可对当前域名进行 API 流量的分析。


## 查看 API 资产列表数据
自开启所选域名的 API 流量分析功能后，API 安全会发现并捕获相关的流量数据，自动对当前业务项进行相关的分析及梳理，并展示在 [API 资产列表页面](https://console.cloud.tencent.com/guanjia/tea-apianalysis)。
- 在 **API 概览模块**中，展示当前域名下的全部的 API 数量、过去7天内活跃/不活跃的 API 数量以及涉敏的 API 数量。并可以直观的了解到对比上一个7日中的环比数量的增减，清晰的了解到当前线上的 API 的现状。
![](https://qcloudimg.tencent-cloud.cn/raw/430cf07ace3aaac382e2ce1e701f71e2.png)
字段说明
 - **API 总数**： API 管控所识别的 API 资产总数。
 - **过去7日活跃 API**：过去7日有活跃流量的 API 数。
 - **过去 7 日不活跃 API**：过去7日没有活跃流量的 API 数，有潜在变为僵尸 API 的风险。
 - **涉敏 API**：API 管控识别的包含涉敏字段的 API 数量。
 - **环比数量变化**：用于统计对比上一统计周期（7天）的对应属性的 API数量变化，快速识别新增、僵尸、涉敏 API 的数量的变化。
- 在 **API 防护概况模块**中，展示当前域名的防护场景数量，并且可以获取对应的防护建议，以及当前 API 分析的内容。
 ![](https://qcloudimg.tencent-cloud.cn/raw/0c76e7e5a159a9ba953d69c097501d98.png)
 字段说明
 - **覆盖场景**：指当前 API 管控中，识别出来当前 API 所覆盖的场景类型的数量，该场景数量会随着识别出来的 API 场景增多而增加。
 - **防护建议**：指在当前的 API 管控中，识别出来对应场景的防护建议。
 - **分析开关**：指当前域名的 API 管控流量分析开关。
- 在 **API 列表**中，展示了 API、请求方式，对应域名、覆盖功能场景、是否包含敏感字段、是否活跃，是否存在相关防护建议、以及 API 发现时间、API 参数最近变更时间等。并支持通过单击对应 API 的**查看详情**，获悉该 API 的相关 API 详情。
![](https://qcloudimg.tencent-cloud.cn/raw/58b02d8766fd77274ec4bc4f840a5abb.png)
 字段说明
 - **API**：指经过 API 管控分析后，识别出来的经过数据归一化折叠后的 API 信息，展示当前 API 的经过数据归一化后的 API 的样式，用户 id 、信息 id 等信息过于分散导致 API 的散列度过大，造成当前 API 观测过难的问题。
 - **请求方法**：HTTP 请求方法。
 - **所属域名**：当前 API 的归属域名。
 - **功能场景**：由 API 管控识别出来的相关业务的功能场景、如验证码、回调等，如果识别出的数据不准确，可以在 [API 详情](#xq) 中进行相关修正。
 - **涉敏字段**：由 API 管控识别出来的传输参数上存在敏感字段的字段内容，包括但不限于银行卡号、身份证号等数据字段，如果识别出来的数据类型不准确，可以在 [API 详情](#xq) 中进行相关修正。
 - **过去7天是否活跃**：过去7天内是否为活跃流量。
 - **最近更新时间**：最新的更新时间，用于检测当前 API 的相关数据字段是否发生新增等情况。
 - **发现时间**：api 首次被 API 分析模块发现的时间。
 - **查看详情**：进入对应 API 的详情页面。


## API 详情[](id:xq)
在 API 列表中，单击目标 API **操作列**的**查看详情**，可以进入 API 详情页面，该页面展示了经过 API 管控分析之后的单一 API 的相关详情，包括如下5个部分内容：
- **API 概要**：展示该 API 所属域名、请求方法、相关功能标签、是否存在敏感字段、是否活跃以及进行数据归一化后的 API 内容。
![](https://qcloudimg.tencent-cloud.cn/raw/43a156f21e4155a152d136fb0ea0c302.png)
- **API 概览**：展示最近7天内，对应 API 的总请求量及请求趋势，访问的来源分布、访问最多的 URL 及 UA 类型。
![](https://qcloudimg.tencent-cloud.cn/raw/80609a6025fa87deb6b49fe0af5a9ccb.png)
- **API 攻击概览**：展示最近7天内，该 API 的攻击趋势，以及攻击分布，包括 IP 类型、IP 来源、URL、UA、攻击类型分类。
![](https://qcloudimg.tencent-cloud.cn/raw/fe01ae16d6dd7bdf8923114e4709b3ef.png)
- **请求参数样例**：展示该 API 经过数据抽象化后，展示的数据内容信息。
![](https://qcloudimg.tencent-cloud.cn/raw/e456bc6588f25458e58707992910d138.png)
- **参数列表**：展示该 API 传输的各个参数字段的内容信息、位置信息，并可以对其进行手动打标。
![](https://qcloudimg.tencent-cloud.cn/raw/538972c73a40ba5b607f8110496bd53a.png)
