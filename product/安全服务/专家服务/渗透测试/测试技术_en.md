## Automated Test
Automated test is to detect known security issues in the target system by fully scanning the system layer and application layer of the site using system and application scanning tools.
### Advantages
- Fast detection speed with automated detection tools
- Complete detection of known vulnerabilities

### Disadvantages
- Automated tools cannot automatically verify certain special information.
- Automated detection is not available to complex client scripts.
- Some logic businesses cannot be detected by automated tools.
-  Automated tools cannot avoid false alarms.

## Manual Test
Manual test is complementary to automated test in depth and breadth. It is an important measure to guarantee the quality of penetration test and also the essence of penetration test. Manual test is conducted by testers whose personal skills and experience directly affect the results of manual test.
Manual test covers the following aspects:
### Validation of Automated Test Results
False alarms are inevitable for automated detection tools. Therefore, manual test needs to filter out the false alarms in automatic test results. Besides, the results of correct alarms must be verified and reused to confirm that the level of danger is consistent with that in automatic scanning results.
### Manual verification of Personalized Page Information 
Most automated test tools verify based on the keyword in the returned page or the HTTP status value. But the returned content of some well-structured personalized page cannot be fully verified by automated tools. Manual test is required for such sites.
### JavaScript Test
With the rise of Web 2.0, JavaScript is widely used. However, automated scanning tools are not good at resolving JavaScript, and inevitably miss scripts in the automated scanning process. Therefore, manual scanning should be additionally conducted on pages that cannot be resolved by automated scanning tools and contain JavaScript to test their security.
### Refinement Test for Data Submission
Automated test follows certain rules when constructing the data for submission. Manual test can avoid such problems. As a result, manual depth test is required on pages that can construct malicious data locally and submit for test.
### Security Test for Business Logic
Business logic has little to do with the program itself. Automated detection tools cannot detect whether the business logic is correct. So it is necessary to manually analyze and identify the existing business logic, and then test the security of the business logic based on the tester's experience.      

