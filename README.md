# Discord Phone Lookup Bot

This Discord bot allows users to lookup phone number details, including country, carrier, and approximate IP location.

## Features
- Validate phone numbers using the NumVerify API
- Retrieve country, carrier, and location information
- Approximate IP lookup using IPInfo API
- Displays results in an embedded message on Discord

## Requirements
- Python 3.8+
- `discord.py`
- `requests`
- NumVerify API Key
- IPInfo API Key
- A Discord bot token

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/discord-phone-lookup.git
   cd discord-phone-lookup
   ```

2. Install dependencies:
   ```sh
   pip install discord requests
   ```

3. Configure environment variables or edit the script:
   - Replace `NUMVERIFY_API_KEY` with your NumVerify API key
   - Replace `IPINFO_API_KEY` with your IPInfo API key
   - Replace `Your_bot_token` with your Discord bot token

## Usage

1. Run the bot:
   ```sh
   python bot.py
   ```

2. Invite the bot to your Discord server.
3. Use the command:
   ```sh
   !lookup <phone_number>
   ```
   Example:
   ```sh
   !lookup +33612345678
   ```

## Notes
- Ensure your bot has message permissions in the Discord server.
- NumVerify free tier may have limitations.
- IPInfo API key is required for IP-based lookups.

## License
MIT License

