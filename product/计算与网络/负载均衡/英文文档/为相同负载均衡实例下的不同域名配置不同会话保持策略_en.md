For example, your CLB has two domains: login.qcloud.com and img.qcloud.com. You hope that login.qcloud.com has session persistence and img.qcloud.com does not have session persistence. You can select "Cookie Stuffing" in the "Enable Session Persistence" configuration and configure it on the backend CVM.

If the backend CVM is a nginx one, enable ngx_http_upstream_session_sticky_module first. It is a CLB module and achieves session persistence between client and backend CVM through a cookie. Under certain conditions, it can ensure that the same client accesses the same backend CVM.

![](//mccdn.qcloud.com/static/img/300b92cca97bbe8fdbf3fd902cb9200e/image.png)

Configuration instructions:
- cookie is used to set the name of cookie that records a session 
- domain is used to set the domain to which the cookie is applied, and is left empty by default 
- path is used to set the URL to which the cookie is applied, and is left empty by default 
- maxage is used to set the lifetime of the cookie.If it is not set, it will default to session cookie, which means the cookie becomes invalid once the browser is closed
- mode is used to set the cookie mode.
insert: Directly insert the cookie with the specified name through Set-Cookie header. 
prefix: No new cookie will be generated, but a specific prefix will be added before the cookie value in the response. When the browser sends a request again with the cookie containing the specific identifier, the module deletes the prefix before sending it to the backend CVM so that the backend CVM gets the original cookie value. These actions are visible to the backend.
rewrite:  Use the server identifier to overwrite the cookie set for session persistence in the backend. If the cookie is not set in the response header for he backend CVM, it is considered that the request does not need session persistence. Under this mode, the backend CVM can control which requests need session persistence and which ones do not.
- option is used to set the option for the cookie for session persistence and can be set to indirect or direct. If it is set to indirect, the cookie will not be sent to the backend CVM, and is completely visible to backend applications. The option direct is contrary to indirect. 
- maxidle is used to set the maximum idle timeout of session cookie 
- maxlife is used to set the maximum lifetime of the session cookie 
- fallback is used to set whether to try other machines when the backend CVM with session persistence is down 
- hash is used to set whether clear text or md5 is used for the server identifier in cookie. Ddefault is md5.
