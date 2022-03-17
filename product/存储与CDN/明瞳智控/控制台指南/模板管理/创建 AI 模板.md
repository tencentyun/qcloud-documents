## 简介

明瞳智控当前支持转码、截帧、AI 三类模板。您可以在**模板管理**中为项目空间创建不同类型的模板，以便进行视图数据分析。本文介绍如何创建 AI 模板。

## 使用说明

当前支持**人员检测、目标识别、智能交通、明厨亮灶**4类 AI 场景下的算法，可依据业务需求选配。
<table>
 <tr><td style="width: 15%">算法分类</td><td style="width: 20%">算法名称</td><td style="width: 65%">说明</td></tr>
	<tr>
		<td rowspan="5">人员检测</td>
    <td>人脸检测</td>
    <td><ul  style="margin: 0;"><li>图片支持格式：PNG、JPG、JPEG、BMP。</li><li>图片大小：所下载图片经 Base64 编码后不超过5MB。</li><li>图片像素：JPG 格式长边像素不可超过4000px，其他格式图片长边像素不可超过2000px。</li></ul></td>
	<tr>
	<tr>
		<td>人体识别</td>
		<td><ul  style="margin: 0;"><li>图片分辨率不得超过1920px * 1080px。</li><li>支持 PNG、JPG、JPEG、BMP，不支持 GIF 图片。</li><li>检测给定图片中的人体（Body）的位置信息及属性信息。</li></ul></td>
	<tr>
  <tr>
		<td>人体关键点分析</td>
		<td><ul  style="margin: 0;"><li>图片分辨率不得超过1920px * 1080px。</li><li>支持 PNG、JPG、JPEG、BMP，不支持 GIF 图片。</li><li>检测给定图片中的人体（Body）的位置信息及属性信息。</li></ul></td>
	</tr>
 <tr>
		<td rowspan="5">目标识别</td>
    <td>宠物识别</td>
    <td>-</td>
	<tr>
	<tr>
		<td>图像标签</td>
		<td>图片格式支持 PNG、JPEG、JPG，图片大小不超过3MB，图片宽高大于50px * 50px。</td>
	<tr>
  <tr>
		<td>婴儿识别</td>
		<td>-</td>
	</tr>
    <tr>
		<td rowspan="4">智能交通</td>
    <td>车牌识别</td>
    <td>-</td>
	<tr>
	<tr>
		<td>车辆识别</td>
		<td><ul  style="margin: 0;"><li>支持的图片格式：PNG、JPG、JPEG、BMP，暂不支持 GIF 格式。</li><li>支持11种车身颜色、20多种车型、300多种品牌、4000多种车系+年款的识别。</li><li>支持对车辆的位置进行检测。如果图片中存在多辆车，会分别输出每辆车的车型和坐标。</li></ul></td>
	<tr>
  <tr>
		<td rowspan="7">明厨亮灶</td>
    <td>口罩识别</td>
    <td><ul  style="margin: 0;"><li>识别内容：蓝色、白色、透明的口罩。</li><li>最小检测尺寸：40px * 40px。</li></ul></td>
	<tr>
	<tr>
		<td>厨师帽识别</td>
		<td><ul  style="margin: 0;"><li>识别内容：长筒厨师帽，圆形厨师帽。</li><li>最小检测尺寸：40px * 40px。</li></ul></td>
	<tr>
  <tr>
		<td>抽烟识别</td>
		<td><ul  style="margin: 0;"><li>识别环境要求：室内、室外环境下，白天环境下，夜间灯光充足情况下。</li><li>识别内容：人员有抽烟行为动作（面部朝向画面角度不超过30°）。</li><li>最小检测尺寸：100px * 150px。</li></ul></td>
	</tr>
   <tr>
		<td>厨师服识别</td>
		<td>最小检测尺寸：40px * 40px。</td>
	</tr>
     <tr>
		<td>接打电话识别</td>
		<td><ul  style="margin: 0;"><li>识别环境要求：室内、室外环境下，白天环境下，夜间灯光充足情况下。</li><li>识别内容：人员有接打手机行为动作（面部朝向画面角度不超过30°）。</li><li>最小检测尺寸：100px * 150px。</li></ul></td>
	</tr>
</table>


## 操作步骤

1. 登录 [明瞳智控控制台](https://console.cloud.tencent.com/iss)。
2. 在左侧导航栏中，单击**模板管理**，进入模板管理页面。
3. 选择**AI 模板**页签，单击**创建模板**。
![](https://qcloudimg.tencent-cloud.cn/raw/dc946e562d4ce8816c0707429e04a370.png)
4. 在弹出的窗口中，设置模板名称和功能配置，单击**提交**。
![](https://qcloudimg.tencent-cloud.cn/raw/962ac92ef4859e47781397d0c32700c3.png)





