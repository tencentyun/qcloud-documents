## 简介

本文档提供关于媒体截图接口的 API 概览和 SDK 示例代码。

| API                        |             操作名                     | 操作描述                                               |
| ------------------------------------------------------------ | --------------------------|---------------------------- |
| [GetSnapshot](https://cloud.tencent.com/document/product/436/55671) | 查询截图	 | 用于查询媒体文件在某个时间的截图 |


## 查询截图

#### 功能说明

用于查询媒体文件在某个时间的截图。

>! COS Go SDK 版本需要大于等于 v0.7.32。

#### 方法原型

```go
func (s *CIService) GetSnapshot(ctx context.Context, name string, opt *GetSnapshotOptions, id ...string) (*Response, error)
```

#### 请求示例
```go
opt := &cos.GetSnapshotOptions{
	Time: 1,
} 
resp, err := c.CI.GetSnapshot(context.Background(), "test.mp4", opt)
if err != nil {
    // ERROR
}
  
fd, err := os.OpenFile("test.jpg", os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0660)
if err != nil {
    // ERROR
} 
_, err = io.Copy(fd, resp.Body)
fd.Close()
```

#### 参数说明

```go
type GetSnapshotOptions struct {
    Time   float32 
    Height int 
    Width  int  
    Format string
    Rotate string
    Mode   string
}
```

| 参数名称 | 参数描述                                                     | 是否必填 | 类型   |
| ------- | ----------------------------------------------------------- | ------- | ----- |
| name     | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名`examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg`中，对象键为 doc/pic.jpg | 是       | name   |
| opt      | 截图参数       | 否       | struct |
| id        | 针对版本控制的对象 VersionId | 否 | String  |
| Time   | 截图的时间点，单位为秒        | 是       | float  |
| Width | 截图的宽。默认为0         | 否       | Int    |
| Height | 截图的高。默认为0 当 width 和 height 都为0时，表示使用视频的宽高；如果单个为0，则以另外一个值按视频宽高比例自动适应 | 否       | Int    |
| Format | 截图的格式，支持 jpg 和 png，默认 jpg    | 否     | String |
| Rotate | 图片旋转方式 auto：按视频旋转信息进行自动旋转off：不旋转默认值为 auto | 否       | String |
| Mode   | 截帧方式 keyframe：截取指定时间点之前的最近的一个关键帧exactframe：截取指定时间点的帧默认值为 exactframe | 否       | String |

#### 返回结果说明

| 参数名称 | 参数描述                                                     | 是否必填 | 类型   |
| ------- | ----------------------------------------------------------- | ------- | ----- |
| Response     | http响应  | 是       | Struct  |
| Response.Header     | http响应头部  | 是       | Struct  |
| Response.Body     | http响应数据  | 是       | Struct  |
