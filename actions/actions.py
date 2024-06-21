from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import logging
import json

logger = logging.getLogger(__name__)

class ActionHandlePredictionModel(Action):
    def name(self) -> Text:
        print("I am inside-1")
        return "action_handle_prediction_model"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("I am inside-2")
        number_of_products = tracker.get_slot("number_of_products")
        print("Number of products:", type(number_of_products))
        
        if not number_of_products:
            dispatcher.utter_message(response="utter_ask_number_of_products")
            print("I am inside-3")
            return []
        
        url = "https://f00c-14-195-25-38.ngrok-free.app/process_data"
        # api_key = "f659e822bd9f2072adcf19736335b5f57b1f44c9dde92e5ac9aa931ed5634d62"

        headers = {
            "Content-Type": "application/json"
        }

        payload = json.dumps({
            "number": number_of_products
            })
        
        try:
            print("I am inside-4")
            response = requests.request("POST", url, headers=headers, data=payload)
            # response = requests.post(api_url, json={"number_of_products": number_of_products}, headers=headers)
            print("API Response:", response.text)
            # Process API response here
            response_data = response.json()
            success_percentage = response_data.get('Success Percentage', 'N/A')
            failure_percentage = response_data.get('Failure Percentage', 'N/A')
            predicted_cost = response_data.get('Predicted_Cost', 'N/A')
            accuracy = response_data.get('Accuracy', 'N/A')

            message = (
                f"Here's my prediction for {number_of_products} products:\n"
                f"Predicted cost is {predicted_cost} and the prediction score is {success_percentage}"
            )

            dispatcher.utter_message(text=message)
        except requests.exceptions.RequestException as e:
            dispatcher.utter_message(text=f"Error calling the API: {str(e)}")

        return []
