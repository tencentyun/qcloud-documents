<table style="display:table">
    <tbody>
        <tr>
            <td style="background-color:#CCCCCC;">
                <strong>
                    API 大类
                </strong>
            </td>
            <td style="background-color:#CCCCCC;">
                <strong>
                    API 子类
                </strong>
            </td>
                        <td style="background-color:#CCCCCC;">
                <strong>
                    功能
                </strong>
            </td>
            <td style="background-color:#CCCCCC;">
                <strong>
                    API
                </strong>
            </td>
        </tr>
        <!--视频上传-->
		<tr>
			<td rowspan=3>
				视频上传
			</td>
			<td>
				URL 拉取视频上传
			</td>
			<td>
				URL 拉取视频上传
			</td>
            <td>
                <a href="/document/product/266/7817">
                    MultiPullVodFile
                </a>
            </td>
		</tr>
        <tr>
            <td rowspan=2>
                服务端视频上传
            </td>
            <td>
                发起上传
            </td>
            <td>
                <a href="/document/product/266/9756">
                    ApplyUpload
                </a>
            </td>
        </tr>
        <tr>
            <td>
                确认上传
            </td>
            <td>
                <a href="/document/product/266/9757">
                    CommitUpload
                </a>
            </td>
        </tr>
        <!--媒资管理-->
        <tr>
			<td rowspan=15>
				媒资管理
			</td>
            <td rowspan=5>
                视频分类管理
            </td>
            <td>
                创建视频分类
            </td>
            <td>
                <a href="/document/product/266/7812">
                    CreateClass
                </a>
            </td>
        </tr>
        <tr>
            <td>
                获取视频分类层次结构
            </td>
			<td>
                <a href="/document/product/266/7813">
                    DescribeAllClass
                </a>
            </td>
        </tr>
        <tr>
            <td>
                获取视频分类信息
            </td>
			<td>
                <a href="/document/product/266/7814">
                    DescribeClass
                </a>
            </td>
        </tr>
        <tr>
            <td>
                修改视频分类
            </td>
			<td>
                <a href="/document/product/266/7815">
                    ModifyClass
                </a>
            </td>
        </tr>
        <tr>
            <td>
                删除视频分类
            </td>
			<td>
                <a href="/document/product/266/7816">
                    DeleteClass
                </a>
            </td>
        </tr>
		<tr>
			<td rowspan=5>
				获取视频信息
			</td>
            <td>
                获取视频信息
            </td>
			<td>
                <a href="/document/product/266/7824">
                    DescribeVodPlayUrls
                </a>
            </td>
		</tr>
		<tr>
            <td>
                获取视频信息 	V2
            </td>
			<td>
                <a href="/document/product/266/8586">
                    GetVideoInfo
                </a>
            </td>
		</tr>
		<tr>
            <td>
                批量获取视频信息
            </td>
			<td>
                <a href="/document/product/266/7823">
                    DescribeVodInfo
                </a>
            </td>
		</tr>
		<tr>
            <td>
                依照视频名称前缀获取视频信息
            </td>
			<td>
                <a href="/document/product/266/7825">
                    DescribeVodPlayInfo
                </a>
            </td>
		</tr>
		<tr>
            <td>
                依照 VID 查询视频信息
            </td>
			<td>
                <a href="/document/product/266/8227">
                    DescribeRecordPlayInfo
                </a>
            </td>
		</tr>
		<tr>
            <td>
                增加视频标签
            </td>
            <td>
                增加视频标签
            </td>
			<td>
                <a href="/document/product/266/7826">
                    CreateVodTags
                </a>
            </td>
		</tr>
		<tr>
            <td>
                删除视频标签
            </td>
            <td>
                删除视频标签
            </td>
			<td>
                <a href="/document/product/266/7827">
                    DeleteVodTags
                </a>
            </td>
		</tr>
		<tr>
            <td>
                删除视频
            </td>
            <td>
                删除视频
            </td>
			<td>
                <a href="/document/product/266/7838">
                    DeleteVodFile
                </a>
            </td>
		</tr>
		<tr>
            <td>
                截图地址设为视频封面
            </td>
            <td>
                截图地址设为视频封面
            </td>
			<td>
                <a href="/document/product/266/8814">
                    DescribeVodCover
                </a>
            </td>
		</tr>
		<tr>
            <td>
                修改视频属性
            </td>
            <td>
                修改视频属性
            </td>
			<td>
                <a href="/document/product/266/7828">
                    ModifyVodInfo
                </a>
            </td>
		</tr>
        <!--视频处理-->
        <tr>
			<td rowspan=7>
				视频处理
			</td>
            <td>
                视频转码
            </td>
            <td>
                视频转码
            </td>
            <td>
                <a href="/document/product/266/7822">
                    ConvertVodFile
                </a>
            </td>
        </tr>
        <tr>
            <td>
                视频剪辑
            </td>
            <td>
                视频剪辑
            </td>
            <td>
                <a href="/document/product/266/10156">
                    ClipVideo
                </a>
            </td>
        </tr>
        <tr>
            <td>
                视频拼接
            </td>
            <td>
                视频拼接
            </td>
            <td>
                <a href="/document/product/266/7821">
                    ConcatVideo
                </a>
            </td>
        </tr>
        <tr>
            <td>
                HLS 视频简单剪切
            </td>
            <td>
                HLS 视频简单剪切
            </td>
            <td>
                <a href="/document/product/266/8859">
                    SimpleClipHls
                </a>
            </td>
        </tr>
        <tr>
            <td>
                指定时间点截图
            </td>
            <td>
                指定时间点截图
            </td>
            <td>
                <a href="/document/product/266/8102">
                    CreateSnapshotByTimeOffset
                </a>
            </td>
        </tr>
        <tr>
            <td>
                截取雪碧图
            </td>
            <td>
                截取雪碧图
            </td>
            <td>
                <a href="/document/product/266/8101">
                    CreateImageSprite
                </a>
            </td>
        </tr>
        <tr>
            <td>
                获取视频解密秘钥
            </td>
            <td>
                获取视频解密秘钥
            </td>
            <td>
                <a href="/document/product/266/9643">
                    DescribeDrmDataKey
                </a>
            </td>
        </tr>
        <!--任务流-->
        <tr>
			<td rowspan=2>
				任务流
			</td>
            <td>
                按指定任务流处理视频
            </td>
            <td>
                按指定任务流处理视频
            </td>
            <td>
                <a href="/document/product/266/9045">
                    ProcessFileByProcedure
                </a>
            </td>
        </tr>
        <tr>
            <td>
                按指定参数处理视频
            </td>
            <td>
                按指定参数处理视频
            </td>
            <td>
                <a href="/document/product/266/9642">
                    ProcessFile
                </a>
            </td>
        </tr>
        <!--参数模版管理-->
        <tr>
			<td rowspan=5>
				参数模版管理
			</td>
			<td rowspan=5>
				转码模版
			</td>
            <td>
                创建转码模板
            </td>
            <td>
                <a href="/document/product/266/9910">
                    CreateTranscodeTemplate
                </a>
            </td>
        </tr>
        <tr>
            <td>
                更新转码模板
            </td>
            <td>
                <a href="/document/product/266/9911">
                    UpdateTranscodeTemplate
                </a>
            </td>
        </tr>
        <tr>
            <td>
                查询转码模板
            </td>
            <td>
                <a href="/document/product/266/9912">
                    QueryTranscodeTemplate
                </a>
            </td>
        </tr>
        <tr>
            <td>
                查询转码模板列表
            </td>
            <td>
                <a href="/document/product/266/9913">
                    QueryTranscodeTemplateList
                </a>
            </td>
        </tr>
		<tr>
            <td>
                删除转码模板
            </td>
            <td>
                <a href="/document/product/266/9914">
                    DeleteTranscodeTemplate
                </a>
            </td>
        </tr>
        <!--可靠事件通知-->
        <tr>
			<td rowspan=2>
				可靠事件通知
			</td>
            <td>
                拉取事件通知
            </td>
            <td>
                拉取事件通知
            </td>
            <td>
                <a href="/document/product/266/7818">
                    PullEvent
                </a>
            </td>
        </tr>
        <tr>
            <td>
                确认事件通知
            </td>
            <td>
                确认事件通知
            </td>
            <td>
                <a href="/document/product/266/7819">
                    ConfirmEvent
                </a>
            </td>
        </tr>
    </tbody>
</table>