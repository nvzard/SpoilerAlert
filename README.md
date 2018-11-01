<h1 align="center">
  <img src="https://raw.githubusercontent.com/nvzard/SpoilerAlert/master/assets/logo.png" alt="Logo">
  <h2 align="center">Spoiler Alert</h2>
  <p align="center">
  This is a script written in python to fetch the release status of the next episode of your favourite TV Shows. This will help us in keeping track of all our favourite season and their latest episode's air time.
  </p>
</h1>

## See it in action
![SpoilerAlert in action](https://raw.githubusercontent.com/nvzard/SpoilerAlert/master/assets/action.gif)

Checkout other images <a href="https://github.com/nvzard/SpoilerAlert/tree/master/assets">here</a>.

### Requirements
You need **requests**, **BeautifulSoup** and **colorama** to run this script.

## Installation
Run the following commands on your terminal

### 1. Install
#### Using pip:
`$ pip3 install -r requirements.txt`

### 2. System-wide installation
#### 1. Requests
Using apt-get:
`$ sudo apt-get install python3-requests`

Using pip:
`$ pip3 install requests`

#### 2. BeautifulSoup
Using apt-get:
`$ sudo apt-get install python3-bs4`

Using pip:
`$ pip3 install beautifulsoup4`

#### 3. Colorama
Using pip:
`$ pip3 install colorama`

### 2. Installation using virtualenv
Fisrt you need to install virtualenv, if you don't already have one. Install it using the following command:

`$ python3 -m pip3 install --user virtualenv`

Then you need to create a virtual environment. To create a virtual environment, go to your project’s directory and run virtualenv using the following command:

`$ python3 -m virtualenv env`

Before you can start installing or using packages in your virtualenv you’ll need to activate it. Run the following command to activate virtualenv:

`$ source env/bin/activate` 

Now, to install the required packages follow the instructions as mentioned under the section `System-wide installation`.

**Note:**
1. It is recommended to run `sudo apt-get update` before running the above commands.
2. If you don't have python3/pip3 installed, replace `python3`/`pip3` with `python`/`pip` and run the command.
3. If you like what you see give it a :star: .

***Thanks @palash25(Palash Nigam) for README.md design inspiration ^_^***
