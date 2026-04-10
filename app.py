"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                           VIRALGEN AI - MARKETING ARCHITECT                  ║
║                          Transform Product Ideas Into Viral Assets          ║
╚══════════════════════════════════════════════════════════════════════════════╝

A world-class AI-powered marketing intelligence platform that generates:
- 3 High-Retention Video Scripts for TikTok/Reels
- Comprehensive Psychological Customer Profiles
- Killer Unique Selling Propositions (USPs)

Author: MiniMax Agent
Version: 1.0.0
"""

import streamlit as st
import json
import time
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.api_client import MiniMaxAPIClient, check_api_credentials
from utils.prompts import (
    generate_video_scripts_prompt,
    generate_psych_profile_prompt,
    generate_usp_prompt
)

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="ViralGen AI - Marketing Architect",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# CUSTOM CSS - PREMIUM DARK MODE WITH GOLD & PLATINUM ACCENTS
# =============================================================================

def load_premium_css():
    """Load premium dark mode CSS with gold and platinum accents"""

    st.markdown("""
    <style>
    /* ═══════════════════════════════════════════════════════════════════
       PREMIUM THEME CONFIGURATION
    ═══════════════════════════════════════════════════════════════════ */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@400;500;600;700&display=swap');

    :root {
        /* Dark Mode Foundation */
        --bg-primary: #0A0A0F;
        --bg-secondary: #12121A;
        --bg-tertiary: #1A1A24;
        --bg-card: #16161F;
        --bg-surface: #1E1E28;

        /* Gold Accents */
        --gold-primary: #D4AF37;
        --gold-light: #F4E4BA;
        --gold-dark: #AA8C2C;
        --gold-glow: rgba(212, 175, 55, 0.3);

        /* Platinum Accents */
        --platinum-primary: #E5E4E2;
        --platinum-light: #F8F8FF;
        --platinum-dark: #A8A8A8;

        /* Status Colors */
        --success: #00D26A;
        --error: #FF4757;
        --info: #5B9BD5;
        --warning: #FFB800;

        /* Gradients */
        --gold-gradient: linear-gradient(135deg, #D4AF37 0%, #F4E4BA 50%, #D4AF37 100%);
        --dark-gradient: linear-gradient(180deg, #0A0A0F 0%, #12121A 100%);
    }

    /* ═══════════════════════════════════════════════════════════════════
       GLOBAL STYLES
    ═══════════════════════════════════════════════════════════════════ */

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html, body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background: var(--bg-primary);
        color: var(--platinum-primary);
        line-height: 1.6;
        overflow-x: hidden;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: var(--bg-secondary);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--gold-dark);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--gold-primary);
    }

    /* ═══════════════════════════════════════════════════════════════════
       HEADER & NAVIGATION
    ═══════════════════════════════════════════════════════════════════ */

    .header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 70px;
        background: rgba(10, 10, 15, 0.95);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(212, 175, 55, 0.1);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 40px;
        z-index: 1000;
    }

    .logo {
        display: flex;
        align-items: center;
        gap: 12px;
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--platinum-light);
    }

    .logo-icon {
        width: 40px;
        height: 40px;
        background: var(--gold-gradient);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        box-shadow: 0 4px 15px var(--gold-glow);
    }

    .nav-links {
        display: flex;
        gap: 32px;
        list-style: none;
    }

    .nav-link {
        color: var(--platinum-dark);
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        position: relative;
    }

    .nav-link:hover {
        color: var(--gold-primary);
    }

    .nav-link::after {
        content: '';
        position: absolute;
        bottom: -4px;
        left: 0;
        width: 0;
        height: 2px;
        background: var(--gold-gradient);
        transition: width 0.3s ease;
    }

    .nav-link:hover::after {
        width: 100%;
    }

    /* ═══════════════════════════════════════════════════════════════════
       MAIN CONTAINER
    ═══════════════════════════════════════════════════════════════════ */

    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 100px 40px 60px;
    }

    /* ═══════════════════════════════════════════════════════════════════
       HERO SECTION
    ═══════════════════════════════════════════════════════════════════ */

    .hero-section {
        text-align: center;
        padding: 60px 0 80px;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(212, 175, 55, 0.1);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 50px;
        padding: 8px 20px;
        font-size: 0.85rem;
        color: var(--gold-primary);
        margin-bottom: 24px;
        animation: pulse-glow 3s ease-in-out infinite;
    }

    @keyframes pulse-glow {
        0%, 100% { box-shadow: 0 0 20px rgba(212, 175, 55, 0.1); }
        50% { box-shadow: 0 0 30px rgba(212, 175, 55, 0.3); }
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 700;
        line-height: 1.1;
        margin-bottom: 24px;
        background: linear-gradient(135deg, var(--platinum-light) 0%, var(--gold-light) 50%, var(--platinum-light) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: var(--platinum-dark);
        max-width: 700px;
        margin: 0 auto 40px;
        line-height: 1.8;
    }

    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 60px;
        margin-top: 50px;
    }

    .stat-item {
        text-align: center;
    }

    .stat-value {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--gold-primary);
    }

    .stat-label {
        font-size: 0.9rem;
        color: var(--platinum-dark);
        margin-top: 4px;
    }

    /* ═══════════════════════════════════════════════════════════════════
       INPUT SECTION
    ═══════════════════════════════════════════════════════════════════ */

    .input-section {
        background: var(--bg-card);
        border-radius: 24px;
        padding: 40px;
        margin: 40px 0;
        border: 1px solid rgba(212, 175, 55, 0.1);
        position: relative;
        overflow: hidden;
    }

    .input-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: var(--gold-gradient);
    }

    .input-label {
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--platinum-light);
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .input-label-icon {
        color: var(--gold-primary);
    }

    /* Custom Text Area */
    .custom-textarea {
        width: 100%;
        background: var(--bg-secondary);
        border: 2px solid rgba(212, 175, 55, 0.1);
        border-radius: 16px;
        padding: 20px;
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: var(--platinum-primary);
        resize: vertical;
        min-height: 150px;
        transition: all 0.3s ease;
    }

    .custom-textarea:focus {
        outline: none;
        border-color: var(--gold-primary);
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
    }

    .custom-textarea::placeholder {
        color: var(--platinum-dark);
    }

    .char-counter {
        text-align: right;
        font-size: 0.85rem;
        color: var(--platinum-dark);
        margin-top: 8px;
    }

    .char-counter.warning {
        color: var(--warning);
    }

    .char-counter.error {
        color: var(--error);
    }

    /* ═══════════════════════════════════════════════════════════════════
       BUTTONS
    ═══════════════════════════════════════════════════════════════════ */

    .generate-btn {
        width: 100%;
        padding: 18px 32px;
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        border: none;
        border-radius: 14px;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        position: relative;
        overflow: hidden;
        margin-top: 24px;
    }

    .generate-btn.primary {
        background: var(--gold-gradient);
        color: var(--bg-primary);
        box-shadow: 0 8px 30px var(--gold-glow);
    }

    .generate-btn.primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(212, 175, 55, 0.4);
    }

    .generate-btn.primary:active {
        transform: translateY(0);
    }

    .generate-btn:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        transform: none !important;
    }

    .btn-icon {
        font-size: 1.3rem;
    }

    /* ═══════════════════════════════════════════════════════════════════
       TABS
    ═══════════════════════════════════════════════════════════════════ */

    .tabs-container {
        display: flex;
        gap: 8px;
        background: var(--bg-secondary);
        padding: 8px;
        border-radius: 16px;
        margin: 30px 0;
    }

    .tab-btn {
        flex: 1;
        padding: 16px 24px;
        background: transparent;
        border: none;
        border-radius: 12px;
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        font-weight: 500;
        color: var(--platinum-dark);
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }

    .tab-btn:hover {
        color: var(--platinum-primary);
        background: rgba(255, 255, 255, 0.05);
    }

    .tab-btn.active {
        background: var(--bg-card);
        color: var(--gold-primary);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    .tab-icon {
        font-size: 1.2rem;
    }

    .tab-count {
        background: var(--gold-dark);
        color: var(--bg-primary);
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    .tab-btn.active .tab-count {
        background: var(--gold-primary);
    }

    /* ═══════════════════════════════════════════════════════════════════
       RESULTS CARDS
    ═══════════════════════════════════════════════════════════════════ */

    .results-section {
        margin-top: 40px;
    }

    .result-card {
        background: var(--bg-card);
        border-radius: 20px;
        padding: 28px;
        margin-bottom: 24px;
        border: 1px solid rgba(212, 175, 55, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .result-card:hover {
        border-color: rgba(212, 175, 55, 0.3);
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.3);
    }

    .result-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: var(--gold-gradient);
    }

    .result-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
    }

    .result-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: var(--platinum-light);
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .result-badge {
        background: var(--gold-dark);
        color: var(--bg-primary);
        padding: 4px 12px;
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    .result-content {
        color: var(--platinum-primary);
        line-height: 1.8;
        font-size: 1rem;
    }

    .result-content p {
        margin-bottom: 16px;
    }

    .result-content strong {
        color: var(--gold-primary);
    }

    .result-content ul, .result-content ol {
        margin: 16px 0;
        padding-left: 24px;
    }

    .result-content li {
        margin-bottom: 10px;
    }

    .copy-btn {
        background: rgba(212, 175, 55, 0.1);
        border: 1px solid rgba(212, 175, 55, 0.3);
        color: var(--gold-primary);
        padding: 8px 16px;
        border-radius: 10px;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .copy-btn:hover {
        background: var(--gold-primary);
        color: var(--bg-primary);
    }

    /* ═══════════════════════════════════════════════════════════════════
       SCRIPT SPECIFIC STYLES
    ═══════════════════════════════════════════════════════════════════ */

    .script-card {
        background: var(--bg-secondary);
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
        border-left: 4px solid var(--gold-primary);
    }

    .script-section {
        margin-bottom: 20px;
    }

    .script-section:last-child {
        margin-bottom: 0;
    }

    .script-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: var(--gold-primary);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .script-content {
        color: var(--platinum-primary);
        line-height: 1.7;
    }

    .hashtag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 12px;
    }

    .hashtag {
        background: rgba(212, 175, 55, 0.1);
        color: var(--gold-light);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
    }

    /* ═══════════════════════════════════════════════════════════════════
       PROFILE SPECIFIC STYLES
    ═══════════════════════════════════════════════════════════════════ */

    .profile-section {
        background: var(--bg-secondary);
        border-radius: 12px;
        padding: 20px;
        margin: 16px 0;
    }

    .profile-section-title {
        font-size: 1rem;
        font-weight: 600;
        color: var(--gold-primary);
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .pain-point, .trigger {
        background: rgba(212, 175, 55, 0.05);
        border-left: 3px solid var(--gold-dark);
        padding: 12px 16px;
        margin: 8px 0;
        border-radius: 0 8px 8px 0;
    }

    /* ═══════════════════════════════════════════════════════════════════
       USP SPECIFIC STYLES
    ═══════════════════════════════════════════════════════════════════ */

    .usp-headline {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 700;
        background: var(--gold-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 16px;
    }

    .proof-point {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 12px;
        background: rgba(0, 210, 106, 0.05);
        border-radius: 10px;
        margin: 8px 0;
    }

    .proof-icon {
        color: var(--success);
        font-size: 1.2rem;
    }

    .tagline-option {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        color: var(--platinum-light);
        padding: 16px;
        background: var(--bg-secondary);
        border-radius: 10px;
        text-align: center;
        margin: 8px 0;
        border: 1px solid rgba(212, 175, 55, 0.2);
    }

    .power-word {
        display: inline-block;
        background: rgba(212, 175, 55, 0.15);
        color: var(--gold-light);
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 0.9rem;
        margin: 4px;
    }

    /* ═══════════════════════════════════════════════════════════════════
       LOADING STATES
    ═══════════════════════════════════════════════════════════════════ */

    .loading-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 60px 20px;
    }

    .loading-spinner {
        width: 60px;
        height: 60px;
        border: 3px solid rgba(212, 175, 55, 0.2);
        border-top-color: var(--gold-primary);
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    .loading-text {
        margin-top: 20px;
        font-size: 1.1rem;
        color: var(--platinum-dark);
    }

    .loading-dots::after {
        content: '';
        animation: dots 1.5s steps(4, end) infinite;
    }

    @keyframes dots {
        0%, 20% { content: ''; }
        40% { content: '.'; }
        60% { content: '..'; }
        80%, 100% { content: '...'; }
    }

    /* ═══════════════════════════════════════════════════════════════════
       SETTINGS SIDEBAR
    ═══════════════════════════════════════════════════════════════════ */

    .settings-section {
        background: var(--bg-card);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        border: 1px solid rgba(212, 175, 55, 0.1);
    }

    .settings-title {
        font-size: 1rem;
        font-weight: 600;
        color: var(--platinum-light);
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .settings-label {
        font-size: 0.9rem;
        color: var(--platinum-dark);
        margin-bottom: 8px;
    }

    /* ═══════════════════════════════════════════════════════════════════
       FOOTER
    ═══════════════════════════════════════════════════════════════════ */

    .footer {
        text-align: center;
        padding: 40px 20px;
        border-top: 1px solid rgba(212, 175, 55, 0.1);
        margin-top: 60px;
    }

    .footer-text {
        color: var(--platinum-dark);
        font-size: 0.9rem;
    }

    .footer-brand {
        color: var(--gold-primary);
        font-weight: 600;
    }

    /* ═══════════════════════════════════════════════════════════════════
       TOAST NOTIFICATIONS
    ═══════════════════════════════════════════════════════════════════ */

    .toast {
        position: fixed;
        bottom: 30px;
        right: 30px;
        padding: 16px 24px;
        background: var(--bg-card);
        border-radius: 12px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        display: flex;
        align-items: center;
        gap: 12px;
        animation: slideIn 0.3s ease;
        z-index: 9999;
    }

    .toast.success {
        border-color: var(--success);
    }

    .toast.error {
        border-color: var(--error);
    }

    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    /* ═══════════════════════════════════════════════════════════════════
       STREAMLIT OVERRIDES
    ═══════════════════════════════════════════════════════════════════ */

    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Streamlit element styling */
    .stTextArea textarea {
        background: var(--bg-secondary) !important;
        border: 2px solid rgba(212, 175, 55, 0.1) !important;
        border-radius: 16px !important;
        color: var(--platinum-primary) !important;
        font-size: 1rem !important;
        padding: 16px !important;
    }

    .stTextArea textarea:focus {
        border-color: var(--gold-primary) !important;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2) !important;
    }

    .stButton > button {
        background: var(--gold-gradient) !important;
        color: var(--bg-primary) !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 14px 32px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 30px var(--gold-glow) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 40px rgba(212, 175, 55, 0.4) !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: var(--bg-secondary);
        padding: 8px;
        border-radius: 16px;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        padding: 12px 24px;
        color: var(--platinum-dark);
    }

    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 0.05);
        color: var(--platinum-primary);
    }

    .stTabs [aria-selected="true"] {
        background: var(--bg-card) !important;
        color: var(--gold-primary) !important;
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        background: var(--bg-card);
        border-radius: 12px;
        border: 1px solid rgba(212, 175, 55, 0.1);
    }

    /* Success/Error boxes */
    .success-box, .info-box {
        background: rgba(0, 210, 106, 0.1);
        border: 1px solid var(--success);
        border-radius: 12px;
        padding: 16px;
        margin: 16px 0;
    }

    .error-box {
        background: rgba(255, 71, 87, 0.1);
        border: 1px solid var(--error);
        border-radius: 12px;
        padding: 16px;
        margin: 16px 0;
    }

    /* ═══════════════════════════════════════════════════════════════════
       RESPONSIVE DESIGN
    ═══════════════════════════════════════════════════════════════════ */

    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }

        .hero-stats {
            flex-direction: column;
            gap: 24px;
        }

        .tabs-container {
            flex-direction: column;
        }

        .nav-links {
            display: none;
        }

        .main-container {
            padding: 80px 20px 40px;
        }
    }
    </style>
    """, unsafe_allow_html=True)


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def show_toast(message: str, type: str = "success"):
    """Display a toast notification"""
    if type == "success":
        st.success(message)
    elif type == "error":
        st.error(message)
    elif type == "info":
        st.info(message)


def format_json_output(text: str) -> str:
    """Format JSON text for better readability"""
    try:
        # Try to find JSON in the text
        import re
        json_match = re.search(r'\[.*\]|\{.*\}', text, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            parsed = json.loads(json_str)
            return json.dumps(parsed, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, re.error):
        pass
    return text


def copy_to_clipboard(text: str):
    """Copy text to clipboard using JavaScript"""
    import json
    js = f"""
    <script>
    navigator.clipboard.writeText({json.dumps(text)}).then(function() {{
        console.log('Copying to clipboard was successful!');
    }}, function(err) {{
        console.error('Could not copy text: ', err);
    }});
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)


