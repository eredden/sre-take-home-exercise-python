import asyncio
import aiohttp
import yaml
import time
from datetime import timedelta
from collections import defaultdict

# Function to load configuration from the YAML file
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to perform health checks
async def check_health(endpoint):
    url = endpoint['url']
    method = endpoint.get('method', 'GET')
    headers = endpoint.get('headers', None)
    body = endpoint.get('body', None)

    try:
        async with aiohttp.ClientSession() as session:
            response = await session.request(method, url, headers=headers, data=body, timeout=0.5)

            if 200 <= response.status < 300:
                return "UP"
            else:
                return "DOWN"
            
    except Exception:
        return "DOWN"

# Main function to monitor endpoints
async def monitor_endpoints(file_path):
    config = load_config(file_path)
    domain_stats = defaultdict(lambda: {"up": 0, "total": 0})

    # Update the domain statistics with availability data from one endpoint
    async def update_domain_stats(endpoint):
        domain = endpoint["url"].split("//")[-1].split("/")[0].split(":")[0]
        result = await check_health(endpoint)

        domain_stats[domain]["total"] += 1
        if result == "UP":
            domain_stats[domain]["up"] += 1

    while True:
        tasks = [update_domain_stats(endpoint) for endpoint in config]
        await asyncio.gather(*tasks)

        # Log cumulative availability percentages
        for domain, stats in domain_stats.items():
            availability = round((stats["up"] / stats["total"]) * 100)
            print(f"{domain} has {availability}% availability percentage.")
        
        print(f"The timestamp is {time.strftime("%Y/%m/%d %H:%M:%S")}.")
        print("---")
        time.sleep(15)

# Entry point of the program
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python monitor.py <config_file_path>")
        sys.exit(1)

    config_file = sys.argv[1]
    try:
        asyncio.run(monitor_endpoints(config_file))
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")