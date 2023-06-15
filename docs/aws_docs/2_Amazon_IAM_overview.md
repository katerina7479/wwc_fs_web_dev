## IAM Overview

Stands for Identity and Access Management
This is your security! It's very important.

When you set up your initial account, you get a root account.
YOU DO NOT WANT TO USE THIS ACCOUNT FOR ONGOING ACCESS, so get out your password manager. 

### Strategy:

* Users are in groups.
* Groups have permission policies
* Avoid assigning permissions directly to Users
* Grant the MINIMUM permissions necessary to do the job




Steps to take to secure Users:
1) Set up an Admin Group

Each IAM user will be granted an Access Key and Secret Access Key. 
These are tied to the username, and are personal to that user. They 
will be used to identify the user, and allow them to access resources via the console or command line.
They will respect the permissions granted. 