def render_markdown_safe(text: str):
    """Render markdown safely in Streamlit"""
    import re
    # Clean up common JSON artifacts
    text = re.sub(r'```json\s*', '', text)
    text = re.sub(r'```\s*', '', text)
    text = text.strip()

    # Try to parse as JSON and render nicely
    try:
        # Find JSON array or object
        json_match = re.search(r'(\[[\s\S]*\]|\{[\s\S]*\})', text)
        if json_match:
            json_str = json_match.group()
            parsed = json.loads(json_str)

            if isinstance(parsed, list):
                for i, item in enumerate(parsed):
                    render_result_item(item, i + 1)
            elif isinstance(parsed, dict):
                render_result_item(parsed, 1)

            # Render any text after JSON
            after_json = text[json_match.end():].strip()
            if after_json:
                st.markdown(after_json)
        else:
            st.markdown(text)
    except json.JSONDecodeError:
        st.markdown(text)


def render_result_item(item: dict, index: int):
    """Render a single result item based on its content"""

    # Determine type of content
    if "script_number" in item or "script_type" in item:
        # Video Script
        render_video_script(item)
    elif "customer_persona" in item or "demographics" in item:
        # Psychological Profile
        render_psych_profile(item)
    elif "main_usp" in item or "taglines" in item:
        # USP
        render_usp(item)
    else:
        # Generic content
        st.markdown(f"""
        <div class="result-card">
            <div class="result-content">
                {item_to_markdown(item)}
            </div>
        </div>
        """, unsafe_allow_html=True)


