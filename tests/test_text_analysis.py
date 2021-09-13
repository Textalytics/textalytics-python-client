import json
import os
from unittest import TestCase

from textalytics_core.resources import TextInput

from textalytics_client.text_analysis import Client

SAMPLE_TEXT = "We went to Contoso Steakhouse located at midtown NYC last week for a dinner party, and we adore the spot! They provide marvelous food and they have a great menu. The chief cook happens to be the owner (I think his name is John Doe) and he is super nice, coming out of the kitchen and greeted us all. We enjoyed very much dining in the place! The Sirloin steak I ordered was tender and juicy, and the place was impeccably clean. You can even pre-order from their online menu at www.contososteakhouse.com, call 312-555-0176 or send email to order@contososteakhouse.com! The only complaint I have is the food didn't come fast enough. Overall I highly recommend it!"

class TestClient(TestCase):
    def test_extract_entities(self):
        language = "en"
        url = os.environ["TEXTALYTICS_ENDPOINT"]
        username = os.environ["TEXTALYTICS_USERNAME"]
        password = os.environ["TEXTALYTICS_PASSWORD"]

        client = Client(service_base_url=url, username=username, password=password)
        text_input = TextInput(source_text=SAMPLE_TEXT, source_language=language)
        extract_entities_response = client.extract_entities(text_input=text_input)
        if extract_entities_response.status_code == 200:
            extracted_entities = extract_entities_response.json()
            for extracted_entity in extracted_entities["entities"]:
                print(extracted_entity["entity"])
                print(extracted_entity["label"])
