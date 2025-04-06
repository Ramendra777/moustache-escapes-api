from pydantic import BaseModel
from typing import List, Optional

class Property(BaseModel):
    name: str
    latitude: float
    longitude: float

class LocationQuery(BaseModel):
    query: str

class PropertyResult(BaseModel):
    property: Property
    distance_km: float

class ApiResponse(BaseModel):
    results: List[PropertyResult]
    processing_time_ms: float
    corrected_query: Optional[str] = None