#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python hello.py <env_name>")
        sys.exit(1)

    env_name = sys.argv[1]

    valid_envs = {"tst", "psr", "prod-na", "prod-eu"}
    if env_name not in valid_envs:
        print(f"ERROR: '{env_name}' is not valid. Must be one of {sorted(valid_envs)}")
        sys.exit(1)

    print(f"Hello world from {env_name} environment!")

if __name__ == "__main__":
    main()
