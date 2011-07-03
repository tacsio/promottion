#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from promottion.twitter.tweet_entry import *
from promottion.twitter.classifier import *
import urllib2, json

import datetime

def index(request):
	dados = __minera_tweets()
	top_tweets = __get_top_tweets(dados)
	return render_to_response('index.html', {'tweets' : dados, 'top_tweets' : top_tweets} )
	
def search(request):
	return render_to_response('search.html')

def __minera_tweets():
	global list_tweets
	list_tweets = []
	subject = ['promocao', 'desconto', 'gratis', 'cadastro', 'oferta', 'retuite']
	url='http://search.twitter.com/search.json?q={0}&rpp=100'  
	
	for i in subject:
		__get_tweets(url.format(i))
		
	return list_tweets

def __get_tweets(url):
	global list_tweets
	dados=json.load(urllib2.urlopen(url))
	redundance = []
	for i in (dados[unicode("results")]):
		tweet = str(i[unicode("text")].encode("utf-8"))
		if(tweet.__hash__() in redundance):
			for j in list_tweets:
				if(j.get_hash() == tweet.__hash__()):
					j.retuited()
		else:
			redundance.append(tweet.__hash__())
			author = str(i[unicode("from_user")].encode("utf-8"))
			avatar = str(i[unicode("profile_image_url")].encode("utf-8"))
			uri = "http://twitter.com/" + str(i[unicode("from_user")].encode("utf-8"))
			category = Classifier.get_category(tweet)
			if(category in [Classifier.CADASTRO, Classifier.RETUITE, Classifier.DESCONTO]):
				list_tweets.append(TweetEntry(author, tweet, avatar, uri, category))
				

def __get_top_tweets(list_tweets):
	return sorted(list_tweets, key=lambda entry : entry.get_num_rt(), reverse=True)[:10]
