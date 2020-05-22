## greet
* greet
  - utter_greet

## goodbye
* goodbye
  - utter_goodbye

## thanks
* thanks
  - utter_welcome

## asknews
* ask_news{"query": "Christmas"}
  - slot{"query": "Christmas"}
  - action_get_news
  - action_slot_reset
  - utter_did_that_help

## chitchat
* chitchat
  - respond_chitchat

## bot challenge
* bot_challenge
  - utter_iamabot

## out of scope
* out_of_scope
  - action_default_fallback

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
  - action_check_subscribe{"subscribed": true}
  - slot{"subscribed": true}
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
  - action_check_subscribe{"subscribed": true}
  - slot{"subscribed": true}
  - utter_ask_subscribe
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
  - action_check_subscribe{"subscribed": true}
  - slot{"subscribed": true}
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* ask_news{"query": "CORONA VIRUS"}
    - slot{"query": "CORONA VIRUS"}
    - action_get_news
    - action_slot_reset
    - utter_did_that_help
* affirm
    - utter_glad_to_help
    - utter_anythingelse
* affirm
    - utter_ask_whatelse
* ask_news{"query": "FUNKE AKINDELE"}
    - slot{"query": "FUNKE AKINDELE"}
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
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye
