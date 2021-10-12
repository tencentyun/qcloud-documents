[](id:que1)
###  跑 Demo 抛出空指针未定义的错误：“cannot read property "dlopen" of undefined”？
![](https://main.qcloudimg.com/raw/fa2ac368a07eefdc63901f3910a122f9.png)
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

[](id:que2)
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

[](id:que3)
###  Windows 32 系统运行报错， 提示需要 32 位的 trtc_electron_sdk.node?
![](https://main.qcloudimg.com/raw/4e0115819b868ee9a6d110f641096e01.png)
1. 进入到工程目录下的 trtc-electron-sdk 库目录下（xxx/node_modules/trtc-electron-sdk）。 执行：
```script
npm run install -- arch=ia32
```
2. 下载完 32 位的 `trtc_electron_sdk.node` 后，重新对项目进行打包。

[](id:que4)
### trtc-electron-sdk 是否兼容官方 Electron v12.0.1 版本?
兼容的，trtc-electron-sdk 没有特别依赖 elecron 自身的 sdk，所以没有相关的版本依赖。

[](id:que5)
### Electron 多次出现重新进房问题?
需要具体 case 进行分析，大致原因如下：
- 客户端网络状态不好（断网会触发重进房）。
- 连着发两次进房信令也会重进房的。
- 有可能是设备负载过高，导致解码失败的重进房。
- 同一个 UID 多端登录互踢导致的重进房。

[](id:que6)
### .node 模块的加载问题?
打包编译出的程序在运行时，在控制台中看到看到类似的报错信息：
- `NodeRTCCloud is not a constructor`
![](https://main.qcloudimg.com/raw/f06737dc6be7d4eeed7573cd495c922f.png)
- `Cannot open xxx/trtc_electron_sdk.node`
![](https://main.qcloudimg.com/raw/a55c9ca2266bc6e591354e23da535e1d.png)
- `dlopen(xxx/trtc_electron_sdk.node, 1): image not found`
![](https://main.qcloudimg.com/raw/36c0e62fee13da96dc2136e10a07824b.png)
出现类似上述的信息，说明 trtc_electron_sdk.node 模块没有被正确的打包到程序中，可参考 [Electron 常见问题收录](https://cloud.tencent.com/developer/article/1616668?from=10680) 进行处理。
