import os
import json
# from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults


class GooglePlaceSearchTool:
    
    def __init__(self, api_key: str = None):
        # Set the environment variable if api_key is provided
        if api_key:
            os.environ["GPLACES_API_KEY"] = api_key
        
        # GooglePlacesAPIWrapper reads from GPLACES_API_KEY environment variable
        self.place_wrapper = GooglePlacesAPIWrapper()
        self.place_tool = GooglePlacesTool(api_wrapper=self.place_wrapper)
    
    def google_search_attractions(self, place: str) -> str:
        """Search for attractions in a given place using Google Places API."""
        return self.place_tool.run(f"top attractive place in and around {place}")
    
    def google_search_restaurants(self, place: str) -> str:
        """Search for restaurants in the specified location using Google Places API."""
        return self.place_tool.run(f"what are the top 10 restaurants and eateries in {place} with their ratings and reviews")
    
    def google_search_activities(self, place: str) -> str:
        """Search for popular activities in the specified place using Google Places API."""
        return self.place_tool.run(f"top activities in {place} with their ratings and reviews")
    
    def google_search_transportation(self, place: str) -> str:
        """Search for transportation options in the specified location using Google Places API."""
        return self.place_tool.run(f"what are the transportation options available in {place} with their ratings and reviews")
        
class TavilyPlaceSearchTool:
    
    def __init__(self):
        pass
    
    def tavily_place_search(self, query: str, category: str = None) -> str:
        """Search for places using Tavily search."""
        # This is a placeholder - implement based on your needs
        return f"Tavily search results for {query}"