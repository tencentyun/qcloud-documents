>? 人脸核身产品于2023年1月4日起，后付费结算周期由月结改为日结：
- 2023年1月4日零点之后开通人脸核身的新用户，后付费结算方式为按日结算。
- 2023年1月4日零点之前开通人脸核身的用户，维持月结的结算周期不变。


## 计费方式

腾讯云人脸核身提供预付费和后付费两种计费方式，您可以结合自身业务场景灵活选择付费方式。 

|   计费方式| 结算方式 |描述  | 
|-----------|-------|-------|
|后付费| 按调用量日结（默认） |后付费方式是人脸核身服务默认的计费方式，根据您使用服务产生的调用量进行计费，每日结算昨日00:00 -23:59:59产生的费用，并出计费账单。（账单将在当天08:00-12:00生成） |
|预付费|[购买资源包](https://buy.cloud.tencent.com/iai_faceid)|通过购买资源包的方式抵扣人脸核身产品的计费量，资源包有效期均为1年（过期作废），支持 [7天内无理由退款](https://cloud.tencent.com/document/product/1007/31008)。|

>?
>- 人脸核身产品的结算顺序：免费资源包>付费资源包>后付费。
>- 预付费资源包用完后，默认会自动转入使用后付费结算方式，如需关闭后付费可到 [控制台](https://console.cloud.tencent.com/faceid/settings) 关闭。
>- 腾讯云人脸核身按调用量计费，调用结果及其对应收费关系请参考 [计费错误码](https://cloud.tencent.com/document/product/1007/48021)。

## 接入渠道与计费标签

### 增强版人脸核身
增强版人脸核身接入渠道与计费标签对应关系说明如下：

<table>
<tr>
<th>接入渠道</th>
<th>比对库源</th>
<th>计费标签</th>
<th>定价</th>
</tr>
<tr>
<td rowspan =2>
<li><a href="https://cloud.tencent.com/document/product/1007/42656">微信原生 H5</a></li><li><a href="https://cloud.tencent.com/document/product/1007/31071">微信小程序</a></li>
</td>
<td>跟权威库比对</td>
<td>增强版人脸核身（权威库）-微信</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.A2.9E.E5.BC.BA.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>        
</tr>
<tr>
<td>跟上传照片比对</td>
<td>增强版人脸核身（自传照片）-微信</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.A2.9E.E5.BC.BA.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>   
</tr>
<tr>
<td rowspan =2><a href="https://cloud.tencent.com/document/product/1007/57617">增强版 SDK（APP）</a>
</td>
<td>跟权威库比对</td>
<td>增强版人脸核身（权威库）-App</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.A2.9E.E5.BC.BA.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>   
</tr>
<tr>
<td>跟上传照片比对</td><td>增强版人脸核身（自传照片）-App</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.A2.9E.E5.BC.BA.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>   
</tr>
<tr>
<td rowspan =2><li><a href="https://cloud.tencent.com/document/product/1007/78124">微信浮层 H5</li><li><a href="https://cloud.tencent.com/document/product/1007/61072">移动浮层 H5</a></td>
<td>跟权威库比对</td>
<td>增强版人脸核身（权威库）-浮层 H5</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.A2.9E.E5.BC.BA.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>   
</tr>
<tr>
<td>跟上传照片比对</td><td>增强版人脸核身（自传照片）-浮层 H5</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.A2.9E.E5.BC.BA.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>   
</tr>
</table>

### 基础版人脸核身
基础版人脸核身接入渠道与计费标签对应关系说明如下：
<table>
    <tr>
        <th>接入渠道</th>
				<th>比对库源</th>
        <th>计费标签</th>
			<th>定价</th>
    </tr>
    <tr>
        <td rowspan =2>
				<li><a href="https://cloud.tencent.com/document/product/1007/42656">微信普通 H5</a></li><li><a href="https://cloud.tencent.com/document/product/1007/35893">PC H5</a></li><li><a href="https://cloud.tencent.com/document/product/1007/35866">基础版 SDK（APP）</a></li>
				</td>
				<td>跟权威库比对</td>
			 <td>基础版人脸核身（权威库）</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>       
    </tr>
		   <tr>
			 <td>跟上传照片比对</td>
			 <td>基础版人脸核身（自传照片）</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
			  </tr>
			   <tr>
                   <td><a href="https://cloud.tencent.com/document/product/1007/31818">活体人脸核身 API</a>
				</td>
				<td>跟权威库比对</td><td>基础版人脸核身（权威库）</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
    </tr>
		   <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/31820">照片人脸核身 API</a></td>
			 <td>跟权威库比对</td><td>基础版人脸核身（权威库）</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>  
			  </tr>
    <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/31819">活体人脸比对 API</a></td><td>跟上传照片比对</td>
			 <td>基础版人脸核身（自传照片）</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
			  </tr>
				    <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/47276">身份证人像照片验真 API</a></td><td>跟权威库比对</td>
			 <td>基础版人脸核身（权威库）</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
			  </tr>
</table>


### 实名信息核验
实名信息核验各 API 接口与计费标签对应关系说明如下：
<table>
    <tr>
        <th> API 接口</th>
        <th>计费标签</th>
			<th>定价</th>
    </tr>	 
				 <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/33188">身份信息认证（二要素核验）</a></td>
			 <td rowspan =2>身份证信息核验</td>
			 			 	<td rowspan =2><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/37980">身份证识别及信息核验</a></td>
			  </tr>
					 <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/35776">银行卡二要素</a></td>
			 <td rowspan =3>银行卡信息核验</td>
<td rowspan =3><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
				 <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/33848">银行卡三要素</a></td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/35775">银行卡四要素</a></td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/40546">手机号在网时长核验</a></td>
			  <td rowspan =2>手机号在网时长/状态查询</td>
<td rowspan =2><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
			 <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/40545">手机号状态查询</a></td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/47837">银行卡基础信息查询</a></td>
			 <td>银行卡基础信息查询</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/60075">身份信息及有效期核验</a></td>
			 <td>身份信息及有效期核验</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
	<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/50364">手机号二要素核验</a></td>
			 <td>手机号信息核验（二要素）</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/39765">手机号三要素核验</a></td>
			 <td> 手机号信息核验（三要素）</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>			
</table>

### E证通
E证通服务与计费标签对应关系说明如下：
<table>
<tr>
<th>接入渠道</th>
<th>比对库源</th>
<th>计费标签</th>
<th>定价</th>
</tr>
<tr>
<td ><a href="https://cloud.tencent.com/document/product/1007/54116">E证通</a>
</td>
<td>跟权威库比对</td>
<td>E证通（权威库）</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#e.E8.AF.81.E9.80.9A.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
</tr>
</table>

### 意愿核身
意愿核身服务与计费标签对应关系说明如下：
<table>
<tr>
<th>接入渠道</th>
<th>比对库源</th>
<th>计费标签</th>
<th>定价</th>
</tr>
<tr>
<td>意愿核身（权威库）</a>
</td>
<td>跟权威库比对</td>
<td>意愿核身（权威库）</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E6.84.8F.E6.84.BF.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
</tr>
<tr>
<td>意愿核身（自传照片）</a>
</td>
<td>跟上传照片比对</td>
<td>意愿核身（自传照片）</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E6.84.8F.E6.84.BF.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
</tr>
</table>

### 实证 NFC

实证 NFC 服务与计费标签对应关系说明如下：

<table>
<tr>
<th>接入渠道</th>
<th>计费标签</th>
<th>定价</th>
</tr>
<tr>
<td>实证 NFC</a>
</td>
<td>证件 NFC 识别</td>
<td><a href="https://cloud.tencent.com/document/product/1007/84321#.E5.AE.9E.E8.AF.81-nfc-.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
</tr>
</table>
