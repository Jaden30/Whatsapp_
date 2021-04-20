from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests 
app = Flask(__name__)

# turning it to lower because we 

url = ('https://newsapi.org/v2/top-headlines?'
       'country=uk&'
       'apiKey=575d1aa3b7474ee8bc0e86204ea5f89d')
@app.route('/bot', methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
  
    if "news" in incoming_msg:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["author"]} {data["title"]} {data["content"]}'
        else: 
            quote = "No news today"

        msg.body(quote)
        responded = True

    if not responded : 
        msg.body("Guess you do not want the news")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)



