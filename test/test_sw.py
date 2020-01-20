import requests
import unittest
from unittest import TestCase
from unittest.mock import MagicMock


class ApiSwapi:
    def __init__(self, requests):
        self.requests = requests

    def get_total_count_of(self, people_or_planet):
        basic_url = 'https://swapi.co/api/'
        data = self.requests.get(f'{basic_url}{people_or_planet}')
        parsed_data = data.json()
        number_in_data = parsed_data.get('count')
        return number_in_data
    

        

class SwapiTests(unittest.TestCase):
    def setUp(self):
        self.my_data = MagicMock()
        self.my_request = MagicMock()
        self.my_request.get.return_value = self.my_data
        self.api_swapi = ApiSwapi(self.my_request)

    def test_get_total_number_of_people(self):
        fake_data = {'count': 87} # number_in_data        
        self.my_data.json.return_value = fake_data 
                
        expected_result = 87

        result = self.api_swapi.get_total_count_of('people')

        assert result == expected_result
        self.my_request.get.assert_called_once_with('https://swapi.co/api/people')
    
    def test_get_total_number_of_planets(self):
        fake_data = {'count': 61}
        self.my_data.json.return_value = fake_data

        expected_result = 61

        result = self.api_swapi.get_total_count_of('planets')

        assert result == expected_result
        self.my_request.get.assert_called_once_with('https://swapi.co/api/planets')



    







        