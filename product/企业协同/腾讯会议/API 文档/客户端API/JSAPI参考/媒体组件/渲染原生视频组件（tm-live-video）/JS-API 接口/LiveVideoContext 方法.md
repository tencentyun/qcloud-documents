- liveVideoContext.bindUser（option：object）
- 功能描述：
切换另外一个会议中用户的视频或者屏幕共享。
- 参数：
option：object
<table>
   <tr>
      <th width="20%" >属性</td>
      <th width="40%" >类型</td>
      <th width="20%" >默认值</td>
      <th width="20%" >必填</td>
      <th width="20%" >描述</td>
   </tr>
   <tr>
      <td>userId</td>
      <td>String</td>
      <td>-</td>
      <td>否</td>
       <td>用户 ID。</td>
 </tr>
   <tr>
      <td>msOpenId</td>
      <td>String</td>
      <td>-</td>
      <td>否</td>
       <td>用户在当前会议中的临时 openId，同一个用户在不同的会议该参数不同。</td>
 </tr>
   <tr>
      <td>streamType</td>
      <td>EmbeddedStreamType</td>
      <td>EmbeddedStreamType.VIDEO</td>
      <td>否</td>
      <td>视频流类型：<br>EmbeddedStreamType.VIDEO：视频<br>EmbeddedStreamType.SCREEN\_SHARING：屏幕共享</td>
</tr>
</table>
>?liveVideoContext.bindUser 接口参数值为驼峰（例如：userId、msOpenId、streamType）。
