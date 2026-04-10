"""
MiniMax API Client for ViralGen AI
Handles all API interactions with MiniMax Chat API
"""

import json
import requests
from typing import Dict, Optional, Any
import streamlit as st


class MiniMaxAPIClient:
    """Client for interacting with MiniMax Chat API"""

    def __init__(self, api_key: str, group_id: str, base_url: str = "https://api.minimax.chat/v1"):
        """
        Initialize the MiniMax API client

        Args:
            api_key: MiniMax API key
            group_id: MiniMax Group ID
            base_url: Base URL for API (default: https://api.minimax.chat/v1)
        """
        self.api_key = api_key
        self.group_id = group_id
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def generate_completion(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        model: str = "MiniMax-Text-01",
        temperature: float = 0.7,
        max_tokens: int = 2000
    ) -> Dict[str, Any]:
        """
        Generate completion from MiniMax API

        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            model: Model to use
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens to generate

        Returns:
            Dict containing the API response
        """
        messages = []

        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })

        messages.append({
            "role": "user",
            "content": prompt
        })

        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(
                f"{self.base_url}/text/chatcompletion_v2",
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return {"error": "Request timed out. Please try again.", "success": False}
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "success": False}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response from API", "success": False}

    def parse_response(self, response: Dict[str, Any]) -> Optional[str]:
        """
        Parse the API response to extract the generated text

        Args:
            response: API response dictionary

        Returns:
            Generated text or None if error
        """
        if "error" in response:
            return None

        try:
            choices = response.get("choices", [])
            if choices and len(choices) > 0:
                return choices[0].get("message", {}).get("content", "")
            return None
        except (KeyError, IndexError):
            return None


def create_api_client() -> Optional[MiniMaxAPIClient]:
    """
    Create MiniMax API client from Streamlit secrets or st.session_state

    Returns:
        MiniMaxAPIClient instance or None if credentials not available
    """
    # Try to get credentials from Streamlit secrets first
    try:
        api_key = st.secrets.get("MINIMAX_API_KEY", "")
        group_id = st.secrets.get("MINIMAX_GROUP_ID", "")
    except Exception:
        api_key = ""
        group_id = ""

    # Fallback to session state
    if not api_key:
        api_key = st.session_state.get("minimax_api_key", "")
    if not group_id:
        group_id = st.session_state.get("minimax_group_id", "")

    if api_key and group_id:
        return MiniMaxAPIClient(api_key=api_key, group_id=group_id)

    return None


def check_api_credentials(api_key: str, group_id: str) -> bool:
    """
    Validate API credentials by making a test request

    Args:
        api_key: MiniMax API key
        group_id: MiniMax Group ID

    Returns:
        True if credentials are valid, False otherwise
    """
    if not api_key or not group_id:
        return False

    client = MiniMaxAPIClient(api_key=api_key, group_id=group_id)
    response = client.generate_completion(
        prompt="Hello, respond with 'OK' if you can hear me.",
        max_tokens=10
    )

    return "error" not in response
