[](id:install)
## 安装相关
[](id:install_q1)
### trtc-electron-sdk 是否兼容官方 Electron v12.0.1 版本?

兼容的，trtc-electron-sdk 没有特别依赖 elecron 自身的 SDK，所以没有相关的版本依赖。


[](id:install_q2)
### Electron 下载慢甚至卡住不动？
当开始下载 `tmp-3320-1-SHASUMS256.txt-6.1.9` 文件或其它文件时，可能会特别慢，甚至在辛苦等待了很长时间后，等到的却是 npm 的 Timeout 错误：
```
Downloading tmp-3320-1-SHASUMS256.txt-6.1.9
[=>                                    ] 1.0% of 5.56 kB (0 B/s)
```

- **解决方案 A：**如果您是在家中办公，可以切换到国内的 npm 镜像。
```
# 指定 npm 国内镜像
$ npm config set registry=https://registry.npm.taobao.org/
# 指定 Electron 的国内镜像地址
$ npm config set ELECTRON_MIRROR=https://npm.taobao.org/mirrors/electron/ 
$ npm install
```
- **解决方案 B：**如果您是在公司办公，那么您公司的网络管理员可能已经设置了代理，需要确认 npm 的 proxy 配置是否指向了公司的代理服务器，以及是否配置了环境变量 `ELECTRON_GET_USE_PROXY`，如均无配置，请按以下步骤执行。
	1. 设置 npm 代理 ： `npm config set all_proxy=[您的代理地址]`。
	2. 配置 `ELECTRON_GET_USE_PROXY` 环境变量，这样 Electron 的安装脚本就会通过 npm 的代理下载。
	
- **解决方案 C：**如果您是 Mac 环境。
```
    $ export ELECTRON_GET_USE_PROXY=true
```

