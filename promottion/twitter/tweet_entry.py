#!/usr/bin/env python
#-*- coding:utf-8 -*-

class TweetEntry:
	
	def __init__(self,author, tweet, avatar, uri):
		self.__author = author
		self.__tweet = tweet
		self.__avatar = avatar
		self.__uri = uri
	
	def __str__(self):
		return ("Author:" + self.__author + "\n" +
				"Tweet:" + self.__tweet + "\n" +
				"Avatar:" + self.__avatar + "\n" +
				"Uri:" + self.__uri) + "\n"
	
	def get_author(self):
		return self.__author
		
	def get_uri(self):
		return self.__uri
		
	def get_avatar(self):
		return self.__avatar
		
	def get_tweet(self):
		return self.__tweet
				
	#TODO: Métodos de atomacao de pag
