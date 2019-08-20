<table>
    <tr>
        <th>分类</th> 
        <th>规格与限制</th> 
    			<th>详细描述</th> 
   </tr>
    <tr>
        <td>QPS</td>
    			<td>限制</td>
    			<td>每个主账号默认为1200qps，如需更高 QPS，请参见 <a href="/document/product/436/13653">请求速率与性能优化</a> </td>
    </tr>
		    <tr>
        <td>带宽</td>
    			<td>限制</td>
    			<td>COS 不对上传和下载带宽进行限制，具体的上传和下载速度与您本地带宽有关 </td>
    </tr>
    	 <tr>
        <td rowspan="3">存储类型</td>
    			<td>标准存储限制</td>
    			<td>计费限制：<br>存储时间、存储单元无限制<br>标准存储计费详情，请参见 <a href="https://cloud.tencent.com/document/product/436/6239">费用说明</a></td>
    </tr>
    	 <tr>
        <td>低频存储限制</td>
    			<td>计费限制：<br>存储时间不足30天，按30天计算<br>存储单元不足64KB，按64KB计算<br>低频存储计费详情，请参见 <a href="https://cloud.tencent.com/document/product/436/6239">费用说明</a></td>
    </tr>
    	 <tr>
        <td>归档存储限制</td>
    			<td>计费限制：<br>存储时间不足90天，按90天计算<br>存储单元不足64KB，按64KB计算<br>归档存储计费详情，请参见 <a href="https://cloud.tencent.com/document/product/436/6239">费用说明</a></td>				
    </tr>
     <tr>
        <td rowspan="3">存储桶</td>
    			<td>限制</td>
    			<td>1. 存储桶一旦创建成功，名称和所处地域不能修改<br>2. 同一用户账号下所有存储桶名称唯一且不支持重命名<br>3. 名称只支持小写字母和数字[a-z，0-9]、中划线“-”及其组合，支持1 - 40字符</td>
     </tr>
    	 <tr>
    			<td> 存储桶数量</td>
    			<td>每个主账户最大200个（默认）</td>
    		</tr>
    			<td> 对象数量</td>
    			<td> 每个存储桶中，对象数不限</td>
    		<tr>
    			<td rowspan="4">对象</td>
    			<td>限制</td>
					<td >对象键长度支持1-850B，详情请参见 <a href="https://cloud.tencent.com/document/product/436/13324">对象概述</a></td>
    		</tr>
    			<tr>
    			<td>上传</td>
    			<td>1. 控制台上传单个对象最大512GB<br>2. API/SDK 上传单个对象最大48.82TB (50,000 GB )<br>上传接口规格：<br>&nbsp;&nbsp;a）简单上传：单个对象最大5GB，详情请参见 <a href="https://cloud.tencent.com/document/product/436/14113">简单上传</a> <br>&nbsp;&nbsp;b）分块上传：单个对象最大48.82TB，块大小1MB - 5GB，最后一个块可小于1MB，分块数1 - 10000，详情请参见 <a href="https://cloud.tencent.com/document/product/436/14112">分块上传</a></td>
    		</tr>
    		<tr>
    			<td >复制</td>
    			<td >1. 支持单个账号在相同地域或跨地域进行对象复制<br>2. 同地域进行对象复制免费，跨地域进行对象复制会产生流量费用，详情请参见 <a href="https://cloud.tencent.com/document/product/436/6239">费用说明</a> 中流量费用信息  <br>3. 复制接口规格：<br>&nbsp;&nbsp;a）简单复制：复制单个对象最大5GB，详情请参见 <a href="https://cloud.tencent.com/document/product/436/14117">简单复制</a><br>&nbsp;&nbsp;b）大于5GB 必须用分块复制，复制单个对象最大48.82TB，详情请参见 <a href="https://cloud.tencent.com/document/product/436/14118">分块复制</a></td>
    		</tr>
    		<tr>
    			<td>批量删除</td>
    			<td>通过 API、SDK 发起批量删除，每次最多删除1000个对象</td>
    		</tr>
    		 <tr>
    			<td >访问策略</td>
    			<td >规则数量</td>
    			<td >每个主账号（即同一个 APPID），存储桶和对象的 ACL、Policy 和 CAM 关联的策略数量总和最多为1000条</td>
    		</tr>
    		<tr>
    			<td rowspan="3">生命周期</td>
    			<td>规则数量</td>
    			<td >每个存储桶最多1000条</td>
    		</tr>
    		<tr>
    			<td >存储类型转化</td>
    			<td >标准转低频：最小1天<br>标准/低频转归档：最小1天 </td>
    		</tr>
    		 <tr>
    			<td >过期删除</td>
    			<td >标准/低频/归档过期删除：最小1天</td>
    		</tr>         
    		<tr>
    			<td colspan="2">SDK 种类</td>
    			<td >12种：<br>Andriod、C、C++、C#、Go、iOS、Java、JavaScript、Node.js、PHP、Python、小程序 SDK</td>
    </tr>
</table>
