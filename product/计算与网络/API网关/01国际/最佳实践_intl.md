API gateway can be used to design your business as open APIs. To make it easy for your future use, it is recommended to follow the rules below when designing APIs:

1. Do not add a slash "/" at the end of the URI. An additional slash at the end of the URL of a resource can be easily misunderstood as a directory, causing errors in calling.

2. Use a dash "-" to improve the readability of the URI. Connect words using "-" so that the URI can be easily understood.

3. It is not allowed to use the underscore `"_"` in the URI, because the underscore "_" may be covered by the special effect of underscore in the text viewer and is less readable.

4. Avoid using uppercase letters which are not aesthetically pleasing and error-prone.

5. Do not include an extension in the URI. REST API client is recommended to use the format selection mechanism "Accept request header" provided by HTTP.

