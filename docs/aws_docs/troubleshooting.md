Docker commands for troubleshooting a docker image on the EC2 instance
Install the docker image yourself:
docker run -it --env-file ./development.env -p 80:80 <public dns>
docker pull <public dns>

aws ecr get-login --no-include-email
^ copy and paste output back into shell to log in with docker


aws ecs list-container-instances --cluster or-development


aws configure set region us-west-2


docker ps -a (all, even exited ones)
docker stop <container> # kill it (gracefully)






# Re-setting ecs agent


sudo docker stop ecs-agent


sudo docker rm ecs-agent


sudo docker run --name ecs-agent \
  --detach=true \
  --restart=on-failure:10 \
  --volume=/var/run/docker.sock:/var/run/docker.sock \
  --volume=/var/log/ecs/:/log \
  --volume=/var/lib/ecs/data:/data \
  --volume=/etc/ecs:/etc/ecs \
  --net=host \
  --env-file=/etc/ecs/ecs.config \
  amazon/amazon-ecs-agent:latest


sudo docker ps


sudo docker logs ecs-agent


sudo usermod -a -G docker ec2-user
sudo yum install docker
