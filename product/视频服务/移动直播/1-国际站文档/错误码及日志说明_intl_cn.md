## 业务服务器如何看log
 我们主要关心业务服务器的2种log：
- nginx的log：如果遇到http返回的错误码（如404，500等），请查看nginx的error级别的log，位于您的nginx安装目录/logs子目录下，一般是nginx、php或者mysql的配置问题
- 业务服务器代码里的log：如果请求能返回，但是回包的json里的returnValue非0，表示该请求失败，请查看php代码所在目录/log目录下的文件，如果log目录不存在，请创建log目录（老版本的代码没有默认创建目录），并添加可读写权限（建议执行chmod 777 开放所有权限）

## 终端如何看log
iOS端log存放路径：`Library/Caches/rtmpsdk_日期.log`
安卓端log存放路径：sdcrad下的`tencent/imsdklogs/com/tencent/qcloud/xiaozhibo/rtmpsdk_日期.log `

## 返回的错误码含义

| 错误码  | 具体含义 |
|---------|---------|
| 1000 | 请求包里的json格式合法，但是参数有误（一般是Action字段有误），请参考[业务后台协议格式](https://cloud.tencent.com/document/product/454/7895) 排查|
| 2003| 数据库操作失败，请确认数据库表已正确创建，您可以参考php代码里的createdb.sh创建数据库表，更详细的错误请查看php代码所在目录/log目录下的mysql_errorxxx的log文件(xxx为错误发生日期)|
| 4001| 请求包的json为空或者格式错误，请检查json格式，有很多在线的json格式检查工具可以帮助您排查，这种错误一般发生在您自行拼接json格式通过curl或者postman发起请求，如果您通过小直播发起请求，是不会发生这种错误，请注意区分|
| 4002| 请求包的部分参数取值非法，请参考[业务后台协议格式](https://cloud.tencent.com/document/product/454/7895) 排查|
| 4003| 优图核身功能超过每日的限制（目前每日限制100个用户体验）|
| 500| 这是http的错误码，可能是数据库配置错误，请查看您的nginx安装目录/logs子目录下的error级别的log，其他http的错误码也是查看该log|

注册登录及消息相关错误，请参考[云通信错误码](https://cloud.tencent.com/document/product/269/1671)
COS相关错误码（用于上传图片、封面），请参考[COS错误码](https://cloud.tencent.com/document/product/436/6281)
 
     
