API request parameters are specific to each API. Different APIs support different API request parameters. The first letter of each API request parameter is in lowercase so that the parameters can be differentiated from common request parameters.
Take API <a href="/doc/api/255/创建命名空间" title="Create Namespace">Create Namespace</a> (CreateNamespace) as an example. It supports the following API request parameters:
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> namespace
<td> Yes
<td> String
<td>Namespace: It contains 32 characters, including letters, numbers and underscores
</tbody></table>

The above field is described below:
<table class="t">
<tbody>
<td> Parameter Name
</td><td> Name of request parameter supported by the API. The user can use this name as an API request parameter when using this API.
</td></tr>
<tr>
<td> Required
</td><td> Indicate whether this parameter is required. "Yes" means the parameter is required when you call the API. "No" means the parameter is not required. All the API request parameters are required in the API "Create Namespace" (CreateNamespace).
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

If a user wants to create a namespace, the request link may be as follows:

```
 https://monitor.api.qcloud.com/v2/index.php?
 &<Common request parameters>
&namespace=name1
```

A complete request requires two types of request parameters: common request parameters and API request parameters. Only API request parameters are listed above. For more information on common request parameters, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> section.
