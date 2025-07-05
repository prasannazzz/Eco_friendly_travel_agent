# eco_trip_planner/utils/carbon_utils.py

def estimate_co2(source: str, destination: str, modes: list) -> float:
    """
    Mock CO2 estimate for trip based on transport mode and approx distance.
    Replace with real APIs later for accuracy.
    """
    # Mocked average emissions (kg CO₂ per km)
    EMISSIONS = {
        "Flight": 0.255,     # average per passenger
        "Train": 0.041,
        "Bus": 0.105,
        "Rental Car": 0.192
    }

    # Approx distance (in km) – placeholder
    distance_km = 500

    total = 0.0
    for mode in modes:
        factor = EMISSIONS.get(mode, 0.1)
        total += factor * distance_km

    return total
