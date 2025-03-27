# Weather MCP Server

A simple MCP (Model Control Protocol) server that provides weather information using the National Weather Service API. This server exposes two tools:

- `get_alerts`: Get weather alerts for a US state
- `get_forecast`: Get weather forecast for a specific location

## Prerequisites

- Python 3.10 or higher
- `uv` package manager (recommended) or `pip`

## Installation

1. Clone this repository:

```bash
git clone <your-repo-url>
cd simple_mcp_server
```

2. Set up your Python environment:

Using `uv` (recommended):

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
uv add "mcp[cli]" httpx
```

Or using `pip`:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install "mcp[cli]" httpx
```

## Usage

1. Run the server:

```bash
mcp dev main.py
```

2. Configure Claude for Desktop:

   - Open your Claude for Desktop App configuration at `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Add the following configuration:

   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "uv",
         "args": [
           "--directory",
           "/ABSOLUTE/PATH/TO/simple_mcp_server",
           "run",
           "main.py"
         ]
       }
     }
   }
   ```

   - Replace `/ABSOLUTE/PATH/TO/simple_mcp_server` with the actual path to your project directory
   - Save the file and restart Claude for Desktop

3. Test the server:
   - Open Claude for Desktop
   - Look for the hammer icon in the interface
   - You should see two tools listed: `get_alerts` and `get_forecast`
   - Try asking questions like:
     - "What's the weather in NY?"
     - "What are the active weather alerts in NY?"

## Available Tools

### get_alerts

Get weather alerts for a US state.

Parameters:

- `state` (str): Two-letter US state code (e.g., 'CA', 'NY')

### get_forecast

Get weather forecast for a specific location.

Parameters:

- `latitude` (float): Latitude of the location
- `longitude` (float): Longitude of the location

## Troubleshooting

1. If the server isn't being picked up by Claude for Desktop:

   - Make sure the configuration file path is correct
   - Verify that the absolute path in the configuration is correct
   - Ensure all dependencies are installed
   - Try restarting Claude for Desktop

2. If you get weather API errors:
   - Check your internet connection
   - Verify that the coordinates or state codes are valid
   - The National Weather Service API only works for US locations

