import os
import time

from unstract.llmwhisperer import LLMWhispererClientV2
from dotenv import load_dotenv
load_dotenv()

client = LLMWhispererClientV2(base_url='https://llmwhisperer-api.us-central.unstract.com/api/v2',
                              api_key=os.getenv('API_KEY'))


result = client.whisper(file_path='eregli_rapor.pdf')

while True:
    status = client.whisper_status(whisper_hash=result['whisper_hash'])
    if status['status'] == 'processed':
        resultx = client.whisper_retrieve(whisper_hash=result['whisper_hash'])
        break
    time.sleep(5)

extract_text = resultx['extraction']['result_text']

print(extract_text)

