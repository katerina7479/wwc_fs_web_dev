1. Go to the Amazon ECS console in AWS.

2. In the navigation pane, choose Clusters.

3. On the Clusters page, select the name of the cluster in which you want to create a service.

4. On the Cluster : cluster_name page, choose the Services tab.

5. Choose Create.

6. For Launch type, choose the launch type for your service. For your case, it would be EC2.

7. For Task Definition, select the task definition to run in your service. This will be the task definition you created earlier.

8. For Service Name, enter a name for your service.

9. For Service type, choose REPLICA.

10. For Number of tasks, set the number of tasks for your service to maintain.

11. (Optional) For Minimum healthy percent and Maximum percent, leave the defaults.

12. (Optional) For Placement Templates, you can leave as default unless you have specific needs.

13. Under Load Balancing, choose none unless you are using a load balancer.

14. For Service Discovery, choose none unless you're using AWS Cloud Map.

15. Click Next step and you can skip and review the next pages and then click Create Service on the final page.

17. Update the deploy_to_dev.yml with the new Cluster, task, service information


```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "The template used to create an ECS Service from the ECS Console.",
  "Parameters": {
    "ECSClusterName": {
      "Type": "String",
      "Default": "or-development"
    },
    "SecurityGroupIDs": {
      "Type": "CommaDelimitedList",
      "Default": "sg-0a065c1899bf111e1"
    },
    "SubnetIDs": {
      "Type": "CommaDelimitedList",
      "Default": ""
    },
    "VpcID": {
      "Type": "String",
      "Default": "vpc-0233f9ea9914f5cd9"
    },
    "LoadBalancerName": {
      "Type": "String",
      "Default": ""
    }
  },
  "Resources": {
    "ECSService": {
      "Type": "AWS::ECS::Service",
      "Properties": {
        "Cluster": "or-development",
        "CapacityProviderStrategy": [
          {
            "CapacityProvider": "Infra-ECS-Cluster-or-development-34e232c1-EC2CapacityProvider-gVLbnrZuV7bB",
            "Base": 1,
            "Weight": 1
          }
        ],
        "TaskDefinition": "arn:aws:ecs:us-west-2:130354956980:task-definition/open-restaurant-task-definition:33",
        "ServiceName": "or-dev-service",
        "SchedulingStrategy": "REPLICA",
        "DesiredCount": 1,
        "DeploymentConfiguration": {
          "MaximumPercent": 200,
          "MinimumHealthyPercent": 100,
          "DeploymentCircuitBreaker": {
            "Enable": false,
            "Rollback": false
          }
        },
        "DeploymentController": {
          "Type": "ECS"
        },
        "ServiceConnectConfiguration": {
          "Enabled": false
        },
        "PlacementStrategies": [
          {
            "Type": "binpack",
            "Field": "CPU"
          }
        ],
        "PlacementConstraints": [],
        "Tags": [],
        "EnableECSManagedTags": true
      }
    }
  },
  "Outputs": {
    "ClusterName": {
      "Description": "The cluster used to create the service.",
      "Value": {
        "Ref": "ECSClusterName"
      }
    },
    "ECSService": {
      "Description": "The created service.",
      "Value": {
        "Ref": "ECSService"
      }
    }
  }
}
```

