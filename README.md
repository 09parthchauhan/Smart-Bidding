# Smart Bidding

It is an online auction web application developed using Python-Django framework. In this application, the user can buy or sell the products he wishes to. When selling a product the user has to set a time limit in which only the buyers can bid for the items. The highest bidder will take the item(s).

NOTE: The paytm payment gateway is not working in this current application as it was only using the free version of it because of the project being an academic project for the college work. 

To run the project(python already installed):
    1. install django: "pip install Django"
    2. check the version of django: "django --version"
    3. gh repo clone 09parthchauhan/Smart-Bidding 
    4. python manage.py createsuper
    5. python manage.py makemigrations
    6. python manage.py migrate
    7. python manage.py runserver

 NOTE: you will find different modules not installed eg: no module named "PIL" found. You have to install the different modules using pip and you can find the packages at "pypi.org". Also install latest version of bootstrap as for frontend it has been used.
    
