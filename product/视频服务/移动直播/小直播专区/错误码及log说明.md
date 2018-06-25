## 业务服务器如何看log
 我们主要关心业务服务器的2种log：
- nginx的log：如果遇到http返回的错误码（如404，500等），请查看nginx的error级别的log，位于您的nginx安装目录/logs子目录下，一般是nginx、php或者mysql的配置问题
- 业务服务器代码里的log：如果请求能返回，但是回包的json里的code非200，表示该请求失败，请查看php代码所在目录/log目录下的文件，如果log目录不存在，请创建log目录，并添加可读写权限（建议执行chmod 777 开放所有权限）

## 终端如何看log
iOS端log存放路径：`Document/Caches/rtmpsdk_日期.log`
安卓端log存放路径：sdcrad下的`tencent/imsdklogs/com/tencent/qcloud/xiaozhibo/rtmpsdk_日期.log `

## 返回的错误码含义

| 错误码  | 具体含义 |
|---------|---------|
| 498 | 校验失败|
| 500 | 数据库操作失败，请确认数据库表已正确创建，更详细的错误请查看php代码所在目录/log目录下的mysql_errorxxx的log文件(xxx为错误发生日期)|
| 601 | 更新失败 |
| 602 | 参数错误|
| 610 | 用户名格式错误|
| 611 | 密码格式错误|
| 612 | 用户已存在|
| 621 | 密码错误|
| 620 | 用户不存在|

IM相关错误，请参考[云通信错误码](https://cloud.tencent.com/document/product/269/1671)
COS相关错误码（用于上传图片、封面），请参考[COS错误码](https://cloud.tencent.com/document/product/436/6281)