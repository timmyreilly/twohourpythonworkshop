"""
Routes and views for the flask application.
"""

from datetime import datetime
import urllib
import urllib2
import json
from tokens import *

from flask import render_template, Flask, request, jsonify, make_response, abort
from FlaskWebProject import app

def binger(search_type, query):
    key = bing_token
    query = urllib.quote(query)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=5&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request)
    response_data = response.read()
    json_result = json.loads(response_data)
    print json.dumps(json_result, indent=4, sort_keys=True )
    
    

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
    
@app.route('/search/<string:search_type>/<string:query>', methods=['GET'])
def search(search_type, query):
    binger(search_type, query)
    return 'Sweet'

    
#result_list = json_result['d']['results']
#print result_list