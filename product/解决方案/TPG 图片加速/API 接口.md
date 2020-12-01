iOS、Android 以及 Windows 三种客户端的 SDK 均由 C 语言实现，下面对 SDK 的 API 接口进行详细说明。

## 解码器
### API 列表

<table>
<thead>
<tr>
<th>名称</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>TPGParseHeader</td>
<td>解析 TPG 码流头数据</td>
</tr>
<tr>
<td>TPGDecCreate</td>
<td>创建 TPG 解码器</td>
</tr>
<tr>
<td>TPGDecodeImage</td>
<td>解码 TPG 码流</td>
</tr>
<tr>
<td>TPGDecDestroy</td>
<td>销毁 TPG 解码器对象</td>
</tr>
<tr>
<td>TPGGetDelayTime</td>
<td>获取动态图片的显示延迟时间</td>
</tr>
<tr>
<td>TPGCanDecode</td>
<td>检测第 index 帧图像是否能解码</td>
</tr>
<tr>
<td>TPGGetAdditionalInfo</td>
<td>获取用户自定义数据，例如 EXIF 信息等</td>
</tr>
<tr>
<td>TPGDecGetVersion</td>
<td>获取解码器版本号</td>
</tr>
</tbody></table>

### TPGParseHeader
- 接口详情：`TPGStatusCode  TPGParseHeader(unsigned char* pData, int len, TPGFeatures* pFeatures);`
- 功能描述：解析 TPG 码流头文件。
- 参数说明：
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>pData</td>
<td>unsigned char*</td>
<td>需解码的 TPG 码流</td>
</tr>
<tr>
<td>len</td>
<td>int</td>
<td>TPG 文件长度</td>
</tr>
<tr>
<td>pFeatures</td>
<td>TPGFeatures*</td>
<td>输出 TPG 文件格式信息（文件头 length、width、height 等）</td>
</tr>
</tbody></table>
- 返回值：解码成功返回0（TPG_STATUS_OK），否则返回相应的错误码。
- 状态码说明：
<table>
<thead>
<tr>
<th align="left">TPGStatusCode 状态码</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">TPG_STATUS_OK</td>
<td>成功</td>
</tr>
<tr>
<td align="left">TPG_STATUS_OUT_OF_MEMORY</td>
<td>内存越界</td>
</tr>
<tr>
<td align="left">TPG_STATUS_INVALID_PARAM</td>
<td>参数无效</td>
</tr>
<tr>
<td align="left">TPG_STATUS_BITSTREAM_ERROR</td>
<td>比特流错误</td>
</tr>
<tr>
<td align="left">TPG_STATUS_UNSUPPORTED_FEATURE</td>
<td>无支持特征</td>
</tr>
<tr>
<td align="left">TPG_STATUS_SUSPENDED,</td>
<td>挂起</td>
</tr>
<tr>
<td align="left">TPG_STATUS_USER_ABORT</td>
<td>用户异常终止</td>
</tr>
<tr>
<td align="left">TPG_STATUS_NOT_ENOUGH_DATA</td>
<td>数据不足</td>
</tr>
<tr>
<td align="left">TPG_STATUS_INIT_ERROR</td>
<td>初始化错误</td>
</tr>
</tbody></table>


###  TPGDecCreate

- 接口详情：`void\*  TPGDecCreate(const unsigned char\* pData, int len);`
- 功能描述：创建 TPG 解码器。
- 参数说明：
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>pData</td>
<td>const unsigned char*</td>
<td>需解码的 TPG 码流</td>
</tr>
<tr>
<td>len</td>
<td>int</td>
<td>TPG 码流长度</td>
</tr>
</tbody></table>
- 返回值：TPG 解码器对象，创建不成功则返回 NULL。

### TPGDecodeImage
- 接口详情：`TPGStatusCode  TPGDecodeImage(void\* hDec, const unsigned char\* pData, int len, int index, TPGOutFrame \*pDecFrame);`
- 功能描述：解码一帧 TPG 图像。
- 参数说明：
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>hDec</td>
<td>void*</td>
<td>创建的 TPG 解码器对象</td>
</tr>
<tr>
<td>pData</td>
<td>const unsigned char*</td>
<td>需解码的 TPG 码流数据（从文件头开始）</td>
</tr>
<tr>
<td>len</td>
<td>int</td>
<td>TPG 文件长度（码流长度）</td>
</tr>
<tr>
<td>index</td>
<td>int</td>
<td>解码帧索引（静态图像该值为0；动态图像表示解码第 index 帧图像）</td>
</tr>
<tr>
<td>pDecFrame</td>
<td>TPGOutFrame*</td>
<td>解码输出帧数据</td>
</tr>
</tbody></table>
- 返回值说明：解码成功返回0（TPG_STATUS_OK），否则返回相应的错误码。

### TPGDecDestroy

- 接口详情：`void  TPGDecDestroy(void\* pDec);`
- 功能描述：销毁 TPG 解码器对象。
- 参数说明：
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>pDec</td>
<td>void*</td>
<td>TPG 解码器对象</td>
</tr>
</tbody></table>


### TPGGetDelayTime

