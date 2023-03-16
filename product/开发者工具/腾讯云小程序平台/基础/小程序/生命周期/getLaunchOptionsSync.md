# getLaunchOptionsSync

- 功能描述

获取小程序启动时的参数。

<!-- 与 [`App.onLaunch`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onlaunchobject-object) 的回调参数一致。 -->

#### 返回值

##### Object

启动参数

| 属性             | 类型            | 说明                                                                                   |
| ---------------- | --------------- | -------------------------------------------------------------------------------------- |
| path             | string          | 启动小程序的路径                                                                       |
| scene            | number          | 启动小程序的[场景值](/develop/frame/logic/logic_scene_value.md)          |
| query            | Object          | 启动小程序的 query 参数                                                                |
| referrerInfo     | Object          | 来源信息。从另一个小程序、公众号或 App 进入小程序时返回。否则返回 `{}`。(参见后文注意) |

**referrerInfo 的结构**

| 属性      | 类型   | 说明                                              |
| --------- | ------ | ------------------------------------------------- |
| appId     | string | 来源小程序、公众号或 App 的 appId                 |
| extraData | Object | 来源小程序传过来的数据，scene=1037 或 1038 时支持 |

**forwardMaterials 的结构**

| 属性 | 类型   | 说明                                |
| ---- | ------ | ----------------------------------- |
| type | string | 文件的 mimetype 类型                |
| name | Object | 文件名                              |
| path | string | 文件路径（如果是 webview 则是 url） |
| size | number | 文件大小                            |

#### 返回有效 referrerInfo 的场景

| 场景值 | 场景                            | appId 含义 |
| ------ | ------------------------------- | ---------- |
| 1020   | 公众号 profile 页相关小程序列表 | 来源公众号 |
| 1035   | 公众号自定义菜单                | 来源公众号 |
| 1036   | App 分享消息卡片                | 来源 App   |
| 1037   | 小程序打开小程序                | 来源小程序 |
| 1038   | 从另一个小程序返回              | 来源小程序 |
| 1043   | 公众号模板消息                  | 来源公众号 |

#### 注意

部分版本在无`referrerInfo`的时候会返回 `undefined`，建议使用 `options.referrerInfo &amp;&amp; options.referrerInfo.appId` 进行判断。