TSF 框架在微服务注册时，会自动收集并注册微服务提供的 API 接口，用户可通过 TSF 控制台实时掌握当前微服务提供的 API 情况。API 注册功能基于 [OpenApi Specification 3.0](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md) 规范注册 API 元数据信息。 用户在查看 API 接口的同时，可查看到 API 出入参数据结构信息。

## 准备工作

开始实践 API 注册功能前，请确保已完成了 [SDK 下载](https://cloud.tencent.com/document/product/649/20231)。

## 添加依赖

向工程中添加 `spring-cloud-tsf-starter` 依赖并开启 `@EnableTsf` 注解，详情请参考 [快速入门](https://cloud.tencent.com/document/product/649/20261) 文档。

>!如果您使用的是 1.15.0-Edgware-RELEASE/1.15.0-Finchley-RELEASE 及之前的版本，使用方法参考 [Spring Cloud SDK 历史版本使用方法](https://cloud.tencent.com/document/product/649/45864)。

## 配置选项

API 注册功能基于 Swagger 原生规范实现，提供多个配置以适配 Swagger 不同配置应用场景，可用配置如下表所示：

| 配置项                  | 类型    | 必填 | 默认值                          | 说明                                                         |
| :---------------------- | :------ | :--- | :------------------------------ | :----------------------------------------------------------- |
| tsf.swagger.enabled     | Boolean | 否   | true                            | 是否开启 TSF API 注册功能                                    |
| tsf.swagger.basePackage | String  | 否   | ApplicationMainClass 所在包路径 | 注册 API 的扫描包路径。 推荐将 ApplicationMainClass 写在外层 Package |
| tsf.swagger.excludePath | String  | 否   | （空）                          | 排除扫描的包路径                                             |
| tsf.swagger.group       | String  | 否   | default                         | swagger docket 分组                                          |

## 代码和示例
- SDK 会自动扫描 API 的 path 和 出入参。
- 如果需要上报 API 的描述，需要`import io.swagger.annotations.ApiOperation;` ，同时在 API 上加上注解 `@ApiOperation(value = "url路径值",notes = "对api资源的描述")`。如果不关注 API 描述，可以不设置 @ApiOperation。

```java
package com.tsf.demo.provider.controller;
// 省略掉部分 import
import io.swagger.annotations.ApiOperation;
import com.tsf.demo.provider.config.ProviderNameConfig;

@RestController
public class ProviderController {
    private static final Logger LOG = LoggerFactory.getLogger(ProviderController.class);

    @Autowired
    private ProviderNameConfig providerNameConfig;
    @ApiOperation(value= "/echo/{param}", notes = "notes") // notes 对应 API 描述
    @RequestMapping(value = "/echo/{param}", method = RequestMethod.GET)
    public String echo(@PathVariable String param) {
        LOG.info("provider-demo -- request param: [" + param + "]");
        String result = "request param: " + param + ", response from " + providerNameConfig.getName();
        LOG.info("provider-demo -- provider config name: [" + providerNameConfig.getName() + ']');
        LOG.info("provider-demo -- response info: [" + result + "]");
        return result;
    }
}
```
