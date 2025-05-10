# Lead Generation & Capture System Documentation

## Overview

This document provides comprehensive documentation for the Green AI Solutions lead generation and capture system. The system is designed to convert website visitors into qualified leads, track their engagement, and nurture them through automated sequences tailored to their interests and behavior.

## System Architecture

The lead generation system consists of several integrated components:

1. **Lead Capture Forms**: Deployed throughout the website to collect visitor information through various offers and interactions
2. **CRM Integration**: Connection to HubSpot CRM for lead management, scoring, and nurturing
3. **Analytics & Tracking**: Comprehensive tracking of visitor behavior, source attribution, and conversion paths
4. **Email Automation**: Personalized nurturing sequences based on interests and engagement
5. **Lead Scoring**: Automated qualification of leads based on demographic and behavioral data

### Component Diagram

```
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│                     │     │                     │     │                     │
│   Website Visitor   │────▶│   Lead Capture      │────▶│   CRM System        │
│                     │     │   Forms & Popups    │     │   (HubSpot)         │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
                                      │                             │
                                      ▼                             ▼
                              ┌─────────────────────┐     ┌─────────────────────┐
                              │                     │     │                     │
                              │   Analytics &       │     │   Email Nurturing   │
                              │   Tracking          │     │   Sequences         │
                              └─────────────────────┘     └─────────────────────┘
                                      │                             │
                                      └─────────────────┬───────────┘
                                                        │
                                                        ▼
                                              ┌─────────────────────┐
                                              │                     │
                                              │   Lead Scoring &    │
                                              │   Qualification     │
                                              └─────────────────────┘
                                                        │
                                                        ▼
                                              ┌─────────────────────┐
                                              │                     │
                                              │   Sales Team        │
                                              │                     │
                                              └─────────────────────┘
```

## Technical Implementation

### JavaScript Files

The system is implemented through several JavaScript files:

| File | Purpose |
|------|---------|
| `lead-capture-implementation.js` | Main implementation script that integrates all components |
| `hubspot-integration.js` | Connects forms and tracking to HubSpot CRM |
| `lead-tracking.js` | Tracks visitor behavior and engagement |
| `crm-config.js` | Configuration settings for CRM integration |

### Form Implementation

Forms across the site follow a consistent structure for easy tracking and data capture:

```html
<form class="lead-capture-form" id="[unique-form-id]" 
      data-lead-asset="[Asset Name]" 
      data-asset-url="[Download URL]"
      data-hubspot-form-id="[HubSpot Form ID]"
      data-lead-source="[Lead Source]"
      data-form-context="[Form Context]">
  <!-- Form fields -->
</form>
```

#### Key Attributes:

- `data-lead-asset`: Identifies the lead magnet or offer
- `data-asset-url`: URL for downloadable resources
- `data-hubspot-form-id`: Links to specific HubSpot form
- `data-lead-source`: Tracks acquisition source
- `data-form-context`: Provides additional context for analytics

#### Standard Form Fields:

| Field | Type | Purpose |
|-------|------|---------|
| full-name | text | Visitor's full name |
| business-email | email | Primary contact email |
| company-name | text | Company identification |
| phone | tel | Contact phone number (optional) |
| industry | select | Industry classification |
| employee-count | select | Company size classification |
| subscribe | checkbox | Marketing consent |
| consent | checkbox | Privacy policy agreement |

### User Identification & Tracking

The system implements a persistent identification method using browser storage:

1. **First Visit**: Generates a unique `visitor_id` stored in localStorage
2. **Attribution Tracking**: Captures first-touch and last-touch attribution data
3. **Visit History**: Maintains a record of pages viewed and engagement
4. **Event Tracking**: Logs significant interactions and high-intent actions

### Lead Source Attribution

The system captures lead source information through multiple mechanisms:

1. **UTM Parameters**: Tracks campaign parameters from inbound links
   ```
   ?utm_source=linkedin&utm_medium=social&utm_campaign=construction-industry
   ```

