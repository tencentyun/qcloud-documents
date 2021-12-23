## 功能简介
Web 应用防火墙当前有基于正则规则和语义规则两种主流检测手段，检测上也都有其固有的局限性，难以避免出现“漏判”和“误判”现象。腾讯云 Web 应用防火墙应用基于机器学习的 Web 攻击检测技术，通过 AI 引擎的自学习、自进化和自适应能力，最大限度减少误报，提高对已知和未知 Web 威胁的检测率和捕获率，并且灵活适应不断变化的 Web 应用。

## 配置案例 
#### 步骤1：AI 引擎模式设置
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia)，在左侧导航栏中，选择**配置中心** > **基础安全**，进入基础安全页面。
2. 在基础安全页面，左上角选择需要防护的域名，单击 **WEB 安全** > **AI 引擎**，进入 AI 引擎页面。
3. 在 AI 引擎页面，将 AI 引擎模式设置为**观察**。
![](https://qcloudimg.tencent-cloud.cn/raw/e63050d6ddfa2efd5e4cf66faeb5d765.png)
4. 在 [攻击日志页面](https://console.cloud.tencent.com/guanjia/tea-attacklog)，单击“全部攻击类型下拉框”，选择 **AI 引擎检出**，可通过筛选条件，查看该类型的攻击日志。
![](https://qcloudimg.tencent-cloud.cn/raw/ae97647226a59f865b998194fc4eef17.png)

#### 步骤2：AI 在线验证
1. 在 [基础安全页面](https://console.cloud.tencent.com/guanjia/tea-baseconfig)，左上角选择需要防护的域名，单击 **WEB 安全** > **AI 引擎**，进入 AI 引擎页面。
2. 在 AI 引擎页面的 AI 在线验证模块，单击**前往验证**，进入 AI 在线验证页面。
![](https://qcloudimg.tencent-cloud.cn/raw/5513bbf29e5dfb0e66821006d8b32989.png)
3. 在 AI 在线验证页面，可对指定访问地址的 GET 参数、POST 参数和 HEADER 参数进行验证，下面以参数名称为“a” ，参数值为“1 and 1=1”为例进行说明，当正常的参数被 AI 引擎误报时，可单击 **AI 误报处理**，将该误报添加到误报列表。
![](https://qcloudimg.tencent-cloud.cn/raw/3f2180e522ce330964ce8b12ae86dd70.png)

#### 步骤3： AI 误报处理
1. 在上方选项卡，单击 **AI 误报处理**，查看添加的误报记录，或单击**手动添加**，填写相关参数，单击**添加**将误报添加到误报列表中。
![](https://qcloudimg.tencent-cloud.cn/raw/319f2d757733938f5cf5b8d8dd97b90a.png)
2. 在 AI 误报处理页面，选择所需规则，单击**学习**，AI 引擎会根据误报信息更新模型、优化算法。
>?AI 引擎学习提交的误报的 payload，从未学习状态到已学习状态需要一定时间，请耐心等待。
>
![](https://qcloudimg.tencent-cloud.cn/raw/71268d582c76d7cc023382844860ae54.png)
3. 在 AI 引擎学习完提交的误报的 payload 之后，可在**AI 在线验证**页面，再次验证该参数是否仍会误报。
![](https://qcloudimg.tencent-cloud.cn/raw/8b1cc3648f6cbf38564cdfb70dfff593.png)

#### 步骤4：添加漏报
当攻击的载荷被 AI 引擎漏报时，单击**AI 漏报处理**，将该漏报信息添加到漏报列表，下面以参数名称为“a”，参数值为“admin^*$”为例进行说明。
![](https://qcloudimg.tencent-cloud.cn/raw/635ffcdfc7725031d861e3cd07e0add2.png)
 
#### 步骤5：AI 漏报处理
1. 在上方选项卡，单击**AI 漏报处理**，可查看添加的漏报记录，或**手动添加**，填写相关参数，单击**添加**将漏报添加到漏报列表中。
![](https://qcloudimg.tencent-cloud.cn/raw/dd2a47c38749d45143d4cae0f3d11fd7.png)
2. 添加完成后，在状态栏中，单击**学习**，AI 引擎会根据漏报信息更新模型、优化算法。
>?AI 引擎学习提交的漏报的 payload，从未学习状态到已学习状态需要一定时间。
>
![](https://qcloudimg.tencent-cloud.cn/raw/b54f5f8bd1ea3b2f43afa2eefec7252d.png)
3. 在 AI 引擎学习完提交的漏报 payload 之后，可在**AI 在线验证**页面，再次验证该参数是否仍会漏报。
![](https://qcloudimg.tencent-cloud.cn/raw/931176f1d1b5d23207566341fd0b89eb.png)

## 特别说明
- 此 AI 引擎采用严格模式，防护等级最高。
- 此 AI 引擎支持学习，既支持控制台主动的反馈学习，也支持后台被动的自主学习。
- 建议先开启此 AI 引擎的观察模式一段时间（如20天），若直接开启拦截模式，可能会存在低概率的误报。
- 此 AI 引擎与规则引擎为串联关系。当恶意请求被规则引擎拦截时，该恶意请求不再经过 AI 引擎检测。当恶意请求被规则引擎放行时，该恶意请求会再经过 AI 引擎检测并拦截。
- 误报提交方式：在**AI 误报处理**页面手动添加。
- 漏报提交方式：在**AI 漏报处理**页面手动添加。
- 当确认提交的误报或漏报有误时，可在**AI 误报处理**或**AI 漏报处理**页面勾选有误的记录，单击**删除**，进过二次确认后，即可删除。
