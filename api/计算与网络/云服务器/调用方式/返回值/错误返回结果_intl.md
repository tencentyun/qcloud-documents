
If the call fails, the returned values are as follows:

<pre>
{
  "Response": {
    "Error": {
      "Code": "AuthFailure",
      "Message": "qcloud was not able to validate the provided access credentials"
    },
    "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
  }
}
</pre>

* The presence of Error means Tencent Cloud cannot process this request.
* Code indicates the specific error code. When an error occurs with the request, you can find the cause and solution in [Common Error Codes](/document/api/213/10146) and the error code list for the current API based on this error code.
* Message indicates the reason for the error, which may be changed or updated from time to time with the business growth or experience optimization. Therefore, you should not rely on this returned value.
* RequestId is used to uniquely identify an API request. If an API exception occurs, you can contact us and provide this ID to solve the problem.
