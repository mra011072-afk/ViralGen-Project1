# ViralGen AI - Marketing Architect Specification

## 1. Project Overview

**Project Name**: ViralGen AI
**Type**: AI-Powered Marketing Intelligence Platform
**Core Functionality**: Transform product ideas into comprehensive marketing assets including video scripts, psychological profiles, and killer USPs using advanced AI
**Target Users**: Entrepreneurs, Marketers, Content Creators, E-commerce Businesses, Marketing Agencies

---

## 2. Visual & Rendering Specification

### 2.1 Theme & Color Palette

**Dark Mode Foundation**:
- Primary Background: `#0D0D0D` (Deep Black)
- Secondary Background: `#1A1A2E` (Dark Navy)
- Card Background: `#16213E` (Deep Blue)
- Surface: `#1F1F23` (Charcoal)

**Gold Accents (Premium)**:
- Primary Gold: `#D4AF37` (Metallic Gold)
- Light Gold: `#F4E4BA` (Champagne)
- Dark Gold: `#AA8C2C` (Antique Gold)

**Platinum Accents (Luxury)**:
- Primary Platinum: `#E5E4E2` (Platinum)
- Light Platinum: `#F8F8FF` (Ghost White)
- Dark Platinum: `#B8B8B8` (Silver)

**Accent Colors**:
- Success: `#00D26A` (Emerald Green)
- Error: `#FF4757` (Coral Red)
- Info: `#5B9BD5` (Sky Blue)

### 2.2 Typography

**Primary Font**: "Inter" (Modern, Professional)
**Display Font**: "Playfair Display" (Luxury, Headlines)
**Monospace**: "JetBrains Mono" (Code, Data)

**Font Sizes**:
- Hero Title: 3.5rem (56px)
- Section Title: 2rem (32px)
- Card Title: 1.25rem (20px)
- Body: 1rem (16px)
- Caption: 0.875rem (14px)

### 2.3 UI Components

**Navigation**:
- Horizontal top navigation bar with logo and menu items
- Active state with gold underline
- Smooth transitions on hover

**Cards**:
- Rounded corners (16px radius)
- Subtle gold border on hover
- Glassmorphism effect with semi-transparent backgrounds
- Box shadows with gold tint

**Buttons**:
- Primary: Gold gradient background
- Secondary: Outlined with gold border
- Hover: Scale up 1.02x with glow effect
- Loading states with animated spinner

**Input Fields**:
- Dark background with subtle border
- Gold accent on focus
- Floating labels
- Placeholder text in muted platinum

---

## 3. Application Structure

### 3.1 Main Sections

**1. Hero Section (Landing)**
- Animated headline with gradient text
- Product idea input form
- Quick stats (scripts generated, users served)

**2. AI Engine Dashboard**
- Three-tab interface:
  - Tab 1: Video Scripts
  - Tab 2: Psychological Profile
  - Tab 3: Killer USP
- Real-time generation status
- Copy-to-clipboard functionality

**3. Results Display**
- Expandable cards for each output
- Syntax highlighting for scripts
- Export options (copy, download)

### 3.2 Layout

