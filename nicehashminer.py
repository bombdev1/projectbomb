import requests
import time

# NiceHash API endpoint
API_URL = 'https://api2.nicehash.com/main/api/v2/mining/external/{ORG_ID}/rigs/stats'

# Your NiceHash organization ID
ORG_ID = '8b5b53a5-d6f2-4d17-a20e-4bd26f11c4d3'

# Your NiceHash API key
API_KEY = 'e73efc38-47e1-4954-92a2-99a78b40872a'

# Minimum profitability threshold in USD
MIN_PROFIT_THRESHOLD = 20.0

def get_profitability():
    headers = {
        'X-Organization-Id': ORG_ID,
        'X-Api-Key': API_KEY
    }
    try:
        response = requests.get(API_URL.format(ORG_ID=ORG_ID), headers=headers)
        if response.status_code == 200:
            data = response.json()
            if 'stats' in data:
                profitability = sum(rig['profitability'] for rig in data['stats'])
                return profitability
            else:
                print("Error: Unable to fetch profitability data.")
                return None
        else:
            print("Error: Unable to fetch data from NiceHash API. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error:", e)
        return None

def start_mining():
    print("Mining started!")

def stop_mining():
    print("Mining stopped!")

def main():
    while True:
        profitability = get_profitability()
        if profitability is not None:
            print("Current profitability:", profitability)
            if profitability >= MIN_PROFIT_THRESHOLD:
                start_mining()
            else:
                stop_mining()
        time.sleep(60)  # Fetch profitability every 60 seconds

if __name__ == '__main__':
    main()
