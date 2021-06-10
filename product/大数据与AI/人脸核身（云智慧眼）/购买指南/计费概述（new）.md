>?本文描述的计费标签适用于2021年6月22日后开通人脸核身服务的客户，如您需要查看2021年6月22日前的计费标签，请查看[计费概述（旧）](https://cloud.tencent.com/document/product/1007/31005)。

## 计费方式
腾讯云人脸核身按调用量计费，调用结果及其对应收费关系请参考 [计费错误码](https://cloud.tencent.com/document/product/1007/48021)。
腾讯云人脸核身提供预付费和后付费两种计费方式，您可以结合自身业务场景灵活选择付费方式。 

|   计费方式|  描述  | 结算方式|
|-----------|-------|-------|
|后付费|后付费方式是人脸核身服务默认的计费方式，根据您使用腾讯云慧眼人脸核身相关产品产生的调用量进行计费，当月1-5号为您推送上个自然月账单并进行扣费结算。 |按调用量月结|
|预付费|资源包是人脸核身服务针对不同的产品类型推出的优惠套餐，您可以通过购买不同的资源包，抵扣使用腾讯云慧眼人脸核身相关产品产生的计费调用量。|购买资源包|

人脸核身的预付费资源包支持多种规格，可以通过打开 [购买页](https://buy.cloud.tencent.com/iai_faceid) 购买，有效期均为1年，1年内若资源包次数未使用完，则过期作废；预付费资源包使用后不支持剩余次数冻结，若购买后未使用，支持7天内无理由退款。


## 接入渠道与计费标签

### 增强版人脸核身
增强版人脸核身接入渠道与计费标签对应关系说明如下，若您想了解详细定价信息请查阅 [价格说明](https://cloud.tencent.com/document/product/1007/56804) 文档。

<table>
    <tr>
        <th>接入渠道</th>
				<th>比对库源</th>
        <th>计费标签</th>
			<th>支持的付费方式</th>
    </tr>
    <tr>
        <td rowspan =2>
            <li><a href="https://cloud.tencent.com/document/product/1007/42656">微信原生 H5</a></li><li><a href="https://cloud.tencent.com/document/product/1007/31071">微信小程序</a></li>
				</td>
				<td>跟权威库比对</td>
			 <td>增强版人脸核身（权威库）-微信</td>
			 	<td>后付费月结、预付费资源包</td>        
    </tr>
		   <tr>
			 <td>跟上传照片比对</td>
			 <td>增强版人脸核身（自传照片）-微信</td>
			 <td>后付费月结、预付费资源包</td> 
			  </tr>
			   <tr>
                   <td rowspan =2><a href="https://cloud.tencent.com/document/product/1007/35866">增强版 App SDK</a>
				</td>
				<td>跟权威库比对</td>
				<td>增强版人脸核身（权威库）-App</td>
		<td>后付费月结、预付费资源包</td> 
    </tr>
		   <tr>
	 <td>跟上传照片比对</td><td>增强版人脸核身（自传照片）-App</td>
			 	<td>后付费月结、预付费资源包</td> 
			  </tr>
</table>

### 基础版人脸核身

基础版人脸核身接入渠道与计费标签对应关系说明如下，若您想了解详细定价信息请查阅 [价格说明](https://cloud.tencent.com/document/product/1007/56804) 文档。

<table>
    <tr>
        <th>接入渠道</th>
				<th>比对库源</th>
        <th>计费标签</th>
			<th>支持的付费方式</th>
    </tr>
    <tr>
        <td rowspan =2>
				<li><a href="https://cloud.tencent.com/document/product/1007/42656">微信普通 H5</a></li><li><a href="https://cloud.tencent.com/document/product/1007/35883">独立 H5</a></li><li><a href="https://cloud.tencent.com/document/product/1007/35893">PC H5</a></li><li><a href="https://cloud.tencent.com/document/product/1007/35866">App SDK</a></li>
				</td>
				<td>跟权威库比对</td>
			 <td>基础版人脸核身（权威库）</td>
			 	<td>后付费月结、预付费资源包</td>       
    </tr>
		   <tr>
			 <td>跟上传照片比对</td>
			 <td>基础版人脸核身（自传照片）</td>
			 <td>后付费月结、预付费资源包</td> 
			  </tr>
			   <tr>
                   <td><a href="https://cloud.tencent.com/document/product/1007/31818">活体人脸核身 API</a>
				</td>
				<td>跟权威库比对</td><td>基础版人脸核身（权威库）</td>
						 	<td>后付费月结、预付费资源包</td> 
    </tr>
		   <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/31820">照片人脸核身 API</a></td>
			 <td>跟权威库比对</td><td>基础版人脸核身（权威库）</td>
			 	<td>后付费月结、预付费资源包</td> 
			  </tr>
    <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/31819">活体人脸比对 API</a></td><td>跟上传照片比对</td>
			 <td>基础版人脸核身（自传照片）</td>
			 	<td>后付费月结、预付费资源包</td> 
			  </tr>
				    <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/47276">身份证人像照片验真 API</a></td><td>跟权威库比对</td>
			 <td>基础版人脸核身（权威库）</td>
			 	<td>后付费月结、预付费资源包</td> 
			  </tr>
</table>





### 实名信息核验

实名信息核验各 API 接口与计费标签对应关系说明如下，若您想了解详细定价信息请查阅 [价格说明](https://cloud.tencent.com/document/product/1007/56804) 文档。

<table>
    <tr>
        <th> API 接口</th>
        <th>计费标签</th>
			<th>是否支持预付费</th>
		 <th>是否支持后付费</th>
    </tr>	 
				 <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/33188">身份信息认证</a></td>
			 <td rowspan =4>身份证信息核验</td>
			 	<td>是</td> 
				<td>是</td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/37980">身份证识别及信息核验</a></td>
			 	<td>是</td> 
				<td>是</td>
			  </tr>
	<tr>
		<tr>
		<td><a href="https://cloud.tencent.com/document/product/1007/51441">微信实名认证授权</a></td>
			 	<td>是</td> 
				<td>是</td>
			  </tr>	
			 <td><a href="https://cloud.tencent.com/document/product/1007/35776">银行卡二要素</a></td>
			 <td rowspan =3>银行卡信息核验</td>
			 	<td>是</td> 
				<td>是</td>
			  </tr>
				 <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/33848">银行卡三要素</a></td>
			 <td>是</td>
			 <td>是</td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/35775">银行卡四要素</a></td>
			 <td>是</td>
			 <td>是</td>
			  </tr>
				<tr>
				 <td><a href="https://cloud.tencent.com/document/product/1007/39765">手机号三要素核验</a></td>
			 <td rowspan =2>手机号信息核验</td>
			 <td>是</td>
			 <td>是</td>
			  </tr>
			 <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/50364">手机号二要素核验</a></td>
			 <td>是</td>
			 <td>是</td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/40546">手机号在网时长核验</a></td>
			  <td rowspan =2>手机号在网时长/状态查询</td>
			 <td>否</td>
			 <td>是</td>
			  </tr>
			 <tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/40545">手机号状态查询</a></td>
			 <td>否</td>
			 <td>是</td>
			  </tr>
				<tr>
			 <td><a href="https://cloud.tencent.com/document/product/1007/47837">银行卡基础信息查询</a></td>
			 <td>增值服务</td>
			<td>否</td>
			<td>是</td>
			  </tr>
</table>


### E 证通

E 证通服务与计费标签对应关系说明如下，若您想了解详细定价信息请查阅 [价格说明](https://cloud.tencent.com/document/product/1007/56804) 文档。

<table>
    <tr>
        <th>接入渠道</th>
				<th>比对库源</th>
        <th>计费标签</th>
			<th>支持的付费方式</th>
    </tr>
			   <tr>
                   <td ><a href="https://cloud.tencent.com/document/product/1007/54116">E 证通</a>
				</td>
				<td>跟权威库比对</td>
				<td>E 证通（权威库）</td>
		<td>后付费月结、预付费资源包</td> 
    </tr>
</table>


