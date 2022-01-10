## Node.js 版本选择

目前支持的 Node.js 开发语言包括如下版本：

- Node.js 16.13
- Node.js 14.18
- Node.js 12.16
- Node.js 10.15
- Node.js 8.9（即将下线）
- Node.js 6.10（即将下线）

您可以在函数创建时，选择您所期望使用的运行环境。

## 相关环境变量

目前 Node.js 运行环境中内置的相关环境变量见下表：

| Node.js  版本 | 环境变量 Key | 具体值或值来源                                               |
| ------------- | ------------ | ------------------------------------------------------------ |
| Node.js 16.13 | `NODE_PATH`  | /var/user:/var/user/node_modules:/var/lang/node16/lib/node_modules:/opt:/opt/node_modules |
| Node.js 14.18 | `NODE_PATH`  | /var/user:/var/user/node_modules:/var/lang/node14/lib/node_modules:/opt:/opt/node_modules |
| Node.js 12.16 | `NODE_PATH`  | /var/user:/var/user/node_modules:/var/lang/node12/lib/node_modules:/opt:/opt/node_modules |
| Node.js 10.15 | `NODE_PATH`  | /var/user:/var/user/node_modules:/var/lang/node10/lib/node_modules:/opt:/opt/node_modules |
| Node.js 8.9   | `NODE_PATH`  | /var/user:/var/user/node_modules:/var/lang/node8/lib/node_modules:/opt:/opt/node_modules |
| Node.js 6.10  | `NODE_PATH`  | /var/user:/var/user/node_modules:/var/lang/node6/lib/node_modules:/opt:/opt/node_modules |

