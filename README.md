# OC-Pr7-GrandPyBot
Repository for Project 7 from Openclassrooms cursus in Software Developement

## Project Description
This is a web application to help user to find an address and learn more about the story of this location.

### Functionalities
* AJAX interactions : the user send his question by pressing enter key and the answer is directly printed on the screen, without reloading the webpage.
* Use of Google Geocoding API, Google Map API and Media Wiki API.
* Nothing is saved. If the user reloads the webpage, all the history is lost.

### User Path
The user opens his browser and enter the specific URL address (Not available yet). The webpage which is loaded owns the following elements:
* header : logo with tagline
* main zone : zone for conversing with the application
* footer : firsname and lastname, link with github repository and other social networks links.

Here is a typical interaction with the application:
* The user writes "Hi GrandPy! Do you know where I can find the Openclassrooms address?" in the form field and press Enter key.
* The message is visible in the chat zone with the older ones. An icon indicates that GrandPy is thinking.
* The answer is appears: "Of course! Here is it: 7 cité Paradis, 75010 Paris." Below, there is a Google map with a flag showing the location.
* GrandPy sends a new message: "Did I told you the story of this area? The cité Paradis is a public street located in the XXe arrondissement of Paris. It looks like a T (the letter).

## App Structure

```
|-- .gitignore
|-- README.md
|-- config.py.dist
|-- requirements.txt
|-- run.py
|-- botapp/
    |-- __init__.py
    |-- app.py
    |-- forms.py
    |-- views.py
    |-- static/
        |-- css/
            |-- main.css
            |-- main.css.map
        |-- sass/
            |-- main.scss
            |-- base/
                |-- _base.scss
            |-- layout/
                |-- _chat.scss
                |-- _grid.scss
                |-- _header.scss
                |-- _info.scss
            |-- modules/
                |-- _mixins.scss
                |-- _variables.scss
        |-- js/
            |-- custom.js
        |-- img/
            |-- avatar.png
    |-- templates/
        |-- base.html
        |-- index.html
    |-- utils/
        |-- geocoding.py
        |-- mediawiki.py
        |-- message_parse.py
        |-- response.py
        |-- stop_words.py
|-- tests/
    |-- utils/
        |-- test_geocoding.py
        |-- test_mediawiki.py
        |-- test_message_parse.py
        |-- test_response.py
```

## Getting Started
1. Clone the repository:
```
git clone https://github.com/JN-Lab/OC-Pr7-GrandPyBot.git
```

When your are in your directory (root):

2. Modify your **config file**:
    * Change the name file config.py.dist into config.py
    * Set-up your secret key -> SECRET_KEY
    * Set-up your Google API Key -> GOOGLE_API_KEY

3. Set-up your virtual environnement:
```
python3 -m venv env
```

4. Activate your virtual environment:
```
source env/bin/activate
```

5. Install all necessary frameworks and libraries:
```
pip install -r requirements.txt
```

6. Initiate FLASK_APP, your local session variable:
```
export FLASK_APP=run.py
```

7. Run flask in local:
```
flask run
```

8. You go on your favorite browser and copy-paste this url:
```
http://127.0.0.1:5000/
```

## Running the tests
To run the unit tests and get all the informations (in the root directory):
```
python3 -m pytest -v
```
