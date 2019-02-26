Tencent Cloud TKE allows you store the deployment information of multiple services into the application templates using the YAML description text. By using application templates and configurations for various environments, you can quickly deploy application services in different environments. For more information on application management, please see [Application Management Overview][12].

## Main Operations on Application Templates

[Create Application Template][3]

[Delete Application Template][4]

[Update Application Template][5]

[View Application Template][6]

[Application Template Operation Instructions][7]

## Orchestration Syntax Overview

In application templates, the service deployment information is described according to orchestration syntax. Orchestration syntax is a set of rules used to describe the service deployment information. Users describe the service deployment information based on these rules. After resolving the service deployment information, the orchestration engine deploys service using the resolved parameters.

The underlying orchestration syntax of application templates in Tencent Cloud TKE supports Kubernetes native orchestration syntax. For more information, please see [Basic Syntax][8]. In addition to Kubernetes orchestration syntax, variable substitution is also supported. For more information, please see [Variable Substitution][9]. In view of the capabilities of TKE platform itself, extended syntax related to the TKE platform is provided. For more information, please see [Extended Syntax][10]. To ensure steady closed-loop features, some limits are imposed on the Kubernetes orchestration syntax in container platform. For more information, please see [Limits][11].

  [1]: https://cloud.tencent.com/document/product/457/11951
  [2]: https://cloud.tencent.com/document/product/457/11944
  [3]: https://cloud.tencent.com/document/product/457/11949
  [4]: https://cloud.tencent.com/document/product/457/11950
  [5]: https://cloud.tencent.com/document/product/457/11954
  [6]: https://cloud.tencent.com/document/product/457/11955
  [7]: https://cloud.tencent.com/document/product/457/12199
  [8]: https://cloud.tencent.com/document/product/457/11957
  [9]: https://cloud.tencent.com/document/product/457/11956
  [10]: https://cloud.tencent.com/document/product/457/11956
  [11]: https://cloud.tencent.com/document/product/457/11959
  [12]: https://cloud.tencent.com/document/product/457/12198
