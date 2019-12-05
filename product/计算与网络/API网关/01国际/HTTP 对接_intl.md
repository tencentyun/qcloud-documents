The HTTP service to be integrated can be a Web service running on a CVM or a CCS, or a service on the public network.
To integrate with a specific HTTP service, the information such as the service address, the service path, HTTP method, timeout and mapping parameters must be provided.

**Service address:** The specific service server address, which can be an internal or an external address, in the format of IP+Port or domain name. For example: `http://10.186.51.24:8080` or `https://demo.test.com`.

**Service path:** The specific backend service request path. If you need to configure a dynamic parameter in the path, use `{}` and enter the parameter name in it. The parameter name will be configured in the parameter mapping configuration as an input parameter from the frontend configuration.

**HTTP method:** You can select GET, POST, PUT, DELETE or HEAD according to the specific method of your backend service. The HTTP method in the frontend configuration can be different from that in the backend configuration. HTTPS is supported.

**Timeout:** The timeout since the API gateway initiates a request until the backend service is called. The maximum value for the timeout is 30 seconds. When no response is returned before the timeout after the API gateway calls the backend service, the API gateway will end this call and return an error message.

**Mapping parameter:** Parameter mapping is to map the frontend input parameters to the parameters of the actual backend service. By default, the mapping parameter maps the input parameters with the same name and parameter location. And you can change way of mapping parameters as needed. For example, to map the input parameter from Path to the Query parameter in the backend service.

**Mapping parameter:** You can add custom constant parameters as needed, which will remain unchanged in each API call. You can use system parameters to pass some of the system information to the backend service.

**Mapping parameter:** If your body parameter is only in form format, you can map the parameter directly when configuring the frontend and backend parameters. If it is in JSON format, the API Gateway will pass it through directly.
![HTTP](https://main.qcloudimg.com/raw/b93201d1c5a20579cf34ae86c586533e.png)

>**Note:**
>To integrate VPC features, you need to apply for a whitelist first.

