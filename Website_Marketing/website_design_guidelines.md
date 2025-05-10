# Green AI & Automation - Website Design Guidelines

## Brand Identity Integration

### Logo Usage
- Primary logo placement: top left of navigation
- Footer logo: monochrome version
- Favicon: simplified icon version
- Minimum clear space: equal to height of "G" in logo
- Never distort, recolor, or apply effects to the logo

### Color Palette

**Primary Colors**
- Green Primary: #0D6E4E (RGB: 13, 110, 78)
  - Usage: Primary buttons, key headings, accents
- Green Secondary: #14B87E (RGB: 20, 184, 126)
  - Usage: Hover states, secondary elements, icons
- Coal Black: #1A1A1A (RGB: 26, 26, 26)
  - Usage: Primary text, footers

**Secondary Colors**
- Light Green: #E7F7F0 (RGB: 231, 247, 240)
  - Usage: Backgrounds, cards, form fields
- Sky Blue: #0E7C94 (RGB: 14, 124, 148)
  - Usage: Links, secondary buttons, highlights
- Sunset Orange: #F57C4D (RGB: 245, 124, 77)
  - Usage: Alerts, important notifications, CTAs

**Neutral Colors**
- White: #FFFFFF
  - Usage: Backgrounds, text on dark colors
- Light Gray: #F4F4F4
  - Usage: Backgrounds, dividers
- Medium Gray: #9A9A9A
  - Usage: Secondary text, disabled elements
- Dark Gray: #4A4A4A
  - Usage: Body text

### Typography

**Primary Font: Inter**
- Headings: Inter Bold, Inter SemiBold
- Body: Inter Regular
- Accents: Inter Medium

**Font Hierarchy**
- H1: 40px/48px, Inter Bold
- H2: 32px/40px, Inter Bold
- H3: 24px/32px, Inter SemiBold
- H4: 20px/28px, Inter SemiBold
- Body Large: 18px/28px, Inter Regular
- Body: 16px/24px, Inter Regular
- Body Small: 14px/20px, Inter Regular
- Caption: 12px/16px, Inter Medium

**Font Usage Guidelines**
- Maximum 3 font sizes per page
- Line length: 60-75 characters
- Always maintain sufficient contrast (WCAG AA compliance)
- Left-align text (except for specific centered design elements)

### Iconography

**Style Guidelines**
- Use outlined icons with 2px stroke
- Rounded corners (4px radius)
- Consistent 24x24px base size
- Primary green color for interactive icons
- Gray for decorative/non-interactive icons

**Icon Library**
- Phosphor Icons as primary icon set
- Custom icons for product-specific features
- Always include text labels with icons for accessibility

## Neurodivergent-Friendly Design Elements

### Visual Clarity
- High contrast mode toggle
- Option to reduce motion
- Clear visual hierarchy
- Consistent navigation patterns
- Visible focus states

### Content Presentation
- Toggle between compact and expanded content views
- Option for increased line spacing (1.5x)
- Reading guides for long-form content
- Progress indicators for multi-step processes
- Time estimates for content consumption

### Interaction Design
- Forgiving input patterns
- Clear error messages with solution suggestions
- Multiple input methods (keyboard shortcuts, click, touch)
- Undo functionality where possible
- Save progress automatically

## UI Component Guidelines

### Buttons