def item_to_markdown(item: dict, indent: int = 0) -> str:
    """Convert dictionary to markdown string"""
    md = ""
    for key, value in item.items():
        formatted_key = key.replace("_", " ").title()
        if isinstance(value, dict):
            md += f"<strong>{formatted_key}:</strong><br>"
            md += item_to_markdown(value, indent + 1)
        elif isinstance(value, list):
            md += f"<strong>{formatted_key}:</strong><br>"
            for v in value:
                if isinstance(v, dict):
                    md += f"&nbsp;&nbsp;• {item_to_markdown(v, indent + 1)}"
                else:
                    md += f"&nbsp;&nbsp;• {v}<br>"
        else:
            md += f"<strong>{formatted_key}:</strong> {value}<br>"
    return md


def render_video_script(script: dict):
    """Render a video script card"""
    script_num = script.get("script_number", script.get("number", ""))
    script_type = script.get("script_type", "")
    title = script.get("title", "")
    hook = script.get("hook", "")
    main_content = script.get("main_content", "")
    cta = script.get("call_to_action", "")
    sound = script.get("trending_sound", "")
    hashtags = script.get("hashtags", [])
    why_works = script.get("why_it_works", "")

    hashtags_html = ""
    if hashtags:
        hashtag_strs = [f"<span class='hashtag'>{h}</span>" for h in hashtags if isinstance(h, str)]
        hashtags_html = "<div class='hashtag-container'>" + "".join(hashtag_strs) + "</div>"

    st.markdown(f"""
    <div class="script-card">
        <div class="result-header">
            <div class="result-title">
                <span class="result-badge">SCRIPT {script_num}</span>
                {title}
            </div>
            <span style="color: var(--gold-primary); font-size: 0.85rem;">{script_type}</span>
        </div>

        <div class="script-section">
            <div class="script-label">🎬 Hook (First 3-5 Seconds)</div>
            <div class="script-content">{hook}</div>
        </div>

        <div class="script-section">
            <div class="script-label">📝 Main Content</div>
            <div class="script-content">{main_content}</div>
        </div>

        <div class="script-section">
            <div class="script-label">📣 Call to Action</div>
            <div class="script-content">{cta}</div>
        </div>

        <div class="script-section">
            <div class="script-label">🎵 Trending Sound</div>
            <div class="script-content">{sound}</div>
        </div>

        {hashtags_html}

        {"<div class='script-section' style='margin-top: 16px; padding-top: 16px; border-top: 1px solid rgba(212, 175, 55, 0.1);'><div class='script-label'>💡 Why It Works</div><div class='script-content' style='color: var(--gold-light);'>" + why_works + "</div></div>" if why_works else ""}
    </div>
    """, unsafe_allow_html=True)


def render_psych_profile(profile: dict):
    """Render a psychological profile"""
    persona = profile.get("customer_persona", "")
    demographics = profile.get("demographics", {})
    psychographics = profile.get("psychographics", {})
    pain_points = profile.get("pain_points", [])
    triggers = profile.get("buying_triggers", [])
    objections = profile.get("objection_handlers", [])
    decision_journey = profile.get("decision_journey", "")
    emotional_lang = profile.get("emotional_language", [])
    trusted = profile.get("influencers_trusted", [])
    secret = profile.get("secret_desires", [])

    st.markdown(f"""
    <div class="result-card">
        <div class="result-header">
            <div class="result-title">
                <span style="font-size: 2rem; margin-right: 12px;">👤</span>
                {persona}
            </div>
        </div>

        <div class="profile-section">
            <div class="profile-section-title">📊 Demographics</div>
            <div style="color: var(--platinum-primary);">
                {" • ".join([f"<strong>{k.replace('_', ' ').title()}:</strong> {v}" for k, v in demographics.items() if isinstance(v, str)]) if isinstance(demographics, dict) else demographics}
            </div>
        </div>

        <div class="profile-section">
            <div class="profile-section-title">🎯 Psychographics</div>
            <div style="color: var(--platinum-primary);">
                {" • ".join([f"<strong>{k.replace('_', ' ').title()}:</strong> {v}" for k, v in psychographics.items() if isinstance(v, str)]) if isinstance(psychographics, dict) else psychographics}
            </div>
        </div>

        <div class="profile-section">
            <div class="profile-section-title">😰 Pain Points</div>
            {"".join([f"<div class='pain-point'>{p}</div>" for p in pain_points if isinstance(p, str)])}
        </div>

        <div class="profile-section">
            <div class="profile-section-title">🔥 Buying Triggers</div>
            {"".join([f"<div class='trigger'>{t}</div>" for t in triggers if isinstance(t, str)])}
        </div>

        <div class="profile-section">
            <div class="profile-section-title">🛡️ Objection Handlers</div>
            {"".join([f"<div class='trigger'>{o}</div>" for o in objections if isinstance(o, str)])}
        </div>

        <div class="profile-section">
            <div class="profile-section-title">💬 Emotional Language</div>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                {"".join([f"<span class='power-word'>{w}</span>" for w in emotional_lang if isinstance(w, str)])}
            </div>
        </div>

        <div class="profile-section">
            <div class="profile-section-title">✨ Secret Desires</div>
            {"".join([f"<div class='trigger'>{s}</div>" for s in secret if isinstance(s, str)])}
        </div>

        {"<div class='profile-section'><div class='profile-section-title'>🛤️ Decision Journey</div><div style='color: var(--platinum-primary);'>" + decision_journey + "</div></div>" if decision_journey else ""}
    </div>
    """, unsafe_allow_html=True)


