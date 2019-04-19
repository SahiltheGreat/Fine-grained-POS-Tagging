# Project Title
Fine Grained POS tagging

### Installing and Prerequisites

```bash
sudo apt-get update
sudo apt-get install python3.6
sudo apt install python3-pip
pip3 install Flask
sudo apt-get install sqlite3
pip3 install flask_sqlalchemy
pip3 install nltk
pip3 install requests
nltk.download('indian')
nltk.download('popular')
```

## Running the Experiment

Step1 --> Run the app.py file using command :-
```python
                                        $ python3 app.py
```

Step2 --> Open the browser and open the link given


Folder structure
______
Assignment-4
├── app.py
├── database.db
├── English_POS.py
├── Hindi_POS.py
├── __pycache__
│   ├── app.cpython-36.pyc
│   ├── check.cpython-35.pyc
│   └── check.cpython-36.pyc
├── requirements.txt
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── style1.css
│   │   ├── style.css
│   │   └── style.css~
│   ├── images
│   │   ├── about-us
│   │   │   ├── img1.png
│   │   │   ├── img2.png
│   │   │   ├── img3.png
│   │   │   └── img4.png
│   │   ├── banner_img.jpg
│   │   ├── bottom-line-n.png
│   │   ├── bottom-line.png
│   │   ├── chat.png
│   │   ├── deivder-green-v.png
│   │   ├── devider-blue-v-o.png
│   │   ├── devider-green-v-o.png
│   │   ├── dotted-devider-h-o.png
│   │   ├── dotted-devider-h.png
│   │   ├── _dotted-devider.png
│   │   ├── dotted-devider-v-o.png
│   │   ├── engineering
│   │   │   ├── icon_1.png
│   │   │   ├── icon_2.png
│   │   │   ├── icon_3.png
│   │   │   ├── icon_4.png
│   │   │   ├── icon_5.png
│   │   │   ├── icon_6.png
│   │   │   ├── icon_7.png
│   │   │   ├── icon_8.png
│   │   │   ├── icon_9.png
│   │   │   └── old
│   │   │       ├── biotechnology-eng.png
│   │   │       ├── chamical-eng.png
│   │   │       ├── chemical-sci.png
│   │   │       ├── civil-eng.png
│   │   │       ├── electrical-eng.png
│   │   │       └── electronics-eng.png
│   │   ├── favicon.ico
│   │   ├── favicon.png
│   │   ├── flask.png
│   │   ├── footer-o.png
│   │   ├── _footer.png
│   │   ├── footer.png
│   │   ├── galat.png
│   │   ├── icon_chat.png
│   │   ├── icon_lab.png
│   │   ├── iit
│   │   │   ├── amrita.jpeg
│   │   │   ├── amrita.png
│   │   │   ├── dayalbagh.jpeg
│   │   │   ├── iit-delhi.png
│   │   │   ├── iit-guwahati.png
│   │   │   ├── iithyderabad.jpeg
│   │   │   ├── iit-kanpur.png
│   │   │   ├── iit-kharagpur.png
│   │   │   ├── iit-madras.png
│   │   │   ├── iit-mumbai.png
│   │   │   ├── iit-roorkee.png
│   │   │   ├── nit.jpeg
│   │   │   ├── pune.jpeg
│   │   │   └── rsz_1amrita.jpg
│   │   ├── left-arrow.png
│   │   ├── logo-new.png
│   │   ├── logo.png
│   │   ├── pos-fg.jpg
│   │   ├── right-arrow.png
│   │   ├── right.png
│   │   ├── sahi.png
│   │   ├── search-box.png
│   │   ├── search.png
│   │   ├── slider-72.png
│   │   ├── slider.png
│   │   ├── social
│   │   │   ├── fb.png
│   │   │   ├── linkedin.png
│   │   │   └── twitter.png
│   │   ├── students.png
│   │   ├── uni-logos
│   │   │   ├── amruta university.png
│   │   │   ├── amrutauniversity.png
│   │   │   ├── COEP.png
│   │   │   ├── dayalbagh.png
│   │   │   ├── iiit_Hyd.png
│   │   │   ├── IIT_bombay.png
│   │   │   ├── IIT_Delhi.png
│   │   │   ├── IIT_guwahati.png
│   │   │   ├── IIT_hyderabad.png
│   │   │   ├── IIT_kanpur.png
│   │   │   ├── IIT_kharagpur.png
│   │   │   ├── IIT_madras.png
│   │   │   ├── IIT_roorkee.png
│   │   │   └── NIIT_karnataka.png
│   │   └── wrong.png
│   ├── js
│   │   ├── bootstrap.js
│   │   ├── bootstrap.min.js
│   │   ├── custom.js
│   │   ├── dispfunc.js
│   │   ├── getdisp.js
│   │   ├── jquery.js
│   │   ├── languagesel.js
│   │   ├── npm.js
│   │   └── splitstring.js
│   └── vendors
│       ├── font-awesome
│       │   ├── css
│       │   │   ├── font-awesome.css
│       │   │   └── font-awesome.min.css
│       │   └── fonts
│       │       ├── FontAwesome.otf
│       │       ├── fontawesome-webfont.eot
│       │       ├── fontawesome-webfont.svg
│       │       ├── fontawesome-webfont.ttf
│       │       ├── fontawesome-webfont.woff
│       │       └── fontawesome-webfont.woff2
│       └── owl-carousel
│           ├── AjaxLoader.gif
│           ├── grabbing.png
│           ├── owl.carousel.css
│           ├── owl.carousel.js
│           └── owl.theme.css
└── templates
    ├── Experiment.html
    ├── Feedback.html
    ├── FurtherReadings.html
    ├── Introduction.html
    ├── Listofexperiments.html
    ├── Objective.html
    ├── Procedure.html
    ├── Quizzes.html
    └── Theory.html

## Exiting 

Just press Ctrl+C on the terminal on which server is runnig.

## Built With

* Python ,Flask
* Javascript, Ajax, Jquery


## Authors

* SAHIL BHATT (2018111002)
* SONU GURU (2018101004)




