from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import time
from .models import LocationQuery, ApiResponse
from .services import LocationService

app = FastAPI(
    title="Moustache Escapes Property Locator",
    description="API to find nearby Moustache properties based on customer locations",
    version="1.0.0"
)

# Enable CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

location_service = LocationService()

@app.post("/find-nearby-properties", response_model=ApiResponse)
async def find_nearby_properties(query: LocationQuery):
    start_time = time.time()
    corrected_query = None
    
    # Step 1: Try to geocode the exact query
    target_coords = location_service.geocode_location(query.query)
    
    # Step 2: If exact geocoding fails, try fuzzy matching
    if target_coords is None:
        corrected_name = location_service.fuzzy_match_location(query.query)
        if corrected_name:
            corrected_query = corrected_name
            target_coords = location_service.geocode_location(corrected_name)
    
    # Step 3: If still no coordinates, return empty response
    if target_coords is None:
        return ApiResponse(
            results=[],
            processing_time_ms=(time.time() - start_time) * 1000,
            corrected_query=corrected_query
        )
    
    # Step 4: Calculate distances and filter properties
    results = location_service.find_nearby_properties(target_coords)
    
    return ApiResponse(
        results=results,
        processing_time_ms=(time.time() - start_time) * 1000,
        corrected_query=corrected_query
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}