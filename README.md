# Team-Management-Application
A Team Management App using Django

## Installation

### Prerequisites

#### 1. Install Python
Install ```python-3.7.2``` or above and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2. Install Django
Install Latest version of ```Django``` Follow the steps from the below reference document based on your OS.                                                                 
Reference: [https://docs.djangoproject.com/en/4.0/topics/install/](https://docs.djangoproject.com/en/4.0/topics/install/)

#### 3. Clone git repository
```bash
git clone "https://github.com/sjsinghh/Team-Management-Django.git"
```

#### 4. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver 

# your server is up on port 8000
```
Try opening [http://localhost:8000](http://localhost:8000) in the browser.
Now you are good to go.


### 5. URLs
#### Team Members List: [http://localhost:8000/(http://localhost:8000/)
![](https://i.imgur.com/76hGcmp.png)
#### Add a new Team Member: [http://localhost:8000/team-add](http://localhost:8000/team-add)
![](https://i.imgur.com/TOAL57C.png)
#### Edit a Team Member: [http://localhost:8000/team-update/{id}](http://localhost:8000/team-update/{id})
![](https://i.imgur.com/2aXNyO6.png)
