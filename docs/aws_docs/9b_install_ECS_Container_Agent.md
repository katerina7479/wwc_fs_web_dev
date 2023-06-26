
1. SSH into your EC2 instance
   `ssh -i /path/my-key-pair.pem ec2-user@my-instance-public-dns-name.`
2. Install docker
   ``
3. Start the Docker service
   4. Install the ECS Container Agent
    ```
    sudo amazon-linux-extras install ecs -y
    sudo service docker start
    ```
5. Register the EC2 Instance with your ECS Cluster
   6. navigate to `/etc/ecs/`
   7. Create the ECS config file `sudo vi ecs.config`
   7. Add the following, with the name of your cluster
   `ECS_CLUSTER=your_cluster_name`
   8. `:wq` to save and exit
8. Start the ECS Agent: Now, start the ECS Agent with the command sudo service ecs start. This will register your EC2 instance with your ECS cluster.
   9. `sudo service ecs start`
9. Run `sudo systemctl enable ecs` to make it start automatically

1. Create a custom AMI to use this for your future ECS autoscaled instances
2. Create the Autoscaling group template from this