- 接口详情：`TPGStatusCode  TPGGetDelayTime(void\* hDec, const unsigned char\* pData, int len, int index, int\* pDelayTime) ;`
- 功能描述：获取动态图片当前帧的显示延迟时间。
- 参数说明：
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>hDec</td>
<td>void*</td>
<td>TPG 解码器对象</td>
</tr>
<tr>
<td>pData</td>
<td>const unsigned char*</td>
<td>需解码的 TPG 码流数据（从文件头开始）</td>
</tr>
<tr>
<td>len</td>
<td>int</td>
<td>TPG 文件长度（码流长度）</td>
</tr>
<tr>
<td>index</td>
<td>int</td>
<td>解码帧索引（静态图像该值为 0；动态图像表示解码第 index 帧图像）</td>
</tr>
<tr>
<td>pDelayTime</td>
<td>int*</td>
<td>输出第index帧的延迟时间</td>
</tr>
</tbody></table>
- 返回值说明：解码成功返回0（TPG_STATUS_OK），否则返回相应的错误码。


###  TPGCanDecode

- 接口详情：`TPGStatusCode  TPGCanDecode(void\* pDec,  const unsigned char\* pData, int len, int index);`
- 功能描述：检测第 index 帧图像是否能够解码。
- 参数说明：
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>pDec</td>
<td>void*</td>
<td>TPG 解码器对象</td>
</tr>
<tr>
<td>pData</td>
<td>const unsigned char*</td>
<td>需解码的 TPG 码流数据（从文件头开始）</td>
</tr>
<tr>
<td>len</td>
<td>int</td>
<td>TPG 文件长度</td>
</tr>
<tr>
<td>index</td>
<td>int</td>
<td>解码帧索引（静态图像该值为0；动态图像表示解码第 index 帧图像）</td>
</tr>
</tbody></table>
- 返回值说明：当前帧可以解码返回0（TPG_STATUS_OK），否则返回相应的错误码。

###  TPGGetAdditionalInfo

- 接口详情：`TPGStatusCode  TPGGetAdditionalInfo(void\* hDec, const unsigned char\* pInData, int nInDatalen, int nIdentity, const unsigned char\*\* pOutData, int\* pOutDataLen) ;`
- 功能描述：获取用户自定义的辅助数据，例如 EXIF 信息等。
- 参数说明：
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>hDec</td>
<td>void*</td>
<td>TPG 解码器对象</td>
</tr>
<tr>
<td>pInData</td>
<td>const unsigned char*</td>
<td>需解码的 TPG 码流数据（从文件头开始）</td>
</tr>
<tr>
<td>nInDatalen</td>
<td>int</td>
<td>已下载数据长度（码流长度）</td>
</tr>
<tr>
<td>nIdentity</td>
<td>int</td>
<td>要获取数据的 ID 标识</td>
</tr>
<tr>
<td>pOutData</td>
<td>const unsigned char*</td>
<td>对应数据段的首地址，如果没有返回 NULL（不需要用户申请内存）</td>
</tr>
<tr>
<td>pOutDataLen</td>
<td>int</td>
<td>对应数据段的长度</td>
</tr>
</tbody></table>
- 返回值说明：获取成功返回0（TPG_STATUS_OK），否则返回相应的错误码。

### TPGDecGetVersion

- 接口详情：`int TPGDecGetVersion();`
- 功能描述：获取解码器版本号。
- 返回值：当前解码器的版本号。

## 编码器

### API 列表

| 名称           | 描述              |
| -------------- | ----------------- |
| TPGEncCreate   | 创建 TPG 编码器对象 |
| TPGEncodeImage | 对图片进行 TPG 编码 |
| TPGEncDestroy  | 销毁 TPG 编码器对象 |

### TPGEncCreate

- 接口详情：`void\*  TPGEncCreate(TPGEncInitParam\* pCreateParam);`
- 功能描述：创建 TPG 编码器对象。
- 参数说明：
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>pCreateParam</td>
<td>TPGEncInitParam*</td>
<td>编码器初始化参数</td>
</tr>
</tbody></table>
- 返回值：TPG 编码器对象。

### TPGEncodeImage

- 接口详情：`unsigned long long  TPGEncodeImage(void\* pEnc, TPGInFrame* pFrame, int* pQP, int nFrameIndex);`
- 功能描述：对图片进行 TPG 编码。
- 参数说明：
<table>
<thead>
<tr>
<th>参数</th>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>pEnc</td>
<td>void*</td>
<td>TPG 编码器对象</td>
</tr>
<tr>
<td>pFrame</td>
<td>TPGInFrame*</td>
<td>编码图片帧数据信息</td>
</tr>
<tr>
<td>pQP</td>
<td>int*</td>
<td>编码 QP</td>
</tr>
<tr>
<td>nFrameIndex</td>
<td>int</td>
<td>编码第 nFrameIndex 帧，静态图片该值为0</td>
</tr>
<tr>
<td>pDecFrame</td>
<td>TPGOutFrame*</td>
<td>解码输出帧数据</td>
</tr>
</tbody></table>
- 返回值说明：返回64位状态码。其中，高32位为 TPGStatusCode 状态值，低32位为编码后码流文件的长度。
