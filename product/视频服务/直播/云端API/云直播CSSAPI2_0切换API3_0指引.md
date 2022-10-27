云直播 API 于**北京时间2020年5月1日**全面升级至3.0版本。基于2.0版本接口访问时延较高和使用复杂的考虑，原云直播 CSS 的 API 2.0 接口服务将不再提供技术支持，并将于**北京时间2023年01月01日起下线**。如果您的业务还在使用云直播 CSS 的 API 2.0 相关接口，建议尽快将服务升级至云直播 API 3.0 接口，以免对您的业务造成影响。
使用 API3.0 时，建议使用 [云产品SDK中心_云产品 SDK 文档-腾讯云](https://cloud.tencent.com/document/sdk)，获取到 API3.0 配套的多种编程语言的SDK，[API Explorer](https://console.cloud.tencent.com/api/explorer?Product=monitor&Version=2018-07-24&Action=GetMonitorData&SignVersion=) 可以直接生成 SDK 的调用代码，方便您实现代码调用。
请您从参照下方的 [API 2.0 切换 3.0 接口表](#list) 找到您需要升级的新接口，完成升级。

[](id:list)
## API 2.0 切换 3.0 接口列表
<table>
<tbody>
<tr>
<th>API 2.0 接口</td>
 <th>API 3.0 接口</td>
 <th>备注</td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/267/4715">CreateLVBChannel</a></td>
 <td>直播码不需要创建接口</td>
 <td>请升级为直播码模式，直播码不需要接口进行创建，直接指定流名称即可推流。</td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/267/4722">DeleteLVBChannel</a></td>
 <td>直播码不需要删除接口</td>
 <td>请升级为直播码模式，直播码不需要接口进行删除，直接停止推流即可。</td>
 </tr>
 <tr>
<td><a href="https://cloud.tencent.com/document/api/267/4717">DescribeLVBChannel</a></td>
 <td><a href="https://cloud.tencent.com/document/product/267/20470">DescribeLiveStreamState</a></td>
 <td>如需查询直播流的状态，请使用该 API3.0 接口进行查询。</td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/267/4719">StartLVBChannel</a></td>
 <td><a href="https://cloud.tencent.com/document/product/267/20467">ResumeLiveStream</a></td>
 <td>可通过该接口对已经禁推的流进行恢复启用。</td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/267/4720">StopLVBChannel</a></td>
 <td><a href="https://cloud.tencent.com/document/product/267/20468">ForbidLiveStream</a></td>
 <td>可通过该接口对直播流进行断流，并指定禁止期限进行禁推。</td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/267/4716">DescribeLVBChannelList</a></td>
 <td><a href="https://cloud.tencent.com/document/product/267/20472">DescribeLiveStreamOnlineList</a></td>
 <td>可通过该接口查询所有直播中的流列表。</td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/267/4723">CreateRecord</a></td>
 <td><a href="https://cloud.tencent.com/document/product/267/45983">CreateRecordTask</a></td>
 <td>请使用新的创建录制任务接口。</td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/267/4729">DeleteRecord</a></td>
 <td><a href="https://cloud.tencent.com/document/product/267/45982">DeleteRecordTask</a></td>
 <td>请使用新的删除录制任务接口。</td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/267/4724">StopRecord</a></td>
 <td><a href="https://cloud.tencent.com/document/product/267/45981">StopRecordTask</a></td>
 <td>请使用该接口对正在录制的任务进行停止。</td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/267/4725">DescribeRecord</a></td>
 <td><a href="https://cloud.tencent.com/document/product/267/56135">DescribeRecordTask</a></td>
 <td>请使用该接口查询对应的录制任务列表信息。</td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/267/4731">DescribeRecordList</a></td>
 <td><a href="https://cloud.tencent.com/document/product/267/56135">DescribeRecordTask</a></td>
 <td>请使用该接口查询指定范围内的录制任务列表信息。</td>
 </tr>
</tbody>
</table>
