"""Agent factories and policy helpers.

Keep the package importable for offline policy tests. ADK is imported only when
an agent factory is actually requested.
"""
from __future__ import annotations

__all__ = [
    "create_blue_agent",
    "create_red_agent_default",
    "create_red_agent_advance",
    # aliases cũ
    "create_protected_agent",
    "create_unsafe_agent",
    "create_guards_agent",
    "test_agent",
    "check_secret_leak",
    "assess_untrusted_document",
    "authorize_guards_action",
]


def __getattr__(name: str):
    if name in {
        "create_blue_agent",
        "create_red_agent_default",
        "create_protected_agent",
        "create_unsafe_agent",
        "test_agent",
    }:
        from agents import agent
        return getattr(agent, name)
    if name in {
        "create_red_agent_advance",
        "create_guards_agent",
        "check_secret_leak",
        "assess_untrusted_document",
        "authorize_guards_action",
    }:
        from agents import guards_agent
        return getattr(guards_agent, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
