本文主要介绍如何快速将腾讯云即时通信 IM SDK 集成到您的 React Native 项目中。

## 环境要求

| 平台         | 版本                                                                  |
| ------------ | --------------------------------------------------------------------- |
| React Native | 2.2.0 及以上版本。                                                    |
| Android      | Android Studio 3.5 及以上版本，App 要求 Android 4.1 及以上版本设备。  |
| iOS          | Xcode 11.0 及以上版本，真机调试请确保您的项目已设置有效的开发者签名。 |

## 集成 IM SDK

您可以通过 npm 的方式直接集成腾讯云 IM SDK（React Native）。

### npm 集成

在终端窗口中输入如下命令：

```
# npm
npm install react-native-tim-js

# yarn
yarn add react-native-tim-js


# RN >= 0.60
cd ios && pod install

# RN < 0.60
react-native link react-native-tim-js
```

### 引入并初始化 SDK

```javascript
import { TencentImSDKPlugin } from "react-native-tim-js";
```
