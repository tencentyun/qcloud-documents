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
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/14190">AddKeyFrameDesc</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31762">ModifyMediaInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/9756">ApplyUpload</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31767">ApplyUpload</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/11607">ApplyUploadWatermark</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33772">CreateWatermarkTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/10156">ClipVideo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/34783">EditMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 EditMedia 的入参 FileInfos.N 传入 FileId, StartTimeOffset 和 EndTimeOffset，即可发起剪辑。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/9757">CommitUpload</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31766">CommitUpload</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/7821">ConcatVideo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/34783">EditMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 EditMedia 的入参 FileInfos.N 传入要拼接的多个 FileId，即可发起拼接。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7819">ConfirmEvent</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33434">ConfirmEvents</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/7822">ConvertVodFile</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33427">ProcessMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 ProcessMedia 的入参 MediaProcessTask.TranscodeTaskSet.Definition 传入转码模板 ID，即可发起转码。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/7812">CreateClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31772">CreateClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/8101">CreateImageSprite</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33427">ProcessMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 ProcessMedia 的入参 MediaProcessTask.ImageSpriteTaskSet.Definition 传入雪碧图模板 ID，即可发起雪碧图。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>CreateSimpleAesTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>原有 API 对应的加密功能属于 <a href="https://cloud.tencent.com/document/product/266/9638">HLS 普通加密</a>，已不再推荐使用。</p>

<p>建议您尽快升级到 <a href="https://cloud.tencent.com/document/product/266/73073">HLS 私有加密</a>。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/8102">CreateSnapshotByTimeOffset</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33427">ProcessMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 ProcessMedia 的入参 MediaProcessTask.SnapshotByTimeOffsetTaskSet.Definition 传入时间点截图模板 ID，即可发起时间点截图。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/9910">CreateTranscodeTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/9910">CreateTranscodeTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7826">CreateVodTags</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31762">ModifyMediaInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/11599">CreateWatermarkTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33772">CreateWatermarkTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/13442">DeleteKeyFrameDesc</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31762">ModifyMediaInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7838">DeleteVodFile</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31764">DeleteMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/11604">DeleteWatermarkTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/33770">DeleteWatermarkTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7813">DescribeAllClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31770">DescribeAllClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>DescribeAutoScreenShot</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/15330">DescribeCdnDetailStat</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/50519">DescribeCDNStatDetails</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/15329">DescribeCdnRegionIspDetailStat</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/50519">DescribeCDNStatDetails</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/15290">DescribeCdnStat</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/38291">DescribeCDNUsageData</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7814">DescribeClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31770">DescribeAllClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/api/266/54177">DescribeDrmDataKey</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/54177">DescribeDrmDataKey</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/15333">DescribePlayStatTopFiles</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/53311">DescribeDailyMostPlayedStat</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/8227">DescribeRecordPlayInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31763">DescribeMediaInfos</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/15332">DescribeStorage</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/41463">DescribeStorageData</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/15339">DescribeTranscodeStat</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/41464">DescribeMediaProcessUsageData</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/8814">DescribeVodCover</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31762">ModifyMediaInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/15331">DescribeVodHosts</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/54176">DescribeVodDomains</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7823">DescribeVodInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31763">DescribeMediaInfos</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7825">DescribeVodPlayInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31813">SearchMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7824">DescribeVodPlayUrls</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31763">DescribeMediaInfos</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/15332">DescribeVodStorage</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/41463">DescribeStorageData</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/15334">GetCdnLogList</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/47706">DescribeCdnLogs</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/12624">GetPlayStatLogList</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/51026">DescribeDailyPlayStatFileList</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/11724">GetTaskInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33431">DescribeTaskDetail</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/11722">GetTaskList</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33430">DescribeTasks</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetUserStatus</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/8586">GetVideoInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31763">DescribeMediaInfos</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetVodFileCount</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>GetVodFileStatInfo</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>LiveRealTimeClip</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/32587">LiveRealTimeClip</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7815">ModifyClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31769">ModifyClass</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>ModifySimpleAesTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>原有 API 对应的加密功能属于 <a href="https://cloud.tencent.com/document/product/266/9638">HLS 普通加密</a>，已不再推荐使用。</p>

<p>建议您尽快升级到<a href="https://cloud.tencent.com/document/product/266/73073">HLS 私有加密</a>。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7828">ModifyVodInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/31762">ModifyMediaInfo</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7817">MultiPullVodFile</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/35575">PullUpload</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p>ProcessCosMedia</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>云点播已不支持对 COS 文件发起媒体处理，如您仍然需要直接对 COS 文件发起媒体处理，建议您使用 MPS 产品的<a href="https://cloud.tencent.com/document/product/862/37578">接口</a>。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/9642">ProcessFile</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33427">ProcessMedia</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>API 3.0 接口 ProcessMedia 可以对指定视频 ID 发起转码、截图、转自适应码流、AI 处理等一系列操作</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/7818">PullEvent</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/33433">PullEvents</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>QuerySimpleAesTemplate</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>原有 API 对应的加密功能属于 <a href="https://cloud.tencent.com/document/product/266/9638">HLS 普通加密</a>，已不再推荐使用。</p>

<p>建议您尽快升级到<a href="https://cloud.tencent.com/document/product/266/73073">HLS 私有加密</a>。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/9912">QueryTranscodeTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/33769">DescribeTranscodeTemplates</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/9913">QueryTranscodeTemplateList</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/33769">DescribeTranscodeTemplates</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/11606">QueryWatermarkTemplate</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/33768">DescribeWatermarkTemplates</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p><a href="https://cloud.tencent.com/document/product/266/11608">QueryWatermarkTemplateList</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/api/266/33768">DescribeWatermarkTemplates</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>RedoTask</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>点播已不再支持 RedoTask 接口，如您需要重做任务，建议您调用 ProcessMedia 重新发起任务。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>RegisterVod</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/11030">RunProcedure</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p><a href="https://cloud.tencent.com/document/product/266/34782">ProcessMediaByProcedure</a></p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>在 API 3.0 接口 ProcessMediaByProcedure 的入参 ProcedureName 传入任务流模板名，即可发起按照任务流名字发起任务。</p></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>SetVodPlayStatus</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""></td>
 </tr>

<tr>
<td   colspan="1" rowspan="1" align="" valign="bottom"><p>WxPublish</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>/</p></td>
 <td   colspan="1" rowspan="1" align="" valign=""><p>点播已不再提供微信发布功能。</p></td>
</tr>

</tbody>
</table>

