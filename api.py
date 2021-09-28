from flask import Flask, request
import requests

url = "https://api.iconfinder.com/v4/icons/search"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer X0vjEUN6KRlxbp2DoUkyHeM0VOmxY91rA6BbU5j3Xu6wDodwS0McmilLPBWDUcJ1"
}

app = Flask(__name__)

@app.route("/", methods=['POST'])
def geticon():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print(data)
            name = data["name"]
            option = data["option"]
            size = data["size"]

            querystring = {"query":name,"count":str(option)}
            response = requests.request("GET", url, headers=headers, params=querystring)
            res = response.json()
            icons = res["icons"]
            
            return icons[option-1]["raster_sizes"][size]["formats"][0]["preview_url"]
        except:
            return ""

app.run(host="localhost", port=5001, debug=True)
