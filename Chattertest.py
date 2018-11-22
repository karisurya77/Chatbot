# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:12:27 2018

@author: suryaprakash.rao
"""

import chatterbot
#import string


bot=chatterbot.ChatBot('ibot',trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
bot.train('chatterbot.corpus.english')

def bot1(qus):
    if qus=='N':
        ans="good Bye"
    else:
        ans=bot.get_response(qus)
    return(ans)
        