#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re

class Classifier:
	
	CADASTRO = 1
	RETUITE  = 2
	DESCONTO = 3
	NONE = 4
	
	@staticmethod
	def get_category(tweet):
	#TODO: Validar classificador
		category = {Classifier.CADASTRO:0, Classifier.RETUITE:0, Classifier.DESCONTO:0, Classifier.NONE : 1}
		
		lower = tweet.lower()
		if(lower.__contains__('cadastr')):
			if(lower.__contains__('sort') or lower.__contains__('http') or lower.__contains__('promo') or lower.__contains__('particip')):
				category[Classifier.CADASTRO] += 1
				category[Classifier.NONE] -= 1
			
		if(lower.__contains__('retuit')):
			category[Classifier.RETUITE] += 1
			category[Classifier.NONE] -= 1
			
		if(re.match('(.+) rt(.*)',lower,re.IGNORECASE)):
			if(lower.__contains__('dê') or lower.__contains__('de') or lower.__contains__('da') or lower.__contains__('sort') or lower.__contains__('http') or lower.__contains__('promo') or lower.__contains__('particip')):
				category[Classifier.RETUITE] += 1
				category[Classifier.NONE] -= 1
				
		if(re.match('(.*)[0-9]*(.*)%', lower, re.IGNORECASE)):
			category[Classifier.DESCONTO] += 1
			category[Classifier.NONE] -= 1
			
		if(lower.__contains__('descont')):
			category[Classifier.DESCONTO] += 1
			category[Classifier.NONE] -= 1
			
		if(re.match('(.*)((de)?)(.*)por(.*)(apenas)?[0-9](.*)', lower, re.IGNORECASE)):
			category[Classifier.DESCONTO] += 1
			category[Classifier.NONE] -= 1
		
		return sorted(category, key=lambda x : category[x], reverse=True)[0]
		
