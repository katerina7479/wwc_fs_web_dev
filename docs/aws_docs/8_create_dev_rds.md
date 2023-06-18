# How to set up a development RDS


**1. Click "RDS"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/d8cc6f58-71ec-4b27-b8d8-8125912b5c95/user_cropped_screenshot.jpeg?tl_px=1,8&br_px=747,428&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**2. Click "DB Instances (0/40)"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/8a5fa0fc-1712-43f1-b1de-51eb9389ec94/user_cropped_screenshot.jpeg?tl_px=27,184&br_px=773,604&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**3. Click "Create database"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/262af893-00e3-406d-8de5-8f5256774055/user_cropped_screenshot.jpeg?tl_px=1065,48&br_px=1811,468&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=430,139)

**4. We're going to make a free-tier postgres db for development**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/1edc5ffd-995c-421a-b8a1-b6b64c12078f/user_cropped_screenshot.jpeg?tl_px=100,342&br_px=846,762&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**5. The latest version is selected by default.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/5e97edce-78f3-4dde-9e7e-9f3eb3646f89/user_cropped_screenshot.jpeg?tl_px=0,260&br_px=746,680&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=227,139)

**6. We're going to select the Free tier db.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/797cb8e1-c0f8-49e8-99bf-5e5ab93eb4c9/user_cropped_screenshot.jpeg?tl_px=378,303&br_px=1124,723&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**7. Give your database an identifier.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/d694c399-902b-471e-9388-e310f9422695/user_cropped_screenshot.jpeg?tl_px=113,219&br_px=859,639&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**8. Click here.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/344a7354-5dc4-4850-bba9-eb89c826d80b/ascreenshot.jpeg?tl_px=0,217&br_px=746,637&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=65,139)

**9. I recommend changing the master username**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/b4e04d65-4e6e-4560-90fd-b73b5b7a0be4/user_cropped_screenshot.jpeg?tl_px=0,199&br_px=746,619&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=164,139)

**10. You can let AWS generate a password.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/6ab60752-ed02-4651-a6cf-b1484fb12384/user_cropped_screenshot.jpeg?tl_px=0,440&br_px=746,860&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=62,139)

**11. Make sure you have the "db.t3.micro" selected.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/85a7b6fc-4999-4c59-949a-99763c1202bb/user_cropped_screenshot.jpeg?tl_px=0,456&br_px=746,876&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=191,139)

**12. We're going to give ourselves public access so we can use our development GUI to connect. That's optional, and somewhat less safe, but ok for a development box.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/4e2d410e-fe37-41fd-8467-1f91bf1c28e6/user_cropped_screenshot.jpeg?tl_px=0,294&br_px=746,714&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=63,139)

**13. Click here.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/9597a2f6-b61a-4667-b048-5af9b9010d83/user_cropped_screenshot.jpeg?tl_px=0,549&br_px=746,969&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=56,139)

**14. Make sure the port is set, take note of the 5432**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/0756b944-98ab-4dca-9699-d84a44451834/user_cropped_screenshot.jpeg?tl_px=0,298&br_px=746,718&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=98,139)

**15. Monitoring is ok. Make sure it's free tier. **

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/7e9810a1-75f3-4f2a-999d-7c106617bcec/user_cropped_screenshot.jpeg?tl_px=0,188&br_px=746,608&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=168,139)

**16. Click here.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/290e4e20-c4b9-481e-acc5-79be0b91de20/user_cropped_screenshot.jpeg?tl_px=0,301&br_px=746,721&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=59,139)

**17. Name your db. This is your DB_NAME. Only letters, numbers & underscores.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/623b6417-0c13-4f17-a795-eb6adced76aa/user_cropped_screenshot.jpeg?tl_px=0,328&br_px=746,748&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=110,139)

**18. Click "Create database"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/81175b31-0d84-4fc3-a4bf-bdc1ca2d09e2/user_cropped_screenshot.jpeg?tl_px=354,662&br_px=1100,1082&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,235)

**19. Wait while your db is created. **

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/740010bb-17c1-48d9-828c-6f6b81284ddb/user_cropped_screenshot.jpeg?tl_px=86,352&br_px=832,772&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**20. You can "View credential details"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/2f25ae3a-c886-4545-8e01-ca914fb2310f/user_cropped_screenshot.jpeg?tl_px=1065,0&br_px=1811,420&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=394,37)

**21. Take note of your username and password. Copy into your .env.dev file.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/72950c9e-5b8c-4aaa-9eef-933cd2a15b05/user_cropped_screenshot.jpeg?tl_px=449,414&br_px=1195,834&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**22. Click "database-dev"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/785c9e6a-e5b2-4f33-a6b5-112b843dbf66/user_cropped_screenshot.jpeg?tl_px=96,192&br_px=842,612&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**23. Copy the info under "Endpoint" that's your DB_HOST**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/cc469a25-324f-4d37-b3ee-a9d4aba05b0b/user_cropped_screenshot.jpeg?tl_px=135,424&br_px=881,844&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**24. Click your default VPV security group. We're going to add two rules.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/453b2143-d323-4c12-bf2e-3db9a1f5f76a/user_cropped_screenshot.jpeg?tl_px=821,410&br_px=1567,830&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**25. Click the security group id**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/37c27dc1-50ac-4957-8737-ff773ca9de78/user_cropped_screenshot.jpeg?tl_px=165,29&br_px=911,449&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**26. Click "Edit inbound rules"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/e0bb3dc9-99b7-4861-9bd8-298274030f10/user_cropped_screenshot.jpeg?tl_px=1065,380&br_px=1811,800&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=416,139)

**27. Click "Add rule" twice**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/19988596-8900-4a7f-b6a2-3bab4b53c7a9/user_cropped_screenshot.jpeg?tl_px=0,209&br_px=746,629&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=59,139)

**28. Click "Custom TCP"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/4ffbbe46-4910-4ff8-815d-39b4f93ee73d/user_cropped_screenshot.jpeg?tl_px=123,189&br_px=869,609&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**29. Click "PostgreSQL"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/52ed055e-d26f-44a8-9543-ed6da0004d97/user_cropped_screenshot.jpeg?tl_px=51,659&br_px=797,1079&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**30. Set one to "Anywhere-IPv4"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/3b522e7e-a486-421e-83c6-e89945138687/user_cropped_screenshot.jpeg?tl_px=590,255&br_px=1336,675&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**31. Set the other to "Anywhere-IPv6"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/eb3ec917-8f64-4a06-93b9-9b7bfd278182/user_cropped_screenshot.jpeg?tl_px=587,389&br_px=1333,809&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**32. Click "Save rules"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-18/7bc3dea0-3844-4dd7-b0c5-9ecb254bf6b9/user_cropped_screenshot.jpeg?tl_px=1065,440&br_px=1811,860&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=418,139)

