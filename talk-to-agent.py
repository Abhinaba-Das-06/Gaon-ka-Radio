# 1. Install
# macOS: brew install portaudio   ·   Ubuntu: apt-get install portaudio19-dev
pip install "sarvam-conv-ai-sdk[all]"

# 2. talk-to-agent.py
import asyncio
from pydantic import SecretStr
from sarvam_conv_ai_sdk import (
    AsyncSamvaadAgent, AsyncDefaultAudioInterface,
    InteractionConfig, InteractionType,
)

async def main():
    config = InteractionConfig(
        org_id="01a144b0-1327-7594-b9f8-75936d7bc6a4",
        workspace_id="01a144b0-132f-742e-a28a-0dddacbf9ce7",
        app_id="Conversatio-ca5efb29-b9fc",
        user_identifier="demo_user",
        interaction_type=InteractionType.CALL,
        sample_rate=16000,
        agent_variables={"call_summary": "<call_summary>", "reported_news": "<reported_news>", "user_name": "<user_name>"},
    )
    agent = AsyncSamvaadAgent(
        api_key=SecretStr("sk_k4j80dhq_bCXwCOxj1YBANhl32YG5XNZa"),
        config=config,
        audio_interface=AsyncDefaultAudioInterface(input_sample_rate=16000),
    )
    await agent.start()
    await agent.wait_for_disconnect()

asyncio.run(main())
