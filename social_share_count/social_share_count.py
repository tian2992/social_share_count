# -*- coding: utf-8 -*-
import os
import logging
import flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from urllib.parse import quote
import twitter
from social_share_count.database import init_db, db_session
from social_share_count.models import Metrique

"""Main module."""

# import configparser
# config = configparser.ConfigParser()
# # User level config file.
# read_files = config.read(os.path.expanduser('~/.config/ocdsdata/config.ini'))
# CONSUMER_KEY = config.get('TW_CONSUMER_KEY', 'HOSTNAME')

CONSUMER_KEY = os.environ.get('TW_CONSUMER_KEY', '')
CONSUMER_SECRET = os.environ.get('TW_CONSUMER_SECRET', '')
ACCESS_TOKEN_KEY = os.environ.get('TW_ACCESS_TOKEN_KEY', '')
ACCESS_TOKEN_SECRET = os.environ.get('TW_ACCESS_TOKEN_SECRET', '')
BASEURL = os.environ.get('BASEURL', '')

tw_api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET)
tw_api.VerifyCredentials()

init_db()
app = flask.Flask(__name__)
CORS(app)

def format_url(url):
    triml = url.lstrip("https://")
    trimr = triml.rstrip("/")
    if trimr.startswith(BASEURL):
        return trimr
    return ""


def get_twitter_shares(uri):
    query = "count=100&q={}".format(quote(uri, safe=''))
    results = tw_api.GetSearch(raw_query=query)
    return len(results)


@app.route('/api/tw/urls/count.json')
def fetch_twitter_shares():
    url_query = request.args['url']
    url_clean = format_url(url_query)
    try:
        shares = get_twitter_shares(url_clean)
        m = Metrique(service="twitter_tweets",
                     url=url_clean,
                     value=shares)
        db_session.add(m)
        db_session.commit()
    except:
        logging.exception('Twitter fetch Fail')
        shares = -1
    resp = {"url":url_clean, "count": shares}
    return jsonify(resp)


@app.after_request
def add_header(response):
    response.cache_control.public = True
    response.cache_control.max_age = 3600
    return response
