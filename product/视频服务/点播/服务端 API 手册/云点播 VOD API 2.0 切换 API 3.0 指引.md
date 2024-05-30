云点播 API 于**北京时间2021年5月1日**全面升级至3.0版本。基于2.0版本接口访问时延较高和使用复杂的考虑，原云点播 VOD 的 API 2.0 接口服务将不再提供技术支持，并将于 北京时间2022年11月30日 起下线。如果您的业务还在使用云点播 VOD 的 API 2.0 相关接口，建议尽快将服务升级至云点播 API 3.0 接口，以免对您的业务造成影响。
        使用 API3.0 时，建议使用 [云产品SDK中心_云产品 SDK 文档-腾讯云](https://cloud.tencent.com/document/sdk)，获取到 API3.0 配套的多种编程语言的SDK，[API Explorer](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=GetMonitorData&SignVersion=) 可以直接生成 SDK 的调用代码，方便您实现代码调用。
       请您从参照下方的 [API 2.0 切换 3.0 接口表](#list)找到您需要升级的新接口，完成升级。

[](id:list)
## API 2.0 切换 3.0 接口列表
<melo-data data-src="{}" data-version="2.1.0"></melo-data><table ><colgroup><col  width="229px"><col  width="199px"><col  width="298px"></colgroup>
<tbody>
<tr>
<th   colspan="1" rowspan="1" align="" valign=""><p>API 2.0 接口</p></td>
 <th   colspan="1" rowspan="1" align="" valign=""><p>API 3.0 接口</p></td>
 <th   colspan="1" rowspan="1" align="" valign=""><p>备注</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>AddKeyFrameDesc</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31762">ModifyMediaInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>ApplyUpload</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31767">ApplyUpload</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>ApplyUploadWatermark</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33772">CreateWatermarkTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>ClipVideo</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/34783">EditMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 EditMedia 的入参 FileInfos.N 传入 FileId, StartTimeOffset 和 EndTimeOffset，即可发起剪辑。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>CommitUpload</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31766">CommitUpload</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>ConcatVideo</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/34783">EditMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 EditMedia 的入参 FileInfos.N 传入要拼接的多个 FileId，即可发起拼接。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>ConfirmEvent</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33434">ConfirmEvents</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>ConvertVodFile</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33427">ProcessMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 ProcessMedia 的入参 MediaProcessTask.TranscodeTaskSet.Definition 传入转码模板 ID，即可发起转码。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>CreateClass</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31772">CreateClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>CreateImageSprite</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33427">ProcessMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 ProcessMedia 的入参 MediaProcessTask.ImageSpriteTaskSet.Definition 传入雪碧图模板 ID，即可发起雪碧图。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>CreateSimpleAesTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>CreateSimpleAesTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>API 3.0 接口不支持公开调用，如有需要，请 <a href="https://cloud.tencent.com/online-service?from=doc_266">联系我们。</a></p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>CreateSnapshotByTimeOffset</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33427">ProcessMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 ProcessMedia 的入参 MediaProcessTask.SnapshotByTimeOffsetTaskSet.Definition 传入时间点截图模板 ID，即可发起时间点截图。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>CreateTranscodeTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/9910">CreateTranscodeTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>CreateVodTags</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31762">ModifyMediaInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>CreateWatermarkTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33772">CreateWatermarkTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DeleteKeyFrameDesc</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31762">ModifyMediaInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DeleteVodFile</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31764">DeleteMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DeleteWatermarkTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/33770">DeleteWatermarkTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeAllClass</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31770">DescribeAllClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeAutoScreenShot</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeCdnDetailStat</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/50519">DescribeCDNStatDetails</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeCdnRegionIspDetailStat</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/50519">DescribeCDNStatDetails</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeCdnStat</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/38291">DescribeCDNUsageData</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeClass</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31770">DescribeAllClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeDrmDataKey</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/54177">DescribeDrmDataKey</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribePlayStatTopFiles</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/53311">DescribeDailyMostPlayedStat</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeRecordPlayInfo</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31763">DescribeMediaInfos</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeStorage</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/41463">DescribeStorageData</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeTranscodeStat</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/41464">DescribeMediaProcessUsageData</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeVodCover</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31762">ModifyMediaInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeVodHosts</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/54176">DescribeVodDomains</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeVodInfo</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/31763">DescribeMediaInfos</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeVodPlayInfo</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31813">SearchMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeVodPlayUrls</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31763">DescribeMediaInfos</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeVodStorage</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/41463">DescribeStorageData</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetCdnLogList</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/47706">DescribeCdnLogs</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetPlayStatLogList</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/51026">DescribeDailyPlayStatFileList</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetTaskInfo</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33431">DescribeTaskDetail</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetTaskList</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33430">DescribeTasks</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetUserStatus</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetVideoInfo</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/31763">DescribeMediaInfos</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetVodFileCount</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetVodFileStatInfo</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>LiveRealTimeClip</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/32587">LiveRealTimeClip</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>ModifyClass</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31769">ModifyClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>ModifySimpleAesTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>ModifySimpleAesTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>API 3.0 接口不支持公开调用，如有需要，请 <a href="https://cloud.tencent.com/online-service?from=doc_266">联系我们</a>。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>ModifyVodInfo</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31762">ModifyMediaInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>MultiPullVodFile</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/35575">PullUpload</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>ProcessCosMedia</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>云点播已不支持对 COS 文件发起媒体处理，如您仍然需要直接对 COS 文件发起媒体处理，建议您使用 MPS 产品的 <a href="https://cloud.tencent.com/document/product/862/37578">接口</a>。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>ProcessFile</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>ProcessFile</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>API 3.0 接口不支持公开调用，如有需要，请 <a href="https://cloud.tencent.com/online-service?from=doc_266">联系我们</a>。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>PullEvent</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33433">PullEvents</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>QuerySimpleAesTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>DescribeSimpleAesTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>API 3.0 接口不支持公开调用，如有需要，请 <a href="https://cloud.tencent.com/online-service?from=doc_266">联系我们</a>。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>QueryTranscodeTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/33769">DescribeTranscodeTemplates</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>QueryTranscodeTemplateList</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/33769">DescribeTranscodeTemplates</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>QueryWatermarkTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/33768">DescribeWatermarkTemplates</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>QueryWatermarkTemplateList</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/33768">DescribeWatermarkTemplates</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>RedoTask</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>点播已不再支持 RedoTask 接口，如您需要重做任务，建议您调用 ProcessMedia 重新发起任务。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>RegisterVod</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>RunProcedure</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/34782">ProcessMediaByProcedure</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 ProcessMediaByProcedure 的入参 ProcedureName 传入任务流模板名，即可发起按照任务流名字发起任务。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>SetVodPlayStatus</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign="">-</td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>WxPublish</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>点播已不再提供微信发布功能。</p></td>
</tr>

</tbody>
</table>

