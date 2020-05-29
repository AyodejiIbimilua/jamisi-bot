## greet
* greet
    - utter_greet

## goodbye
* goodbye
    - utter_goodbye

## thanks
* thanks
    - utter_welcome

## chitchat
* chitchat
    - respond_chitchat

## bot challenge
* bot_challenge
    - utter_iamabot

## okay
* okay
    - utter_okay

## out of scope
* out_of_scope
    - action_default_fallback
* out_of_scope
    - action_default_fallback
* out_of_scope
    - utter_help_message

## Ask news without query
* greet
    - utter_greet
* ask_news
    - utter_ask_topic
* inform{"query": "Obama"}
    - slot{"query": "Obama"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* deny
    - utter_rephrase_your_query
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": false}
    - slot{"subscribed": false}
    - utter_ask_subscribe
* affirm
    - action_subscribe
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## Ask news without query 2
* greet
    - utter_greet
* ask_news
    - utter_ask_topic
* inform{"query": "Obama"}
    - slot{"query": "Obama"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* affirm
    - utter_ask_whatelse
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": false}
    - slot{"subscribed": false}
    - utter_ask_subscribe
* affirm
    - action_subscribe
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## happy path + satisfied + nothing else + non subscriber
* greet
    - utter_greet
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": false}
    - slot{"subscribed": false}
    - utter_ask_subscribe
* affirm
    - action_subscribe
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## happy path + satisfied + something else + non subscriber
* greet
    - utter_greet
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* affirm
    - utter_ask_whatelse
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": false}
    - slot{"subscribed": false}
    - utter_ask_subscribe
* affirm
    - action_subscribe
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## sad path + not satisfied + nothing else + non subscriber
* greet
    - utter_greet
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* deny
    - utter_rephrase_your_query
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": false}
    - slot{"subscribed": false}
    - utter_ask_subscribe
* affirm
    - action_subscribe
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## sad path + not satisfied + something else + non subscriber
* greet
    - utter_greet
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* deny
    - utter_rephrase_your_query
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* affirm
    - utter_ask_whatelse
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": false}
    - slot{"subscribed": false}
    - utter_ask_subscribe
* affirm
    - action_subscribe
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## happy path + satisfied + nothing else + subscriber
* greet
    - utter_greet
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": true}
    - slot{"subscribed": true}
* goodbye
    - utter_goodbye

## happy path + satisfied + something else + non subscriber
* greet
    - utter_greet
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* affirm
    - utter_ask_whatelse
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": true}
    - slot{"subscribed": true}
* goodbye
    - utter_goodbye

## sad path + not satisfied + nothing else + non subscriber
* greet
    - utter_greet
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* deny
    - utter_rephrase_your_query
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": true}
    - slot{"subscribed": true}
* goodbye
    - utter_goodbye

## sad path + not satisfied + something else + non subscriber
* greet
    - utter_greet
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* deny
    - utter_rephrase_your_query
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* affirm
    - utter_ask_whatelse
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": true}
    - slot{"subscribed": true}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* ask_news{"query": "Covid"}
    - slot{"query": "Covid"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* affirm
    - utter_ask_whatelse
* ask_news{"query": "Funke Akindele"}
    - slot{"query": "Funke Akindele"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* deny
    - utter_rephrase_your_query
* ask_news{"query": "Yaradua"}
    - slot{"query": "Yaradua"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": true}
    - slot{"subscribed": true}
* goodbye
    - utter_goodbye

## interactive_story_2
* ask_news{"query": "DBanj"}
    - slot{"query": "DBanj"}
    - action_get_news
    - action_slot_reset
    - slot{"query": null}
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe
    - slot{"subscribed": false}
    - utter_ask_subscribe
* affirm
    - action_subscribe
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## ask subscribe
* greet
    - utter_greet
* ask_news{"query": "DBanj"}
    - slot{"query": "DBanj"}
    - action_get_news
    - action_slot_reset
    - slot{"query": null}
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe
    - slot{"subscribed": false}
    - utter_ask_subscribe
* deny
    - utter_okay
* goodbye
    - utter_goodbye

## Ask News Negative
* greet
    - utter_greet
* ask_news{"query": "TD Jakes"}
    - slot{"query": "TD Jakes"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* affirm
    - utter_ask_whatelse
* ask_news{"query": "Christmas"}
    - slot{"query": "Christmas"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* deny
    - utter_rephrase_your_query
* ask_news{"query": "Bill Gates"}
    - slot{"query": "Bill Gates"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe{"subscribed": true}
    - slot{"subscribed": true}
* goodbye
    - utter_goodbye

## New Story

* ask_news{"ORG":"Buhari","query":"Buhari"}
    - slot{"query":"Buhari"}
    - action_get_news
    - action_slot_reset
    - slot{"query":null}
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* deny
    - action_check_subscribe
    - slot{"subscribed":false}
    - utter_ask_subscribe
* affirm
    - action_subscribe
* goodbye
    - utter_goodbye
