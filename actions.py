# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="aac1749d71c1403e9c3be7b474fc8e0f")



# country_list = [ae, ar, at, au, be, bg, br, ca, ch, cn, co, cu, cz, de, eg, fr, gb, gr, hk, gu
# id, ie, il, in, it, jp, kr, lt, lv, ma, mx, my, ng, nl, no, nz, ph, pl, pt, ro, rs, ru, sa, se,
# sg, si, sk, th, tr, tw, ua, us, ve, za]

class ActionGetNews(Action):

    def name(self):
        return "action_get_news"

    def run(self, dispatcher, tracker, domain):

        query = tracker.get_slot("query")
        source = tracker.get_slot("source")
        category = tracker.get_slot("category")
        country = tracker.get_slot("country")
    
        if source and (country or category):
            values_dict = {"q":query, "source": source, "category": category, "country": country}
            values_dict["source"] = None
            top_headlines = newsapi.get_top_headlines(**values_dict)
            dispatcher.utter_message(text="Here is what I found")
            if top_headlines["totalResults"] > 5:
                for i in range(0, 5):
                    dispatcher.utter_message(text=top_headlines["articles"][i]["title"])
                    dispatcher.utter_message(image=top_headlines["articles"][i]["urlToImage"])
                    dispatcher.utter_message(text=top_headlines["articles"][i]["description"])
                    dispatcher.utter_message(text="Read more here:"+ top_headlines["articles"][i]["url"])
                    # dispatcher.utter_message(template="utter_urlToImage", url=top_headlines["articles"][i]["url"])
            else:
                for i in range(0, top_headlines["totalResults"]):
                    dispatcher.utter_message(text=top_headlines["articles"][i]["title"])
                    dispatcher.utter_message(image=top_headlines["articles"][i]["urlToImage"])
                    dispatcher.utter_message(text=top_headlines["articles"][i]["description"])
                    dispatcher.utter_message(text="Read more here:"+ top_headlines["articles"][i]["url"])
                    dispatcher.utter_message(template="utter_urlToImage", url=top_headlines["articles"][i]["url"]) 
        else:
            values_dict2 = {"q":query, "source": source, "category": category,
            "country": country}
            top_headlines2 = newsapi.get_top_headlines(**values_dict2)
            dispatcher.utter_message(text="Here is what I found")
            
            if top_headlines2["totalResults"] > 5:
                for i in range(0, 5):
                    dispatcher.utter_message(text=top_headlines2["articles"][i]["title"])
                    dispatcher.utter_message(image=top_headlines2["articles"][i]["urlToImage"])
                    dispatcher.utter_message(text=top_headlines2["articles"][i]["description"])
                    dispatcher.utter_message(text="Read more here:"+ top_headlines2["articles"][i]["url"])
                    # dispatcher.utter_message(template="utter_urlToImage", url=top_headlines2["articles"][i]["url"])
            else:
                for i in range(0, top_headlines["totalResults"]):
                    dispatcher.utter_message(text=top_headlines2["articles"][i]["title"])
                    dispatcher.utter_message(image=top_headlines2["articles"][i]["urlToImage"])
                    dispatcher.utter_message(text=top_headlines2["articles"][i]["description"])
                    dispatcher.utter_message(text="Read more here:"+ top_headlines2["articles"][i]["url"])
                    dispatcher.utter_message(template="utter_urlToImage", url=top_headlines2["articles"][i]["url"])

        return [SlotSet("query", None)]

class ActionSlotReset(Action):
    def name(self):
        return "action_slot_reset"

    def run(self, dispatcher, tracker, domain):
        return[
            SlotSet("query", None),
            SlotSet("category", None),
            SlotSet("country", None),
            SlotSet("source", None)
        ]