def render_usp(usp: dict):
    """Render a USP card"""
    main_usp = usp.get("main_usp", "")
    sub_usp = usp.get("sub_usp", "")
    proof_points = usp.get("proof_points", [])
    emotional = usp.get("emotional_hook", "")
    diff = usp.get("competitor_differentiation", "")
    risk = usp.get("risk_reversal", "")
    urgency = usp.get("urgency_element", "")
    taglines = usp.get("taglines", [])
    power_words = usp.get("power_words", [])
    pitch = usp.get("elevator_pitch", "")

    proof_html = ""
    if proof_points:
        proof_items = []
        for p in proof_points:
            if isinstance(p, dict):
                proof_items.append(f"<div class='proof-point'><span class='proof-icon'>✓</span><span>{list(p.values())[0] if p else p}</span></div>")
            else:
                proof_items.append(f"<div class='proof-point'><span class='proof-icon'>✓</span><span>{p}</span></div>")
        proof_html = "<div class='profile-section'><div class='profile-section-title'>📈 Proof Points</div>" + "".join(proof_items) + "</div>"

    taglines_html = ""
    if taglines:
        tagline_items = [f"<div class='tagline-option'>\"{t}\"</div>" for t in taglines if isinstance(t, str)]
        taglines_html = "<div class='profile-section'><div class='profile-section-title'>✨ Tagline Options</div>" + "".join(tagline_items) + "</div>"

    st.markdown(f"""
    <div class="result-card">
        <div class="result-header">
            <div class="result-title">
                <span style="font-size: 2rem; margin-right: 12px;">💎</span>
                KILLER USP
            </div>
        </div>

        <div class="profile-section" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.05) 100%); border: 1px solid rgba(212, 175, 55, 0.2);">
            <div class="usp-headline">{main_usp}</div>
            <div style="color: var(--platinum-primary); font-size: 1.05rem;">{sub_usp}</div>
        </div>

        {proof_html}

        <div class="profile-section">
            <div class="profile-section-title">❤️ Emotional Hook</div>
            <div style="color: var(--gold-light); font-size: 1.05rem;">{emotional}</div>
        </div>

        <div class="profile-section">
            <div class="profile-section-title">⚡ Urgency Element</div>
            <div style="color: var(--platinum-primary);">{urgency}</div>
        </div>

        <div class="profile-section">
            <div class="profile-section-title">🛡️ Risk Reversal</div>
            <div style="color: var(--platinum-primary);">{risk}</div>
        </div>

        <div class="profile-section">
            <div class="profile-section-title">🔄 Competitor Differentiation</div>
            <div style="color: var(--platinum-primary);">{diff}</div>
        </div>

        {taglines_html}

        <div class="profile-section">
            <div class="profile-section-title">💪 Power Words</div>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                {"".join([f"<span class='power-word'>{w}</span>" for w in power_words if isinstance(w, str)])}
            </div>
        </div>

        {"<div class='profile-section' style='background: rgba(91, 155, 213, 0.05); border: 1px solid rgba(91, 155, 213, 0.2);'><div class='profile-section-title'>🎤 Elevator Pitch</div><div style='color: var(--platinum-primary); font-style: italic;'>" + pitch + "</div></div>" if pitch else ""}
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# API KEY SETTINGS
# =============================================================================

def render_settings_sidebar():
    """Render settings in sidebar"""
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; color: var(--gold-primary);">⚙️ API Settings</div>
        </div>
        """, unsafe_allow_html=True)

        with st.container():
            st.markdown('<div class="settings-section">', unsafe_allow_html=True)
            st.markdown('<div class="settings-label">MiniMax API Key</div>', unsafe_allow_html=True)
            api_key = st.text_input(
                "API Key",
                type="password",
                placeholder="Enter your API key",
                key="api_key_input",
                label_visibility="collapsed"
            )

            st.markdown('<div class="settings-label" style="margin-top: 16px;">MiniMax Group ID</div>', unsafe_allow_html=True)
            group_id = st.text_input(
                "Group ID",
                type="password",
                placeholder="Enter your Group ID",
                key="group_id_input",
                label_visibility="collapsed"
            )

            # Save to session state
            if api_key:
                st.session_state.minimax_api_key = api_key
            if group_id:
                st.session_state.minimax_group_id = group_id

            st.markdown('</div>', unsafe_allow_html=True)

            # Validate button
            if st.button("🔐 Validate Credentials", use_container_width=True):
                if api_key and group_id:
                    with st.spinner("Validating..."):
                        is_valid = check_api_credentials(api_key, group_id)
                        if is_valid:
                            st.success("✅ Credentials validated!")
                        else:
                            st.error("❌ Invalid credentials")
                else:
                    st.warning("⚠️ Please enter both API Key and Group ID")

        st.markdown("---")
        st.markdown("""
        <div style="font-size: 0.85rem; color: var(--platinum-dark); text-align: center; padding: 16px 0;">
            <p>Don't have an API key?</p>
            <p>Get one at <a href="https://platform.minimax.chat" target="_blank" style="color: var(--gold-primary);">MiniMax Platform</a></p>
        </div>
        """, unsafe_allow_html=True)


# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main():
    """Main application entry point"""

    # Load premium CSS
    load_premium_css()

    # Initialize session state
    if "minimax_api_key" not in st.session_state:
        st.session_state.minimax_api_key = ""
    if "minimax_group_id" not in st.session_state:
        st.session_state.minimax_group_id = ""
    if "generation_count" not in st.session_state:
        st.session_state.generation_count = 0
    if "results" not in st.session_state:
        st.session_state.results = {}

    # Render settings in sidebar
    render_settings_sidebar()

    # Header
    st.markdown("""
    <div class="header">
        <div class="logo">
            <div class="logo-icon">🎯</div>
            ViralGen AI
        </div>
        <ul class="nav-links">
            <li><a href="#" class="nav-link">Features</a></li>
            <li><a href="#" class="nav-link">Pricing</a></li>
            <li><a href="#" class="nav-link">About</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Main Container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Hero Section
    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-badge">
            <span>✨</span>
            AI-Powered Marketing Intelligence
        </div>
        <h1 class="hero-title">Transform Your Product Ideas Into<br>Viral Marketing Assets</h1>
        <p class="hero-subtitle">
            Enter your product idea and let our AI Marketing Architect generate
            3 high-retention video scripts, psychological customer profiles,
            and killer USPs that convert viewers into buyers.
        </p>
        <div class="hero-stats">
            <div class="stat-item">
                <div class="stat-value">3</div>
                <div class="stat-label">Video Scripts</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">1</div>
                <div class="stat-label">Customer Profile</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">1</div>
                <div class="stat-label">Killer USP</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Input Section
    st.markdown("""
    <div class="input-section">
        <div class="input-label">
            <span class="input-label-icon">💡</span>
            Enter Your Product Idea
        </div>
    """, unsafe_allow_html=True)

    product_idea = st.text_area(
        "",
        placeholder="Describe your product or service in detail. Include key features, benefits, target audience hints, and what makes it unique. The more details you provide, the better your marketing assets will be...",
        height=150,
        label_visibility="collapsed",
        key="product_input"
    )

    char_count = len(product_idea)
    if char_count < 50:
        counter_class = "error" if char_count > 0 else ""
        counter_color = "var(--error)" if char_count > 0 else "var(--platinum-dark)"
    elif char_count > 1000:
        counter_class = "error"
        counter_color = "var(--error)"
    else:
        counter_class = "warning" if char_count > 800 else ""
        counter_color = "var(--warning)" if char_count > 800 else "var(--platinum-dark)"

    st.markdown(f'<div class="char-counter {counter_class}" style="color: {counter_color};">{char_count}/1000 characters</div>', unsafe_allow_html=True)

    # Generate Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_clicked = st.button(
            "🎯 Generate Marketing Assets",
            use_container_width=True,
            type="primary"
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # Generation Logic
    if generate_clicked:
        if not product_idea or len(product_idea) < 50:
            show_toast("Please enter a product description (at least 50 characters)", "error")
            return

        if not st.session_state.minimax_api_key or not st.session_state.minimax_group_id:
            show_toast("Please enter your API credentials in the sidebar", "error")
            return

        # Create API client
        client = MiniMaxAPIClient(
            api_key=st.session_state.minimax_api_key,
            group_id=st.session_state.minimax_group_id
        )

        # Update session state
        st.session_state.generation_count += 1

        # Create placeholders for results
        scripts_placeholder = st.empty()
        profile_placeholder = st.empty()
        usp_placeholder = st.empty()

        # Generate Video Scripts
        with scripts_placeholder.container():
            st.markdown("""
            <div style="display: flex; align-items: center; gap: 12px; margin: 30px 0;">
                <span style="font-size: 1.5rem;">🎬</span>
                <h2 style="color: var(--platinum-light); margin: 0;">Video Scripts</h2>
            </div>
            """, unsafe_allow_html=True)

            with st.spinner("🎬 Generating viral video scripts..."):
                system_prompt, user_prompt = generate_video_scripts_prompt(product_idea)
                response = client.generate_completion(
                    prompt=user_prompt,
                    system_prompt=system_prompt,
                    temperature=0.8,
                    max_tokens=3000
                )

                if "error" in response:
                    st.error(f"Error: {response['error']}")
                else:
                    content = client.parse_response(response)
                    if content:
                        st.session_state.results["scripts"] = content
                        render_markdown_safe(content)
                    else:
                        st.warning("Could not parse video scripts response")

        # Generate Psychological Profile
        with profile_placeholder.container():
            st.markdown("""
            <div style="display: flex; align-items: center; gap: 12px; margin: 30px 0;">
                <span style="font-size: 1.5rem;">🧠</span>
                <h2 style="color: var(--platinum-light); margin: 0;">Psychological Profile</h2>
            </div>
            """, unsafe_allow_html=True)

            with st.spinner("🧠 Analyzing target customer psychology..."):
                system_prompt, user_prompt = generate_psych_profile_prompt(product_idea)
                response = client.generate_completion(
                    prompt=user_prompt,
                    system_prompt=system_prompt,
                    temperature=0.7,
                    max_tokens=3000
                )

                if "error" in response:
                    st.error(f"Error: {response['error']}")
                else:
                    content = client.parse_response(response)
                    if content:
                        st.session_state.results["profile"] = content
                        render_markdown_safe(content)
                    else:
                        st.warning("Could not parse psychological profile response")

        # Generate USP
        with usp_placeholder.container():
            st.markdown("""
            <div style="display: flex; align-items: center; gap: 12px; margin: 30px 0;">
                <span style="font-size: 1.5rem;">💎</span>
                <h2 style="color: var(--platinum-light); margin: 0;">Killer USP</h2>
            </div>
            """, unsafe_allow_html=True)

            with st.spinner("💎 Crafting unique selling proposition..."):
                system_prompt, user_prompt = generate_usp_prompt(product_idea)
                response = client.generate_completion(
                    prompt=user_prompt,
                    system_prompt=system_prompt,
                    temperature=0.75,
                    max_tokens=3000
                )

                if "error" in response:
                    st.error(f"Error: {response['error']}")
                else:
                    content = client.parse_response(response)
                    if content:
                        st.session_state.results["usp"] = content
                        render_markdown_safe(content)
                    else:
                        st.warning("Could not parse USP response")

        show_toast("🎉 Marketing assets generated successfully!", "success")

    # Display previous results if any
    elif st.session_state.results:
        st.markdown("""
        <div style="text-align: center; padding: 40px 0; color: var(--platinum-dark);">
            <p>Your previously generated results are shown above.</p>
            <p>Enter a new product idea above to generate fresh content.</p>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <p class="footer-text">
            © 2024 <span class="footer-brand">ViralGen AI</span> — Marketing Architect
            <br>
            <small style="color: var(--platinum-dark);">Powered by MiniMax AI</small>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # Close main container


if __name__ == "__main__":
    main()
