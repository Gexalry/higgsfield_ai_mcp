"""Higgsfield AI MCP Server - HTTP entry point for Prefect Horizon deployment"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from dotenv import load_dotenv
load_dotenv()

from higgsfield_mcp.server import mcp

if __name__ == "__main__":
      port = int(os.environ.get("PORT", 8000))
      mcp.run(transport="streamable-http", host="0.0.0.0", port=port, path="/mcp")
