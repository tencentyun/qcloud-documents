## 概述

Serverless Web IDE 是腾讯云 Serverless 和 CODING 基于浏览器的集成式开发环境 CloudStudio 深度合作推出的云函数在线开发 IDE，提供接近原生 IDE 的云端开发体验。

Serverless Web IDE 支持：

- 完整的函数开发、部署、测试能力。
- 终端能力，预置了常用的 pip，npm 等开发工具和云函数 SCF 已经支持的编程语言开发环境。
- 完整的 IDE 所含的基础能力，包括智能提示、代码自动补全等。
- 用户自定义 IDE 配置，在不同函数的在线开发中提供一致的 IDE 使用体验。


>! 
>- 我们会为您保留 Serverless Web IDE 中的个性化配置以及代码状态，为了确保函数修改生效，请及时将修改部署到云端。
>- 建议使用最新版本的 Google Chrome 浏览器以获得最佳的 IDE 使用体验。


## 使用方式


1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1)，在左侧选择**函数服务**。
2. 在函数列表中，单击函数名，进入该函数的详情页面。
3. 在“函数管理”页面中，选择**函数代码** > **在线编辑**，即可查看并编辑函数。

## 概览图

本文将以 Serverless Web IDE 工具整体页面从左至右顺序依次介绍。如下图所示： 
![](https://main.qcloudimg.com/raw/9aa546f0ac96be58e8b1fecde7fc5387.png)

1. **资源管理器**
2. **文件编辑区**
3. **函数操作区**
4. **命令行终端**


## 函数操作

在 Serverless Web IDE 中，可以完成函数代码编辑、部署、测试全流程操作。函数测试、部署、测试模板选择等常用操作统一设置在 IDE 右上角的操作区。如下图所示： 
![](https://main.qcloudimg.com/raw/8dca3247b542495680335a64f2a9cc2b.png)

### 函数部署

Serverless Web IDE 提供手动部署和自动部署两种函数部署方式，支持在线安装依赖。

- **部署方式**：
  - **手动部署**：手动部署模式下，您可以通过单击 IDE 右上角**部署**按钮触发函数部署到云端。
  - **自动部署**：自动部署模式下，保存（ctrl + s 或 command + s）即可触发函数部署到云端。
- **在线安装依赖**：目前只支持 Node.js 运行环境，在线安装依赖开启后，在函数部署时会根据 package.json 中的配置自动安装依赖，详情可参考 [在线依赖安装](https://cloud.tencent.com/document/product/583/37920)。

>!
>
>- 函数的根目录为 `/src`，部署操作默认将 `/src` 目录下的文件打包上传。请将需要部署到云端的文件放在 `/src` 目录下。
>- 自动部署模式下保存即触发函数部署到云端，不建议在有流量的函数上开启。

切换部署方式和启用在线依赖安装可通过单击 IDE 右上角操作区箭头的下拉列表中的**自动部署**进行切换，**自动部署：关闭**则代表手动部署模式。
![](https://main.qcloudimg.com/raw/ad8d7ad3a914de0370da5ac9c332b595.png)



### 函数测试

您可以单击 IDE 右上角操作区**测试**触发函数运行，并在输出中查看函数运行结果。

- **选择测试模板**：单击 IDE 操作区的**测试模板**选择函数测试触发事件。
- **新增测试模板**：如果现有的测试模板不能满足您的测试需求，可以在测试模板下拉列表中选择**新增测试模板**自定义测试事件，新增测试事件将以 JSON 文件的格式存储在函数根目录 /src 下的 scf\_test\_event 文件夹中，跟随函数一起部署到云端。如下图所示： 
  ![](https://main.qcloudimg.com/raw/ebf7659796f947ca8630efe57fa87d53.png)


### 查看日志

您可以在输出中查看函数测试结果，包括返回数据 Response、日志 Output 和函数执行摘要 Summary。
![](https://main.qcloudimg.com/raw/cd3fc07e7dc904b45f2e9f1a66222bf9.png)


### 更多操作

在资源管理器函数文件上单击右键展开的列表中，包含了函数相关的全部操作。除部署、测试、新增测试模板等操作外，还提供以下内容：

- **生成 serverless.yml**：将函数当前的配置写入配置文件 serverless.yml，可以使用 Serverless Framework 命令行工具进行二次开发；
- **丢弃当前修改**：重新拉取云端已经部署的函数覆盖当前工作区。

## IDE 操作

Serverless Web IDE 中常用命令、运行环境和预置的扩展版本如下所示：

### 常用命令
<table>
<thead>
<tr>
<th style="text-align:center">命令</th>
<th style="text-align:center">版本</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">python3</td>
<td style="text-align:center">Python 3.7.12<br>python3 默认跟随最新的 Python 3 版本</td>
</tr>
<tr>
<td style="text-align:center">python37</td>
<td style="text-align:center">Python 3.7.12</td>
</tr>
<tr>
<td style="text-align:center">python36</td>
<td style="text-align:center">Python 3.6.1</td>
</tr>
<tr>
<td style="text-align:center">python27</td>
<td style="text-align:center">Python 2.7.13</td>
</tr>
<tr>
<td style="text-align:center">python</td>
<td style="text-align:center">Python 2.7.13</td>
</tr>
<tr>
<td style="text-align:center">node</td>
<td style="text-align:center">Node.js 16.13.1<br>node 命令默认跟随最新 Node.js 版本，环境中还安装了 Node.js 14.18、Node.js 12.16、Node.js 10.15，可在终端执行 n 命令进行切换</td>
</tr>
<tr>
<td style="text-align:center">php80</td>
<td style="text-align:center">PHP 8.0.13</td>
</tr>
<tr>
<td style="text-align:center">php74</td>
<td style="text-align:center">PHP 7.4.26</td>
</tr>
<tr>
<td style="text-align:center">php72</td>
<td style="text-align:center">PHP 7.2.2</td>
</tr>
<tr>
<td style="text-align:center">php56</td>
<td style="text-align:center">PHP 5.6.33</td>
</tr>
<tr>
<td style="text-align:center">php</td>
<td style="text-align:center">PHP 7.2.2</td>
</tr>
<tr>
<td style="text-align:center">pip3</td>
<td style="text-align:center">pip 22.0.4 (python 3.7)</td>
</tr>
<tr>
<td style="text-align:center">pip37</td>
<td style="text-align:center">pip 22.0.4 (python 3.7)</td>
</tr>
<tr>
<td style="text-align:center">pip36</td>
<td style="text-align:center">pip 21.3.1 (python 3.6)</td>
</tr>
<tr>
<td style="text-align:center">pip</td>
<td style="text-align:center">pip 20.3.4 (python 2.7)</td>
</tr>
<tr>
<td style="text-align:center">npm</td>
<td style="text-align:center">8.1.2</td>
</tr>
<tr>
<td style="text-align:center">composer</td>
<td style="text-align:center">2.2.9</td>
</tr>
</tbody>
</table>

### 常用工具
<table>
<thead>
<tr>
<th width="50%" style="text-align:center">工具</th>
<th style="text-align:center">版本</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">yarn</td>
<td style="text-align:center">1.22.18</td>
</tr>
<tr>
<td style="text-align:center">wget</td>
<td style="text-align:center">1.14</td>
</tr>
<tr>
<td style="text-align:center">zip、unzip</td>
<td style="text-align:center">6</td>
</tr>
<tr>
<td style="text-align:center">Git</td>
<td style="text-align:center">2.24.1</td>
</tr>
<tr>
<td style="text-align:center">zsh</td>
<td style="text-align:center">5.0.2</td>
</tr>
<tr>
<td style="text-align:center">dash</td>
<td style="text-align:center">0.5.10.2</td>
</tr>
<tr>
<td style="text-align:center">make</td>
<td style="text-align:center">3.82</td>
</tr>
<tr>
<td style="text-align:center">jupyter</td>
<td style="text-align:center">4.6.3</td>
</tr>
<tr>
<td style="text-align:center">pylint</td>
<td style="text-align:center">1.9.5</td>
</tr>
<tr>
<td style="text-align:center"><a href="https://cloud.tencent.com/document/product/583/44751">Serverless Framework CLI</a></td>
<td style="text-align:center">3.2.1</td>
</tr>
</tbody>
</table>


### 运行环境
<table>
<thead>
<tr>
<th width="50%" style="text-align:center">运行环境</th>
<th style="text-align:center">版本</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Node.js</td>
<td style="text-align:center">16.13、14.18、12.16、10.15</td>
</tr>
<tr>
<td style="text-align:center">Python</td>
<td style="text-align:center">3.7、3.6、2.7</td>
</tr>
<tr>
<td style="text-align:center">PHP</td>
<td style="text-align:center">8.0、7.4、7.2、5.6</td>
</tr>
</tbody>
</table>


### 扩展

<table>
<thead>
<tr>
<th width="50%" style="text-align:center">扩展</th>
<th style="text-align:center">版本</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Python</td>
<td style="text-align:center">2020.11.371526539</td>
</tr>
<tr>
<td style="text-align:center">Jupyter</td>
<td style="text-align:center">2020.12.411183155</td>
</tr>
<tr>
<td style="text-align:center">PHP-IntelliSense</td>
<td style="text-align:center">2.3.14</td>
</tr>
<tr>
<td style="text-align:center">ESLint</td>
<td style="text-align:center">2.1.13</td>
</tr>
<tr>
<td style="text-align:center">Prettier</td>
<td style="text-align:center">5.8.0</td>
</tr>
</tbody>
</table>


## 配额限制

- IDE 为每个用户提供5GB的存储空间，超出将无法执行写入操作，请及时清理。
- 为保证体验，不建议在多个浏览器页面中同时打开3个以上的函数。

## 注意事项

在 IDE 中执行以下操作可能会带来数据泄漏等安全隐患，如必须执行，请谨慎操作。

- 安装 phpmyadmin、struts2 等高危开源组件。

## 常见问题

#### 1. IDE 加载异常如何处理？
如遇工作空间异常无法正常启动等情况，您可以单击 IDE 右下角“**使用遇到问题**”，在展开的页面中点击”**重置工作空间**”将工作空间初始化。

#### 2. 函数在终端中执行成功，点击测试执行失败？

   在线 IDE 的终端和 SCF 的云上运行环境相互独立，点击“**测试**”后返回的运行结果即为函数真实的执行结果。

#### 3. 在终端中执行命令，结果不符合预期？

   如果执行依赖包安装相关命令，请确保在`src`目录下进行操作。

   在使用命令前，请先查看命令的版本，默认支持的命令列表请参考 [常用命令](#ide-.E6.93.8D.E4.BD.9C)。

