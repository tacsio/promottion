#!/usr/bin/env python
#-*- coding:utf-8 -*-

class TweetEntry:
	
	def __init__(self,author, tweet, avatar, uri, category):
		self.__author = author
		self.__tweet = tweet
		self.__avatar = avatar
		self.__uri = uri
		self.__category = category
		self.__num_rt = 0
		self.__hash = tweet.__hash__()
	
	def __str__(self):
		return ("Author:" + self.__author + "\n" +
				"Tweet:" + self.__tweet + "\n" +
				"Avatar:" + self.__avatar + "\n" +
				"Uri:" + self.__uri + "\n" +
				"Category:" + str(self.__category) + "\n" +
				"Num RT:" + str(self.__num_rt)) + "\n"
	
	def get_author(self):
		return self.__author
		
	def get_uri(self):
		return self.__uri
		
	def get_avatar(self):
		return self.__avatar
		
	def get_tweet(self):
		return self.__tweet
	
	def get_category(self):
		return self.__category
	
	def get_hash(self):
		return self.__hash
		
	def get_num_rt(self):
		return self.__num_rt
		
	def retuited(self):
		self.__num_rt += 1
		
	#TODO: Métodos de atomacao de pag
