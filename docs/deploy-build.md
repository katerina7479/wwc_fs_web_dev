1. Create AWS account
   2. Configuring
      3. Set  budget
   3. IAM Access key & Secret key
      4. User Permissions
         * AmazonEC2ContainerRegistryFullAccess
         * AmazonECS_FullAccess
   3. S3
      4. Set up S3 buckets
         * static
         * media
   * Set up RDS database remotely
     * Get credentials
     * Add to .env.dev file
   * Set up EC2
     * 


6. Create Github workflow files in .github
   3. Workflow is the deploy_to_dev.yml
   4. Add task-definition to workflow
4. Add secret keys to github
5. Add appropriate dockerfile for deploying
6. Add setup run.sh
7. Add custom nginx.conf