2. **Referrer Tracking**: Captures the referring website or search engine
3. **Direct Navigation**: Identifies direct traffic to the site
4. **Campaign Tracking**: Links lead generation to specific marketing campaigns

### Conversion Tracking

Conversion points are tracked throughout the user journey:

1. **Micro-Conversions**:
   - Blog post reading (75%+ scroll)
   - Video views
   - Multiple page visits
   - Resource page views

2. **Lead Conversions**:
   - Newsletter signups
   - Lead magnet downloads
   - Webinar registrations
   - Contact form submissions

3. **High-Intent Conversions**:
   - Demo requests
   - Pricing page views
   - Multiple visits to high-value pages
   - Specific page sequences (e.g., case study → pricing → demo)

### Lead Scoring Model

The lead scoring system allocates points based on demographic fit and behavioral engagement:

#### Demographic Scoring
- Industry match: 5-15 points
- Company size match: 5-15 points
- Role seniority: 5-20 points
- Location (Melbourne): 10 points

#### Behavioral Scoring
- High-value page view: 5 points
- Return visit: 5 points
- Multiple page views: 1-10 points
- Resource download: 15 points
- Webinar registration: 15 points
- Webinar attendance: 25 points
- Demo page view: 15 points
- Pricing page view: 20 points

#### Qualification Thresholds
- Cold Lead: 0-20 points
- Marketing Qualified Lead (MQL): 21-50 points
- Sales Qualified Lead (SQL): 51+ points

## Lead Capture Forms

### Form Types & Placement

The system includes various form types strategically placed throughout the website:

1. **Newsletter Signup Forms**
   - Location: Footer, Blog sidebar
   - Fields: Email only
   - Purpose: Top-of-funnel lead acquisition

2. **Lead Magnet Forms**
   - Location: Landing pages, Resource pages
   - Fields: Name, Email, Company, Industry
   - Purpose: Mid-funnel lead acquisition with content value exchange

3. **Contact Forms**
   - Location: Contact page
   - Fields: Name, Email, Phone, Message
   - Purpose: Direct inquiry capture

4. **Demo Request Forms**
   - Location: Demo page, High-intent CTAs
   - Fields: Name, Email, Company, Industry, Size, Needs
   - Purpose: Bottom-of-funnel conversion of high-intent leads

5. **Exit Intent Popups**
   - Location: Triggered when user moves to exit site
   - Fields: Email only
   - Purpose: Recover potentially lost leads

### Form Conversion Optimization

Forms are optimized for maximum conversion through several techniques:

1. **Progressive Profiling**: Forms adapt based on already known information, reducing friction for returning visitors
2. **Contextual Lead Magnets**: Offers are dynamically matched to page content and visitor interests
3. **A/B Testing**: Form fields, button text, and layouts are tested for optimal conversion
4. **Mobile Optimization**: Forms are fully responsive with touch-friendly inputs
5. **Error Handling**: Real-time validation with clear error messages to reduce abandonment

## Email Nurturing Sequences

### Sequence Types

The system includes several types of automated email sequences:

1. **Welcome Sequence**: For all new contacts
   - Introduction to Green AI Solutions
   - Value overview for HR automation and AI
   - Educational content based on interests
   - Invitation to engage further

2. **Lead Magnet Follow-up**: Resource-specific nurturing
   - Resource delivery and usage tips
   - Related content recommendations
   - Case studies relevant to the resource
   - Next steps and consultation offers

3. **Industry-Specific Sequences**: Tailored to industry interest
   - Industry-specific challenges and solutions
   - Relevant case studies and social proof
   - Industry compliance considerations
   - Industry-specific consultation offers

4. **Re-engagement Sequences**: For inactive leads
   - New resource offers
   - Industry updates and regulatory changes
   - Exclusive content or special offers
   - Final high-value resource

### Sample Sequence: Construction Industry

The construction industry sequence demonstrates our approach to industry-specific nurturing:

