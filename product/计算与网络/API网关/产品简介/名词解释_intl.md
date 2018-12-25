The following definitions can help you better understand the API gateway.

| Term | Description |
| ---      | --- |
| Service | Comprised of multiple associated APIs, it is used to provide the capabilities described by APIs. |
| API | A specific API description that contains basic information, frontend configuration, backend configuration, and response message.
| Environment | The target for service release. After the APIs in the service have been configured, they are released to a specified environment to provide external services. Existing environments include: test, pre-release, release. |
| Release | A process of exposing an API for external access. The object for release is service, which is subject to the current API configuration. After being released, API can be accessed from the public network. | 
| Frontend configuration | The configurations exposed to the public and provided for external access and use. |
| Backend configuration | The configurations for interfacing with actual backend services to provide specific capabilities. |
| Request method | HTTP method, including GET, POST, PUT, PATCH, DELETE, HEAD. |
| Parameter mapping | Changes from frontend parameters to backend parameters. |
| APIs for API gateway | Tencent Cloud APIs provided for managing various configurations in the API Gateway. |
