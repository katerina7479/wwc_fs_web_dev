# Creating an IAM User Group and Adding Users with Limited Permissions.

**1. Click the "Search" field.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/569fd6c3-09e1-4d85-9282-019d63b1275e/ascreenshot.jpeg?tl_px=0,0&br_px=746,420&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=162,-5)

**2. Search for IAM, and click the service**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/71db362f-04d7-49d4-a0fc-c9d1f62ed2a0/ascreenshot.jpeg?tl_px=125,0&br_px=871,420&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,135)

**3. Make sure the Root User has MFA set up!**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/9fb180ea-d8cf-423a-b54a-2115da2ab547/ascreenshot.jpeg?tl_px=104,0&br_px=850,420&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,128)

**4. Click "User groups"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/232c6af9-e256-408f-ac59-16167b725027/ascreenshot.jpeg?tl_px=0,101&br_px=746,521&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=36,139)

**5. Click "Create group"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/df3de7af-7114-4f92-a64a-d301abed4336/ascreenshot.jpeg?tl_px=810,0&br_px=1556,420&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=413,81)

**6. This will be our "Admin" group**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/d0fda3ee-54d6-43b6-b8f6-15482a915365/user_cropped_screenshot.jpeg?tl_px=136,173&br_px=882,593&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**7. Seach the Policies for "AdministratorAccess"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/5618931b-aca9-4166-bef2-f4055b551ff4/ascreenshot.jpeg?tl_px=107,359&br_px=853,779&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**8. Select "AdministratorAccess"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/9675f800-da83-4740-ac47-f7be68611cf4/ascreenshot.jpeg?tl_px=0,110&br_px=746,530&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=244,139)

**9. Search for "IAMUser"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/c27c42ad-5d2f-4891-a8fe-b604b0df50e6/ascreenshot.jpeg?tl_px=112,322&br_px=858,742&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**10. Let's let the user change their password**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/dc0199b8-3781-4993-b278-5e55d3bc2da6/ascreenshot.jpeg?tl_px=0,548&br_px=746,968&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=243,190)

**11. While you are in here, add two more policies we will need.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/96d4a340-ffd5-448b-9e20-84e8cebfbb52/ascreenshot.jpeg?tl_px=48,135&br_px=794,555&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**12. AmazonEC2ContainerRegistryFullAccess**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/491d56a3-1782-441b-b3d4-b24d694c71b8/ascreenshot.jpeg?tl_px=0,353&br_px=746,773&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=237,139)

**13. AmazonECS_FullAccess**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/bc670e89-20ca-4b9d-b6eb-a1c95a37a8f1/ascreenshot.jpeg?tl_px=0,275&br_px=746,695&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=242,139)

**14. Click "Create group"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/dd7a5bc2-2076-41d0-92ee-88af71f65ffc/ascreenshot.jpeg?tl_px=810,548&br_px=1556,968&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=430,248)

**15. Click "Users"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/59abb0c3-3cb3-4676-bdd2-fb4c88440189/ascreenshot.jpeg?tl_px=0,130&br_px=746,550&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=27,139)

**16. Click "Add users"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/fd3274b0-b8a2-4443-88fa-40bb71a3aaff/ascreenshot.jpeg?tl_px=810,0&br_px=1556,420&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=436,86)

**17. Enter in a unique user name**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/26ab4e5e-8bed-4b31-94f2-adc0a098e0b8/ascreenshot.jpeg?tl_px=63,70&br_px=809,490&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**18. We want to provide access to the console**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/9c9c0399-7a91-4036-a633-e183a7f6fa6d/user_cropped_screenshot.jpeg?tl_px=14,134&br_px=760,554&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**19. We want an IAM user, so they can use Access Keys.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/1108b6f1-3bc1-4dd3-8b88-bdda1be21762/ascreenshot.jpeg?tl_px=72,327&br_px=818,747&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**20. In this case, I'm going to create my own password.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/0d014590-ffd0-45f9-ba72-c61aa50c4264/ascreenshot.jpeg?tl_px=13,331&br_px=759,751&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**21. Click this password field.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/e8e042cd-c907-4909-9344-bdd83c2c4ed7/ascreenshot.jpeg?tl_px=133,386&br_px=879,806&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**22. And not require myself to regenerate it.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/852633d0-d4e7-4310-b0be-4caec7b1677e/ascreenshot.jpeg?tl_px=12,515&br_px=758,935&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**23. Click "Next"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/b5614fa5-dfc3-4c6b-8fc0-471aa40e2771/ascreenshot.jpeg?tl_px=810,548&br_px=1556,968&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=452,248)

**24. Let's Add the Admin Group to this user**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/cd1d4b02-a8c1-49f2-8b69-41f085c9b140/ascreenshot.jpeg?tl_px=11,382&br_px=757,802&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**25. Click "Next"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/177063d0-8cbe-4215-863e-dc6438e08b67/user_cropped_screenshot.jpeg?tl_px=810,521&br_px=1556,941&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=459,139)

**26. Click "Create user"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/002f6a46-1193-4eee-bba8-d21b555022ea/ascreenshot.jpeg?tl_px=810,548&br_px=1556,968&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=424,186)

**27. It's a good idea to download the csv file and keep it somewhere safe.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/9ad96eb9-fef8-4430-beae-e8b82b5e1906/user_cropped_screenshot.jpeg?tl_px=810,398&br_px=1556,818&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=268,139)

**28. Click "Return to users list"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/b92a5f92-2d79-43df-bcbc-757a7bd7c891/user_cropped_screenshot.jpeg?tl_px=810,403&br_px=1556,823&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=384,139)

**29. You can create an alias on your account that you can log into**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/b5a694f4-7209-48c6-a1af-0dcfeb5c4896/user_cropped_screenshot.jpeg?tl_px=810,59&br_px=1556,479&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=374,139)

**30. Click the "Preferred alias" field.**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/23b12cb4-5bd2-45e4-bf88-157119c3043a/user_cropped_screenshot.jpeg?tl_px=272,240&br_px=1018,660&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**31. Click "Save changes"**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/980ad4fd-80f6-4981-bd52-ad1a57b5e91d/ascreenshot.jpeg?tl_px=620,387&br_px=1366,807&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=262,139)

**32. Now you and your users can log in under your aliased account!**

![](https://ajeuwbhvhr.cloudimg.io/colony-recorder.s3.amazonaws.com/files/2023-06-15/a3a06c07-11d3-48a2-99a5-152a32e37878/user_cropped_screenshot.jpeg?tl_px=810,169&br_px=1556,589&force_format=png&width=560&wat_scale=50&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=288,139)
