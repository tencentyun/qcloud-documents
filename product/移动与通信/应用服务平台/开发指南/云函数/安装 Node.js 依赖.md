云函数安装 Node.js 依赖有两种方式：**本地 npm 安装**和**在线依赖安装**。

## 本地 npm 安装

使用 npm 安装第三方依赖，只能对每个云函数分别安装依赖。进入函数代码根目录，通过终端执行以下命令安装 request 库。

```bash
npm install request --save
```
安装成功的依赖文件会作为该云函数代码的一部分，手动上传到云端使用。

## 在线依赖安装

CloudBase 提供了云端安装依赖，免去了在终端手动安装依赖的工作。

<dx-tabs>

::: 云开发&nbsp;CloudBase&nbsp;控制台

登录 [云开发 CloudBase 控制台](https://console.cloud.tencent.com/tcb)，在 [函数编辑页面](https://console.cloud.tencent.com/tcb/scf/index)，在线编辑或者上传 zip 代码包之后，单击**保存并安装依赖**。

![](https://main.qcloudimg.com/raw/f51de788458b296091f3017ff999e6c3.png)

:::

::: CloudBase&nbsp;CLI&nbsp;工具
在配置文件 **cloudbaserc.json** 对应的云函数的配置项中添加

```bash
installDependency:true
```

示例如下：

```json
{
  "envId": "xxx",
  "functionRoot": "./functions",
  "functions": [
    {
      "name": "app",
      "config": {
        // 超时时间
        "timeout": 5,
        // 环境变量
        "envVariables": {
          "key": "value"
        },
        "runtime": "Nodejs10.15",
        "installDependency": true
      },
      // 调用云函数时的输入参数
      "params": {},
      "handler": "index.main"
    }
  ]
}
```

:::

</dx-tabs>
