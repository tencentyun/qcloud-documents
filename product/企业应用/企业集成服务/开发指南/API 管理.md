## 使用场景
各大企业每天都有大量的 API 增长，同时越来越多公司开始公开 Web API，API 的使用场景正在累积。日前，每日 API 调用量不断飙升，如何能够安全有效管理 API 对于企业而言并不容易。 

企业集成服务提供 API 发布功能，可以一键将已发布的应用打包生成 API，方便用户进行管理和调用；同时提供 API 管理能力，可以针对 API 进行访问权限管控和流量调度。页面内可以进行 API 的创建和查看工作，API 列表中展示有 API 名称、协议、接口数、创建时间和特殊操作等内容。如下图：
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/eis/54.png)  

## 操作步骤
### 步骤1：创建 API
API 管理功能支持 3.0.0 版本的 OpenAPI 规范。登录 [企业集成服务控制台](https://console.cloud.tencent.com/eis)，选择**深度集成 > API 管理**，选择对应项目名称后单击**创建 API** 进入 API 创建界面。当前支持两种创建模式，用户可以选择手动编辑一个 API 描述文件，也可以上传填写好的 JSON 或者 YAML 文件进行 API 的生成，按照页面提示全部填写完成并且内容校验通过后，单击**下一步**即可进入 API 的管理详情配置界面。
>?
- OpenAPI 3.0.0 规范的对象定义请参考 [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md)。
- 如果您需要更多帮助，如获取 API 描述文档样例文件，请参考 [API 描述文件样例](#sample)。
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/eis/55.png)  

### 步骤2：API 管理配置
企业集成服务会根据用户上传或者填写的 API 描述文件内容生成对应的 API，在此页面中，将会基于描述文件展示 API 的基本信息，包括 API 名称、API 版本和 API ID。此外，用户可以进行 API 绑定行为，用户可以从该项目中**有权限**且**拥有 HTTP Listener** 的应用中进行选择（如果所选应用没有正在运行的 HTTP Listener，则无法正确生成 API），从而将此应用与 API 进行绑定，绑定后用户即可通过调用此 API 来访问应用的服务。
>!只有激活状态的 API 可以成功访问对应的应用服务。 

- API 状态：企业集成服务会根据 API 绑定的应用状态来判断 API 的状态，当前支持的状态有：
  - 已激活：若已经成功绑定正在运行的应用，则此 API 为已激活状态。
  - 未激活：若绑定的应用为非发布状态或者未绑定任何应用，则此 API 为未激活状态。  
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/eis/56.png)  
- API 控制策略：企业集成服务允许用户对所发布的 API 的访问权限进行配置。当前版本仅支持 Basic Auth（账户密码模式），其他验证方式敬请关注！
 ![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/eis/57.png)  

### 步骤3：使用 API 
1. 当 API 配置完成后，您即可通过 API 进行应用的控制和管理。打开绑定 API 的应用及其具体的流，通过流中 trigger 上的“复制域名”方式即可获取 API 的请求地址；或者在流左侧边栏“连接器配置”中找到对应的请求配置，并复制请求地址。地址构成方式一般为："HTTP Listener 监听端口"-"HTTP Listener 监听路径".ipaas.ap-"环境".mycloud.com/。
>!同应用下不同的流则会拥有不同 HTTP Listener 监听端口和监听路径，请在使用 API 服务时注意区分，避免调用不正确的服务。

2. 获取请求地址后，通过该地址以及配置好的 Basic Auth 的账号密码（如有）即可访问，此处以绑定 helloworld 模板为例：
 - 复制触发链接地址：
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/eis/58.png)  
 - 配置 API 后增加身份校验：
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/eis/58.1.png) 
>!您在此过程中所使用的请求参数会作为被绑定的流的入参使用，如果正在使用的是正式环境中的 API 服务，请谨慎使用避免对生产数据造成影响。
 - [API 描述文件样例](id:sample)：
