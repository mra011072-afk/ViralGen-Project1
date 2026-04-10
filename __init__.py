"""
ViralGen AI - Utils Package
Marketing intelligence utilities for content generation
"""

from .api_client import MiniMaxAPIClient, create_api_client, check_api_credentials
from .prompts import (
    MARKETING_ARCHITECT_SYSTEM,
    generate_video_scripts_prompt,
    generate_psych_profile_prompt,
    generate_usp_prompt
)

__all__ = [
    "MiniMaxAPIClient",
    "create_api_client",
    "check_api_credentials",
    "MARKETING_ARCHITECT_SYSTEM",
    "generate_video_scripts_prompt",
    "generate_psych_profile_prompt",
    "generate_usp_prompt"
]
