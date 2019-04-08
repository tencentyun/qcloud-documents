## 1. API调用说明

### 1.1 通信协议和规则
		
详见[《腾讯云通信协议和规则》](//cloud.tencent.com/doc/api/256/%E8%AF%B7%E6%B1%82%E7%BB%93%E6%9E%84)

### 1.2 公共参数

公共参数是用于标识用户和接口鉴权的参数, 每次请求均需要携带这些参数, 才能正常发起请求。
		
<table class="t" style="margin-left:20px">
<tr>
<th> <b>名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th><th> <b>必选</b>
</th></tr>
<tr>
<td> Action
</td><td> String
</td><td> 接口指令的名称，例如: DataManipulation
</td><td> 是
</td></tr>
<tr>
<td> Region
</td><td> String
</td><td> 区域参数，用来标识希望操作哪个区域的实例。可选: gz:广州; sh:上海;hk:香港;等<br />部分云产品并非每个区域都有提供, 获取产品对应的地域列表可以使用 <a href="/wiki/v2/DescribeProductRegionList" title="v2/DescribeProductRegionList">/v2/DescribeProductRegionList</a>
</td><td> 是
</td></tr>
<tr>
<td> Timestamp
</td><td> UInt
</td><td> 当前UNIX时间戳
</td><td> 是
</td></tr>
<tr>
<td> Nonce
</td><td> UInt
</td><td> 随机正整数，与Timestamp联合起来, 用于防止重放攻击
</td><td> 是
</td></tr>
<tr>
<td> SecretId
</td><td> String
</td><td> 由腾讯云平台上申请的标识身份的SecretId和SecretKey, 其中SecretKey会用来生成Signature<br />具体参考<a href="http://cloud.tencent.com/doc/api/256/%E6%8E%A5%E5%8F%A3%E9%89%B4%E6%9D%83" title="接口鉴权">接口鉴权</a>页面
</td><td> 是
</td></tr>
<tr>
<td> Signature
</td><td> String
</td><td> 请求签名，用来验证此次请求的合法性, <br />具体参考<a href="http://cloud.tencent.com/doc/api/256/%E6%8E%A5%E5%8F%A3%E9%89%B4%E6%9D%83" title="接口鉴权">接口鉴权</a>页面
</td><td> 是
</td></tr></table>

公共参数详见[《腾讯云公共参数》](//cloud.tencent.com/doc/api/256/%E5%85%AC%E5%85%B1%E5%8F%82%E6%95%B0)


### 1.3 接口鉴权

接口鉴权方法详见[《腾讯云接口鉴权》](https://cloud.tencent.com/document/api/270/1992)

注意：在生成签名的过程中，需要将加密字符串中包含的“_”改写成“.”，从而加密产生签名。

### 1.4 异步任务接口返回格式

详见[《腾讯云异步任务接口返回格式》](//cloud.tencent.com/doc/api/256/%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E6%8E%A5%E5%8F%A3%E8%BF%94%E5%9B%9E%E6%A0%BC%E5%BC%8F)

### 1.5 错误码

详见[《腾讯云错误码》](//cloud.tencent.com/doc/api/256/%E9%94%99%E8%AF%AF%E7%A0%81)

## 2. 数据操作（更新/删除）

### 2.1 接口描述

域名：yunsou.api.qcloud.com
接口名: DataManipulation
对数据进行添加和删除操作

### 2.2 输入参数

<table class="t" style="margin-left:20px">
<tr>
<th> <b>参数名称</b>
</th><th> <b>必选</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> appId
</td><td> 是
</td><td> Int
</td><td> 云搜的业务ID，用以表明当前数据请求的业务
</td></tr>
<tr>
<td> op_type
</td><td> 是
</td><td> String
</td><td> 操作类型，可为"add"或者"del"
</td></tr>
<tr>
<td> contents.n
</td><td> 是
</td><td> Array
</td><td> 文档内容(UTF8编码，长度限制在32k以下)
</td></tr></table>

### 2.3 输出参数

<table class="t" style="margin-left:20px">
<tr>
<th> <b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> 错误码, 0: 成功, 其他值: 失败
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 错误信息，错误码详情参见<a href="http://cloud.tencent.com/doc/api/256/%E9%94%99%E8%AF%AF%E7%A0%81" class="external text" title="//cloud.tencent.com/doc/api/256/%E9%94%99%E8%AF%AF%E7%A0%81" target="_blank" rel="nofollow">错误码说明</a>
</td></tr>
<tr>
<td> data
</td><td> Array
</td><td> 返回详细信息
</td></tr></table>

数据操作错误码详细信息如下：

<table class="t" style="margin-left:20px">
<tr>
<th width="150"> <b>错误码</b>
</th><th> <b>含义说明</b>
</th></tr>
<tr>
<td> -30630001
</td><td> 服务器处理超时
</td></tr>
<tr>
<td> -30630002
</td><td> 内部状态非法
</td></tr>
<tr>
<td> -30630005
</td><td> 服务器响应错误
</td></tr>
<tr>
<td> -30630008
</td><td> 数据发送失败
</td></tr>
<tr>
<td> -30630010
</td><td> 建立数据顺排失败
</td></tr>
<tr>
<td> -30630014
</td><td> 数据包过期
</td></tr>
<tr>
<td> -30630015
</td><td> 数据jason字段不正确
</td></tr>
<tr>
<td> -30630016
</td><td> 数据jason格式不正确
</td></tr>
<tr>
<td> -30630017
</td><td> 服务器流量控制
</td></tr>
<tr>
<td> -30630018
</td><td> 发送数据过长
</td></tr>
<tr>
<td> -30630019
</td><td> 业务不支持，该业务未申请或申请未通过
</td></tr>
<tr>
<td> -30630020
</td><td> 业务尚未初始化
</td></tr>
<tr>
<td> -30630021
</td><td> 业务数据管理初始化失败
</td></tr>
<tr>
<td> -30630022
</td><td> 鉴权消息发送失败
</td></tr>
<tr>
<td> -30630023
</td><td> 鉴权不通过
</td></tr></table>

### 2.4 详细示例


示例业务详细信息如下表：

<table class="t" style="margin-left:20px">
<tr>
<th>
</th><th> <b>参数名称</b>
</th><th> <b>参数描述</b>
</th><th> <b>必选</b>
</th><th> <b>参数值示例</b>
</th></tr>
<tr>
<td rowspan="4"> 腾讯云公共参数
</td><td> Action
</td><td> 方法名
</td><td> 是
</td><td> DataManipulation
</td></tr>
<tr>
<td> SecretId
</td><td> SecretId
</td><td> 是
</td><td> AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
</td></tr>
<tr>
<td> Timestamp
</td><td> 当前时间戳
</td><td> 是
</td><td> 1408704141
</td></tr>
<tr>
<td> Nonce
</td><td> 随机正整数
</td><td> 是
</td><td> 345122
</td></tr>
<tr>
<td rowspan="3"> 业务参数
</td><td> op_type
</td><td> 操作类型
</td><td> 是
</td><td> add
</td></tr>
<tr>
<td> appId
</td><td> 业务ID
</td><td> 是
</td><td> 1
</td></tr>
<tr>
<td> contents.n
</td><td> 更新数据
</td><td> 是
</td><td> 业务结构：<br />文本域-TA\TB\TC;<br />数值域：NA
</td></tr></table>

下面以上述业务为例，详细说明“数据操作”接口的使用方法。

#### 2.4.1 接口鉴权

示例要新增的业务数据为：｛"NA": 1000, "TA": "test1", "TB": "testtitle1", "TC": "testcontent1"}
则上述业务的参数列表如下：

<div class="code" style="margin-left:20px">
<pre>   {
        'Action' : 'DataManipulation',
        'Nonce' : 345122,
        'Region' : 'sz',
        'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
        'Timestamp' : 1408704141,
        'op_type': add,
        'appId': 1,
        'contents.0.NA': 1000,
        'contents.0.TA': test1,
        'contents.0.TB': testtitle1,
        'contents.0.TC': testcontent1
    }
</pre>
</div>

根据上述参数列表进行签名，得出的数字签名为：HgIYOPcx5lN6gz8JsCFBNAWp2oQ（示例），详细的数字签名的生成方法请参照：[《腾讯云接口鉴权》](https://cloud.tencent.com/document/api/270/1992)
注意：
1）在生成签名的过程中，需要将加密字符串中包含的“_”改写成“.”，从而加密产生签名；
2）鉴权时，需要将参数列表按key进行排序：字典序，同时大写在前。

#### 2.4.2 数据更新

根据上一步（2.4.1）中得到的数字签名，以GET请求为例构造请求URL,将数字签名加入到参数Signature中。

<div class="code" style="margin-left:20px">
<pre>   https://yunsou.api.qcloud.com/v2/index.php?
	Action=DataManipulation
	&amp;Nonce=345122
	&amp;Region=sz
	&amp;SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&amp;Timestamp=1408704141
        <b>&amp;Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ</b>
        &amp;op_type=add
	&amp;appId=1
	&amp;contents.0.NA=1000
	&amp;contents.0.TA=test1
	&amp;contents.0.TB=testtitle1
</pre>
</div>

执行上述操作之后，会将文档｛"NA":"1000", "TA":"test1", "TB": "testtitle1", "TC": "testcontent1"｝插入到用户的应用中，从而参与检索。
注意：在发送请求过程中，不能将参数字符串中包含的“_”改写成“.”。
上述指令返回的数据结构如下：

<div class="code" style="margin-left:20px">
<pre>   {
        retcode: 0,
        errmsg: &quot;succ&quot;,
        data: {
            app_id: 14950002,
            result: [
       	        {
                    doc_id: &quot;1000&quot;,
            	    errno: 0,
            	    result: &quot;succ&quot;
        	}
            ],
            seq: 1427872563,
            total_result: &quot;succ&quot;
        },
        code: 0,
        message: &quot;&quot;
    }
</pre>
</div>

#### 2.4.3 数据删除

<div class="code" style="margin-left:20px">
<pre>   https://yunsou.api.qcloud.com/v2/index.php?
	Action=DataManipulation
	&amp;Nonce=345122
	&amp;Region=sz
	&amp;SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&amp;Timestamp=1408704141
	<b>&amp;Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ</b>
        &amp;op_type=del 
	&amp;appId=1
	&amp;contents.0.doc_id=1000
	&amp;contents.1.doc_id=2000
</pre>
</div>

执行上述操作之后，会将文档ID为：1000和2000的文档从用户应用中删除，从而不被检索到。

注意：在发送请求过程中，不能将参数字符串中包含的“_”改写成“.”。

## 3. 数据检索（查询）

### 3.1 接口描述

域名：yunsou.api.qcloud.com

接口名: DataSearch

对数据进行查询操作

### 3.2 输入参数

<table class="t" style="margin-left:20px">
<tr>
<th> <b>参数名称</b>
</th><th> <b>必选</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> appId
</td><td> 是
</td><td> Int
</td><td> 云搜的业务ID，用以表明当前数据请求的业务
</td></tr>
<tr>
<td> search_query
</td><td> 是
</td><td> String
</td><td> 检索串
</td></tr>
<tr>
<td> page_id
</td><td> 是
</td><td> Int
</td><td> 当前页，从第0页开始计算
</td></tr>
<tr>
<td> num_per_page
</td><td> 是
</td><td> Int
</td><td> 每页结果数
</td></tr>
<tr>
<td> search_id
</td><td> 否
</td><td> String
</td><td> 当前检索号，用于定位问题，建议指定并且全局唯一
</td></tr>
<tr>
<td> query_encode
</td><td> 否
</td><td> Int
</td><td> 请求编码，0表示utf8，1表示gbk，建议指定
</td></tr>
<tr>
<td> rank_type
</td><td> 否
</td><td> Int
</td><td> 排序类型
</td></tr>
<tr>
<td> num_filter
</td><td> 否
</td><td> String
</td><td> 数值过滤，结果中按属性过滤（格式参见后面说明）
</td></tr>
<tr>
<td> cl_filter
</td><td> 否
</td><td> String
</td><td> 分类过滤，导航类检索请求（格式参见后面说明）
</td></tr>
<tr>
<td> extra
</td><td> 否
</td><td> String
</td><td> 检索用户相关字段（格式参见后面说明））
</td></tr>
<tr>
<td> source_id
</td><td> 否
</td><td> Int
</td><td> 检索来源
</td></tr>
<tr>
<td> second_search
</td><td> 否
</td><td> Int
</td><td> 是否进行二次检索，0关闭，1打开,默认是0
</td></tr>
<tr>
<td> max_doc_return
</td><td> 否
</td><td> Int
</td><td> 指定返回最大篇数，无特殊原因不建议指定，默认300篇
</td></tr>
<tr>
<td> is_smartbox
</td><td> 否
</td><td> Int
</td><td> 是否smartbox检索，0关闭，1打开,默认是0
</td></tr>
<tr>
<td> enable_abs_highlight
</td><td> 否
</td><td> Int
</td><td> 是否打开高红标亮，0关闭，1打开,默认是0
</td></tr>
<tr>
<td> qc_bid
</td><td> 否
</td><td> Int
</td><td> 指定访问QC业务ID
</td><td>
</td></tr>
<tr>
<td> l4_rank_expression
</td><td> 否
</td><td> String
</td><td> 指定高级排序表达式
</td></tr>
<tr>
<td> match_value
</td><td> 否
</td><td> String
</td><td> 指定排序参考值
</td></tr>
<tr>
<td> longitude
</td><td> 否
</td><td> Double
</td><td> 指定经度
</td></tr>
<tr>
<td> latitude
</td><td> 否
</td><td> Double
</td><td> 指定纬度
</td></tr>
<tr>
<td> group_by
</td><td> 否
</td><td> String
</td><td> 指定group_by的字段名，仅能指定数值字段
</td></tr>
<tr>
<td> distinct
</td><td> 否
</td><td> String
</td><td> 指定distinct的字段名，仅能指定数值字段
</td></tr></table>

下面将详细介绍其中重要的数值过滤、分类检索以及用户指定排序参数的详细用法：

#### 3.2.1 数值过滤

数值过滤功能对应检索请求中的num_filter参数，其参数值的结构描述为:

[N:meta:start:end]

该表达式含义为：属性满足start <= meta值 <= end的文档将会被留下，其它的被过滤。其中，meta字段必须为数值字段。

另外，数值过滤表达式之间支持“与”“或”关系。用&和|符号连接，支持使用括号标识优先级。如，[N:meta1:start:end]&([N:meta2:start:end]|[N:meta3:start:end])

示例：数值过滤表达式

[N:NA:100:150]&[N:NB:200:200]

上述表达式的含义为：查找NA字段在100-150之间，并且NB等于200的结果（其中NA和NB为数值字段）。

#### 3.2.2 分类检索

分类检索对应检索请求中的cl_filter参数，其参数值的结构描述为：

[C:meta:value]

该表达式含义为：对该meta域使用特殊的倒排索引进行检索，特别适用于导航检索。其中meta字段可为数字或数值。

另外，分类检索表达式支持“与”“或”关系。用&和|符号连接，支持使用括号标识优先级。如，[C:meta1:value1]&([C:meta2:value2]|[C:meta3:value3])。

示例：分类过滤表达式

[C:CA:store]&[C:CB:log]

上述表达式的含义为：查找CA字段为store，并且CB字段为log的结果（其中CA和CB为分类域字段）。

#### 3.2.3 用户指定排序

用户指定排序涉及到检索请求中的两个参数：rank_type和extra。

其使用方法如下：

1）rank_type=0：搜索结果按照文本相关性打分降序排列，extra字段被忽略；

2）rank_type=1：搜索结果按照文本相关性打分升序排列，extra字段被忽略；

3) rank_type=2：按照用户输入的extra字段，结合用户在高级组件中定制的排序对返回结果的顺序进行排序

4) rank_type=5：不使用额外的排序策略，按搜索结果直接返回，extra字段被忽略；


当rank_type的值被指定为2时，extra参数值的格式为：

META1_TYPE1_META2_TYPE2_rel_TYPE3

以上表达式表示的含义为，排序分成三档，仅在前一档值相同情况下，才会进行下一档排序:

1）第一档按照META1的属性值进行排序，排序类型为TYPE1

2）第二档按照META2的属性值进行排序，排序类型为TYPE2

3）第三档按照rel（即文本相关性得分进行排序），排序类型为TYPE3。注意：rel字段的值非业务数据，而是搜索侧的计算结果


表达式取值方法：

1) Meta：meta本身为属性字段名即可（不含下划线，避免冲突），但是需要保证需要进行排序的属性是数值字段

2) Type:

Type=0: 当前属性越小，排序越靠前；

Type=1：当前属性越大，排序越靠前；

### 3.3 输出参数

<table class="t" style="margin-left:20px">
<tr>
<th> <b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> 错误码, 0: 成功, 其他值: 失败
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 错误信息，错误码详情参见<a href="http://cloud.tencent.com/doc/api/256/%E9%94%99%E8%AF%AF%E7%A0%81" class="external text" title="http://cloud.tencent.com/doc/api/256/%E9%94%99%E8%AF%AF%E7%A0%81" target="_blank" rel="nofollow">错误码说明</a>
</td></tr>
<tr>
<td> echo
</td><td> String
</td><td> 与检索请求中的echo相对应
</td></tr>
<tr>
<td> result_num
</td><td> Int
</td><td> 检索返回的当前页码结果数
</td></tr>
<tr>
<td> display_num
</td><td> Int
</td><td> 搜索最多可展示结果数，多页
</td></tr>
<tr>
<td> eresult_num
</td><td> Int
</td><td> 检索结果的估算篇数
</td></tr>
<tr>
<td> cost_time
</td><td> Int
</td><td> 检索耗时，单位为ms
</td></tr>
<tr>
<td> result_list
</td><td> Array
</td><td> 检索结果列表
</td></tr>
<tr>
<td> seg_list
</td><td> Array
</td><td> 检索的分词结果，array类型，可包含多个
</td></tr></table>

检索结果列表说明：

<table class="t" style="margin-left:20px">
<tr>
<th> <b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> doc_id
</td><td> Int
</td><td> 检索文档id
</td></tr>
<tr>
<td> doc_meta
</td><td> String
</td><td> 摘要信息
</td></tr>
<tr>
<td> search_debuginfo
</td><td> String
</td><td> 文档级回传信息
</td></tr>
<tr>
<td> l2_score
</td><td> Float
</td><td> 精计算打分
</td></tr></table>


数据检索错误码详细信息如下：

<table class="t" style="margin-left:20px">
<tr>
<th width="150"> <b>错误码</b>
</th><th> <b>含义说明</b>
</th></tr>
<tr>
<td> -2100007
</td><td> 请求页码错误
</td></tr>
<tr>
<td> -2100008
</td><td> 检索服务无效输入参数
</td></tr>
<tr>
<td> -2100009
</td><td> 检索服务请求下游失败
</td></tr>
<tr>
<td> -2100010
</td><td> 检索服务请求超时
</td></tr>
<tr>
<td> -2100011
</td><td> 检索服务获取下游信息失败
</td></tr>
<tr>
<td> -2100012
</td><td> 检索服务merge失败
</td></tr>
<tr>
<td> -2100013
</td><td> 检索服务编码转化失败
</td></tr>
<tr>
<td> -2100014
</td><td> 检索服务获取路由信息失败
</td></tr>
<tr>
<td> -2100015
</td><td> 检索服务获取路由信息超时
</td></tr>
<tr>
<td> -2100016
</td><td> 检索服务获取下游地址失败
</td></tr>
<tr>
<td> -2100017
</td><td> 检索服务不可信
</td></tr>
<tr>
<td> -2100018
</td><td> 输入检索串超过限定长度
</td></tr>
<tr>
<td> -2100019
</td><td> 生成语法树失败
</td></tr>
<tr>
<td> -2100022
</td><td> 无效下游请求
</td></tr>
<tr>
<td> -2100023
</td><td> 生成数值过滤逻辑错误
</td></tr>
<tr>
<td> -2100025
</td><td> 检索零结果
</td></tr>
<tr>
<td> -2100026
</td><td> Query改写返回错误
</td></tr>
<tr>
<td> -2100027
</td><td> Query改写结果解析失败
</td></tr>
<tr>
<td> -2100030
</td><td> Qery改写返回语法数节点个数为零
</td></tr>
<tr>
<td> -2100031
</td><td> 摘要错误
</td></tr>
<tr>
<td> -2100032
</td><td> L4排序错误
</td></tr>
<tr>
<td> -2100033
</td><td> 无效编码请求
</td></tr>
<tr>
<td> -2100034
</td><td> 检索服务流控过滤当前请求
</td></tr>
<tr>
<td> -2200008
</td><td> 检索接口无效检索参数
</td></tr>
<tr>
<td> -2200010
</td><td> 请求超时
</td></tr>
<tr>
<td> -2200017
</td><td> 检索服务不可信
</td></tr>
<tr>
<td> -2200020
</td><td> 发送请求失败
</td></tr>
<tr>
<td> -2200021
</td><td> 接受响应失败
</td></tr>
<tr>
<td> -2200025
</td><td> 检索零结果
</td></tr></table>


### 3.4 详细示例


示例业务详细信息如下表：

<table class="t" style="margin-left:20px">
<tr>
<th>
</th><th> <b>参数名称</b>
</th><th> <b>参数描述</b>
</th><th> <b>必选</b>
</th><th> <b>参数值示例</b>
</th></tr>
<tr>
<td rowspan="4"> 腾讯云公共参数
</td><td> Action
</td><td> 方法名
</td><td> 是
</td><td> DataSearch
</td></tr>
<tr>
<td> SecretId
</td><td> SecretId
</td><td> 是
</td><td> AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
</td></tr>
<tr>
<td> Timestamp
</td><td> 当前时间戳
</td><td> 是
</td><td> 1408704141
</td></tr>
<tr>
<td> Nonce
</td><td> 随机正整数
</td><td> 是
</td><td> 345122
</td></tr>
<tr>
<td rowspan="4"> 业务参数
</td><td> appId
</td><td> 业务ID
</td><td> 是
</td><td> 1
</td></tr>
<tr>
<td> search_query
</td><td> 检索串
</td><td> 是
</td><td> qq
</td></tr>
<tr>
<td> page_id
</td><td> 检索页码
</td><td> 是
</td><td> 0
</td></tr>
<tr>
<td> num_per_page
</td><td> 每页结果数
</td><td> 是
</td><td> 10
</td></tr></table>

下面以上述业务为例，详细说明“数据检索”接口的使用方法。

#### 3.4.1 接口鉴权

上述业务的参数列表如下：

<div class="code" style="margin-left:20px">
<pre>   {
        'Action' : 'DataSearch',
        'Nonce' : 345122,
        'Region' : 'sz',
        'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
        'Timestamp' : 1408704141,
        'appId': 1,
        'search_query': 'qq', 
        'page_id': 0,
        'num_per_page': 10
    }
</pre>
</div>

根据上述参数列表进行签名，得出的数字签名为：HgIYOPcx5lN6gz8JsCFBNAWp2oQ（示例），详细的数字签名的生成方法请参照：《腾讯云接口鉴权》。
注意：
1）在生成签名的过程中，需要将加密字符串中包含的“_”改写成“.”，从而加密产生签名；
2）鉴权时，需要将参数列表按key进行排序：字典序，同时大写在前。

#### 3.4.2 数据检索


根据上一步（3.4.1）中得到的数字签名，以GET请求为例构造请求URL,将数字签名加入到参数Signature中。

<div class="code" style="margin-left:20px">
<pre>   https://yunsou.api.qcloud.com/v2/index.php?
	Action=DataSearch
	&amp;Nonce=345122
	&amp;Region=sz
	&amp;SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&amp;Timestamp=1408704141
	<b>&amp;Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ</b>
        &amp;appId=1
	&amp;search_query=qq
	&amp;page_id=0
	&amp;num_per_page=10
</pre>
</div>

执行上述操作之后，会将文档｛"NA":"1000", "TA":"test1", "TB": "testtitle1", "TC": "testcontent1"｝插入到用户的应用中，从而参与检索。

注意：在发送请求过程中，不能将参数字符串中包含的“_”改写成“.”。

执行上述操作之后，将会返回和检索串“qq”相关的文档，上述指令返回的数据结构如下：

<div class="code" style="margin-left:20px">
<pre>   {
        &quot;code&quot;: 0,
        &quot;message&quot;: &quot;&quot;
        &quot;data&quot;: {
            &quot;cost_time&quot;: 19,
            &quot;display_num&quot;: 2,
            &quot;echo&quot;: &quot;&quot;,
            &quot;eresult_num&quot;: 2,
            &quot;result_list&quot;: [
                {
                    &quot;doc_id&quot;: &quot;200&quot;,
                    &quot;doc_meta&quot;: &quot;{
                	&quot;AA&quot;: &quot;41&quot;,
                   	&quot;NA&quot;: &quot;200&quot;,
                        &quot;TA&quot;: &quot;qq&quot;,
                        &quot;TB&quot;: &quot;cloudsearchdoc&quot;,
                        &quot;TC&quot;: &quot;qq&quot;
                    }&quot;,
                    &quot;l2_score&quot;: 0,
                    &quot;search_debuginfo&quot;: &quot;&quot;
                },
                {
                    &quot;doc_id&quot;: &quot;11005&quot;,
                    &quot;doc_meta&quot;: &quot;{
                    	&quot;AA&quot;: &quot;41&quot;,
                	&quot;NA&quot;: &quot;200&quot;,
                	&quot;TA&quot;: &quot;qq&quot;,
                	&quot;TB&quot;: &quot;cloudsearchdoc&quot;,
                 	&quot;TC&quot;: &quot;qq&quot;
               	    }&quot;,
                    &quot;l2_score&quot;: 0,
                    &quot;search_debuginfo&quot;: &quot;&quot;
                }
            ],
            &quot;result_num&quot;: 2,
            &quot;seg_list&quot;: [
                {
                    &quot;seg_str&quot;: &quot;qq&quot;
                },
                {
                    &quot;seg_str&quot;: &quot;腾讯&quot;
                }
            ]
        }
    }
</pre>
</div>


## 4. 云搜SDK参考

为方便开发者调试和接入云API， 我们提供了一些常用语言的 SDK。如下所示：

| 开发语言 | github地址 | 下载 |
|---------|---------|---------|
| PHP | https://github.com/QcloudApi/qcloudapi-sdk-php | [单击下载](https://mc.qcloudimg.com/static/archive/cd1857b4d9a9aeb0179e72a59f235c41/qcloudapi-sdk-php-master.zip) |
| Python | https://github.com/QcloudApi/qcloudapi-sdk-python | [单击下载](https://mc.qcloudimg.com/static/archive/b61ee1ce734e7437530304152c20ee14/qcloudapi-sdk-python-master.zip) |
| Java | https://github.com/QcloudApi/qcloudapi-sdk-java | [单击下载](https://mc.qcloudimg.com/static/archive/72dbc1a82ad8e18dead2e6dc07acd5d7/qcloudapi-sdk-java-master.zip) |
| .Net | https://github.com/QcloudApi/qcloudapi-sdk-dotnet | [单击下载](https://mc.qcloudimg.com/static/archive/b55098d83c78db530c53fb10f44c3fef/qcloudapi-sdk-dotnet-master.zip) |
