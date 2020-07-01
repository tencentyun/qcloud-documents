## URL Organization in the Background 
If the incoming request is `/release/apia/20171012/index.html`, the API with the path of `/apia/` is hit:
- If the backend path is an empty string, the URL transferred to the backend is `/apia/20171012/index.html`.
- If the backend path is `/endpoint/`, cut off `/apia/` and paste the rest behind the path in the backend, and then the URL becomes `/endpoint/20171012/index.html`.

## API Hit Priority 
- If the API path starts with "=", it has the highest priority, and exact match is used.
- If the API path starts with "^~", it has the second priority and cannot contain regular expressions. The prefix match is used.
- If the API path is a regular expression including path variables, it has the third priority.
- If the API path is a normal string, the longest string has the highest priority. The longest match is used.

## API Gateway Supports CORS 
When creating an API, if you select "Support CORS", then API Gateway supports cross-domain requests. The default configuration is as follows:

```
#define CORS_DEFAULT_AC_ALLOW_ORIGIN  ("*")

#define CORS_DEFAULT_AC_ALLOW_METHODS  ("GET,POST,PUT,DELETE,HEAD,OPTIONS,PATCH")

#define CORS_DEFAULT_AC_ALLOW_CREDENTIALS  ("true")

#define CORS_DEFAULT_AC_ALLOW_HEADERS  ("X-Api-ID,X-Service-RateLimit,X-UsagePlan-RateLimit,X-UsagePlan-Quota,Cache-   Control,Connection,Content-Disposition,Date,Keep-Alive,Pragma,Via,Accept,Accept-Charset,Accept-Encoding,Accept-Language,Authorization,Cookie,Expect,From,Host,If-Match,If-Modified-Since,If-None-Match,If-Range,If-Unmodified-Since,Range,Origin,Referer,User-Agent,X-Forwarded-For,X-Forwarded-Host,X-Forwarded-Proto,Accept-Range,Age,Content-Range,Content-Security-Policy,ETag,Expires,Last-Modified,Location,Server,Set-Cookie,Trailer,Transfer-Encoding,Vary,Allow,Content-Encoding,Content-Language,Content-Length,Content-Location,Content-Type")

#define CORS_DEFAULT_AC_EXPOSE_HEADERS  (CORS_DEFAULT_AC_ALLOW_HEADERS)

#define CORS_DEFAULT_AC_MAX_AGE  ("86400")
```

## API Request Failure 
After a user creates an API service, call failures often occur and the following prompt is returned:

{"message":"There is no api match uri[\/api\/v1\/tool\/123\/ico] host [service-asoj98o0-1251762227.ap-guangzhou.apigateway.myqcloud.com]"}

Check whether the API service has been published in an environment.
A created API can be called only after the service is published into the environment. If an API is modified, it won't take effect until the service is republished.

If a service is published in different environments, the default calling address must carry the environment name, such as:
`service-asoj98o0-1251762227.ap-guangzhou.apigateway.myqcloud.com/release/user path`



