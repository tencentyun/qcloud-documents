Tencent Cloud TKE To ensure steady closed-loop features, some restrictions are imposed on the Kubernetes orchestration syntax in the container platform. This document describes the restrictions and reasons for them.

## Restriction on Supported Resource Types

Kubernetes contains many different types of resources. Only the most commonly used resources `Deployment` and ` Service` are available in TKE to meet user needs. (When you create `Deployment`, `Pod` and `replicaset` are created automatically).

Only `Deployment` and `Service` are available in all the application orchestrations in TKE.

## Restriction on Resource Name

In each service of application template, `Deployment` and `Service` resource names must be consistent with the service name.

## Restriction on Namespace

(1) All the resources in the application template must be in one namespace.

(2) The `kube-system` namespace does not support the creation of service, so the namespace `kube-system` is not supported in the application template.

## Restrictions on Label
(1) In an application template, you can label the resources in the service with Label. In TKE, `Service` searches for the corresponding `Pod` via `Select Label`, thus associating it with `Deployment`. `Deployment` is associated with `Pod` with its own `Select Label`. Therefore, in order to manage `Deployment` and `Service`, the restriction that the `Select Label` of `Deployment` must be the same as that of `Service` is added.

(2) By default, `qcloud-app` is provided for each service in the application template to identify the service, and `qcloud-application-label` is provided to identify the application to which the service belongs. Modification to these two labels is not supported.

## Restrictions on CBS Disk Usage

(1) A CBS can only be mounted to one container pod at a time, so the maximum number of pods is 1 for all the services that use CBS disk.

(2) The services that use CBS disk can be updated only through recreation. Rolling update is not supported.













