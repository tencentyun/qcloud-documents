## 注意事项
由于目前官方 webview 组件暂未上线，使用自定义组件实现的 webview 组件仅支持打开与当前小程序绑定的公众号页面，并且不支持个人小程序使用。自定义组件的基础开发说明可参见 [快速开始创建自定义组件](https://docs.cloudbase.net/lowcode/custom-components/quick-start/comps)。

## 操作步骤
### 步骤1：创建组件库
进入**微搭控制台** > [**组件库管理**](https://console.cloud.tencent.com/lowcode/element/index?envId=lowcode-2gadiaws6be78eca) 页面，单击左上角**新建组件库**进行组件库的创建，组件库的名称与标识填写为 **mydemo**。
![](https://qcloudimg.tencent-cloud.cn/raw/8e10b42c17d98e92dcf3e9888d105503.png)

### 步骤2：安装云开发 CLI 工具
1. 若当前电脑未安装 node.js，需要先前往 [node.js 官网](https://nodejs.org/zh-cn/) 进行安装。
2. node.js 安装完成后，调出 cmd 工具，输入 `npm install -g @cloudbase/cli` 命令进行 CLI 工具的安装。

> !如果运行 `npm install -g @cloudbase/cli` 命令失败，您可能需要修改 npm 权限，或者以系统管理员身份运行：`sudo npm install -g @cloudbase/cli`。
### 步骤3：关联控制台组件库
在 cmd 工具输入 `tcb lowcode create mydemo`，与控制台创建的组件库进行关联，关联完成后本地会生成对应的 mydemo 文件夹，通过在 mydemo 文件夹中对组件代码文件进行编辑即可实现 webview 组件的创建。
### 步骤4：编辑组件文件
1. 在对应目录下找到生成的 mydemo 文件夹,开始进行 web-view 组件文件的编辑。
![](https://qcloudimg.tencent-cloud.cn/raw/9fcc6b564c3cc5da6e23383b45754199.png)
2. 进入 `mydemo/src/mp/components` 文件夹，新建一个文件夹并命名为 webview。
![](https://qcloudimg.tencent-cloud.cn/raw/a90456c7dfb335dd3de01b8c6d1d6d2c.png)
3. 创建四个组件文件，其中 index.wxss 无需填写。不同文件的代码如下：
![](https://qcloudimg.tencent-cloud.cn/raw/8262a03b2c13d389598500acbb48628f.png)
<dx-codeblock>
:::  index.js js
Component({
  properties: {
    src: {
      type: String,
      value: '',
    }
  },
  data: {},
  methods: {
    triggerCustomEvent(e) {
      this.triggerEvent('customevent', e);
    },
  },
});
:::
:::  index.json json
{
  "component": true
}
:::
:::  index.wxml wxml
<web-view src="{{src}}"></web-view>
:::
</dx-codeblock>
4. 组件文件编辑完成后，对 `mydemo/src/mp` 目录下的 index.json 文件进行编辑，代码如下：
<dx-codeblock>
:::  json
{
  "components": {
    "Button": "components/button/index",
    "webview":"components/webview/index"
  },
  "actions": {
    "showToast": "actions/showToast/index"
  }
}
:::
</dx-codeblock>
5. 随后进入 `mydemo/src/configs/components` 文件夹，新建一个名为 webview.json 的文件，代码如下：
<dx-codeblock>
:::  json
{
  "$schema": "https://comp-public-1303824488.cos.ap-shanghai.myqcloud.com/schema/lcds_component.json",
  "data": {
    "type": "object",
    "properties": {
      "src": {
        "title": "链接",
        "default": "https://www.cnblogs.com/-nothing-/p/7910355.html",
        "type": "string"
      }
    }
  },
  "events": [{ "name": "customevent", "title": "自定义事件" }],
  "meta": {
    "title": "webview",
    "description": "webview组件测试",
    "icon": "../icons/button.svg",
    "category": "表单",
    "componentOrder": 1
  }
}
:::
</dx-codeblock>
6. 最后打开 `mydemo/src/configs/components` 下的 index.js 文件，对代码进行编辑，代码如下：
<dx-codeblock>
:::  js
import Button from './components/button';
import webview from './components/webview';
import showToast from './actions/showToast';
export const components = {
  Button,webview
};
export const actions = {
  showToast,
};
export default {
  components,
  actions,
};
:::
</dx-codeblock>
### 步骤5：调试组件库
1. 在 cmd 工具中输入 `cd mydemo` 命令后进入组件文件夹，之后输入 `tcb lowcode debug` 即可进行组件库的调试。
2. 此时浏览器会自动打开组件调试页面，在左侧配置区中可以看到 webview 组件已正常展示，并且可以在右侧的组件配置区中进行 webview 组件链接的配置。
![](https://qcloudimg.tencent-cloud.cn/raw/c92a182a555330d13721a051a55efe02.png)
> ? 由于 webview 组件仅支持在真实小程序环境中运行，因此该组件需要在应用发布为小程序之后才能够看到真实效果。
### 步骤6：发布组件库
在 cmd 工具输入 `tcb lowcode publish`，进行组件的发布，随后在控制台-组件库管理中单击 mydemo 组件库的**发布组件库**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/e88e34475523859ad318c5631e99257f.png)
### 步骤7：在应用中使用 webview 组件
创建一个应用，构建模式选择小程序构建，之后在应用编辑器中选择 webview 组件，在组件配置区中填写自己的公众号文章链接。
![](https://qcloudimg.tencent-cloud.cn/raw/21a6f078682269b0ed72dba3657e12d3.png)
## 发布查看效果
发布后即可查看组件在小程序端的运行效果，如下所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/c349ca0a60cb7845e4d574acae32a7b4.png" style="width:50%;" />