```
┌─────────────────────────────────────────────────────────────┐
│  [Logo] ViralGen AI        [Features] [Pricing] [About]    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│     ╔══════════════════════════════════════════════╗        │
│     ║  ENTER YOUR PRODUCT IDEA                    ║        │
│     ║  ┌──────────────────────────────────────┐   ║        │
│     ║  │                                      │   ║        │
│     ║  └──────────────────────────────────────┘   ║        │
│     ║  [🎯 Generate Marketing Assets]             ║        │
│     ╚══════════════════════════════════════════════╝        │
│                                                             │
│     ┌─────────────┬─────────────┬─────────────┐            │
│     │   Scripts   │  Profile    │    USP      │            │
│     │   [3]       │   [1]       │    [1]      │            │
│     └─────────────┴─────────────┴─────────────┘            │
│                                                             │
│     [Footer: © 2024 ViralGen AI]                           │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Functional Specification

### 4.1 Core Features

**Feature 1: Product Idea Input**
- Large text area for product description
- Character counter (min 50, max 1000)
- Validation for empty or too short inputs
- Optional: Target audience selector (dropdown)

**Feature 2: AI Video Script Generator**
- Generate 3 unique TikTok/Reels scripts
- Each script includes:
  - Hook (first 3 seconds)
  - Body (main content)
  - Call-to-Action (end)
  - Estimated duration
  - Trending sound recommendation
  - Hashtag suggestions
- Script types:
  - Script 1: "Problem-Solution" format
  - Script 2: "Social Proof" format
  - Script 3: "Urgency/Scarcity" format

**Feature 3: Psychological Profile Generator**
- Comprehensive target customer analysis including:
  - Demographics (age, gender, income, location)
  - Psychographics (values, interests, lifestyle)
  - Pain Points (emotional and functional)
  - Buying Triggers (what makes them purchase)
  - Media Consumption (platforms, content types)
  - Objection Handlers (how to overcome resistance)

**Feature 4: Killer USP Generator**
- Unique Selling Proposition that converts
- Components:
  - Main USP statement
  - Supporting proof points (3)
  - Emotional hook
  - Competitor differentiation
  - Catchy tagline options (3)

### 4.2 API Integration

**MiniMax API Configuration**:
```python
# Placeholder credentials
MINIMAX_API_KEY = "YOUR_MINIMAX_API_KEY_HERE"
MINIMAX_GROUP_ID = "YOUR_GROUP_ID_HERE"

# API Endpoint
BASE_URL = "https://api.minimax.chat/v1"
```

**Request Structure**:
```python
headers = {
    "Authorization": f"Bearer {MINIMAX_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "MiniMax-Text-01",
    "messages": [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT}
    ],
    "temperature": 0.7,
    "max_tokens": 2000
}
```

### 4.3 Prompts Engineering

**Video Script Prompt Template**:
```
You are an expert TikTok content strategist specializing in viral marketing.
Create 3 high-retention video scripts for this product: {product_description}

For each script, provide:
1. Script Title
2. Hook (first 3-5 seconds)
3. Main Content (30-60 seconds)
4. Call-to-Action
5. Trending Sound Suggestion
6. 5 Relevant Hashtags

Format as JSON array.
```

**Psychological Profile Prompt Template**:
```
You are a senior marketing psychologist. Create a detailed psychological profile
of the ideal customer for: {product_description}

Include:
- Demographics
- Psychographics
- Pain Points
- Buying Triggers
- Objection Handlers
- Media Consumption

Be specific and actionable.
```

**Killer USP Prompt Template**:
```
You are a conversion copywriting expert. Create a killer USP for: {product_description}

Include:
- Main USP Statement
- 3 Supporting Proof Points
- Emotional Hook
- Competitor Differentiation
- 3 Tagline Options

Make it compelling and conversion-focused.
```

---

## 5. Technical Implementation

### 5.1 Technology Stack

- **Framework**: Streamlit 1.28+
- **HTTP Client**: requests library
- **JSON Parsing**: Built-in json module
- **UI Enhancements**: Custom CSS
- **Icons**: Font Awesome (CDN)
- **Animations**: CSS keyframes

### 5.2 File Structure

```
/workspace/viralgen_ai/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── SPEC.md               # This specification
├── assets/
│   └── logo.svg          # ViralGen AI logo
└── utils/
    ├── api_client.py      # MiniMax API wrapper
    └── prompts.py        # Prompt templates
```

### 5.3 Error Handling

- Network errors: Display user-friendly message with retry button
- API errors: Log and show specific error details
- Empty results: Show fallback content
- Rate limiting: Implement exponential backoff

---

## 6. Quality Checklist

- [ ] All buttons are functional
- [ ] API integration uses correct endpoints
- [ ] Prompts generate high-quality marketing content
- [ ] UI matches premium dark mode design
- [ ] Animations are smooth (60fps)
- [ ] Responsive on mobile devices
- [ ] Error states are handled gracefully
- [ ] Loading states provide feedback
- [ ] Copy-to-clipboard works correctly
- [ ] No console errors

---

## 7. Deployment

**Target**: Deploy as Streamlit Cloud application
**Requirements**:
- Python 3.9+
- All dependencies in requirements.txt
- Environment variables for API keys

---

## 8. Success Metrics

- Fast load time (< 3 seconds)
- API response time (< 10 seconds)
- 100% uptime
- Positive user feedback on output quality
