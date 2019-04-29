The frontend configurations of an API refer to the relevant configurations provided for external access, including the definition of request protocol, HTTP method, URL path and input parameters.

* Request protocol: API Gateway supports the http/https protocol, and three modes: http only, https only, and http + https.
* HTTP method: You can select GET, POST, PUT, DELETE, or HEAD.
* URL path: You can write a valid URL path as needed. If you need to configure a dynamic parameter in the path, use `{}` and enter the parameter name in it. For example, in the `/user/{userid}` path, the userid parameter is declared, which also needs to be defined as a Path type parameter in the input parameters. The Query parameter is not required to be defined in the URL path.
* Input parameter: The input parameters include the parameters from Header, Query and Path, where the Path parameter corresponds to the dynamic parameter defined in the URL path. The parameter name, parameter type and parameter data type should be specified for each parameter. You can also specify whether the fields are required, their default values, sample data and descriptions. With these configurations, API Gateway can help you complete the documentation and preliminary verification of input parameters. You can also add more verification configurations in more detail to the parameter as needed, such as the maximum/minimum values/lengths, enumerated values, or even regular expressions.
![Frontend Configuration](//mc.qcloudimg.com/static/img/6ed7547cf6003ccf61d7b61dbb5c0d8f/image.png)

