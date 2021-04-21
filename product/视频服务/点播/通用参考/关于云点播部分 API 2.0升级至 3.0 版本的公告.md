云点播产品自从对外提供服务以来，服务了众多用户，随着点播产品能力日益丰富，为进一步提高用户体验，云点播团队优化了部分云 API 2.0 接口，详情如下：

**云点播 VOD 计划于2021年5月1日对点播服务进行全面升级**，[全新的 API 3.0接口文档](https://cloud.tencent.com/document/product/266/31752) 更加规范和全面，统一的参数风格和公共错误码，统一的 SDK/CLI 版本与 API 文档严格一致，给您带来简单快捷的使用体验。支持全地域就近接入让您更快连接腾讯云产品。升级后原云点播 VOD 的 API 2.0 接口服务将不再进行技术支持，但 API2.0 功能不会受到影响。如果您的业务还在使用云点播 VOD 的 API 2.0 相关接口，建议尽快将服务升级至云点播 API 3.0 接口。

相关升级接口如下：

| API 2.0接口 | 对应 API 3.0接口 | 	功能是否兼容 |	用户升级方法 |
|---------|---------|---------|---------|
| [PullEvent](https://cloud.tencent.com/document/product/266/7818) | [PullEvents](https://cloud.tencent.com/document/product/266/33433) | 是 |直接替换，推荐任务发起方式也可以升级为3.0 |
| [ConfirmEvent](https://cloud.tencent.com/document/product/266/7819) | [ConfirmEvents](https://cloud.tencent.com/document/product/266/33434) | 是 |直接替换，推荐任务发起方式也可以升级为3.0 |
| [DeleteVodFile](https://cloud.tencent.com/document/product/266/7838) | [DeleteMedia](https://cloud.tencent.com/document/product/266/31764) | 是 |直接替换 |
| [GetVideoInfo](https://cloud.tencent.com/document/product/266/8586) | [DescribeMediaInfos](https://cloud.tencent.com/document/product/266/31763) | 否，AI 处理结果、DRM、播放器 ID<br><li>basicInfo.playerId</li><li>aiAnalysisInfo</li><li>classificationInfo</li><li>tagInfo</li><li>contentReviewInfo</li><li>pornInfo</li><li>drm</li> |取决于用户是否用到了不兼容字段|
| [DescribeVodPlayInfo](https://cloud.tencent.com/document/product/266/7825) | [SearchMedia](https://cloud.tencent.com/document/product/266/31813) | 是 |直接替换 |
| [DescribeVodPlayUrls](https://cloud.tencent.com/document/product/266/7824) | 	[DescribeMediaInfos](https://cloud.tencent.com/document/product/266/31763) | 是 |直接替换 |
| [DescribeVodInfo](https://cloud.tencent.com/document/product/266/7828) | [DescribeMediaInfos](https://cloud.tencent.com/document/product/266/31763) | 是 |直接替换 |
| [ModifyVodInfo](https://cloud.tencent.com/document/product/266/7828) | [ModifyMediaInfo](https://cloud.tencent.com/document/product/266/31762) | 是 |直接替换 |
| [DescribeDrmDataKey](https://cloud.tencent.com/document/product/266/9643) | [DescribeDrmDataKey](https://cloud.tencent.com/document/product/266/54177) | 是 |直接替换 |
| [GetTaskInfo](https://cloud.tencent.com/document/product/266/11724) | [DescribeTaskDetail](https://cloud.tencent.com/document/product/266/33431) |  是 |直接替换，推荐任务发起方式也可以升级为3.0 |

感谢您对腾讯云的信赖与支持！

2021-04-21

腾讯云
