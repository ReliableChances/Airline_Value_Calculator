# Content: Mock Data, VPM Calculator, Core Algorithm, Streamlit Deployment

# Mock Data
mock_data = [
    {'origin': 'JFK', 'destination': 'LIS', 'date': '2025-07-01', 'miles': 20000, 'fees': 50, 'cash_value': 400},
    {'origin': 'LIS', 'destination': 'BCN', 'date': '2025-07-02', 'miles': 10000, 'fees': 30, 'cash_value': 150},
    {'origin': 'JFK', 'destination': 'BCN', 'date': '2025-07-01', 'miles': 45000, 'fees': 90, 'cash_value': 500},
    {'origin': 'JFK', 'destination': 'CDG', 'date': '2025-07-01', 'miles': 22000, 'fees': 60, 'cash_value': 420},
    {'origin': 'CDG', 'destination': 'BCN', 'date': '2025-07-02', 'miles': 9000, 'fees': 25, 'cash_value': 130},
]


# VPM Calculator
def VPM (price, tax, miles):
    return ((price * (1 - tax/100))/miles)