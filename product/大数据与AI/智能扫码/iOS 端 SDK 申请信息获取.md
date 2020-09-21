## 获取 iOS Bundle ID

- 使用开发者工具 XCode，在 TARGETS->General->Identity->Bundle Identifier 中获取 (例子：cloud.QBTestDemo)

  ![](https://main.qcloudimg.com/raw/75683e4b5aab8bb0ceedf36846af5077.png)

- 代码获取：[[NSBundle mainBundle] objectForInfoDictionaryKey:@"CFBundleIdentifier"];

## iOS DEVELOPMENT_TEAM

- 方法1：cd 到工程文件 **aaa.xcodeproj** 目录下，执行以下命令。
```
grep -h -r --include *.pbxproj DEVELOPMENT_TEAM . | uniq
```


![](https://main.qcloudimg.com/raw/d2976606a35525addad7f9b82c09ffe3.png)


- 方法2：在 Xcode 中查看 DEVELOPMENT_TEAM，注意格式。(例子：HKB8BBFBR9)
