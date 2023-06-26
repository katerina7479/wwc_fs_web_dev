# Work Breakdown Document (WBD)

## Project Timeline

8 weeks total (4 more weeks)

## Work Breakdown Structure

[List the major work packages or deliverables for the project, along with their corresponding subtasks or activities. Use a hierarchical structure to organize the tasks.]

### 1. Backend API

- Task 1.1: Initial Models / Database 
- Task 1.2: Create Serializers
- Task 1.3: Create Filters
- Task 1.4: Add Swagger
- Task 1.5: Add Permissions / sign-in
- Task 1.6: Add Backend Unit Tests
- Task 1.7: Handle Special API Endpoints
- Task 1.8: Set up Notifications

### 2. Frontend
#### Prerequisites:
- Task 2.1: Create React-app
- Task 2.2: Design Admin App (wireframes)
- Task 2.3: Handle Admin sign-in
- Task 2.4: Develop Admin Form components
- Task 2.5: Develop Admin View components

### 3. Deployments
#### Prerequisites: 1.1-1.3, 2.1
- Task 3.1: Set up Local Docker
- Task 3.2: Set up Prod Docker
- Task 3.3: Set up AWS Account / keys / IAM user
- Task 3.4: Set up S3
- Task 3.5: Set up Dev RDS
- Task 3.6: Set up Dev EC2 instance
- Task 3.7: Set up Dev ECR respository
- Task 3.8: Set up Dev ECS task definition
- Task 3.9: Set up Dev ECS service
- Task 3.10: Set up github actions

## Task Dependencies

[Specify any dependencies or relationships between the tasks, such as task dependencies, prerequisites, or constraints.]

* We can deploy with skeletons in place for development
* It's helpful to have basic CRUD API's available for Frontend before starting frontend development
* Backend needs seed data at least locally

## Resource Allocation

[List the resources assigned to each task, including team members, roles, and responsibilities.]

* Katerina's extra time
* Volunteers:

## Milestones

[List the key milestones for the project, including their expected completion dates and associated deliverables.]

Session 1: Project Intro / Models

Session 2: API Development

Session 3: AWS Deployment Pipeline 

Session 4: Frontend Development

Session 5: Extending Functionality


## Risk Assessment

[Identify potential risks or challenges that may impact the project, along with their likelihood and impact. Include mitigation strategies for each risk.]

* Likely to run out of steam / have other obligations
  * Be brutal about minimizing V0 Scope
  * Have fun!
