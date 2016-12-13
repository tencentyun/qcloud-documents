<table style="display:table">
    <tbody>
        <tr>
            <td style="background-color:#CCCCCC;">
                <strong>
                    分类
                </strong>
            </td>
            <td style="background-color:#CCCCCC;">
                <strong>
                    功能
                </strong>
            </td>
            <td style="background-color:#CCCCCC;">
                <strong>
                    接口名称
                </strong>
            </td>
            <td style="background-color:#CCCCCC;">
                <strong>
					接口别名(兼容点播1.0)
                </strong>
            </td>
        </tr>
        <!--视频上传-->
        <tr>
            <td rowspan=3>
                服务端视频上传
            </td>
            <td>
                初始化上传
            </td>
            <td>
                <a href="/document/product/266/7809">
                    InitUpload
                </a>
            </td>
			<td>
			</td>
        </tr>
        <tr>
            <td>
                分片上传
            </td>
            <td>
                <a href="/document/product/266/7810">
                    UploadPart
            </td>
			<td>
			</td>
        </tr>
        <tr>
            <td>
                结束上传
            </td>
            <td>
                <a href="/document/product/266/7811">
                    FinishUpload
                </a>
            </td>
			<td>
			</td>
        </tr>
        <!--URL拉取视频上传-->
        <tr>
            <td rowspan=1>
                URL拉取视频上传
            </td>
            <td>
                URL拉取视频上传
            </td>
            <td>
                <a href="/document/product/266/7817">
                    MultiPullVideoFromUrl
                </a>
            </td>
			<td>
                <a href="/document/product/266/7817">
                    MultiPullVodFile
                </a>
			</td>
        </tr>
        <!--视频管理-->
        <tr>
            <td rowspan=7>
                视频管理
            </td>
            <td>
                获取视频信息
            </td>
            <td>
                <a href="/document/product/266/7824">
                    GetVideoInfo
                </a>
            </td>
			<td>
                <a href="/document/product/266/7824">
                    DescribeVodPlayUrls
                </a>
			</td>
        </tr>
        <tr>
            <td>
                批量获取视频信息
            </td>
            <td>
                <a href="/document/product/266/7823">
                    GetVideoInfoBatch
                </a>
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
                    GetVideoInfoByNamePrefix
                </a>
            </td>
			<td>
                <a href="/document/product/266/7825">
                    DescribeVodPlayInfo
                </a>
			</td>
        </tr>
        <tr>
            <td>
                修改视频属性
            </td>
            <td>
                <a href="/document/product/266/7828">
                    ModifyVideoInfo
                </a>
            </td>
			<td>
                <a href="/document/product/266/7828">
                    ModifyVodInfo
                </a>
			</td>
        </tr>
        <tr>
            <td>
                增加视频标签
            </td>
            <td>
                <a href="/document/product/266/7826">
                    AddVideoTags
                </a>
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
                <a href="/document/product/266/7827">
                    DeleteVideoTags
                </a>
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
                <a href="/document/product/266/7838">
                    DeleteVideo
                </a>
            </td>
			<td>
                <a href="/document/product/266/7838">
                    DeleteVodFile
                </a>
			</td>
        </tr>
        <!--视频转码-->
        <tr>
            <td>
                视频转码
            </td>
            <td>
                视频转码
            </td>
            <td>
                <a href="/document/product/266/7822">
                    TranscodeVideo
                </a>
            </td>
			<td>
                <a href="/document/product/266/7822">
                    ConvertVodFile
                </a>
			</td>
        </tr>
        <!--视频拼接-->
        <tr>
            <td rowspan=2>
                视频拼接
            </td>
            <td>
                普通视频拼接
            </td>
            <td>
                <a href="/document/product/266/7821">
                    ConcatVideo
                </a>
            </td>
			<td>
			</td>
        </tr>
        <tr>
            <td>
                HLS视频简单拼接
            </td>
            <td>
                <a href="/document/product/266/7820">
                    SimpleConcatHls
                </a>
            </td>
			<td>
			</td>
        </tr>
        <!--视频分类管理-->
        <tr>
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
			<td>
			</td>
        </tr>
        <tr>
            <td>
                获取视频分类层次结构
            </td>
            <td>
                <a href="/document/product/266/7813">
                    GetClassHierarchy
                </a>
            </td>
			<td>
                <a href="/document/product/266/7813">
                    DescribeAllClass
                </a>
			</td>
        </tr>
        <tr>
            <td>
                获取全部视频分类列表
            </td>
            <td>
                <a href="/document/product/266/7814">
                    GetAllClassInfo
                </a>
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
			<td>
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
			<td>
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
                <a href="/document/product/266/7818">
                    PullVodEvent
                </a>
            </td>
			<td>
			</td>
        </tr>
        <tr>
            <td>
                确认事件通知
            </td>
            <td>
                <a href="/document/product/266/7819">
                    ConfirmVodEvent
                </a>
            </td>
			<td>
			</td>
        </tr>
        <!--任务管理-->
        <!-- <tr>
        <td rowspan=1>任务管理</td>
        <td>查询异步任务的状态</td>
        <td><a href="">QueryVodTaskStatus</a></td></tr>
        -->
    </tbody>
</table>