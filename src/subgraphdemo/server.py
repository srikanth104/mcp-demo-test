from mcp.server.mcpserver import MCPServer


mcp = MCPServer("enterprise-tools")

@mcp.tool()
def analyze_project(project_type: str) -> dict:
    """
    Analyze a software project and return basic architecture recommendations.
    """

    recommendations = {
        "python": [
            "Use layered architecture",
            "Separate API, service, and repository layers",
            "Use dependency injection",
            "Add unit and integration tests",
        ],
        "android": [
            "Use MVVM or Clean Architecture",
            "Separate UI, domain, and data layers",
            "Use repositories for data access",
            "Use ViewModel for presentation state",
        ],
        "agentic-ai": [
            "Separate agent orchestration from tools",
            "Use MCP for external capabilities",
            "Add model routing",
            "Add observability and tracing",
            "Enforce authorization at the tool boundary",
        ],
    }

    return {
        "project_type": project_type,
        "recommendations": recommendations.get(
            project_type.lower(),
            ["Define clear architecture boundaries"]
        ),
    }


@mcp.tool()
def check_python_version() -> dict:
    """
    Check the Python version used by the MCP server.
    """
    import sys

    return {
        "python_version": sys.version,
        "major": sys.version_info.major,
        "minor": sys.version_info.minor,
    }