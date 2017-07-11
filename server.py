from flask import Flask , jsonify, Response
from main import getRawFeed, getFeed

app = Flask(__name__)

@app.route('/wsj',methods=['GET'])
def wsj():
    feed =  getFeed()
    return Response(feed, mimetype='text/plain')

if __name__=='__main__':
  HOST='127.0.0.1'
  PORT='4000'

  app.run(HOST,PORT)

