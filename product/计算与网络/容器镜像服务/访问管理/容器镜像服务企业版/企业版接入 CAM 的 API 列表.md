### 实例管理相关接口
| API 名                 | API 描述          | 资源类型 | 资源六段式示例                                                                           |
| :--------------------- | :--------------- | :------- | :--------------------------------------------------------------------------------------- |
| CreateInstance         | 创建实例         | instance | `qcs::tcr:$region:$account:instance/$instanceid`                                         |
| DescribeInstances      | 查询实例信息     | instance | `qcs::tcr:$region:$account:instance/*`  `qcs::tcr:$region:$account:instance/$instanceid` |
| DescribeInstanceStatus | 查询实例状态     | instance | `qcs::tcr:$region:$account:instance/$instanceid`                                         |
| CreateInstanceToken    | 获取临时登陆密码 | instance | `qcs::tcr:$region:$account:instance/$instanceid`                                         |