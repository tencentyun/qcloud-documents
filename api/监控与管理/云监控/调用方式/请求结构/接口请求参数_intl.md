API request parameters are specific to each API. This means that different APIs support different API request parameters. The first letter of each API request parameter is in lowercase so that the parameters can be differentiated from common request parameters.
Take API <a href="https://intl.cloud.tencent.com/document/api/248/7630" title="Get the List of Monitoring Metrics">Get the List of Monitoring Metrics</a> (DescribeMetrics) as an example. It supports the following API request parameters:
<table class="t"><tbody><tr>
<th><b>Parameter</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> namespace
<td> Yes
<td> String
<td>Namespace: A namespace refers to a category of resources. After specifying a namespace, you can obtain all types of monitoring metrics under the specified category of resource. Currently, this parameter can only be specified with "qce/cvm" and is used to get all types of monitoring metrics under the CVM.
<tr>
<td> metricName
<td> No 
<td> String
<td>Monitoring metric name, such as "cpu_usage" and "mem_usage", which should contain 1-64 characters. If it is not specified, the list of all the metrics under the namespace will be returned 
</tbody></table>

Here are the descriptions of each field:
<table class="t">
<tbody>
<td> Parameter Name
</td><td> Name of request parameter supported by the API. The user can use this name as an API request parameter when using this API.
</td></tr>
<tr>
<td> Required
</td><td> Indicates whether this parameter is required. "Yes" means the parameter is required for the API, while "No" means the parameter is not required.
</td></tr>
<tr>
<td> Type
</td><td> Data type of the API parameter.
</td></tr>
<tr>
<td> Description
</td><td> A brief description of the API request parameter.
</td></tr>
</tbody></table>

If a user wants to get the list of monitoring metrics, the request link may be as follows:

```
 https://monitor.api.qcloud.com/v2/index.php?
 &<Common request parameters>
&namespace=qce/cvm
```

A complete request needs two types of request parameters: common request parameters and API request parameters. Only API request parameters are listed here. For more information on common request parameters, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> section.
