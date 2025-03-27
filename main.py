from mcp.server.fastmcp import FastMCP
from helpers.helpers import (
    NWS_API_BASE,
    make_request_to_national_weather_service,
    format_alert,
)

# Initialize the mcp server
mcp = FastMCP("Weather MCP Server")


@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alerts for a US state

    Args:
        state (str): The two-letter state code (e.g., 'CA', 'NY')
    """

    url = f"{NWS_API_BASE}/alerts/active/area/{state}"

    data = await make_request_to_national_weather_service(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found"

    if not data["features"]:
        return "No active alerts found for the specified state"

    alerts = [format_alert(feature) for feature in data["features"]]

    return "\n\n".join(alerts)


@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    # First get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_request_to_national_weather_service(points_url)

    if not points_data:
        return "Unable to fetch forecast data for this location."

    # Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_request_to_national_weather_service(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    # Format the periods into a readable forecast
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
            {period['name']}:
            Temperature: {period['temperature']}°{period['temperatureUnit']}
            Wind: {period['windSpeed']} {period['windDirection']}
            Forecast: {period['detailedForecast']}
        """
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)


if __name__ == "__main__":
    #initialize and run the MCP server
    mcp.run(transport='stdio')
