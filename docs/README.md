# How to setup the docs

- Install required packages
```
$ pip3 install -r requirements.txt
```

- Generate html files with sphinx
```
$ make html
```

- Open the html file
```
$ firefox build/html/index.html
```

- If sphinx-build command error is encountered, please remove sphinx using pip3 and install it using
```
$ apt-get install python3-sphinx
or
$ yum install python3-sphinx
```
