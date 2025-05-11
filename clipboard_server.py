from mcp.server.fastmcp import FastMCP
import pyperclip

mcp = FastMCP("Clipboard Server")

@mcp.resource("clipboard://current")
def get_clipboard() -> str:
    """Get the current clipboard content"""
    return pyperclip.paste()


@mcp.tool()
def set_clipboard(content: str) -> str:
    """Set the clipboard content and add to history"""
    pyperclip.copy(content)
    return "Clipboard updated."

server = mcp

if __name__ == "__main__":
    mcp.run()