更多详细环境变量说明请参见 [环境变量说明](https://cloud.tencent.com/document/product/583/30228)。

## 已包含的库及使用方法

> !   Node.js 14.18 及之后版本，平台不再额外内置依赖库。代码运行所需依赖，请参考 [依赖安装](https://cloud.tencent.com/document/product/583/39780#node.js-.E8.BF.90.E8.A1.8C.E6.97.B6) 及 [在线依赖安装](https://cloud.tencent.com/document/product/583/37920)。

### COS SDK

云函数 Node.js 12.16 及更早版本的运行环境内已包含 [COS 的 Node.js SDK](https://cloud.tencent.com/document/product/436/8629)，具体版本为 `cos-nodejs-sdk-v5`。

可在代码内通过如下方式引入 COS SDK 并使用：
```
var COS = require('cos-nodejs-sdk-v5');
```

更详细的 COS SDK 使用说明请参见 [COS Node.js SDK](https://cloud.tencent.com/document/product/436/8629)。

### 环境内的内置库

 Node.js 各版本运行时内已支持的库如下表：


<dx-tabs>
::: Node.js 12.16
<table><thead>
<tr><th width="60%">库名称</th><th width="40%">版本</th></tr>
</thead>
<tbody><tr>
<td align="left">cos-nodejs-sdk-v5</td>
<td align="left">2.5.20</td>
</tr>
<tr>
<td align="left">base64-js</td>
<td align="left">1.3.1</td>
</tr>
<tr>
<td align="left">buffer</td>
<td align="left">5.5.0</td>
</tr>
<tr>
<td align="left">crypto-browserify</td>
<td align="left">3.12.0</td>
</tr>
<tr>
<td align="left">ieee754</td>
<td align="left">1.1.13</td>
</tr>
<tr>
<td align="left">imagemagick</td>
<td align="left">0.1.3</td>
</tr>
<tr>
<td align="left">isarray</td>
<td align="left">2.0.5</td>
</tr>
<tr>
<td align="left">jmespath</td>
<td align="left">0.15.0</td>
</tr>
<tr>
<td align="left">lodash</td>
<td align="left">4.17.15</td>
</tr>
<tr>
<td align="left">microtime</td>
<td align="left">3.0.0</td>
</tr>
<tr>
<td align="left">npm</td>
<td align="left">6.13.4</td>
</tr>
<tr>
<td align="left">punycode</td>
<td align="left">2.1.1</td>
</tr>
<tr>
<td align="left">puppeteer</td>
<td align="left">2.1.1</td>
</tr>
<tr>
<td align="left">qcloudapi-sdk</td>
<td align="left">0.2.1</td>
</tr>
<tr>
<td align="left">querystring</td>
<td align="left">0.2.0</td>
</tr>
<tr>
<td align="left">request</td>
<td align="left">2.88.2</td>
</tr>
<tr>
<td align="left">sax</td>
<td align="left">1.2.4</td>
</tr>
<tr>
<td align="left">scf-nodejs-serverlessdb-sdk</td>
<td align="left">1.1.0</td>
</tr>
<tr>
<td align="left">tencentcloud-sdk-nodejs</td>
<td align="left">3.0.147</td>
</tr>
<tr>
<td align="left">url</td>
<td align="left">0.11.0</td>
</tr>
<tr>
<td align="left">uuid</td>
<td align="left">7.0.3</td>
</tr>
<tr>
<td align="left">xml2js</td>
<td align="left">0.4.23</td>
</tr>
<tr>
<td align="left">xmlbuilder</td>
<td align="left">15.1.0</td>
</tr>
</tbody></table>
:::
::: Node.js 10.15
<table>
<thead>
<tr><th width="60%">库名称</th><th width="40%">版本</th></tr>
</thead>
<tbody><tr>
<td align="left">cos-nodejs-sdk-v5</td>
<td align="left">2.5.14</td>
</tr>
<tr>
<td align="left">base64-js</td>
<td align="left">1.3.1</td>
</tr>
<tr>
<td align="left">buffer</td>
<td align="left">5.4.3</td>
</tr>
<tr>
<td align="left">crypto-browserify</td>
<td align="left">3.12.0</td>
</tr>
<tr>
<td align="left">ieee754</td>
<td align="left">1.1.13</td>
</tr>
<tr>
<td align="left">imagemagick</td>
<td align="left">0.1.3</td>
</tr>
<tr>
<td align="left">isarray</td>
<td align="left">2.0.5</td>
</tr>
<tr>
<td align="left">jmespath</td>
<td align="left">0.15.0</td>
</tr>
<tr>
<td align="left">lodash</td>
<td align="left">4.17.15</td>
</tr>
<tr>
<td align="left">microtime</td>
<td align="left">3.0.0</td>
</tr>
<tr>
<td align="left">npm</td>
<td align="left">6.4.1</td>
</tr>
<tr>
<td align="left">punycode</td>
<td align="left">2.1.1</td>
</tr>
<tr>
<td align="left">puppeteer</td>
<td align="left">2.0.0</td>
</tr>
<tr>
<td align="left">qcloudapi-sdk</td>
<td align="left">0.2.1</td>
</tr>
<tr>
<td align="left">querystring</td>
<td align="left">0.2.0</td>
</tr>
<tr>
<td align="left">request</td>
<td align="left">2.88.0</td>
</tr>
<tr>
<td align="left">sax</td>
<td align="left">1.2.4</td>
</tr>
<tr>
<td align="left">scf-nodejs-serverlessdb-sdk</td>
<td align="left">1.0.1</td>
</tr>
<tr>
<td align="left">tencentcloud-sdk-nodejs</td>
<td align="left">3.0.104</td>
</tr>
<tr>
<td align="left">url</td>
<td align="left">0.11.0</td>
</tr>
<tr>
<td align="left">uuid</td>
<td align="left">3.3.3</td>
</tr>
<tr>
<td align="left">xml2js</td>
<td align="left">0.4.22</td>
</tr>
<tr>
<td align="left">xmlbuilder</td>
<td align="left">13.0.2</td>
</tr>
</tbody></table>

:::
::: Node.js 8.9
<table>
<thead>
<tr><th width="60%">库名称</th><th width="40%">版本</th></tr>
</thead>
<tbody><tr>
<td align="left">cos-nodejs-sdk-v5</td>
<td align="left">2.5.8</td>
</tr>
<tr>
<td align="left">base64-js</td>
<td align="left">1.2.1</td>
</tr>
<tr>
<td align="left">buffer</td>
<td align="left">5.0.7</td>
</tr>
<tr>
<td align="left">crypto-browserify</td>
<td align="left">3.11.1</td>
</tr>
<tr>
<td align="left">ieee754</td>
<td align="left">1.1.8</td>
</tr>
<tr>
<td align="left">imagemagick</td>
<td align="left">0.1.3</td>
</tr>
<tr>
<td align="left">isarray</td>
<td align="left">2.0.2</td>
</tr>
<tr>
<td align="left">jmespath</td>
<td align="left">0.15.0</td>
</tr>
<tr>
<td align="left">lodash</td>
<td align="left">4.17.4</td>
</tr>
<tr>
<td align="left">npm</td>
<td align="left">5.6.0</td>
</tr>
<tr>
<td align="left">punycode</td>
<td align="left">2.1.0</td>
</tr>
<tr>
<td align="left">puppeteer</td>
<td align="left">1.14.0</td>
</tr>
<tr>
<td align="left">qcloudapi-sdk</td>
<td align="left">0.1.5</td>
</tr>
<tr>
<td align="left">querystring</td>
<td align="left">0.2.0</td>
</tr>
<tr>
<td align="left">request</td>
<td align="left">2.87.0</td>
</tr>
<tr>
<td align="left">sax</td>
<td align="left">1.2.4</td>
</tr>
<tr>
<td align="left">tencentcloud-sdk-nodejs</td>
<td align="left">3.0.56</td>
</tr>
<tr>
<td align="left">url</td>
<td align="left">0.11.0</td>
</tr>
<tr>
<td align="left">uuid</td>
<td align="left">3.1.0</td>
</tr>
<tr>
<td align="left">xml2js</td>
<td align="left">0.4.17</td>
</tr>
<tr>
<td align="left">xmlbuilder</td>
<td align="left">9.0.1</td>
</tr>
</tbody></table>
:::
::: Node.js 6.10
<table>
<thead>
<tr><th width="60%">库名称</th><th width="40%">版本</th></tr>
</thead>
<tbody><tr>
<td align="left">base64-js</td>
<td align="left">1.2.1</td>
</tr>
<tr>
<td align="left">buffer</td>
<td align="left">5.0.7</td>
</tr>
<tr>
<td align="left">cos-nodejs-sdk-v5</td>
<td align="left">2.0.7</td>
</tr>
<tr>
<td align="left">crypto-browserify</td>
<td align="left">3.11.1</td>
</tr>
<tr>
<td align="left">ieee754</td>
<td align="left">1.1.8</td>
</tr>
<tr>
<td align="left">imagemagick</td>
<td align="left">0.1.3</td>
</tr>
<tr>
<td align="left">isarray</td>
<td align="left">2.0.2</td>
</tr>
<tr>
<td align="left">jmespath</td>
<td align="left">0.15.0</td>
</tr>
<tr>
<td align="left">lodash</td>
<td align="left">4.17.4</td>
</tr>
<tr>
<td align="left">npm</td>
<td align="left">3.10.10</td>
</tr>
<tr>
<td align="left">punycode</td>
<td align="left">2.1.0</td>
</tr>
<tr>
<td align="left">qcloudapi-sdk</td>
<td align="left">0.1.5</td>
</tr>
<tr>
<td align="left">querystring</td>
<td align="left">0.2.0</td>
</tr>
<tr>
<td align="left">request</td>
<td align="left">2.87.0</td>
</tr>
<tr>
<td align="left">sax</td>
<td align="left">1.2.4</td>
</tr>
<tr>
<td align="left">tencentcloud-sdk-nodejs</td>
<td align="left">3.0.10</td>
</tr>
<tr>
<td align="left">url</td>
<td align="left">0.11.0</td>
</tr>
<tr>
<td align="left">uuid</td>
<td align="left">3.1.0</td>
</tr>
<tr>
<td align="left">xml2js</td>
<td align="left">0.4.17</td>
</tr>
<tr>
<td align="left">xmlbuilder</td>
<td align="left">9.0.1</td>
</tr>
</tbody></table>


:::
</dx-tabs>
