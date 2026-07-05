---
name: Executive Distinction
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf1'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fa'
  on-surface: '#111c2c'
  on-surface-variant: '#44474d'
  inverse-surface: '#263142'
  inverse-on-surface: '#ebf1ff'
  outline: '#75777e'
  outline-variant: '#c5c6cd'
  surface-tint: '#515f78'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#0d1c32'
  on-primary-container: '#76849f'
  inverse-primary: '#b9c7e4'
  secondary: '#775a19'
  on-secondary: '#ffffff'
  secondary-container: '#fed488'
  on-secondary-container: '#785a1a'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#191c1d'
  on-tertiary-container: '#828485'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e9c176'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4201'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#f9f9ff'
  on-background: '#111c2c'
  surface-variant: '#d8e3fa'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Montserrat
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-sm:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Source Serif 4
    fontSize: 20px
    fontWeight: '400'
    lineHeight: 32px
  body-md:
    fontFamily: Source Serif 4
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 32px
  section-padding-v: 120px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system is engineered to project authority, intellectual depth, and executive-level precision. The brand personality is rooted in "Premium Minimalism"—a fusion of high-end editorial aesthetics and modern digital fluidity. It targets stakeholders, high-value clients, and industry peers who value clarity, understated luxury, and meticulous attention to detail.

The visual style draws heavily from **Minimalism** and **Glassmorphism**. It utilizes expansive white space to frame content as high-art, while employing frosted glass textures and subtle blurs to create a sense of multi-dimensional depth. The emotional response should be one of immediate trust, calm sophistication, and professional excellence. Interaction is characterized by smooth transitions and low-friction layouts that allow the content to breathe.

## Colors

The palette is anchored by **Deep Navy Blue**, providing a foundational weight and "executive" feel. **Gold Accents** are used sparingly for critical calls-to-action and highlights, symbolizing premium quality and success.

- **Primary (#0A192F):** Used for primary headings, navigation backgrounds, and high-emphasis elements.
- **Secondary (#C5A059):** Reserved for accentuation, links, active states, and decorative section dividers.
- **Background (#F8F9FA):** A soft, light gray that reduces eye strain and provides a sophisticated alternative to pure white.
- **Surface (White):** Used for cards and elevated components to create contrast against the background.

## Typography

This system utilizes a high-contrast typographic pairing to balance modern tech with traditional authority. **Montserrat** provides a clean, geometric structure for headlines, while **Source Serif 4** offers an academic, literary quality to body text that signals expertise.

For display sizes, tight letter spacing and heavy weights are used to command attention. Body text maintains generous line height and a slightly larger base size (20px for lead paragraphs) to ensure a comfortable, premium reading experience. Labels and metadata use **Inter** in uppercase with expanded tracking to provide a technical, organized counterpoint to the serif body copy.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** system centered on a 12-column desktop architecture. To evoke a premium feel, the design utilizes "Over-spacing"—intentionally large vertical margins (120px+) between sections to allow the user to focus on one narrative block at a time.

- **Desktop (1280px+):** 12 columns, 32px gutters, auto margins.
- **Tablet (768px - 1024px):** 8 columns, 24px gutters, 40px side margins.
- **Mobile (< 768px):** 4 columns, 16px gutters, 20px side margins. Horizontal padding is prioritized to keep text readable on small widths.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and **Ambient Shadows** rather than stark borders.

1.  **The Base Layer:** Light Gray (#F8F9FA) creates the foundation.
2.  **The Surface Layer:** White cards use a very soft, diffused shadow (0px 10px 30px rgba(10, 25, 47, 0.04)) to appear as if floating just above the background.
3.  **The Interactive Layer:** Navigation bars and floating action elements use a backdrop blur (12px to 20px) with a semi-transparent white fill (opacity 0.7) and a 1px white border (opacity 0.1) to create the signature "frosted glass" look.
4.  **The Focus Layer:** Active elements may feature a subtle Gold (#C5A059) outer glow to signify priority.

## Shapes

The shape language is "Rounded-Sophisticated." We avoid sharp, aggressive corners in favor of a 0.5rem (8px) base radius, which feels approachable yet disciplined. For larger components like hero images or feature cards, the `rounded-xl` (24px) setting is used to emphasize the soft, premium aesthetic. Buttons and pills should lean towards higher roundedness to differentiate them from structural layout containers.

## Components

### Buttons
- **Primary:** Deep Navy background, White text, 8px radius. On hover, the background transitions to a slightly lighter navy with a 2px vertical lift.
- **Secondary (Outline):** 1px Gold border, Gold text. On hover, fills with a 5% Gold tint.

### Cards
Cards are the primary content vessel. They feature white backgrounds, the standard ambient shadow, and no visible border except on hover, where a 1px Gold border at 30% opacity fades in.

### Animated Progress Bars
Used for skill visualization. The track is Light Gray, and the fill is a Gold-to-Navy gradient. The fill should animate from 0 to its value on scroll-into-view with a "power4.out" easing.

### Section Dividers
Dividers are not simple lines. They are 1px thick Gold lines that span only 40% of the container width, centered, often accompanied by a small geometric Gold diamond or the user's initials in the center to create an editorial feel.

### Input Fields
Minimalist design: only a bottom border (1px, Deep Navy, 20% opacity). When focused, the border becomes Gold and a very subtle 2px Gold glow appears at the base. Labels remain small and uppercase above the field.

### Interactive Hover States
All links should feature a "sliding underline" effect—a 2px Gold line that expands from the center outward when hovered.