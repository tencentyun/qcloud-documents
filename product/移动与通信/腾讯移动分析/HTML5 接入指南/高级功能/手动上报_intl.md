### Description
Reporting is automatically controlled by programs.
### Application Scenarios
Auto reporting is enabled by default when connecting to HTML 5. In case of single-sided page update, only elements are updated, but the page is not refreshed. You can disable auto reporting and use manual reporting.

### Tips on Usage
1. Disable auto reporting in **App Management**.
2. Load js sdk synchronously.
3. Execute MtaH5.pgv().

Tracking code provided by the reporting console is async. The following is the method of sync loading:
```
<script>
//Configure information
var _mtac = {};
</script>
<script src="http://pingjs.qq.com/h5/stats.js?v2.0.4" name="MTAH5" sid="sid in the tracking code of the console" cid="cid can be deleted if no cid exists"></script>
```
### Notes
1. "js sdk" must be loaded before pgv is executed.
2. "_mtac" configuration file must be set before "js sdk" is loaded. It can be defined if it is empty.

