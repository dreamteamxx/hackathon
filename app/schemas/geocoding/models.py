from dataclasses import dataclass


@dataclass
class Feature:
    center: list
    geometry: dict


@dataclass
class Geocoding:
    type: str
    query: list
    features: list[Feature]
    attribution: str
