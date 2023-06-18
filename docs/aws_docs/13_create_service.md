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