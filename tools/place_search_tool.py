import os
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from dotenv import load_dotenv
from langchain.tools import tool 

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        # The Google Places helper reads GPLACES_API_KEY (plural); keep names consistent
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()
        
    def _setup_tools(self)->List:
        """Setup all tools for the place search tool"""
        @tool 
        def search_attractions(place:str)->str:
            """Search attractions of a place"""
            try:
                attraction_results = self.google_places_search.google_search_attractions(place)
                if attraction_results:
                    return f"Top attractions in {place} are: {attraction_results}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_place_search(place)
                return f"Tavily search results for attractions in {place} are: {tavily_result}"
        
        @tool
        def search_restaurants(place:str)-> str:
            """Search restaurants of a place"""
            try:
                restaurant_results = self.google_places_search.google_search_restaurants(place)
                if restaurant_results:
                    return f"Top restaurants in {place} are: {restaurant_results}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_place_search(place, category="restaurant")
                return f"Tavily search results for restaurants in {place} are: {tavily_result}"
            
        @tool 
        def search_activities(place:str)-> str:
            """Search activities of a place"""
            try:
                activity_results = self.google_places_search.google_search_activities(place)
                if activity_results:
                    return f"Top activities in {place} are: {activity_results}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_place_search(place, category="activities")
                return f"Tavily search results for activities in {place} are: {tavily_result}"
            
        @tool 
        def search_transportation(place:str)-> str:
            """Search transportation options of a place"""
            try:
                transportation_results = self.google_places_search.google_search_transportation(place)
                if transportation_results:
                    return f"Transportation options in {place} are: {transportation_results}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_place_search(place, category="transportation")
                return f"Tavily search results for transportation in {place} are: {tavily_result}"
            
        return [search_attractions, search_restaurants, search_activities, search_transportation]