
本文为您介绍正版曲库直通车 AME & 实时音视频 TRTC 在线 KTV 解决方案服务开通指引。

## 步骤1：开通直播互动曲库
完成 [直播曲库服务开通](https://cloud.tencent.com/document/product/1155/61649)。

## 步骤2：实时音视频 TRTC 服务开通

创建 [实时音视频 TRTC 应用](https://console.cloud.tencent.com/trtc/quickstart)。

### 步骤3：API 联调


|API 名称 | 描述 | 使用说明 |
|---------|---------|---------|
| SearchKTVMusics | 搜索曲目 | [搜索直播互动曲库歌曲](https://cloud.tencent.com/document/product/1155/56401) |
| DescribeKTVMusicDetail | 查询歌曲详情 | [查询直播互动曲目详情](https://cloud.tencent.com/document/product/1155/56402) |

1. 调用 SearchKTVMusics 搜索目标歌曲，返回的列表包含歌曲的信息及 Id。
<dx-codeblock>
:::  HTTP
// 请求
POST / HTTP/1.1
Host: ame.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: SearchKTVMusics
<公共请求参数>

{
    "Limit": 10,
    "KeyWord": "周杰伦",
    "Offset": 0
}

// 响应
{
  "Response": {
    "TotalCount": 1,
    "KTVMusicInfoSet": [
      {
        "ComposerSet": [
          "方文山"
        ],
        "MusicId": "ame-78dxxx",
        "SingerSet": [
          "周杰伦"
        ],
        "Name": "七里香",
        "LyricistSet": [
          "周杰伦"
        ],
        "TagSet": [
          "华语",
          "流行"
        ]
      }
    ],
    "RequestId": "xx"
  }
}

:::
</dx-codeblock>
2. 根据上面接口返回的 Id 查询歌曲详情，包含 SDK 中所需要的 PlayToken。
<dx-codeblock>
:::  HTTP
// 请求
POST / HTTP/1.1
Host: ame.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeKTVMusicDetail
<公共请求参数>

{
    "MusicId": "ame-78d2xxx"
}

// 响应
{
  "Response": {
    "PlayToken": "DUE3344xxxxxx",
    "KTVMusicBaseInfo": {
      "ComposerSet": [
        "周杰伦"
      ],
      "MusicId": "ame-78d2xxx",
      "SingerSet": [
        "周杰伦"
      ],
      "Name": "七里香",
      "LyricistSet": [
        "方文山"
      ],
      "TagSet": [
        "华语",
        "流行"
      ]
    },
    "RequestId": "xx"
  }
}

:::
</dx-codeblock>


## 步骤4：SDK 接入

### 集成 SDK
 
- **Android**
a. 拷贝 TXCopyrightedMedia-release-1.0.1.aar 到 libs目录，添加依赖项 `implementation(name:'TXCopyrightedMedia-release-1.0.1', ext:'aar')`。
b. 参考此处集成 TRTC SDKimplementation `com.tencent.liteav:LiteAVSDK_TRTC:latest.release` 并 [设置混淆规则](https://cloud.tencent.com/document/product/647/32175#.E8.AE.BE.E7.BD.AE.E6.B7.B7.E6.B7.86.E8.A7.84.E5.88.99)。
- **iOS**
a. 集成版权曲库 SDK（拷贝TXCopyrightedMedia.framework）到项目工程中并集成。
b. 若使用 pod 导入，则需要在 podfile 里添加以下代码。
```
pod 'TXCopyrightedMedia', :podspec => 'https://mediacloud-76607.gzc.vod.tencent-cloud.com/Podspec/TXCopyrightedMedia/1.0.1/TXCopyrightedMedia.podspec'
```
c. [集成TRTC SDK ]( https://cloud.tencent.com/document/product/647/32173)。
<dx-alert infotype="explain" title="">
请搭配 professional 或 enterprise 版本的 TRTC SDK 使用。
</dx-alert>

- **Windows** 

