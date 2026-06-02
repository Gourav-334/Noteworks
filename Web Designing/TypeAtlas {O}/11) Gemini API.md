# Gemini API Cheat Sheet

## Purpose

Gemini API allows your application to send prompts to an AI model and receive responses.

For TypeAtlas:

```text
User Input
      ↓

Gemini API
      ↓

Analysis
      ↓

Structured Result
```

Examples:

- Type Analysis
- Theory Classification
- Debate Analysis
- Profile Summaries
- Content Moderation

---

# Mental Model

```text
Application
      ↓

Request
      ↓

Gemini API
      ↓

Response
      ↓

Application
```

---

# Real Flow

```text
User Writes Text
       ↓

Next.js API Route
       ↓

Gemini API
       ↓

Response
       ↓

Store / Display
```

---

# 1. API Keys

## Concept

Secret password for accessing Gemini.

---

# Example

```text
AIzaSyXXXXXXXXXXXXX
```

---

# Store in Environment Variables

Never hardcode:

❌ Bad

```typescript
const apiKey =
    "AIzaSy...";
```

---

✅ Good

```env
GEMINI_API_KEY=AIzaSy...
```

---

Access:

```typescript
const apiKey =
    process.env.GEMINI_API_KEY;
```

---

# Mental Model

```text
API Key
 ↓
Application Identity
```

---

# Environment Variables

```env
GEMINI_API_KEY=xxxxx
SUPABASE_URL=xxxxx
SUPABASE_KEY=xxxxx
```

---

# 2. Requests

## Concept

Send a prompt to Gemini.

---

# Install SDK

```bash
npm install @google/genai
```

---

# Create Client

```typescript
import {

    GoogleGenAI

}
from "@google/genai";

const ai =
    new GoogleGenAI({

        apiKey:
            process.env.GEMINI_API_KEY

    });
```

---

# Simple Request

```typescript
const response =
    await ai.models.generateContent({

        model:
            "gemini-2.5-flash",

        contents:
            "Explain MBTI"

    });
```

---

# Get Text

```typescript
console.log(
    response.text
);
```

---

# Request Flow

```text
Prompt
 ↓

Gemini
 ↓

Generated Answer
```

---

# 3. Responses

## Concept

Gemini returns generated content.

---

# Example

Request:

```text
Explain MBTI
```

---

Response:

```text
MBTI is a personality
framework based on
cognitive preferences...
```

---

# Access Response

```typescript
const result =
    response.text;
```

---

# Typical Flow

```typescript
const response =
    await ai.models.generateContent({

        model:
            "gemini-2.5-flash",

        contents:
            prompt

    });

const text =
    response.text;
```

---

# Mental Model

```text
Request
 ↓

Response
```

Like:

```text
Question
 ↓

Answer
```

---

# 4. Prompt Engineering

## Concept

Writing prompts that produce reliable output.

---

# Bad Prompt

```text
Analyze this.
```

Result:

```text
Unpredictable
```

---

# Better Prompt

```text
Analyze this MBTI profile.

Return:

- Type
- Confidence
- Reasoning
```

Result:

```text
Predictable
```

---

# Best Prompt

```text
You are an MBTI analyst.

Analyze the text.

Return:

1. Type
2. Confidence
3. Explanation

Text:

<user_text>
```

---

# Mental Model

```text
Prompt Quality
      ↓
Output Quality
```

---

# Prompt Structure

## Role

```text
You are an MBTI analyst.
```

---

## Task

```text
Analyze the text.
```

---

## Rules

```text
Use only evidence.

Do not speculate.
```

---

## Output Format

```text
Return JSON.
```

---

## Data

```text
User Text Here
```

---

# Template

```text
ROLE

TASK

RULES

OUTPUT FORMAT

INPUT DATA
```

---

# Example

```text
You are a typology analyst.

Analyze the profile.

Determine:

- MBTI
- Enneagram
- Confidence

Return JSON.

Profile:

<text>
```

---

# 5. Structured JSON Output

## Concept

Make Gemini return machine-readable data.

Avoid:

```text
Long Paragraphs
```

Prefer:

```json
{
  "type": "INTP",
  "confidence": 92
}
```

---

# Example Prompt

```text
Analyze this profile.

Return ONLY JSON.

{
  "type": "",
  "confidence": 0
}
```

---

# Example Response

```json
{
  "type": "INTP",
  "confidence": 92
}
```

---

# Parse JSON

```typescript
const result =
    JSON.parse(
        response.text
    );
```

---

# Access Values

```typescript
console.log(
    result.type
);

console.log(
    result.confidence
);
```

---

# Why Structured Output?

Without JSON:

```text
Long essay
```

Hard to process.

---

With JSON:

```json
{
  "type": "INTP"
}
```

Easy to process.

---

# Real TypeAtlas Example

## Prompt

```text
Analyze the profile.

Return JSON.

{
  "mbti": "",
  "confidence": 0,
  "evidence": []
}

Profile:

<text>
```

---

## Response

```json
{
  "mbti": "INTP",
  "confidence": 91,
  "evidence": [
    "abstract reasoning",
    "system building",
    "independent thinking"
  ]
}
```

---

# Typical Next.js API Route

```typescript
import {

    GoogleGenAI

}
from "@google/genai";

const ai =
    new GoogleGenAI({

        apiKey:
            process.env.GEMINI_API_KEY

    });

export async function POST(
    request: Request
) {

    const body =
        await request.json();

    const response =
        await ai.models.generateContent({

            model:
                "gemini-2.5-flash",

            contents:
                body.prompt

        });

    return Response.json({

        result:
            response.text

    });

}
```

---

# TypeAtlas Analysis Flow

```text
User Profile
       ↓

Prompt Builder
       ↓

Gemini API
       ↓

JSON Response
       ↓

Store in Database
       ↓

Display Analysis
```

---

# Common Prompt Patterns

## Classification

```text
Determine MBTI type.
```

---

## Summarization

```text
Summarize this profile.
```

---

## Comparison

```text
Compare MBTI and Socionics.
```

---

## Extraction

```text
Extract key traits.
```

---

## Validation

```text
Verify evidence quality.
```

---

# 90% of Gemini API You'll Use

## API Key

```env
GEMINI_API_KEY=
```

---

## Create Client

```typescript
new GoogleGenAI(...)
```

---

## Send Request

```typescript
generateContent(...)
```

---

## Read Response

```typescript
response.text
```

---

## Parse JSON

```typescript
JSON.parse(...)
```

---

## Prompt Structure

```text
Role

Task

Rules

Output Format

Data
```

---

# Core Memory

```text
API Key
 ↓
Access Gemini

Prompt
 ↓
Request

Gemini
 ↓
Analysis

Response
 ↓
Generated Result

Prompt Engineering
 ↓
Control Output

JSON
 ↓
Machine Readable
```

---

# Most Important Flow

```text
User Input
      ↓

Prompt
      ↓

Gemini API
      ↓

JSON Response
      ↓

Application Logic
      ↓

UI
```

For TypeAtlas, the most valuable skill is not calling Gemini itself—it is designing prompts that consistently produce reliable, structured JSON output that your application can trust and process automatically.