Hi!!!, This is a Python GUI - Store Manager Software made using Tkinter and SQLite. It features a "Billing System" and a "GUI Database Manager Interface". The application opens up with a "User Validation Window" and after the validation allows you to open up both the "Billing System and "GUI Database Manager Interface" applications. The project has a few bugs but none that can interrupt the working of the application.

!!!CAUTION!!! : The project requires a Python - SQLite Enviornment Set-up for running.Instructions follow!!!.

On opening the .exe file you will be required to login via the "Username" = "user"  and "Password" = "passwrd".

![image](https://user-images.githubusercontent.com/88616188/150667127-7ca8ce03-f227-4545-834f-e28aca10f9df.png)

Once the login is successful you will be notified and will have the option to open both "Billing System" and a "GUI Databse Manager Interface".

![image](https://user-images.githubusercontent.com/88616188/150667183-addab029-e14c-44a1-96a2-cac1f4ce9d44.png)

!!!Billing System!!!   

On selecting the "Billing System" button the application will open and you can start billing your products that are stored in the SQLite Database by searching 
its unique id.

![image](https://user-images.githubusercontent.com/88616188/150667205-fc0f245f-54be-4e76-affd-4ff55a4acdaf.png)

Upon searching the id u will be shown the product name and price and will have the option to select the quantity and add the product to cart which will display it for billing.

![image](https://user-images.githubusercontent.com/88616188/150667243-41e14db9-0171-4434-b6fa-ac0c5750719d.png)

![image](https://user-images.githubusercontent.com/88616188/150667261-563c3b23-f839-4c6c-b4ee-9f860f7ddad6.png)

You now have the option to "Claculate Change" to be returned to the customer and can generate the bill. Which will print a bill automatically if connected to a printer
and save it in a dedicated folder called "Invoice".

![image](https://user-images.githubusercontent.com/88616188/150667314-f79109cd-0586-458b-adb1-816ee7815c69.png)

![image](https://user-images.githubusercontent.com/88616188/150667341-8cb0ebd1-23eb-4cbf-9645-9d49f50c0e3a.png)

!!!GUI Databse Manager Interface!!!     

On selecting the "GUI Databse Manager Interface" button the application will open and you can interact with the database containing the details of the products.

![image](https://user-images.githubusercontent.com/88616188/150667525-791f00c3-90d7-4326-9f2b-b3aef5187795.png)

You can access the product details by searching for it's unique id which will bring up all its details. 
You have the option to do the following interactions with the databse via the application:
1. Search Product
2. Update Product Detais
3. Add a "New Product"
4. Clear the "Search Results"
5. Delete the Product

![image](https://user-images.githubusercontent.com/88616188/150667546-901b0072-eba6-45b7-bda8-c4f810e60d8d.png)

!!!INSTRUCTION FOR USE AND SETTING UP EVIORNMENT!!!

!!!NOTE!!! : The unique id once used can not be used again, even after deleting the product the id will continue in ascending order 1-10000000. 
The database file "Store.db" can be accessed via "DB for SQLite" application, available on the internet for free for Windows / MacOS / Linux.
(https://sqlitebrowser.org/dl)

!!!NOTE!!! : After cloning the files using Git or saving it in your directory, the file location for the database file "Store.db" has to be updated on both "Billing System.py" and a "GUI Databse Manager Interface.py" else the program will run but not function. A simillar change has to be done in the Billing System.py file to set the folder for saving the "Invoice".

![image](https://user-images.githubusercontent.com/88616188/150667890-2829be76-06d1-4ac3-b7c9-789527bb3a4b.png)

![image](https://user-images.githubusercontent.com/88616188/150667923-3e712dae-73ab-4ff4-8cd9-67c81970d68c.png)

![image](https://user-images.githubusercontent.com/88616188/150667942-e8dc8cfa-3f71-4ede-9a84-e1dfecbde1cc.png)

Upon facing any issues with the project please don't hesitate to contact me !! :)
