## 通过命令行或 Filebeat 等客户端使用
<table>
<tr>
        <th width=30%>API uri</th>
        <th width=30%>适用 Method</th>
        <th width=40%>作用描述</th>
    </tr>
    <tr>
        <td >/_bulk</td>
        <td >"PUT", "POST"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html">Bulk API</a></td>
 </tr>
 <tr>
        <td >/{index}/_bulk</td>
        <td >"PUT", "POST"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html">Bulk API</a></td>
    </tr>
     <tr>
        <td >/{index}/_doc/{id}</td>
        <td >"PUT", "POST"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html">Index API</a></td>
    </tr>
     <tr>
        <td >/{index}/_doc</td>
        <td >"POST"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html">Index API</a></td>
    </tr>
     <tr>
        <td >/{index}/_create/{id}</td>
        <td >"PUT", "POST"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html">Index API</a></td>
    </tr>
     <tr>
        <td >/{index}/_mapping</td>
        <td >"GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-get-mapping.html">Get mapping API</a></td>
    </tr>
     <tr>
        <td >/{index}/_msearch</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/search-multi-search.html">Multi search API</a></td>
    </tr>
     <tr>
        <td >/_msearch</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/search-multi-search.html">Multi search API</a></td>
    </tr>
     <tr>
        <td >/{index}/_count</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/search-count.html">Count API</a></td>
    </tr>
     <tr>
        <td >/{index}/_search</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html">Search API</a></td>
    </tr>
 </table>

 ## 通过 Kibana 使用
<table>
<tr>
        <th width=30%>API uri</th>
        <th width=30%>适用 Method</th>
        <th width=40%>作用描述</th>
    </tr>
    <tr>
        <td >/{index}/_bulk</td>
        <td >"PUT", "POST"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html">Bulk API</a></td>
 </tr>
 <tr>
        <td >/{index}/_doc/{id}</td>
        <td >"PUT", "POST"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html">Index API</a></td>
    </tr>
     <tr>
        <td >/{index}/_doc</td>
        <td >"POST"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html">Index API</a></td>
    </tr>
     <tr>
        <td >/{index}/_create/{id}</td>
        <td >"PUT", "POST"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html">Index API</a></td>
    </tr>
     <tr>
        <td >/_security/user/_has_privileges</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-has-privileges.html">Has privileges API</a></td>
    </tr>
     <tr>
        <td >/{index}/_field_caps</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/search-field-caps.html">Field capabilities API</a></td>
    </tr>
     <tr>
        <td >/{index}/_flush</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch//reference/current/indices-flush.html">Flush API</a></td>
    </tr>
     <tr>
        <td >/{index}/_mapping</td>
        <td >"GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-get-mapping.html">Get mapping API</a></td>
    </tr>
     <tr>
        <td >/{index}/_mappings</td>
        <td >"GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-get-mapping.html">Get mapping API</a></td>
    </tr>
     <tr>
        <td >/{index}/_refresh</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-refresh.html">Refresh API</a></td>
    </tr>
     <tr>
        <td >/_resolve/index/{name}</td>
        <td >"GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-resolve-index-api.html">Resolve API</td>
    </tr>
     <tr>
        <td >/{index}/_count</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/search-count.html">Count API</td>
    </tr>
     <tr>
        <td >/{index}/_msearch</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/search-multi-search.html">Multi search API</td>
    </tr>
     <tr>
        <td >/{index}/_search</td>
        <td >"POST", "GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html">Search API</td>
    </tr>
     <tr>
        <td >/_async_search/{id}</td>
        <td >"GET"</td>
        <td >-</td>
    </tr>
     <tr>
        <td >/{index}/_async_search</td>
        <td >"POST"</td>
        <td >-</td>
    </tr>
     <tr>
        <td >/_security/_authenticate</td>
        <td >"GET"</td>
        <td >详情参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-authenticate.html">authenticate API</td>
    </tr>
 </table>