| Email | Timing | Focus | CTA |
|-------|--------|-------|-----|
| 1. Welcome & Guide | Immediate | Introduction and resource delivery | Download guide |
| 2. Case Study | Day 3 | Smith Construction compliance success | Read case study |
| 3. Educational | Day 8 | Common compliance mistakes in construction | Watch video |
| 4. Social Proof | Day 15 | Testimonials from construction clients | Book demo |
| 5. Objection Handling | Day 25 | Addressing construction-specific concerns | Implementation discussion |
| 6. ROI & Conversion | Day 39 | Expected ROI timeline for construction | Book ROI assessment |

## Landing Pages

### Landing Page Types

The system includes several types of landing pages optimized for conversion:

1. **Lead Magnet Landing Pages**
   - Purpose: Convert traffic to leads through valuable resources
   - Examples:
     - Fair Work Compliance Checklist Landing Page
     - HR Automation ROI Calculator Landing Page
     - AI Implementation Roadmap Landing Page

2. **Service-Specific Landing Pages**
   - Purpose: Generate leads interested in specific services
   - Examples:
     - HR Automation Landing Page
     - AI Consulting Landing Page
     - Neurodivergent Interface Landing Page

3. **Industry-Specific Landing Pages**
   - Purpose: Convert industry-targeted traffic
   - Examples:
     - Construction HR Solutions Landing Page
     - Professional Services Automation Landing Page
     - Retail Workforce Management Landing Page

### Landing Page Optimization

Landing pages are optimized for conversion through:

1. **Clear Value Proposition**: Immediately communicates benefits
2. **Social Proof**: Testimonials and case studies
3. **Benefit-Focused Content**: Emphasizes outcomes rather than features
4. **Strong Visuals**: Screenshots, mockups, and diagrams
5. **Minimal Navigation**: Focused on conversion without distractions
6. **Mobile Optimization**: Fully responsive design
7. **A/B Testing**: Continuous optimization of headlines, imagery, and CTAs

## CRM Integration

### HubSpot Configuration

The system integrates with HubSpot CRM for lead management:

1. **Contact Properties**
   - Standard fields (name, email, company)
   - Custom fields for industry-specific data
   - Behavioral tracking fields
   - Lead source and attribution data

2. **Form Mappings**
   - Each website form is mapped to a HubSpot form
   - Field mappings ensure data consistency
   - Hidden fields capture additional context

3. **Automation Workflows**
   - Lead scoring automation
   - Sequence enrollment based on triggers
   - Internal notifications for high-value actions
   - Lead assignment to appropriate team members

4. **Lists and Segmentation**
   - Industry-specific lists
   - Engagement-based segmentation
   - Lead status segmentation
   - Campaign-specific lists

### Data Flow

The system maintains a consistent data flow from capture to CRM:

1. Visitor completes form on website
2. Form data is validated client-side
3. Submission is sent to HubSpot via API
4. Contact is created or updated in CRM
5. Lead scoring is applied
6. Contact is enrolled in appropriate sequence
7. Sales notifications are triggered for high-value leads

## Analytics & Reporting

### Tracking Framework

The system implements a comprehensive tracking framework:

1. **Visitor Tracking**
   - Unique visitor identification
   - Session tracking
   - Device and browser information
   - Geographic data

2. **Engagement Tracking**
   - Page views and time on page
   - Scroll depth
   - Click interactions
   - Form interactions

3. **Conversion Tracking**
   - Form submissions
   - Resource downloads
   - High-intent actions
   - Multi-touch attribution

### Key Metrics

The system tracks several key performance metrics:

1. **Traffic Metrics**
   - Visitors by source
   - Page popularity
   - Entry and exit pages
   - Return visitor rate

2. **Engagement Metrics**
   - Average session duration
   - Pages per session
   - Content popularity
   - Video engagement

3. **Conversion Metrics**
   - Form conversion rates
   - Lead magnet popularity
   - Cost per lead by source
   - Lead-to-MQL conversion rate

4. **ROI Metrics**
   - MQL-to-SQL conversion rate
   - Cost per qualified lead
   - Lead-to-customer rate
   - Customer acquisition cost

### Reporting Dashboards

The system provides several dashboards for performance monitoring:

