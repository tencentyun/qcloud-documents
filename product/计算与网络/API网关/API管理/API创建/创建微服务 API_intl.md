After entering the service, you can create a generic API or a microservice API according to your backend service type. If the backend service is implemented in TSF, select the Microservice API tab, and click **New**:
![](https://main.qcloudimg.com/raw/914798c521505d7350fa2282bc75ecb8.png)

## Frontend Configuration

As shown in the following figure, for the frontend configuration required to configure the microservice API, you need to select the microservices to be integrated to the backend and the cluster and namespace of these microservices. The API publisher can integrate multiple microservices in one API.

**HTTP method**: You can select GET, POST, PUT, DELETE, PATCH or HEAD.

**URL path**: You can write a valid URL path as needed. If you need to configure a dynamic parameter in the path, use `{}` and enter the parameter name in it. For example, in the `/user/{userid}` path, the userid parameter is declared, which also needs to be defined as a Path type parameter in the input parameters. The Query parameter is not required to be defined in the URL path.

**Input parameter**: The input parameters include the parameters from Header, Query and Path, where the Path parameter corresponds to the dynamic parameter defined in the URL path. The parameter name, parameter type and parameter data type should be specified for each parameter. You can also specify whether the fields are required, their default values, sample data and descriptions. With these configurations, API Gateway can help you complete the documentation and preliminary verification of input parameters. You can also add more verification configurations in more detail to the parameter as needed, such as the maximum/minimum values/lengths, enumerated values, or even regular expressions.
When the API is called, two required parameters (X-NameSpace-Code and X-MicroService-Name) must be passed in to inform the API Gateway of the microservice to which this request is sent. These two parameters can be placed in header, path or query. If they are placed in path, the path parameter must be configured in the path, just like that in the generic API. Apart from these two fixed parameters, other parameters are configured in the same way with those for generic APIs.
![](https://main.qcloudimg.com/raw/58d61ef247203e8826943b0f965b476b.png)

## Backend Configuration

**Backend request path:** The specific backend service request path. If you need to configure a dynamic parameter in the path, use `{}` and enter the parameter name in it. The parameter name will be configured in the parameter mapping configuration as an input parameter from the frontend configuration. Different from the one in the frontend service, this path is used for path mapping, and it is the actual request path.

**Timeout**: The timeout since the API gateway initiates a request until the backend service is called. The maximum value for the timeout is 30 seconds. When no response is returned before the timeout after the API gateway calls the backend service, the API gateway will end this call and return an error message.

**Backend parameters**: Both X-NameSpace-Code and X-MicroService-Name are fixed parameters and cannot be used for mapping. Other parameters you configured can be used for mapping.

**Mapping parameter:** Parameter mapping is to map the frontend input parameters to the parameters of the actual backend service. By default, the mapping parameter maps the input parameters with the same name and parameter location. And you can change way of mapping parameters as needed. For example, to map the input parameter from Path to the Query parameter in the backend service.

**Mapping parameter:** You can add custom constant parameters as needed, which will remain unchanged in each API call. You can use system parameters to pass some of the system information to the backend service.

**Mapping parameter:** If your body parameter is only in form format, you can map the parameter directly when configuring the frontend and backend parameters. If it is in JSON format, the API Gateway will pass it through directly.

![](https://main.qcloudimg.com/raw/84b525b8b150995def8c2b64cb3489ad.png)

## Response Result

API response configuration includes the configuration of API response data and that of API error codes.
API response data configuration is used to indicate the type of returned data, including data examples of successful and failed calls.
API error code definition is used to indicate additional error codes, error messages and descriptions.
![](https://main.qcloudimg.com/raw/edcbca70d8c41ab625fdac18cda9c8f4.png)
Response result configuration is only used to generate documentation.



