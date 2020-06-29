## 开发模式

开发模式是为处于开发状态下的项目可以更便捷的进行代码编写、开发调试而设计的。在开发模式中，用户可以持续地进行开发-调试的过程，尽量减少打包、更新等其他工作的干扰。

### 进入开发模式

在项目下执行 `serverless dev`命令，可以进入项目的开发模式。

示例如下：
```
$ sls dev
serverless ⚡ framework
Dev Mode - Watching your Component for changes and enabling streaming logs, if supported...

Debugging listening on ws://127.0.0.1:9222.
For help see https://nodejs.org/en/docs/inspector.
Please open chorme, and visit chrome://inspect, click [Open dedicated DevTools for Node] to debug your code.
--------------------- The realtime log ---------------------
17:13:38 - express-api-demo - deployment
region: ap-guangzhou
apigw:
  serviceId:   service-b77xtibo
  subDomain:   service-b77xtibo-1253970226.gz.apigw.tencentcs.com
  environment: release
  url:         http://service-b77xtibo-1253970226.gz.apigw.tencentcs.com/release/
scf:
  functionName: express_component_6r6xkh60k
  runtime:      Nodejs10.15
  namespace:    default

express-api-demo › Watching
```

在进入 dev 模式后，Serverless 工具将输出部署的内容，并启动持续文件监控；在代码文件有修改的情况下，将自动再次进行部署，将本地文件更新到云端。

再次部署并输出部署信息：
```plaintext
express-api-demo › Deploying ...
Debugging listening on ws://127.0.0.1:9222.
For help see https://nodejs.org/en/docs/inspector.
Please open chorme, and visit chrome://inspect, click [Open dedicated DevTools for Node] to debug your code.
--------------------- The realtime log ---------------------
21:11:31 - express-api-demo - deployment
region: ap-guangzhou
apigw:
  serviceId:   service-b7dlqkyy
  subDomain:   service-b7dlqkyy-1253970226.gz.apigw.tencentcs.com
  environment: release
  url:         http://service-b7dlqkyy-1253970226.gz.apigw.tencentcs.com/release/
scf:
  functionName: express_component_uo5v2vp
  runtime:      Nodejs10.15
  namespace:    default
```

>!当前 `serverless dev` 仅支持 Node.js 10 运行环境，后续将支持 Python、PHP 等运行环境的实时日志。

### 退出开发模式

在开发模式下，通过 Ctrl+C 可以退出开发模式（dev 模式）。

```
express-api-demo › Disabling Dev Mode & Closing ...

express-api-demo › Dev Mode Closed
```

## 云端调试：Node.js 10+

针对 Runtime 为 Node.js 10+ 的项目，可以通过开启云端调试，并使用针对 Node.js 的调试工具来连接云端调试，例如 Chrome DevTools、VS Code Debugger。

### 开启云端调试

在按如上方案进入开发模式时，如果是 Runtime 为 Node.js 10及以上版本的函数，会自行开启云端调试，并输出调试相关信息。

例如在开启开发模式时，如果有如下输出，则代表已经启动云函数的云端调试：
```plaintext
Debugging listening on ws://127.0.0.1:9222.
For help see https://nodejs.org/en/docs/inspector.
Please open chorme, and visit chrome://inspect, click [Open dedicated DevTools for Node] to debug your code.
```

### 调试工具连接：Chrome DevTools

接下来将说明如何使用 Chrome 浏览器的 DevTools 工具来连接远程环境并进行调试。

1. 启动 Chrome 浏览器。
2. 在地址栏中输入`chrome://inspect/`。
3. 通过 Devices 栏下的`Open dedicated DevTools for Node`来打开 DevTools 调试工具（推荐），或者通过点击`Remote Target #LOCALHOST`中具体 Target 下的`inspect`来打开 DevTools。如果无法打开或者没有 Target，检查 Device 的 Configure 中有`localhost:9229`或`localhost:9222`的配置，与开启云端调试时的输出可以对应。
4. 通过`Open dedicated DevTools for Node`打开的 DevTools 调试工具，可以切换到 Sources Tab 页查看远端代码。函数的实际代码在`/var/user/`目录下。
5. Sources Tab 页看到的代码有时是进加载了的代码，可能会随着调试进行而展示出更多远端文件。
6. 可以通过双击打开文件后，在文件的指定位置设置断点。
7. 通过任意方式，例如 URL 访问、页面触发、命令触发、接口触发等触发的函数，会使得远端环境开始运行，并将会在设置了断点的位置中断，等待进一步的运行。
8. 通过 DevTools 的右侧栏，可以控制中断的程序继续执行、单步执行、步入步出的操作，也可以直接查看当前变量，或设定要跟踪查看的变量。DevTools 的进一步使用可以搜索查询 DevTools 使用说明文档。


### 云端调试使用须知和注意事项

当前云函数的云端调试能力处于 Beta 阶段，欢迎试用并向我们反馈试用中碰到的问题或建议。
在使用云函数的云端调试时，需要了解如下信息或注意点：
1. 云端调试是使用了云函数的一个实际运行实例来进行调试。
2. 由于触发事件的随机性，如果有多个实例存在的情况下，触发事件可能随机的落到某个实例上，因此不是任意请求均能命中调试实例并可以开始调试。
3. 由于调试断点暂停运行时，长时间未运行且返回的情况下，可能会导致触发端例如 API 网关提示超时。
4. 由于调试断点暂停运行时，实例将仍然处于计时状态，并在此次调试完成，继续执行直到执行完成时，记录耗费的总时长作为此次函数的运行时长。
5. 从触发实例运行，到最终完成调试，此次执行完成的最长时间为 900秒，即在调试时如果中断执行 900 秒后，将会强制终止此次执行，并按函数运行 900 秒并超时进行统计和计量。
6. 当前版本的调试能力，会使得云函数超时配置为 900 秒，在正常退出调试时将会重新设置超时为正常值；如果调试命令异常退出或强行终止，会导致云函数超时未能设置为正常值，此时可以通过再次部署（命令行）或手工编辑（控制台）的方式修改云函数的超时配置。


### 关闭云端调试

在退出开发模式时，将会自动关闭云端调试功能。
