## happy path
* greet
  - utter_greet
* ask_news
  - action_get_news
* thanks
  - utter_welcome


## bot challenge
* bot_challenge
  - utter_iamabot


## story 1
* greet
  - utter_greet
* ask_news{"query": "Buhari"}
  - slot{"query": "Buhari"}
  - action_get_news
  - utter_did_that_help
* affirm
  - utter_glad_to_help
* thanks
  - utter_welcome
  - action_check_subscribe{"subscribed": "False"}
  - slot{"subscribed": "False"}
  - utter_ask_subscribe
* affirm
    - action_subscribe
    - utter_anythingelse
* deny
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* ask_news{"query": "Drake"}
    - slot{"query": "Drake"}
    - action_get_news
    - utter_did_that_help
* affirm
