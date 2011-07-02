#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from promottion.twitter.tweet_entry import *
import urllib2, json

def index(request):
	dados = _minera_tweets()
	return render_to_response('index.html', {'tweets' : dados} )
	
def search(request):
	return render_to_response('search.html')

def _get_tweets(url):
	global list_tweets
	dados=json.load(urllib2.urlopen(url))
	
	for i in (dados[unicode("results")]):
		author = str(i[unicode("from_user")].encode("utf-8"))
		tweet = str(i[unicode("text")].encode("utf-8"))
		avatar = str(i[unicode("profile_image_url")].encode("utf-8"))
		uri = "http://twitter.com/" + str(i[unicode("from_user")].encode("utf-8"))
		list_tweets.append(TweetEntry(author, tweet, avatar, uri))

def _minera_tweets():
	global list_tweets
	list_tweets = []
	subject = ['promocao', 'desconto', 'gratis', 'cadastro', 'oferta', 'retuite']
	url='http://search.twitter.com/search.json?q={0}&rpp=10'  

	for i in subject:
		_get_tweets(url.format(i))
		
	return list_tweets
