import os
import requests

BASE_URL = "https://raw.githubusercontent.com/twilio/twilio-oai/952411590cde787d02b7d4267df101dde85b9a1d/spec/json/"

FILE_NAMES = [
 "twilio_accounts_v1.json",
    "twilio_api_v2010.json",
    "twilio_assistants_v1.json",
    "twilio_bulkexports_v1.json",
    "twilio_chat_v1.json",
    "twilio_chat_v2.json",
    "twilio_chat_v3.json",
    "twilio_content_v1.json",
    "twilio_content_v2.json",
    "twilio_conversations_v1.json",
    "twilio_events_v1.json",
    "twilio_flex_v1.json",
    "twilio_flex_v2.json",
    "twilio_frontline_v1.json",
    "twilio_iam_organizations.json",
    "twilio_iam_v1.json",
    "twilio_insights_v1.json",
    "twilio_intelligence_v2.json",
    "twilio_ip_messaging_v1.json",
    "twilio_ip_messaging_v2.json",
    "twilio_knowledge_v1.json",
    "twilio_lookups_v1.json",
    "twilio_lookups_v2.json",
    "twilio_marketplace_v1.json",
    "twilio_messaging_v1.json",
    "twilio_messaging_v2.json",
    "twilio_microvisor_v1.json",
    "twilio_monitor_v1.json",
    "twilio_monitor_v2.json",
    "twilio_notify_v1.json",
    "twilio_numbers_v1.json",
    "twilio_numbers_v2.json",
    "twilio_oauth_v1.json",
    "twilio_preview.json",
    "twilio_pricing_v1.json",
    "twilio_pricing_v2.json",
    "twilio_proxy_v1.json",
    "twilio_routes_v2.json",
    "twilio_serverless_v1.json",
    "twilio_studio_v1.json",
    "twilio_studio_v2.json",
    "twilio_supersim_v1.json",
    "twilio_sync_v1.json",
    "twilio_taskrouter_v1.json",
    "twilio_trunking_v1.json",
    "twilio_trusthub_v1.json",
    "twilio_verify_v2.json",
    "twilio_video_v1.json",
    "twilio_voice_v1.json",
    "twilio_wireless_v1.json"
]

def download_twilio_openapi():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_folder = os.path.join(base_dir, "docs")

    os.makedirs(output_folder, exist_ok=True)

    for file_name in FILE_NAMES:
        url = BASE_URL + file_name
        print(f"Downloading: {url}")
        response = requests.get(url)

        if response.status_code == 200:
            file_path = os.path.join(output_folder, file_name)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"Saved: {file_name} in {output_folder}")
        else:
            print(f"Failed to download {file_name} (status {response.status_code})")

if __name__ == "__main__":
    download_twilio_openapi()
