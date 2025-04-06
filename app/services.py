from geopy.distance import geodesic
from rapidfuzz import process, fuzz
import requests
from typing import List, Optional, Tuple
from .models import Property, PropertyResult

# Property data
PROPERTIES = [
    Property(name="Moustache Udaipur Luxuria", latitude=24.57799888, longitude=73.68263271),
    # ... (all other properties from the assignment)
]

class LocationService:
    def __init__(self):
        self.location_cache = {
            "sissu": (32.4357785, 77.18518717),
            "kokshar": (32.4357785, 77.18518717),
        }
    
    def geocode_location(self, location_name: str) -> Optional[Tuple[float, float]]:
        """Convert location name to coordinates"""
        try:
            # Check cache first
            if location_name.lower() in self.location_cache:
                return self.location_cache[location_name.lower()]
            
            # Use Nominatim geocoding
            url = f"https://nominatim.openstreetmap.org/search?q={location_name}&format=json"
            headers = {'User-Agent': 'MoustacheEscapes/1.0'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            if data:
                lat = float(data[0]['lat'])
                lon = float(data[0]['lon'])
                # Cache the result
                self.location_cache[location_name.lower()] = (lat, lon)
                return (lat, lon)
        except Exception:
            return None
    
    def fuzzy_match_location(self, input_name: str) -> Optional[str]:
        """Handle spelling mistakes using fuzzy matching"""
        known_locations = list(self.location_cache.keys())
        if not known_locations:
            return None
        
        best_match, score = process.extractOne(
            input_name.lower(),
            known_locations,
            scorer=fuzz.WRatio
        )
        
        return best_match if score > 80 else None
    
    def find_nearby_properties(self, coords: Tuple[float, float], max_km: float = 50) -> List[PropertyResult]:
        """Find properties within given radius"""
        results = []
        for prop in PROPERTIES:
            distance = geodesic(coords, (prop.latitude, prop.longitude)).kilometers
            if distance <= max_km:
                results.append(PropertyResult(property=prop, distance_km=distance))
        
        results.sort(key=lambda x: x.distance_km)
        return results