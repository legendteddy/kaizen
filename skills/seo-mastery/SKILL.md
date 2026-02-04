---
name: seo-mastery
description: Engineering discoverability for humans and Agents (Robots.txt, JSON-LD, Meta Tags).
---

# SEO Mastery (Search & Discovery)

> "If the Agents can't read it, it doesn't exist."

## Activation Trigger
- "Fix SEO"
- "Make the site visible"
- "Add meta tags"
- "Configure robots.txt"

## Protocols

### 1. First Principle: Agent Permissiveness
In the AI era, blocking crawlers is suicide. You WANT `GPTBot`, `ClaudeBot`, and `Google-Extended` to read your site so they can answer user questions about you.
**Default Policy**: Allow all major AI bots.

### 2. The "Schema First" Rule
Visual content is for humans. JSON-LD is for machines.
Every page must have a `<script type="application/ld+json">` block describing its content (Product, Article, LocalBusiness).

### 3. The "Meta Trifecta"
Every HTML file must have:
1.  `<title>` (60 chars max)
2.  `<meta name="description">` (160 chars max)
3.  `<meta property="og:image">` (Social preview)

## Code Patterns

### The AI-Optimized Robots.txt
```txt
User-agent: *
Allow: /

# EXPLICITLY ALLOW AI AGENTS
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: PerplexityBot
Allow: /
```

### The LocalBusiness JSON-LD
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Brand Name",
  "image": "https://example.com/logo.jpg",
  "telephone": "+123456789",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressCountry": "US"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday"
    ],
    "opens": "09:00",
    "closes": "17:00"
  }
}
</script>
```

## Safety Guardrails
- **No Keyword Stuffing**: Write for humans, structure for bots.
- **Canonical URLs**: Always define `<link rel="canonical">` to prevent duplicate content penalties.
- **Alt Text**: All `<img>` tags must have descriptive alt text.
- **Performance**: High CLS (Cumulative Layout Shift) kills rankings. Dimensions on images are mandatory.
