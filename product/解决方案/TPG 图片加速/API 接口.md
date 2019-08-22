iOS、Android 以及 Windows 三种客户端的 SDK 均由 C 语言实现，下面对 SDK 的 API 接口进行详细说明。

## 解码器

### API 列表

| 名称                 | 描述                               |
| -------------------- | ---------------------------------- |
| TPGParseHeader       | 解析 TPG 码流头数据                  |
| TPGDecCreate         | 创建 TPG 解码器                      |
| TPGDecodeImage       | 解码 TPG 码流                        |
| TPGDecDestroy        | 销毁 TPG 解码器对象                  |
| TPGGetDelayTime      | 获取动态图片的显示延迟时间         |
| TPGCanDecode         | 检测第 index 帧图像是否能解码        |
| TPGGetAdditionalInfo | 获取用户自定义数据，例如 EXIF 信息等 |
| TPGDecGetVersion     | 获取解码器版本号                   |



### TPGParseHeader

接口详情：TPGStatusCode  TPGParseHeader(unsigned char* pData, int len, TPGFeatures* pFeatures);

功能描述：解析 TPG 码流头文件

参数说明：

| 参数      | 类型           | 说明                                                 |
| --------- | -------------- | ---------------------------------------------------- |
| pData     | unsigned char\* | 需解码的 TPG 码流                                      |
| len       | int            | TPG 文件长度                                          |
| pFeatures | TPGFeatures\*   | 输出 TPG 文件格式信息（文件头 length、width、height 等） |

返回值：解码成功返回0（TPG_STATUS_OK），否则返回相应的错误码

状态码说明：

| TPGStatusCode 状态码           | 说明         |
| :----------------------------- | ------------ |
| TPG_STATUS_OK                  | 成功         |
| TPG_STATUS_OUT_OF_MEMORY       | 内存越界     |
| TPG_STATUS_INVALID_PARAM       | 参数无效     |
| TPG_STATUS_BITSTREAM_ERROR     | 比特流错误   |
| TPG_STATUS_UNSUPPORTED_FEATURE | 无支持特征   |
| TPG_STATUS_SUSPENDED,          | 挂起         |
| TPG_STATUS_USER_ABORT          | 用户异常终止 |
| TPG_STATUS_NOT_ENOUGH_DATA     | 数据不足     |
| TPG_STATUS_INIT_ERROR          | 初始化错误   |

###  TPGDecCreate

接口详情：void\*  TPGDecCreate(const unsigned char\* pData, int len);

功能描述：创建 TPG 解码器

参数说明：

| 参数  | 类型                 | 说明            |
| ----- | -------------------- | --------------- |
| pData | const unsigned char\* | 需解码的 TPG 码流 |
| len   | int                  | TPG 码流长度     |

返回值：TPG 解码器对象，创建不成功则返回 NULL。

### TPGDecodeImage
接口详情：TPGStatusCode  TPGDecodeImage(void\* hDec, const unsigned char\* pData, int len, int index, TPGOutFrame \*pDecFrame);

功能描述：解码一帧 TPG 图像

参数说明：

| 参数      | 类型                 | 说明                                                         |
| --------- | -------------------- | ------------------------------------------------------------ |
| hDec      | void\*                | 创建的 TPG 解码器对象                                          |
| pData     | const unsigned char\* | 需解码的TPG码流数据（从文件头开始）                          |
| len       | int                  | TPG文件长度（码流长度）                                      |
| index     | int                | 解码帧索引（静态图像该值为0；动态图像表示解码第 index 帧图像） |
| pDecFrame | TPGOutFrame\*         | 解码输出帧数据                                               |

返回值说明：解码成功返回0（TPG_STATUS_OK），否则返回相应的错误码。

### TPGDecDestroy

接口详情：void  TPGDecDestroy(void\* pDec);

功能描述：销毁 TPG 解码器对象。

参数说明：

| 参数 | 类型  | 说明          |
| ---- | ----- | ------------- |
| pDec | void\* | TPG 解码器对象 |



### TPGGetDelayTime

接口详情：TPGStatusCode  TPGGetDelayTime(void\* hDec, const unsigned char\* pData, int len, int index, int\* pDelayTime) ;

功能描述：获取动态图片当前帧的显示延迟时间。

