### Serverless Framework 报错 "component" input is requires to run custom methods 如何处理？

运行 Serverless Framework CLI 时，如果 yaml 配置文件中默认引用了 Component 组件，则需要保证当前文件夹内容为空，才可以正确运行 Component 的安装命令。
您可以尝试在一个空文件夹中重新运行`serverless create`命令，则不会再出现该错误。

更多的问题和反馈，可以参考 [Github 仓库 Issues](https://github.com/serverless-components?q=tencent)。