```plaintext
`{
    "openapi": "3.0.0",
    "info": {
        "title": "Simple API overview1",
        "version": "2.0.0",
        "description": "test desc"
    },
    "paths": {
        "/": {
            "get": {
                "description": "get desc",
                "operationId": "listVersionsv2",
                "summary": "List API versions",
                "responses": {
                    "200": {
                        "description": "200 response",
                        "content": {
                            "application/json": {
                                "examples": {
                                    "foo": {
                                        "value": {
                                            "versions": [
                                                {
                                                    "status": "CURRENT",
                                                    "updated": "2011-01-21T11:33:21Z",
                                                    "id": "v2.0",
                                                    "links": [
                                                        {
                                                            "href": "http://127.0.0.1:8774/v2/",
                                                            "rel": "self"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "status": "EXPERIMENTAL",
                                                    "updated": "2013-07-23T11:33:21Z",
                                                    "id": "v3.0",
                                                    "links": [
                                                        {
                                                            "href": "http://127.0.0.1:8774/v3/",
                                                            "rel": "self"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "300": {
                        "description": "300 response",
                        "content": {
                            "application/json": {
                                "examples": {
                                    "foo": {
                                        "value": "{\n \"versions\": [\n       {\n         \"status\": \"CURRENT\",\n         \"updated\": \"2011-01-21T11:33:21Z\",\n         \"id\": \"v2.0\",\n         \"links\": [\n             {\n                 \"href\": \"http://127.0.0.1:8774/v2/\",\n                 \"rel\": \"self\"\n             }\n         ]\n     },\n     {\n         \"status\": \"EXPERIMENTAL\",\n         \"updated\": \"2013-07-23T11:33:21Z\",\n         \"id\": \"v3.0\",\n         \"links\": [\n             {\n                 \"href\": \"http://127.0.0.1:8774/v3/\",\n                 \"rel\": \"self\"\n             }\n         ]\n     }\n ]\n}\n"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/v2": {
            "get": {
                "description": "get v2 desc",
                "operationId": "getVersionDetailsv2",
                "summary": "Show API version details",
                "responses": {
                    "200": {
                        "description": "200 response",
                        "content": {
                            "application/json": {
                                "examples": {
                                    "foo": {
                                        "value": {
                                            "version": {
                                                "status": "CURRENT",
                                                "updated": "2011-01-21T11:33:21Z",
                                                "media-types": [
                                                    {
                                                        "base": "application/xml",
                                                        "type": "application/vnd.openstack.compute+xml;version=2"
                                                    },
                                                    {
                                                        "base": "application/json",
                                                        "type": "application/vnd.openstack.compute+json;version=2"
                                                    }
                                                ],
                                                "id": "v2.0",
                                                "links": [
                                                    {
                                                        "href": "http://127.0.0.1:8774/v2/",
                                                        "rel": "self"
                                                    },
                                                    {
                                                        "href": "http://docs.openstack.org/api/openstack-compute/2/os-compute-devguide-2.pdf",
                                                        "type": "application/pdf",
                                                        "rel": "describedby"
                                                    },
                                                    {
                                                        "href": "http://docs.openstack.org/api/openstack-compute/2/wadl/os-compute-2.wadl",
                                                        "type": "application/vnd.sun.wadl+xml",
                                                        "rel": "describedby"
                                                    },
                                                    {
                                                        "href": "http://docs.openstack.org/api/openstack-compute/2/wadl/os-compute-2.wadl",
                                                        "type": "application/vnd.sun.wadl+xml",
                                                        "rel": "describedby"
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "203": {
                        "description": "203 response",
                        "content": {
                            "application/json": {
                                "examples": {
                                    "foo": {
                                        "value": {
                                            "version": {
                                                "status": "CURRENT",
                                                "updated": "2011-01-21T11:33:21Z",
                                                "media-types": [
                                                    {
                                                        "base": "application/xml",
                                                        "type": "application/vnd.openstack.compute+xml;version=2"
                                                    },
                                                    {
                                                        "base": "application/json",
                                                        "type": "application/vnd.openstack.compute+json;version=2"
                                                    }
                                                ],
                                                "id": "v2.0",
                                                "links": [
                                                    {
                                                        "href": "http://23.253.228.211:8774/v2/",
                                                        "rel": "self"
                                                    },
                                                    {
                                                        "href": "http://docs.openstack.org/api/openstack-compute/2/os-compute-devguide-2.pdf",
                                                        "type": "application/pdf",
                                                        "rel": "describedby"
                                                    },
                                                    {
                                                        "href": "http://docs.openstack.org/api/openstack-compute/2/wadl/os-compute-2.wadl",
                                                        "type": "application/vnd.sun.wadl+xml",
                                                        "rel": "describedby"
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}`
```
