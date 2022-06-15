# Question 2, Flickr API

I have used flask backend with python, running in port 5000, with react frontend running in port 3000. 

## Installation

First, from the root directory, move to "assessment 2" folder, and then go to "backend". From here, run the commands:

### `sudo apt install python3.8-venv`
### `python3 -m venv env`
### `source env/bin/activate`
### `pip install flask`
### `pip install flickrapi`
### `python3 server.py`

Note: Make sure you have ubuntu installed (if in windows).

Now the backend is up and running. we cn now move to frontend. Go to "client" directory and run:

### `yarn install`
### `yarn start`

or

### `npm install`
### `npm start`

Now the frontend is also running. Now we can go to [http://localhost:3000], and test the app.

## Usage

To use the app, just type any keyword/keywords, seperated by comas, and press enter. You shall see 12 photos of the most relevant images pop up. To view more photos, you can click enter once more, or click on "show more". This will automatically display 12 more unique photos related to the search.
The backend has been designed to serve only this one client, in the case of showing more photos. Else can be used for multiple clients.