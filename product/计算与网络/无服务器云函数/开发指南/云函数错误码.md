| 状态码 | 状态消息                        | 含义    |
| ------ | ------------------------------- | ---------------- |
| 200    | Success                         | 成功。             |
| 400    | InvalidParameterValue           | 无效请求。         |
| 401    | InvalidCredentials              | 认证失败。         |
| 403    | ResourceUnavailable             | 资源不可用。      |
| 404    | InvalidSubnetID                 | 无效子网 ID。     |
| 406    | RequestTooLarge                 | 请求 size 过大。     |
| 430    | User code exception caught      | 用户代码执行错误。 |
| 432    | ResourceLimitReached            | 资源超限。         |
| 433    | TimeLimitReached                | 函数执行超时。     |
| 434    | MemoryLimitReached              | 内存超限。         |
| 435    | FunctionNotFound                | 用户函数不存在。   |
| 436    | InvalidParameterValue           | 参数不合法。       |
| 437    | HandlerNotFount                 | 包加载错误。     |
| 438    | FunctionStatusError             | 函数关停。        |
| 439    | User preocess exit when running | 执行过程中退出。   |
| 441    | UnauthorizedOperation           | 鉴权不通过。       |
| 442    | QualifierNotFound               | 函数版本不存在。   |
| 500    | InternalError                   | 内部错误。         |
| 532    | ResourceExhausted               | 计算资源不足。     |
