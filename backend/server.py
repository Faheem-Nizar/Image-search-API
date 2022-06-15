from flask import Flask
from flask import request
app = Flask(__name__)


from flickrapi import FlickrAPI
import json


KEY = '6f28e1f2db1124bbe22de887249bfac5'
SECRET = '0bd4bc4e11efec8'

SIZES = ["url_o", "url_k", "url_h", "url_l", "url_c"] 


def get_photos(image_tag):
    extras = ','.join(SIZES)
    flickr = FlickrAPI(KEY, SECRET)
    photos = flickr.walk(text=image_tag,  # it will search by image title and image tags
                            extras=extras,  # get the urls for each size we want
                            privacy_filter=1,  # search only for public photos
                            per_page=50,
                            sort='relevance')  # we want what we are looking for to appear first
    return photos

def get_url(photo):
    for i in range(len(SIZES)):  # makes sure the loop is done in the order we want
        url = photo.get(SIZES[i])
        if url:  # if url is None try with the next size
            return url


def get_urls(image_tag, max, iter):
    photos = get_photos(image_tag)
    counter=0
    urls=[]
    count = 0
    iteration = int(iter)

    for photo in photos:
        if counter < max:
            url = get_url(photo)  # get preffered size url
            if url:
                count += 1
                if(count >= 12*(iteration-1)):
                    urls.append(url)
                    counter += 1
            # if no url for the desired sizes then try with the next photo
        else:
            break
    jsondata = json.dumps(urls)
    return jsondata



@app.route("/api/photos")
def photos():
    tags = request.args.get('tags')
    iter = request.args.get('iter')
    print(tags)
    return get_urls(tags, 12, iter)

if __name__ == "__main__":
    app.run(debug=True)