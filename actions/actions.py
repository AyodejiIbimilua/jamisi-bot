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

from requests import request
import re
import datetime
class ActionGetNews(Action):

    def name(self):
        return "action_get_news"

    def slot_mappings(self):
        return {
            "query": [
                self.from_entity(entity="query"),
                self.from_intent(intent="ask_news")
            ]
        }

    def run(self, dispatcher, tracker, domain):

        url = "https://microsoft-azure-bing-news-search-v1.p.rapidapi.com/search"
        headers = {
            'x-rapidapi-host': "microsoft-azure-bing-news-search-v1.p.rapidapi.com",
            'x-rapidapi-key': "62f069db3amsh7a4af5f3cb21c69p1ddf82jsn30dd7882d4a8"
            }

        query = tracker.get_slot("query")
        querystring = {"q":query, "mkt":"en-US", "count": 200}
        response = request("GET", url, headers=headers, params=querystring)
        data = response.json()
        raw_date = datetime.datetime.now()
        pattern = raw_date.strftime("%Y-%m-%d")
        count = len(data["value"])

        if count>0:
            if count > 5:
                dispatcher.utter_message(text="Here's what I've got for you:\n \n ")
                for i in range(0, 5):
                    if re.match(pattern, data["value"][i]["datePublished"]):
                        # dispatcher.utter_message(text=data["value"][i]["name"])
                        # dispatcher.utter_message(image=data["value"][i]["image"]["thumbnail"]["contentUrl"])
                        # dispatcher.utter_message(text=data["value"][i]["description"])
                        dispatcher.utter_message(text=data["value"][i]["url"])
            else:
                dispatcher.utter_message(text="Here's what I've got for you:\n \n ")
                for i in range(0, count):
                    if re.match(pattern, data["value"][i]["datePublished"]):
                        # dispatcher.utter_message(text=data["value"][i]["name"])
                        # dispatcher.utter_message(image=data["value"][i]["image"]["thumbnail"]["contentUrl"])
                        # dispatcher.utter_message(text=data["value"][i]["description"])
                        dispatcher.utter_message(text=data["value"][i]["url"])
        else:
            dispatcher.utter_message(text="No top news for " + query + " at this moment")
        

        return []

class ActionSlotReset(Action):
    def name(self):
        return "action_slot_reset"

    def run(self, dispatcher, tracker, domain):
        return[
            SlotSet("query", None)
        ]

class ActionSubscribe(Action):
    def name(self):
        return "action_subscribe"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(text="You have been succesfully subscribed to my daily news.")
        return[]

class ActionCheckSubscribe(Action):
    def name(self):
        return "action_check_subscribe"

    def run(self, dispatcher, tracker, domain):

        subscribe = False
        return[
            SlotSet("subscribed", subscribe)
        ]