**Primary Button**
- Background: Green Primary (#0D6E4E)
- Text: White (#FFFFFF)
- Border Radius: 8px
- Padding: 12px 24px
- Font: Inter SemiBold, 16px
- Hover State: Green Secondary (#14B87E)
- Active State: Darken by 10%
- Disabled State: Medium Gray (#9A9A9A)

**Secondary Button**
- Background: Transparent
- Text: Green Primary (#0D6E4E)
- Border: 2px solid Green Primary
- Border Radius: 8px
- Padding: 12px 24px
- Font: Inter SemiBold, 16px
- Hover State: Light Green background (#E7F7F0)
- Active State: Darken by 10%
- Disabled State: Medium Gray (#9A9A9A)

**Tertiary Button**
- Background: Transparent
- Text: Green Primary (#0D6E4E)
- Border: None
- Padding: 12px 24px
- Font: Inter Medium, 16px
- Hover State: Light Green background (#E7F7F0)
- Active State: Darken by 10%
- Disabled State: Medium Gray (#9A9A9A)

### Cards

**Service Card**
- Background: White (#FFFFFF)
- Border: None
- Border Radius: 12px
- Shadow: 0px 4px 12px rgba(0, 0, 0, 0.08)
- Padding: 24px
- Heading: H3
- Icon: 40x40px at top
- Hover State: Scale 1.02, Shadow increase

**Content Card**
- Background: White (#FFFFFF)
- Border: 1px solid Light Gray (#F4F4F4)
- Border Radius: 8px
- Shadow: 0px 2px 8px rgba(0, 0, 0, 0.05)
- Padding: 20px
- Image: Top position if applicable
- Heading: H4
- Hover State: Border color change to Green Secondary

**Feature Card**
- Background: Light Green (#E7F7F0)
- Border: None
- Border Radius: 12px
- Padding: 24px
- Icon: Left or top position
- Heading: H4 in Green Primary
- Hover State: Background darken slightly

### Forms

**Input Fields**
- Background: White (#FFFFFF)
- Border: 1px solid Medium Gray (#9A9A9A)
- Border Radius: 8px
- Padding: 12px 16px
- Label: Above input, Body Small, Dark Gray
- Focus State: Border color Green Primary, subtle glow
- Error State: Border color Sunset Orange, error message below
- Success State: Border color Green Secondary, success icon

**Checkboxes & Radio Buttons**
- Size: 20x20px
- Border: 1px solid Medium Gray
- Border Radius: 4px (checkbox), 50% (radio)
- Selected State: Green Primary fill, white checkmark
- Focus State: Border color Green Primary, subtle glow

**Dropdown Menus**
- Same styling as input fields
- Icon: Chevron down, right aligned
- Options Menu: White background, 1px border, 8px radius
- Option Hover: Light Green background
- Selected Option: Checkmark icon, semi-bold text

### Navigation

**Main Navigation**
- Background: White (#FFFFFF)
- Height: 72px
- Shadow: 0px 2px 8px rgba(0, 0, 0, 0.05)
- Links: Body text, Dark Gray
- Current Page: Green Primary text, subtle underline
- Hover: Green Secondary text
- Mobile: Hamburger menu, slide-in panel

**Secondary Navigation**
- Background: Light Gray (#F4F4F4)
- Height: 48px
- Links: Body Small text, Dark Gray
- Current Section: Green Primary text, subtle underline
- Hover: Green Secondary text

**Footer Navigation**
- Background: Coal Black (#1A1A1A)
- Text: White (#FFFFFF)
- Links: Body Small text
- Hover: Green Secondary text
- Padding: 64px top/bottom, 32px sides

## Page Templates

### Homepage

**Hero Section**
- Full-width background
- H1 heading
- Subheading (Body Large)
- Primary CTA button
- Secondary CTA link
- Optional: background image or illustration

**Feature Showcase**
- Three-column layout
- Icon + H3 + description
- Consistent height
- Optional: "Learn more" link

**Testimonial Section**
- Background: Light Green
- Large quote marks
- Body Large text
- Attribution with logo
- Optional: testimonial carousel

**Blog Preview**
- Two-column or three-column grid
- Featured image
- H4 heading
- Category tag
- Publication date
- Excerpt (2-3 lines)

### Service Page

**Hero Section**
- Two-column layout
- H1 heading + description on left
- Illustration or screenshot on right
- Primary and secondary CTAs

**Feature List**
- Alternating left/right sections
- Icon + H3 + description
- Screenshot or illustration
- Subtle dividers between sections

**Pricing/Packages**
- Three-column comparison
- Feature table
- Highlighted recommended option
- CTA button for each option

**FAQ Section**
- Accordion style
- H4 questions
- Body text answers
- Contact link at bottom

### Blog Article

**Header**
- Category tag
- H1 heading
- Publication date
- Author information
- Featured image (16:9 ratio)

**Content**
- Body text (18px for readability)
- Subheadings (H2, H3)
- Blockquotes for important points
- Images with captions
- Code blocks where applicable

**Sidebar**
- Related articles
- Categories
- Popular posts
- Newsletter signup

### Dashboard (Client Portal)

**Header**
- Welcome message with name
- Quick stats summary
- Alert notifications
- Quick action buttons

**Main Content**
- Card-based layout
- Clear section headings
- Visual data representations
- Progress indicators
- Action buttons within each section

**Navigation**
- Left sidebar with icons + text
- Current section highlighted
- Collapsible categories
- Quick support access

## Responsive Design Guidelines

### Breakpoints
- Mobile: 320px - 767px
- Tablet: 768px - 1023px
- Desktop: 1024px - 1439px
- Large Desktop: 1440px and above

### Mobile Adaptations
- Single column layouts
- Larger touch targets (min 44px)
- Condensed navigation (hamburger menu)
- Reduced animations
- Stack elements vertically
- Adjust font sizes (min 16px for body)
- Hide non-essential content

### Tablet Adaptations
- Two-column layouts where appropriate
- Simplified navigation
- Reduced padding
- Combine some sections

### Responsive Images
- Use responsive image techniques (srcset, sizes)
- Art direction for different breakpoints
- Ensure text remains readable over images
- Consider loading performance

## Accessibility Guidelines

### Compliance Standards
- WCAG 2.1 AA minimum
- Focus on keyboard navigation
- Screen reader compatibility
- Color contrast compliance

### Specific Requirements
- Alt text for all images
- ARIA labels for interactive elements
- Skip navigation link
- Keyboard focus indicators
- Sufficient color contrast
- Resizable text without breaking layout
- Multiple ways to navigate
- Error identification and suggestion

## Animation & Interaction

### Principles
- Purpose: Enhance understanding, not decorate
- Performance: Optimize for smooth rendering
- Subtlety: Avoid excessive motion
- Consistency: Use similar patterns throughout

### Specific Animations
- Hover states: Subtle scale or color change
- Page transitions: Fade in (optional)
- Button feedback: Visual change on click
- Loading states: Simple spinners or progress bars
- Scroll effects: Minimal parallax for key sections

### Reduced Motion
- Honor prefers-reduced-motion media query
- Provide static alternatives to animations
- Keep essential motion subtle

## Implementation Notes

### CSS Methodology
- Use Tailwind CSS utility-first approach
- Custom components for repeated patterns
- CSS variables for theming and consistency
- Mobile-first responsive design

### Component Architecture
- Follow atomic design principles
- Build reusable components
- Document component usage
- Maintain storybook or component gallery

### Performance Considerations
- Optimize image loading (WebP format, lazy loading)
- Minimize JavaScript bundle size
- Implement code splitting
- Use caching strategies
- Optimize for Core Web Vitals

These design guidelines provide a comprehensive framework for creating a consistent, accessible, and neurodivergent-friendly website for Green AI & Automation. All visual and interactive elements should adhere to these standards while maintaining flexibility for specific content needs.