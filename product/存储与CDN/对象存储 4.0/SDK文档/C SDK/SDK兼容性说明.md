## 简介

为了提升 cos 的服务质量，cos 上线了新域名，并且区分了内网和公网域名，后续推荐使用新域名。同时，旧域名(cos.${region}.myqcloud.com)依然能提供服务。

- 新内网域名格式：cos-internal.${region}.tencentcos.cn
- 新公网域名格式：cos.${region}.tencentcos.cn

当您的 SDK 升级到 6.0.0 版本后，您会面临以下几种选择：

### 兼容之前的方式（代码中设置endpoint）
还是采用之前直接设置endpoint的方式，这里推荐修改为新域名格式，根据自己在内网还是公网环境来选择对应的域名

- 如果您在内网环境使用：
```cpp
cos_str_set(&options->config->endpoint, "cos-internal.${region}.tencentcos.cn");
```

- 如果您在公网环境使用：
```cpp
cos_str_set(&options->config->endpoint, "cos.${region}.tencentcos.cn");
```

### 代码中设置 region
不去设置endpoint，只需要指定region，sdk内部会拼接为默认的新内网域名格式：https://cos-internal.${region}.tencentcos.cn

如果需要其它域名格式，还有如下的参数可配置：
| 参数名称                  | 描述                          | 类型           |
| ------------------------ | ---------------------------- | -------------- |
| region                   | endpoint为空时有效，cos地域信息  | Int         |
| enable_old_domain        | endpoint为空时有效，设置为1采用myqcloud.com旧域名方式(此情况下disable_internal_domain值强制为1) | Int         |
| disable_internal_domain  | endpoint为空时有效，设置为1禁止内网新域名方式，采用公网域名 | Int         |
| use_http                 | endpoint为空时有效，设置为1采用http协议，0采用https协议 | Int         |

根据上述4个配置项可以按照您的场景来组合不同的域名格式。

- 如果您在内网环境使用：
```cpp
// https://cos-internal.${region}.tencentcos.cn
cos_str_set(&options->config->endpoint, "");
cos_str_set(&options->config->region, "${region}");
```

- 如果您在公网环境使用：
```cpp
// https://cos.${region}.tencentcos.cn
cos_str_set(&options->config->endpoint, "");
cos_str_set(&options->config->region, "${region}");
options->config->disable_internal_domain = 1;
```

- 如果您想使用旧域名：
```cpp
// https://cos.${region}.myqcloud.com
cos_str_set(&options->config->endpoint, "");
cos_str_set(&options->config->region, "${region}");
options->config->enable_old_domain = 1;
```