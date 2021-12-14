>?人脸核身产品于2021年6月22日进行了产品升级：
- 6月22日之后开通人脸核身的用户参照本文中描述的计费标签逻辑。
- 6月22日之前开通人脸核身的用户，计费标签及计费方式请参阅 [计费概述(旧)](https://cloud.tencent.com/document/product/1007/31005) 文档。

## 计费方式

腾讯云人脸核身提供预付费和后付费两种计费方式，您可以结合自身业务场景灵活选择付费方式。 

|   计费方式|  描述  | 结算方式|
|-----------|-------|-------|
|后付费|后付费方式是人脸核身服务默认的计费方式，根据您使用腾讯云慧眼人脸核身相关产品产生的调用量进行计费，当月1-3号为您推送上个自然月账单并进行扣费结算。 |按调用量月结|
|预付费|通过购买资源包的方式抵扣人脸核身产品的计费量，资源包有效期均为1年（过期作废），支持 [7天内无理由退款](https://cloud.tencent.com/document/product/1007/31008)。|[购买资源包](https://buy.cloud.tencent.com/iai_faceid)|

>?人脸核身产品的结算顺序：免费资源包>付费资源包>后付费；
> 腾讯云人脸核身按调用量计费，调用结果及其对应收费关系请参考 [计费错误码](https://cloud.tencent.com/document/product/1007/48021)。

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
			 	<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.A2.9E.E5.BC.BA.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>        
    </tr>
		   <tr>
			 <td>跟上传照片比对</td>
			 <td>增强版人脸核身（自传照片）-微信</td>
			 <td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.A2.9E.E5.BC.BA.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
			  </tr>
			   <tr>
                   <td rowspan =2><a href="https://cloud.tencent.com/document/product/1007/57617">增强版 App SDK</a>
				</td>
				<td>跟权威库比对</td>
				<td>增强版人脸核身（权威库）-App</td>
		<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.A2.9E.E5.BC.BA.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
    </tr>
		   <tr>
	 <td>跟上传照片比对</td><td>增强版人脸核身（自传照片）-App</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.A2.9E.E5.BC.BA.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
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
				<li><a href="https://cloud.tencent.com/document/product/1007/42656">微信普通 H5</a></li><li><a href="https://cloud.tencent.com/document/product/1007/35883">独立 H5</a></li><li><a href="https://cloud.tencent.com/document/product/1007/35893">PC H5</a></li><li><a href="https://cloud.tencent.com/document/product/1007/35866">基础版App SDK</a></li>
				</td>
				<td>跟权威库比对</td>
			 <td>基础版人脸核身（权威库）</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>       
    </tr>
		   <tr>
			 <td>跟上传照片比对</td>
			 <td>基础版人脸核身（自传照片）</td>
			 <td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
			  </tr>
			   <tr>
                   <td><a href="https://cloud.tencent.com/document/product/1007/31818">活体人脸核身 API</a>
				</td>
				<td>跟权威库比对</td><td>基础版人脸核身（权威库）</td>
						 	<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
    </tr>
		   <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/31820">照片人脸核身 API</a></td>
			 <td>跟权威库比对</td><td>基础版人脸核身（权威库）</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
			  </tr>
    <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/31819">活体人脸比对 API</a></td><td>跟上传照片比对</td>
			 <td>基础版人脸核身（自传照片）</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
			  </tr>
				    <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/47276">身份证人像照片验真 API</a></td><td>跟权威库比对</td>
			 <td>基础版人脸核身（权威库）</td>
			 	<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.9F.BA.E7.A1.80.E7.89.88.E4.BA.BA.E8.84.B8.E6.A0.B8.E8.BA.AB.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td> 
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
			 <td><a href="https://cloud.tencent.com/document/product/1007/33188">身份信息认证</a></td>
			 <td rowspan =3>身份证信息核验</td>
			 			 	<td rowspan =3><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/37980">身份证识别及信息核验</a></td>
			  </tr>
		<tr>
		<td><a href="https://cloud.tencent.com/document/product/1007/51441">微信实名认证授权</a></td>
			  </tr>	
								 <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/35776">银行卡二要素</a></td>
			 <td rowspan =3>银行卡信息核验</td>
<td rowspan =3><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
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
<td rowspan =2><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
			 <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/40545">手机号状态查询</a></td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/47837">银行卡基础信息查询</a></td>
			 <td>银行卡基础信息查询</td>
<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/60075">身份信息及有效期核验</a></td>
			 <td>身份信息及有效期核验</td>
<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
	<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/50364">手机号二要素核验</a></td>
			 <td>手机号信息核验（二要素）</td>
<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/33848">手机号三要素核验</a></td>
			 <td> 手机号三要素</td>
<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
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
<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
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
<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
    </tr>
		 <tr>
                   <td>意愿核身（自传照片）</a>
				</td>
				<td>跟上传照片比对</td>
				<td>意愿核身（自传照片）</td>
<td><a href="https://cloud.tencent.com/document/product/1007/56804#.E5.AE.9E.E5.90.8D.E4.BF.A1.E6.81.AF.E6.A0.B8.E9.AA.8C.E4.BB.B7.E6.A0.BC.E8.AF.B4.E6.98.8E">价格说明</a></td>
    </tr>
</table>

>?目前意愿核身服务为内测阶段，如需接入使用，欢迎您 [点此链接](https://cloud.tencent.com/document/product/1007/56130) 扫描二维码添加腾讯云人脸核身小助手进行询问。
