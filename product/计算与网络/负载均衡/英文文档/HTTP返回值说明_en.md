HTTP Status Code is a three-digit code used to indicate the web server HTTP response status. It is defined by RFC 2616 and is extended by RFC 2518, RFC 2817, RFC 2295, RFC 2774, RFC 4918 and other specifications.

The first digit of the status code specifies one of five standard classes of responses.

1xx: Informational responses, indicating that the request has been received and needs to be processed further
2xx: Success responses, indicating that the action has been successfully received, understood and accepted
3xx: Redirection responses, indicating that in order to complete the specified action, further processing is required
4xx: Client errors, indicating that the client request contains syntax errors or cannot be executed correctly
5xx: Server errors, indicating that the server cannot execute a correct request correctly

Here are descriptions of common response return values:

100 - The client must continue to send the request
101 - The client requests the server to switch HTTP protocol versions as requested

200 - The transaction is successful
201 - Prompt that the URL of the new file has been known
202 - The request has been accepted for processing, but the processing has not been completed.
203 - The returned message is indefinite or incomplete
204 - The request has been received, but the returned message is empty
205 - The server has completed the request, but the user agent must reset the viewed files
206 - The server has completed part of the user's GET requests

300 - There are multiple options for the requested resource
301 - The request data was deleted
302 - The request data was found at other addresses
303 - The client is recommended to visit other URLs or use other access methods
304 - The client has executed a GET, but the file has not changed
305 - The requested resource must be obtained from the address specified by the server
306 - The code used in the previous version of HTTP is no longer used in the current version
307 - Declaring that the requested resource was temporarily deleted

400 - Bad request, such as syntax error
401 - The request authorization failed
402 - The valid ChargeTo header response is kept
403 - The request is forbidden
404 - No file, query, or URL was found
405 - The method defined by the user in the Request-Line field is not allowed
406 - The requested resource is not accessible according to the Accept header sent by the user
407 - Similar to 401, the user must be authorized first on the proxy server
408 - The client failed to complete the request within the time specified by the user
409 - The request cannot be completed in view of the current resource status
410 - This resource is no longer available on the server and there is no reference address
411 - The server rejects the user-defined Content-Length attribute request
412 - One or more request header fields are incorrect in the current request
413 - The requested resource is larger than the size allowed by the server
414 - The requested resource URL is longer than the length allowed by the server
415 - The format of the requested resource is not supported
416 - The request contains the Range request header field, but there is no range indication value within the current requested resource, and the request does not contain the If-Range request header field
417 - The server does not satisfy the expected value specified in the request Expect header field. if it is a proxy server, it's possible that the next level server cannot meet the request

500 - An internal server error occurred
501 - The requested function is not supported by the server
502 - The server is temporarily unavailable, sometimes to prevent system overload
503 - The server is overloaded or down for maintenance
504 - The gateway is overloaded, and the server uses another gateway or service to respond to the user, but the waiting time set is too long
505 - The server does not support or reject the HTTP version specified in the request header
