# config.py - Simplified version
import os

api_id = int(os.environ["API_ID"])  # Will crash if not set - ensures you must set it
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]
auth_users = [int(os.environ["AUTH_USER"])]