1. **Lead Generation Overview**
   - Lead volume by source
   - Conversion rates by form
   - Lead quality distribution
   - Trend analysis

2. **Content Performance**
   - Top converting content
   - Lead magnet performance
   - Blog post engagement
   - Landing page effectiveness

3. **Campaign Performance**
   - UTM source tracking
   - Campaign ROI
   - Campaign influence on leads
   - Multi-touch attribution

4. **Sales Pipeline Impact**
   - MQLs and SQLs generated
   - Sales pipeline velocity
   - Revenue influence
   - Closed-won attribution

## Implementation Instructions

### Adding a New Form

To add a new lead capture form:

1. Create the HTML form with the standard structure
   ```html
   <form class="lead-capture-form" id="new-form-id" 
         data-lead-asset="New Asset Name" 
         data-asset-url="/path/to/download.pdf"
         data-hubspot-form-id="hubspot-form-id"
         data-lead-source="Form Source"
         data-form-context="Form Context">
     <!-- Form fields -->
   </form>
   ```

2. Add the form ID to the `FORM_MAPPING` object in `crm-config.js`
   ```javascript
   const FORM_MAPPING = {
       // Existing mappings...
       'new-form-id': 'hubspot-form-id'
   };
   ```

3. Create a corresponding form in HubSpot
4. Test the form submission and data flow

### Adding a New Lead Magnet

To add a new lead magnet:

1. Create the lead magnet content (PDF, guide, template, etc.)
2. Create a landing page for the lead magnet
3. Add a lead capture form to the landing page
4. Create a thank you page or download delivery mechanism
5. Add tracking for the new lead magnet
6. Create a follow-up email sequence in HubSpot
7. Add to the appropriate promotional channels

### Adding a New Landing Page

To create a new landing page:

1. Use the landing page template appropriate for the content type
2. Customize the messaging for the specific offer
3. Implement a lead capture form
4. Add social proof relevant to the offer
5. Optimize for SEO with appropriate keywords
6. Set up tracking and analytics
7. Create a thank you page for conversions

## Maintenance & Optimization

### Regular Maintenance Tasks

1. **Weekly Tasks**
   - Review form submissions and conversion rates
   - Check for form errors or technical issues
   - Monitor lead quality and scoring
   - Update content offers as needed

2. **Monthly Tasks**
   - Analyze conversion performance by source
   - Review email sequence effectiveness
   - A/B test form and landing page elements
   - Update tracking and analytics configuration

3. **Quarterly Tasks**
   - Comprehensive performance review
   - Update lead scoring model based on data
   - Refresh landing pages and content offers
   - Review CRM integration and data quality

### Continuous Optimization

The system is designed for ongoing optimization:

1. **Form Optimization**
   - A/B testing of form fields and length
   - Testing different CTAs and button text
   - Optimizing form placement and design
   - Testing progressive profiling approaches

2. **Landing Page Optimization**
   - A/B testing headlines and value propositions
   - Testing different social proof elements
   - Optimizing page length and content structure
   - Testing different visual approaches

3. **Email Sequence Optimization**
   - Testing subject lines and sender names
   - Optimizing email content and length
   - Testing send times and frequency
   - Refining sequence logic and triggers

4. **Lead Scoring Optimization**
   - Analyzing correlation between scores and conversions
   - Adjusting point values based on performance
   - Adding new scoring factors as identified
   - Refining threshold definitions

## Conclusion

The Green AI Solutions lead generation and capture system provides a comprehensive framework for converting website visitors into qualified leads. By implementing this system, we establish a sustainable pipeline of inbound leads that can be effectively nurtured and converted into clients.

The system's integration with HubSpot CRM ensures efficient lead management, while the comprehensive tracking and analytics provide insights for continuous optimization. The customized nurturing sequences and landing pages create personalized experiences for different audience segments, maximizing conversion potential.

---

**Document Metadata**
- **Version**: 1.0
- **Last Updated**: May 7, 2025
- **Owner**: Marketing Team
- **Status**: Approved