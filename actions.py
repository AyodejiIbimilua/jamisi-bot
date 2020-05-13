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
            "country": country, "page_size":100}
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


import requests

url = "https://microsoft-azure-bing-news-search-v1.p.rapidapi.com/search"

querystring = {"q":"Robert T Kiyosaki", "mkt":"en-US"}

headers = {
    'x-rapidapi-host': "microsoft-azure-bing-news-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "62f069db3amsh7a4af5f3cb21c69p1ddf82jsn30dd7882d4a8"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)