参数说明：

| 参数       | 类型                 | 说明                                                         |
| ---------- | -------------------- | ------------------------------------------------------------ |
| hDec       | void\*                | TPG 解码器对象                                                |
| pData      | const unsigned char\* | 需解码的 TPG 码流数据（从文件头开始）                          |
| len        | int                | TPG 文件长度（码流长度）                                      |
| index      | int             | 解码帧索引（静态图像该值为 0；动态图像表示解码第 index 帧图像） |
| pDelayTime | int\*             | 输出第index帧的延迟时间                                      |

返回值说明：解码成功返回0（TPG_STATUS_OK），否则返回相应的错误码。



###  TPGCanDecode

接口详情：TPGStatusCode  TPGCanDecode(void\* pDec,  const unsigned char\* pData, int len, int index);

功能描述：检测第 index 帧图像是否能够解码

参数说明：

| 参数  | 类型                 | 说明                                                         |
| ----- | -------------------- | ------------------------------------------------------------ |
| pDec  | void\*                | TPG 解码器对象                                                |
| pData | const unsigned char\* | 需解码的 TPG 码流数据（从文件头开始）                          |
| len   | int                  | TPG 文件长度                                                  |
| index | int                | 解码帧索引（静态图像该值为0；动态图像表示解码第 index 帧图像） |

返回值说明：当前帧可以解码返回0（TPG_STATUS_OK），否则返回相应的错误码。



###  TPGGetAdditionalInfo

接口详情：TPGStatusCode  TPGGetAdditionalInfo(void\* hDec, const unsigned char\* pInData, int nInDatalen, int nIdentity, const unsigned char\*\* pOutData, int\* pOutDataLen) ;

功能描述：获取用户自定义的辅助数据，例如 EXIF 信息等。

参数说明：

| 参数        | 类型                 | 说明                                                       |
| ----------- | -------------------- | ---------------------------------------------------------- |
| hDec        | void\*                | TPG 解码器对象                                              |
| pInData     | const unsigned char\* | 需解码的 TPG 码流数据（从文件头开始）     |
| nInDatalen  | int                  | 已下载数据长度（码流长度）                                 |
| nIdentity   | int                  | 要获取数据的 ID 标识                                         |
| pOutData    | const unsigned char\* | 对应数据段的首地址，如果没有返回 NULL（不需要用户申请内存） |
| pOutDataLen | int                  | 对应数据段的长度                                           |

返回值说明：获取成功返回0（TPG_STATUS_OK），否则返回相应的错误码。

### TPGDecGetVersion

接口详情：int  TPGDecGetVersion();

功能描述：获取解码器版本号。

返回值：当前解码器的版本号。

## 编码器

### API 列表

| 名称           | 描述              |
| -------------- | ----------------- |
| TPGEncCreate   | 创建 TPG 编码器对象 |
| TPGEncodeImage | 对图片进行 TPG 编码 |
| TPGEncDestroy  | 销毁 TPG 编码器对象 |

### TPGEncCreate

接口详情：void\*  TPGEncCreate(TPGEncInitParam\* pCreateParam);

功能描述：创建 TPG 编码器对象。

参数说明：

| 参数         | 类型             | 说明             |
| ------------ | ---------------- | ---------------- |
| pCreateParam | TPGEncInitParam\* | 编码器初始化参数 |

返回值：TPG 编码器对象。

### TPGEncodeImage

接口详情：unsigned long long  TPGEncodeImage(void\* pEnc, TPGInFrame* pFrame, int* pQP, int nFrameIndex);

功能描述：对图片进行 TPG 编码。

参数说明：

| 参数        | 类型         | 说明                                   |
| ----------- | ------------ | -------------------------------------- |
| pEnc        | void\*        | TPG 编码器对象                          |
| pFrame      | TPGInFrame\*  | 编码图片帧数据信息                     |
| pQP         | int\*         | 编码 QP                                 |
| nFrameIndex | int          | 编码第 nFrameIndex 帧，静态图片该值为0 |
| pDecFrame   | TPGOutFrame\* | 解码输出帧数据                         |

返回值说明：返回64位状态码。其中，高32位为 TPGStatusCode 状态值，低32位为编码后码流文件的长度。
