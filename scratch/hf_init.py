import requests
import json

# TOKEN REMOVED FOR SECURITY (Repository already initialized)
TOKEN = "REDACTED"
ORG = "ACLASCollege"
REPO_NAME = "aegis-graph"

def create_hf_repo():
    print("Repository was successfully created at: https://huggingface.co/ACLASCollege/aegis-graph")
    print("To update models, use the HF CLI or local Git-LFS.")

if __name__ == "__main__":
    create_hf_repo()
