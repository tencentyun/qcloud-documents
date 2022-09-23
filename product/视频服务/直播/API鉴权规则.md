用户对主账号的视频直播资源访问时需要遵循鉴权规则，本文为您介绍视频直播 API 鉴权的规则。

## 鉴权规则

当子账号通过直播服务 API 对主账号的直播资源进行访问时，直播服务后台向子用户进行权限检查，以确保资源拥有者的确将相关资源的相关权限授予了调用者。

每个不同的直播服务 API 会根据涉及到的资源以及 API 的语义来确定需要检查哪些资源的权限。每个 API 的鉴权规则具体见下表。

## 支持资源级授权的 API

| 接口名称                        | 接口功能                          | 资源（Resource）                                      |
| ------------------------------- | --------------------------------- | ----------------------------------------------------- |
| DescribeLiveDomainReferer       | 查询直播域名 Referer 黑白名单配置 | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DescribeLivePlayAuthKey         | 查询播放鉴权 key                  | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DescribeLivePushAuthKey         | 查询推流鉴权 key                  | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| ModifyLiveDomainReferer         | 设置直播域名 Referer 黑白名单     | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| ModifyLivePlayAuthKey           | 修改播放鉴权 key                  | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| ModifyLivePushAuthKey           | 修改推流鉴权 key                  | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DescribeLiveStreamEventList     | 查询推断流事件                    | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DescribeLiveStreamOnlineList    | 查询直播中的流                    | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DescribeLiveStreamPublishedList | 查询历史流列表                    | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DescribeLiveStreamState         | 查询流状态                        | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DropLiveStream                  | 断开直播流                        | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| ForbidLiveStream                | 禁推直播流                        | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| ResumeLiveStream                | 恢复直播推流                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| CreateLiveWatermarkRule         | 创建水印规则                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DeleteLiveWatermarkRule         | 删除水印规则                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| CreateLiveTranscodeRule         | 创建转码规则                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DeleteLiveTranscodeRule         | 删除转码规则                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| AddLiveDomain                   | 添加域名                          | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DeleteLiveDomain                | 删除域名                          | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DescribeLiveDomain              | 查询域名信息                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| EnableLiveDomain                | 启用域名                          | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| ForbidLiveDomain                | 禁用域名                          | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| ModifyLivePlayDomain            | 修改播放域名信息                  | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| CreateLiveSnapshotRule          | 创建截图规则                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DeleteLiveSnapshotRule          | 删除截图规则                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| AddDelayLiveStream              | 延迟播放                          | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| ResumeDelayLiveStream           | 恢复延播                          | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DescribeLiveStreamPushInfoList  | 获取在线流的推流数据              | qcs::${ApiModule}:${Region}:uin/:domain/${PushDomain} |
| DescribeLiveTranscodeDetailInfo | 查询直播转码统计信息              | qcs::${ApiModule}:${Region}:uin/:domain/${PushDomain} |
| DescribeStreamDayPlayInfoList   | 查询所有流的流量数据              | qcs::${ApiModule}:${Region}:uin/:domain/${PlayDomain} |
| DescribeStreamPlayInfoList      | 查询流的播放信息列表              | qcs::${ApiModule}:${Region}:uin/:domain/${PlayDomain} |
| CreateLiveCallbackRule          | 创建回调规则                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DeleteLiveCallbackRule          | 删除回调规则                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| BindLiveDomainCert              | 域名绑定证书                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DescribeLiveDomainCert          | 获取域名证书信息                  | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| ModifyLiveDomainCert            | 修改域名和证书绑定信息            | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| UnBindLiveDomainCert            | 解绑域名证书                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| CreateLiveRecordRule            | 创建录制规则                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| CreateRecordTask                | 创建录制任务（新）                | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DeleteLiveRecordRule            | 删除录制规则                      | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DeleteRecordTask                | 删除录制任务（新）                | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| DescribeRecordTask              | 查询录制任务列表（新）            | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |
| StopRecordTask                  | 终止录制任务（新）                | qcs::${ApiModule}:${Region}:uin/:domain/${DomainName} |

