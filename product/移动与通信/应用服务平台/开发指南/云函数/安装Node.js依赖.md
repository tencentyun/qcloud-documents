本文档将指导您如何安装云函数安装 Node.js 依赖。
安装云函数安装 Node.js 依赖有两种方式：本地npm安装和在线依赖安装。

## 本地 npm 安装
使用 npm 安装第三方依赖，只能对每个云函数分别安装依赖。
进入函数代码根目录，如安装request库，终端执行如下代码：
```
npm install request --save
```
安装成功的依赖文件会作为该云函数代码的一部分，手动上传到云端使用。



## 在线依赖安装
云开发提供了云端安装依赖，免去了在终端手动安装依赖的工作。


### 在小程序中
在云函数的根目录下，单击右键需要安装依赖的云函数，选择上传并部署：云端安装依赖

### 在 cloudbase CLI
在配置文件cloudbaserc.js对应的云函数的配置项中添加
```
installDependency:true
```

示例如下：

```
module.exports = {
    envId: 'jimmytest-088bef',
    functionRoot: './functions',
    functions: [
        {
            name: 'app',
            config: {
                // 超时时间
                timeout: 5,
                // 环境变量
                envVariables: {
                    key: 'value'
                },
                runtime: 'Nodejs10.15',
                installDependency: true
            },
            // 调用云函数时的输入参数
            params: {},
            handler: 'index.main'
        }
    ]
}

```
