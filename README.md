# Checkout-Python-REST
#### Sample code to showcase PayPal Express Rest checkout in Python Flask

## Run

Clone the repo and cd into Checkout-Python-REST
python controller.py
See the demo in http://localhost:5000

## config

change the configuration json in config.py to reflect your own sandbox and live credentials

"IS_APPLICATION_IN_SANDBOX" : "true" --> Application in sandbox environment

"IS_APPLICATION_IN_SANDBOX" : "false"--> Application in Live environment

## The SSL version should be TLS1_2 [details here](https://www.paypal.com/us/webapps/mpp/ssl-security-update). To achieve this the following is needed: 

> a.    python version -- 2.7.14
> b.	>> python -c "import ssl; print ssl.OPENSSL_VERSION" OpenSSL 0.9.8zh 14 Jan 2016
> c.    pip, Flask and requests need to be already installed

> i.	sudo easy_install pip
> ii.	sudo pip install Flask
> iii.	sudo pip install requests



## Environment changes (The following needs to be documented in README. This may work by default on Windows, but on Mac the defaults are different).

> 1) Make sure Python version is correct (2.7.14 or later)

> $ python --version

> Python 2.7.14

> 2)	Make sure that the open SSL version is correct:

> python -c "import ssl; print ssl.OPENSSL_VERSION"

> OpenSSL 1.0.2m  2 Nov 2017

> [Link here explains how to accomplish both](https://stackoverflow.com/questions/24323858/python-referencing-old-ssl-version).


