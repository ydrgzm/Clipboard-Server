# Clipboard-Server

A minimal MCP server to access and update your system clipboard programmatically.

## Features

- Get the current clipboard content via an MCP resource.
- Set clipboard content remotely using an MCP tool.

## Requirements

- Python 3.8+
- [pyperclip](https://pypi.org/project/pyperclip/)
- [fastmcp](https://github.com/modelcontext/fastmcp)

## Installation

```powershell
pip install pyperclip fastmcp
```

## Running the Server

```powershell
python clipboard_server.py
```

The server will start and expose clipboard operations via MCP.

## Usage

- **Get clipboard:**  
  Access the resource `clipboard://current` to fetch the current clipboard content.

- **Set clipboard:**  
  Use the `set_clipboard` tool with your desired content.

## Example

```python
import requests

# Example: Fetch clipboard content (replace with your actual MCP client code)
response = requests.get("http://localhost:8000/clipboard://current")
print(response.text)
```

## Integrating with Claude Desktop or VS Code Agent Mode

You can add this MCP server as a custom context provider in Claude Desktop or in VS Code agent mode:

### Claude Desktop
1. Open Claude Desktop settings.
2. Go to the "Context Providers" section.
3. Click "Add Provider" and enter the MCP server URL (e.g., `http://localhost:8000`).
4. Save and enable the provider. You can now use clipboard resources and tools from Claude Desktop.

### VS Code Agent Mode
1. Open the VS Code agent extension settings.
2. Locate the section for custom MCP servers or context providers.
3. Add the server URL: `http://localhost:8000`.
4. Save your settings. The clipboard server will now be available as a context provider in agent mode.

Refer to the documentation for your tool for more details on adding custom MCP servers.
