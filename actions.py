# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.e

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="aac1749d71c1403e9c3be7b474fc8e0f")

top_headlines = newsapi.get_top_headlines()

country_list = [ae, ar, at, au, be, bg, br, ca, ch, cn, co, cu, cz, de, eg, fr, gb, gr, hk, gu
id, ie, il, in, it, jp, kr, lt, lv, ma, mx, my, ng, nl, no, nz, ph, pl, pt, ro, rs, ru, sa, se,
sg, si, sk, th, tr, tw, ua, us, ve, za]

class ActionGetNews(Action):

    def name(self):
        return "action_get_news"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(text="Hello World!")

        return []


country
query
source
category
country, query
country, source
country, category
query, source
query, category
source, category
country, query, source
country, query, category
country, source,category
query, source, category

def performsearch():
    return("print hey")
    