>!
- 腾讯文智自然语言处理已于2019年7月09日全新升级为 [新版](https://cloud.tencent.com/document/product/271/3317)，接口功能更全面，服务更加稳定，且公测期间免费使用。
- 老版本接口不再继续维护，将于2019年11月16日零点下线，建议您使用 [新版 API ](https://cloud.tencent.com/document/product/271/35484)，体验更优服务。
- 接口切换过程中，若您有相关问题，可加入官方 QQ 群（330130409）详细咨询。

## 1. 接口描述
  域名：wenzhi.api.qcloud.com
  接口名: TextClassify
	
  为用户提供自动文本分类服务，平台已对文本分类的模型算法进行了封装，用户只需提供待分类的文本数据，而不必关注具体的实现，通过平台就能得到提供文本的所属类别。目前平台能识别类别囊括了求职招聘、影视、音乐、健康养生、财经、广告推广、犯罪、政治等90多个类别，且算法支持快速迭代更新已有类别及增加新类别。
## 2. 输入参数
<table class="t">
<tr>
<th width="80"> <b>参数名称</b>
</th><th width="50"> <b>必选</b>
</th><th width="80"> <b>类型</b>
</th><th width="200"> <b>描述</b>
</th></tr>
<tr>
<td> title </td><td> 否 </td><td> String </td><td> 文章标题，编码格式utf8
</td></tr>
<tr>
<td>content </td><td> 是 </td><td> String </td><td> 正文内容，编码格式utf8
</td></tr>
<tr>
<td> secd_nav </td><td> 否 </td><td> String </td><td> 二级导航，编码格式utf8
</td></tr>
<tr>
<td> url </td><td> 否 </td><td> String </td><td> 文章对应的url
</td></tr></table>


## 3. 输出参数
<table class="t">
<tr>
<th width="80"> <b>参数名称</b>
</th><th width="80"> <b>类型</b>
</th><th colspan="3"> <b>描述</b>
</th></tr>
<tr>
<td> code </td><td> Int</td><td colspan="3">错误码，0：成功，其他值：失败
</td></tr>
<tr>
<td> message </td><td> String </td><td colspan="3">错误信息</a>
</td></tr>
<tr>
<td rowspan="4">classes  </td><td rowspan="4">Array  </td><td colspan="3">文本分类结果，其中Array元素包含以下字段(一般取conf最大的为分类结果)
</td></tr>
<tr>
<td> class </td><td> String </td><td> 类别
</td></tr>
<tr>
<td> class_num </td><td> UInt32 </td><td> 类别编号
</td></tr>
<tr>
<td> conf </td><td> Double </td><td> 分类置信度
</td></tr></table>


文本分类API支持的类别列表如下：
（下表类别不全）
<table class="t">
<tr>
<th width="200"> <b>分类代码</b>
</th><th width="100"> <b>值</b>
</th><th width="250"> <b>说明</b>
</th></tr>
<tr>
<td> E_PTC_CATEGORY_UNKNOWN </td><td> 0X00000000 </td><td> 未知分类
</td></tr>
<tr>
<td> E_PTC_CATEGORY_TRAVEL </td><td> 0X00000001 </td><td> 旅游 旅游攻略，景点介绍等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_GAMES </td><td> 0X00000002 </td><td> 游戏 游戏下载，攻略，介绍，新闻等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_CHARACTERS </td><td> 0X00000003 </td><td> 人物 主要是人物介绍、人物访谈类页面
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SPORTS </td><td> 0X00000004 </td><td> 体育 体育赛事，运动等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_MUSIC </td><td> 0X00000005 </td><td> 音乐 音乐相关，乐器等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_MOVIE </td><td> 0X00000006 </td><td> 影视 电影，电视剧，电视节目
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SOFTWARE </td><td> 0X00000007 </td><td> 软件 软件介绍，下载
</td></tr>
<tr>
<td> E_PTC_CATEGORY_LITERATURE </td><td> 0X00000008 </td><td> 文学 小说，文言文，散文等相关页面
</td></tr>
<tr>
<td> E_PTC_CATEGORY_FOOD </td><td> 0X00000009 </td><td> 美食 菜谱，食品制作，介绍等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_INTERACTION_HEALTH </td><td> 0X0000000A </td><td> 健康 医疗、保健、健身等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_INTERACTION_MEDICINE </td><td> 0X0000000B </td><td> 医药 药品介绍，药方等，其他是健康类别
</td></tr>
<tr>
<td> E_PTC_CATEGORY_RETAILSHOP </td><td> 0X0000000C </td><td> 商铺 公司黄页、店铺首页等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_FINANCE </td><td> 0X0000000D </td><td> 财经 股票证券、理财、银行
</td></tr>
<tr>
<td> E_PTC_CATEGORY_CAR </td><td> 0X0000000E </td><td> 汽车 汽车，租车等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_HOUSE </td><td> 0X0000000F </td><td> 房产 房地产，租房，装修等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_COMIC </td><td> 0X00000010</td><td> 动漫 动画，漫画
</td></tr>
<tr>
<td> E_PTC_CATEGORY_INTERACTION_EDUCATION </td><td> 0X00000011 </td><td> 教育 学校、学科、考试，培训等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_TECHNOLOGY </td><td> 0X00000012 </td><td> 科技 手机、电子数码、互联网技术等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_MILITARY </td><td> 0X00000013 </td><td> 军事 国防，军队，战争等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_WEATHER </td><td> 0X00000014 </td><td> 天气 天气预报，气候等
</td></tr>
<tr>
<td> E_PTC_CATEGORY_INTERACTION_ADVERTISE </td><td> 0X00000016 </td><td> 广告
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SOCIAL_ASSEMBLE </td><td> 0X00000017 </td><td> 群体聚集
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SOCIAL_DISASTER </td><td> 0X00000018 </td><td> 自然灾害
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SOCIAL_ACCIDENT </td><td> 0X00000019 </td><td> 交通事故
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SOCIAL_OFFENSE </td><td> 0X0000001A </td><td> 刑事犯罪
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SOCIAL_FORCE </td><td> 0X0000001B </td><td> 暴力执法
</td></tr>
<tr>
<td> E_PTC_CATEGORY_INTERACTION_JOB </td><td> 0X0000001C </td><td> 求职招聘
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SOCIAL_FOODSAFETY </td><td> 0X0000001D </td><td> 食品安全
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SOCIAL_POLLUTION </td><td> 0X0000001E </td><td> 环境污染
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SOCIAL_EPIDEMIC </td><td> 0X0000001F </td><td> 疾病疫情
</td></tr>
<tr>
<td> E_PTC_CATEGORY_SOCIAL_FINANCE </td><td> 0X00000020 </td><td> 金融安全
</td></tr>
<tr>
<td> E_PTC_CATEGORY_POLITICAL_SENSITIVE </td><td> 0X00000021 </td><td> 敏感 政治
</td></tr>
<tr>
<td> E_PTC_CATEGORY_POLITICAL_CORRUPTION </td><td> 0X00000022 </td><td> 贪腐
</td></tr>
<tr>
<td> E_PTC_CATEGORY_POLITICAL_CULT </td><td> 0X00000023 </td><td> 非法组织
</td></tr>
<tr>
<td> E_PTC_CATEGORY_POLITICAL_REACTION </td><td> 0X00000024 </td><td> 反动言论
</td></tr>
<tr>
<td> E_PTC_CATEGORY_POLITICAL_MODEL </td><td> 0X00000025 </td><td> 先进事迹
</td></tr>
<tr>
<td> E_PTC_CATEGORY_INTERACTION_INSPIRATION </td><td> 0X00000028 </td><td> 心灵鸡汤
</td></tr>
<tr>
<td> E_PTC_CATEGORY_POLITICAL_OTHER </td><td> 0X0000002A </td><td> 其它政治类
</td></tr>
<tr>
<td> E_PTC_CATEGORY_OTHER </td><td> 0X0000FFFF </td><td> 其他
</td></tr></table>


## 4. 示例

```
https://wenzhi.api.qcloud.com/v2/index.php?
	Action=TextClassify
	&Nonce=345122
	&Region=sz
	&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&Timestamp=1408704141
	&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ
	&content=腾讯入股京东
```

输出

  
<div class="code">
 <pre>
    {
        &quot;code&quot;: 0,
        &quot;message&quot;: &quot;&quot;,
        &quot;classes&quot;: [
            {
                &quot;class&quot;: &quot;未分类&quot;,
                &quot;class_num&quot;: 0,
                &quot;conf&quot;: 0.291
            },
            {
                &quot;class&quot;: &quot;旅游&quot;,
                &quot;class_num&quot;: 1,
                &quot;conf&quot;: 0.291
            },
            {
                &quot;class&quot;: &quot;科技&quot;,
                &quot;class_num&quot;: 18,
                &quot;conf&quot;: 0.419
            }
        ]
    }
</pre>
</div>
   
