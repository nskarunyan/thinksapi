#!/usr/bin/env python3
import argparse
import requests
import sys

def parse_dynamic_args(args_list):
    """Converts --key value pairs into a dictionary."""
    args_dict = {}
    key = None
    for item in args_list:
        if item.startswith('--'):
            key = item[2:]
        elif key:
            args_dict[key] = item
            key = None
        else:
            print(f"[ERROR] Unexpected argument format: {item}")
            sys.exit(1)

    if key is not None:
        print(f"[ERROR] Value missing for argument: --{key}")
        sys.exit(1)

    return args_dict

def make_api_request(url, payload):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "User-Agent": "curl/7.81.0"
    }

    try:
        response = requests.post(url, data=payload, headers=headers, timeout=10)
        print(f"Status Code: {response.status_code}")
        print("Response Text:")
        print(response.text)
    except requests.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Dynamic Things Mobile API CLI Tool")
    parser.add_argument("--url", required=True, help="Full Things Mobile API URL (e.g., https://api.thingsmobile.com/services/business-api/activateSim)")
    
    # This captures all other args as a list of key-value pairs
    args, unknown = parser.parse_known_args()
    dynamic_args = parse_dynamic_args(unknown)

    make_api_request(args.url, dynamic_args)

if __name__ == "__main__":
    main()