- **解决方案 D：**如果您是 Windows 环境。
	1. 右键单击 **计算机 > 属性 > 高级系统设置 > 环境变量**。
	2. 按下图操作设置环境变量 ELECTRON_GET_USE_PROXY ，然后执行 `npm install` 或 `npm install --proxy=[您的代理地址]`：
	![](https://qcloudimg.tencent-cloud.cn/raw/2788a541f1f409a1e68bc25ade65ca27.png)


[](id:install_q3)
### 下载 Electron 时出现 404 错误？
![](https://qcloudimg.tencent-cloud.cn/raw/a1855dc24d83db2f0fabe03fcdbce916.png)

在终端中输入如下指令：
```
$ npm config set electron_custom_dir 8.1.1 # 根据版本号来决定
```

[](id:run)
## 运行相关
[](id:run_q1)

###  Windows 32 系统运行报错 `Error：resource\trtc_electron_sdk.node is not a valid Win32 application`， 提示需要 32 位的 trtc_electron_sdk.node?

![](https://main.qcloudimg.com/raw/4e0115819b868ee9a6d110f641096e01.png)
**解决方法**：
1. 进入到工程目录下的 trtc-electron-sdk 库目录下（xxx/node_modules/trtc-electron-sdk）。 执行：
```script
npm run install -- arch=ia32
```
2. 下载完 32 位的 `trtc_electron_sdk.node` 后，重新对项目进行打包。


[](id:run_q2)
###  vscode terminal 启动 Electron Demo，进入房间后白屏？

vscode 需有摄像头权限, 可采用如下方式进行权限添加。

```script
    cd ~/Library/Application\ Support/com.apple.TCC/
    cp TCC.db TCC.db.bak
    sqlite3 TCC.db    # sqlite> prompt appears.

    # for Mojave, Catalina
    INSERT into access VALUES('kTCCServiceCamera',"com.microsoft.VSCode",0,1,1,NULL,NULL,NULL,'UNUSED',NULL,0,1541440109);

    # for BigSur
    INSERT into access VALUES('kTCCServiceCamera',"com.microsoft.VSCode",0,1,1,1,NULL,NULL,NULL,'UNUSED',NULL,0,1541440109);
```

[](id:run_q3)

###  跑 Demo 抛出空指针未定义的错误：`“cannot read property 'dlopen' of undefined”`？

![](https://main.qcloudimg.com/raw/fa2ac368a07eefdc63901f3910a122f9.png)
**解决方法**：
Electron 12 版本上下文隔离默认启用，可设置 contextIsolation 为 false。

```javascript
let win = new BrowserWindow({
	width: 1366,
	height: 1024,
	minWidth: 800,
	minHeight: 600,
	webPreferences: {
	nodeIntegration: true,
	contextIsolation: false
		},
});
```


[](id:run_q4)
### Electron 多次出现重新进房问题?

需要具体 case 进行分析，大致原因如下：

- 客户端网络状态不好（断网会触发重进房）。
- 连着发两次进房信令也会重进房的。
- 有可能是设备负载过高，导致解码失败的重进房。
- 同一个 UID 多端登录互踢导致的重进房。


[](id:run_q5)
### 终端出现提示“Electron failed to install correctly”？
当看似安装完成，运行项目时，终端上出现以下错误：
```
Error: Electron failed to install correctly, please delete node_modules/electron and try installing again
```
按照如下三个步骤进行**手动下载**：
1. 执行 `npm config get cache` 查看缓存目录。
2. 手动下载 Electron ，并放到缓存目录中。
3. 重新执行`npm install`。

[](id:run_q6)

### 调用摄像头或麦克风时直接崩溃？

使用 vscode 终端启动项目，当 trtc-electron-sdk 启动摄像头和麦克风时，程序直接崩溃：
![](https://qcloudimg.tencent-cloud.cn/raw/1f1ebae1eb7703c907ef5d6332901248.png)

- **解决方案 A**：使用有授权的终端运行项目。
- **解决方案 B**：给 vscode 授权：在 **系统偏好设置 > 安全与隐私** 中允许 vscode 的授权。
- **解决方案 C**：按以下步骤关闭保护机制：
	1. 重启系统，**按住** command + r 键，**直到**系统进入保护模式。
	2. 打开 terminal 输入 `csrutil disable` 禁用保护机制。
	3. 重启，正常进入系统，此时就可以使用 vscode 的终端启动项目了。
	4. 如需重新启动保护机制，只需要在第二步中执行`csrutil enable`。


[](id:run_q7)
### Electron 在控制台中报错“xx is not defined”？
当运行项目时，Electron 在控制台中提示 `xx is not defined`，其中 `xx` 指代 node 模块。例如：
```
	Uncaught ReferenceError: require is not defined
```
在 Electron 的 `main.js` 文件中将  `nodeIntegration` 配置项改成 true：
```
	let win = new BrowserWindow({
        width: 1366,
        height: 1024,
        webPreferences: {
     		nodeIntegration: true,  // 请将此项设置为 true
    	},
	  });
```


[](id:pack)
## 打包相关
[](id:pack_q1)
### .node 模块的加载问题?
#### 报错信息
打包编译出的程序在运行时，在控制台中看到看到类似的报错信息：

- `NodeRTCCloud is not a constructor`
	![](https://main.qcloudimg.com/raw/f06737dc6be7d4eeed7573cd495c922f.png)
- `Cannot open xxx/trtc_electron_sdk.node` 或者 `The specified module could not be found`
	![](https://main.qcloudimg.com/raw/a55c9ca2266bc6e591354e23da535e1d.png)
- `dlopen(xxx/trtc_electron_sdk.node, 1): image not found`
	![](https://main.qcloudimg.com/raw/36c0e62fee13da96dc2136e10a07824b.png)

#### 解决方法
出现类似上述的信息，说明 trtc_electron_sdk.node 模块没有被正确的打包到程序中，可按照以下步骤进行处理。

1. 安装 `native-ext-loader`。
```
	 $ npm i native-ext-loader -D
```
2. 修改 webpack 配置。
	1. 使 `webpack.config.js` 在构建时可以接收名为 `--target_platform` 的命令行参数，以使代码构建过程按不同的目标平台特点正确打包，在 `module.exports` 之前添加以下代码：
```
const os = require('os');
// 如果不传 target_platform 参数，程序会默认按当前平台类型进行打包
const targetPlatform = (function(){
	let target = os.platform();
	for (let i=0; i<process.argv.length; i++) {
		if (process.argv[i].includes('--target_platform=')) {
			target = process.argv[i].replace('--target_platform=', '');
			break;
		}
	}
	// win32 统一表示 Windows 平台，包含 32 位和 64 位。darwin 表示 Mac 平台
	if (!['win32', 'darwin'].includes) target = os.platform();
		return target;
})();
```
	2. 添加以下 rules 配置：
```
module: {
	rules: [
		{ 
			test: /\.node$/, 
			loader: 'native-ext-loader', 
			options: { 
				rewritePath: targetPlatform === 'win32' ? './resources' : '../Resources' 
			} 
		},
	]
}
```
> !
> - 使用 `vue-cli` 创建的项目，webpack 配置存放在 `vue.config.js` 文件中的 `configureWebpack` 选项中。
> - 使用 `create-react-app` 创建的项目，webpack 配置文件为 `[项目目录]/node_modules/react-scripts/config/webpack.config.js` 。
3. 配置 packages.json 文件，添加打包配置和构建脚本。
	1. 添加 `electron-builder` 打包配置（注意大小写）：
```
"build": {
	"省略": "...",
	"win": {
		"extraFiles": [
			{
			"from": "node_modules/trtc-electron-sdk/build/Release/",
			"to": "./resources",
			"filter": ["**/*"]
			}
		]
	},
	"mac": {
		"extraFiles": [
			{ 
			"from": "node_modules/trtc-electron-sdk/build/Release/trtc_electron_sdk.node", 
			"to": "./Resources" 
			}
		]
	},
	"directories": {
		"output": "./bin"
	}
},
```
	2. 添加 scripts 构建、打包脚本 `create-react-app` 项目请参考以下配置：
```
"scripts": {
	"build:mac": "react-scripts build --target_platform=darwin",
	"build:win": "react-scripts build --target_platform=win32",
	"compile:mac": "node_modules/.bin/electron-builder --mac",
	"compile:win64": "node_modules/.bin/electron-builder --win --x64",
	"pack:mac": "npm run build:mac && npm run compile:mac",
	"pack:win64": "npm run build:win && npm run compile:win64"
}
```
	3. `vue-cli` 项目请参考以下配置：
```
"scripts": {
	"build:mac": "vue-cli-service build --target_platform=darwin",
	"build:win": "vue-cli-service build --target_platform=win32",
	"compile:mac": "node_modules/.bin/electron-builder --mac",
	"compile:win64": "node_modules/.bin/electron-builder --win --x64",
	"pack:mac": "npm run build:mac && npm run compile:mac",
	"pack:win64": "npm run build:win && npm run compile:win64"
}
```


[](id:pack_q2)
### 找不到入口文件？
使用 `create-react-app` 创建的项目，使用 `electron-builder` 打包时可能会遇到此问题：
```
    $ node_modules\.bin\electron-builder.cmd
      • electron-builder  version=22.6.0 os=6.1.7601
      • loaded configuration  file=package.json ("build" field)
      • public/electron.js not found. Please see https://medium.com/@kitze/%EF%B8%8F-from-react-to-an-electron-app-ready-for-production-a0468ecb1da3
      • loaded parent configuration  preset=react-cra
```
其中 `public/electron.js not found` 指的就是无法找到入口文件。

#### 解决方案
1. 移动并重命名入口文件：
```
$ cd [项目目录]
$ mv main.electron.js ./public/electron.js
```
2. 修改 pacakge.json 文件：
```
{
	"main": "public/electron.js",
	"省略": "..."
}
```

[](id:pack_q3)
### 在执行打包时，出现 fs-extra 模块的语法错误？
```
[项目目录]\node_modules\electron-builder\node_modules\fs-extra\lib\empty\index.js:33
	} catch {
            ^

SyntaxError: Unexpected token {
	at new Script (vm.js:51:7)
```
可以升级到最新的 node ，具体请参见 [Node.js 官方网站](https://nodejs.org/en/download/)。


>? 更多 Electron 相关问题请关注 [Electron 常见问题收录](https://cloud.tencent.com/developer/article/1616668) 和 [Electron 常见问题收录II](https://cloud.tencent.com/developer/article/1694758)，我们将持续更新。

