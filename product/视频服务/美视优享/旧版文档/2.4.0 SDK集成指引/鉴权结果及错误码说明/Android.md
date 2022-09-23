## Auth.AuthResult

授权返回结果实体类。

| 属性                                                | 含义                               |
| ------------------------------------------------- | ---------------------------------- |
| `public final boolean isSucceed;`                   | 是否授权成功                       |
| `public final AuthResultSucceed authResultSucceed;` | 授权成功详情                       |
| `public final AuthResultFail authResultFail;`       | 授权失败详情                       |
| `public final AuthInfo authInfo;`                   | 授权详情信息，一般供排查问题时使用 |


## Auth.AuthResultSucceed

授权成功详情实体类。

| 属性                                                | 含义                               |
| ------------------------------------------------------------ | -------------------------------------- |
| `public final Map<Integer, String> features = new HashMap<Integer, String>();` | 已授权的能力：`<能力ID, 能力名称> `    |
| `public final long endTime;`                                   | 授权结束时间, UNIX 时间戳, 单位是秒    |
| `public final String endTimeStr;`                              | 授权结束时间格式化后的字符串, 方便阅读 |


## Auth.AuthResultFail

授权失败详情实体类。

| 属性                                                | 含义                               |
| -------------------------- | ------------ |
| `public final int code;`   | 错误码       |
| `public final String msg;` | 错误提示信息 |


## 错误码
如果 ret 授权返回0，则已授权成功。否则请按照返回值来排查问题：

| 错误码    |     原因     |     处理建议     |
| --------- | --------- | --------- |
| 3004/3005 | 无效授权 | 检查授权文件的文件名/路径是否正确，比如 license 和 licence 的拼写方式是否统一 |
| 3015 | Bundle Id / Package Name 不匹配 | 检查您的 App 使用的 Bundle Id / Package Name 和申请的是否一致，检查是否使用了正确的授权文件 |
| 3018 | 授权文件已过期 | 需要向腾讯云申请续期 |
| 其他 | 内部错误 | 请将错误码上报给腾讯云支持团队处理 |

