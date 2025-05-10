# Client-Facing Portfolio and Demonstration Environment Setup Guide

This guide provides instructions for setting up and configuring the client-facing portfolio and demonstration environment for Green AI Solutions.

## Overview

The client-facing portfolio is a comprehensive demonstration environment designed to showcase Green AI Solutions' capabilities to potential clients in a structured, engaging manner. The environment includes interactive demonstrations, case studies, pricing models, and compliance frameworks organized by industry and use case.

## System Requirements

### Hosting Environment

- **Web Server**: Apache or Nginx
- **PHP**: Version 7.4 or higher (for dynamic content)
- **Database**: MySQL 5.7 or higher
- **Storage**: Minimum 10GB for all assets
- **SSL Certificate**: Required for secure access

### Development Environment

- **Local Development**: XAMPP, MAMP, or Docker environment
- **Version Control**: Git repository
- **Deployment**: CI/CD pipeline or manual deployment process

## Directory Structure

The demonstration environment follows this structure:

```
demo-environment/
├── index.html                  # Main landing page
├── css/                        # Stylesheets
│   ├── styles.css              # Main stylesheet
│   ├── components.css          # UI components
│   └── responsive.css          # Responsive design rules
├── js/                         # JavaScript files
│   ├── main.js                 # Main functionality
│   ├── demos.js                # Demo-specific functionality
│   └── calculators.js          # Interactive calculators
├── images/                     # Image assets
│   ├── logos/                  # Logo files
│   ├── mockups/                # System mockups
│   ├── diagrams/               # Conceptual diagrams
│   └── industry/               # Industry-specific images
├── hr-system/                  # HR system demonstrations
│   ├── command-center.html     # HR Command Center demo
│   ├── compliance.html         # Compliance features demo
│   ├── document-automation.html # Document automation demo
│   └── ...
├── ai-consulting/              # AI consulting demonstrations
│   ├── methodology.html        # Implementation methodology
│   ├── knowledge-transfer.html # Knowledge transfer approach
│   └── ...
├── industry-solutions/         # Industry-specific solutions
│   ├── construction/           # Construction industry solutions
│   ├── professional-services/  # Professional services solutions
│   ├── retail/                 # Retail industry solutions
│   └── ...
├── case-studies/               # Case study showcase
│   ├── construction-compliance.html
│   ├── professional-services-automation.html
│   └── ...
├── tools/                      # Interactive tools
│   ├── roi-calculator.html     # ROI calculator
│   ├── compliance-assessment.html # Compliance assessment
│   └── ...
├── resources/                  # Downloadable resources
│   ├── guides/                 # Educational guides
│   ├── templates/              # Document templates
│   └── checklists/             # Compliance checklists
└── admin/                      # Administration tools
    ├── client-setup.php        # Client customization tools
    ├── content-manager.php     # Content management
    └── analytics.php           # Usage analytics
```

## Installation Steps

### 1. Server Preparation

1. Set up web server with required specifications
2. Configure SSL certificate for secure access
3. Set up database for dynamic content
4. Configure server-side caching for optimal performance

```bash
# Example Apache configuration
<VirtualHost *:443>
    ServerName demo.greenaisolutions.com.au
    DocumentRoot /var/www/demo-environment
    
    SSLEngine on
    SSLCertificateFile /path/to/certificate.crt
    SSLCertificateKeyFile /path/to/private.key
    
    <Directory /var/www/demo-environment>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    
    # Caching configuration
    <IfModule mod_expires.c>
        ExpiresActive On
        ExpiresByType image/jpg "access plus 1 year"
        ExpiresByType image/jpeg "access plus 1 year"
        ExpiresByType image/gif "access plus 1 year"
        ExpiresByType image/png "access plus 1 year"
        ExpiresByType text/css "access plus 1 month"
        ExpiresByType application/pdf "access plus 1 month"
        ExpiresByType text/javascript "access plus 1 month"
        ExpiresByType application/javascript "access plus 1 month"
        ExpiresByType image/x-icon "access plus 1 year"
        ExpiresDefault "access plus 2 days"
    </IfModule>
</VirtualHost>
```

### 2. Code Deployment

1. Clone the repository or extract the demonstration environment files
2. Set appropriate file permissions
3. Configure environment-specific settings

```bash
# Clone repository
git clone https://github.com/green-ai-solutions/demo-environment.git /var/www/demo-environment

# Set permissions
find /var/www/demo-environment -type d -exec chmod 755 {} \;
find /var/www/demo-environment -type f -exec chmod 644 {} \;

# Configure environment
cp /var/www/demo-environment/config/env.example.php /var/www/demo-environment/config/env.php
# Edit env.php with appropriate settings
```

### 3. Database Setup

1. Create the database
2. Import the initial schema
3. Set up database user with appropriate permissions

```bash
# Create database
mysql -u root -p -e "CREATE DATABASE green_ai_demo;"

# Import schema
mysql -u root -p green_ai_demo < /var/www/demo-environment/database/schema.sql

# Create user
mysql -u root -p -e "CREATE USER 'green_ai_demo'@'localhost' IDENTIFIED BY 'secure_password';"
mysql -u root -p -e "GRANT ALL PRIVILEGES ON green_ai_demo.* TO 'green_ai_demo'@'localhost';"
mysql -u root -p -e "FLUSH PRIVILEGES;"
```

### 4. Demo Content Installation

1. Upload demonstration assets (images, videos, PDFs)
2. Import sample data for interactive demonstrations
3. Verify content integrity

```bash
# Upload assets
rsync -av --progress ./demo-assets/ /var/www/demo-environment/assets/

# Import sample data
php /var/www/demo-environment/admin/import-sample-data.php

# Verify content
php /var/www/demo-environment/admin/verify-content.php
```

## Client Customization

The demonstration environment supports client-specific customization to create a personalized experience.

### 1. Client Profile Setup

1. Access the admin interface at `/admin/client-setup.php`
2. Create a new client profile with the following information:
   - Company name
   - Industry
   - Size (employees)
   - Location
   - Key challenges
   - Primary interests

### 2. Customization Options

The following elements can be customized for each client:

- **Welcome Message**: Personalized greeting with company name
- **Featured Solutions**: Prioritized based on client needs
- **Case Studies**: Filtered to show relevant industries and challenges
- **Industry Content**: Focused on client's specific industry
- **ROI Calculations**: Pre-populated with industry benchmarks
- **Visual Theme**: Subtle branding adjustments (optional)

### 3. Custom URL Generation

Generate a unique, secure URL for client access:

1. In the admin interface, go to "Client Access Management"
2. Select the client profile
3. Click "Generate Access Link"
4. Set expiration date (optional)
5. Add access restrictions (optional)
6. Copy and share the generated URL with the client

## Demonstration Preparation

### 1. Environment Verification

Before a client demonstration, verify the environment:

```bash
# Run environment verification script
php /var/www/demo-environment/admin/verify-environment.php --client="client_id"

# Check log for any issues
cat /var/www/demo-environment/logs/environment-check.log
```

### 2. Data Preparation

1. Reset demonstration data to ensure a clean environment
2. Pre-populate with industry-appropriate sample data
3. Verify all interactive elements are functioning correctly

```bash
# Reset demo data
php /var/www/demo-environment/admin/reset-demo-data.php --client="client_id"

# Import industry-specific data
php /var/www/demo-environment/admin/import-industry-data.php --client="client_id" --industry="construction"

# Test interactive elements
php /var/www/demo-environment/admin/test-interactive-elements.php --client="client_id"
```

### 3. Access Verification

1. Test client access link in multiple browsers
2. Verify all demonstrations load correctly
3. Test interactive tools with sample inputs
4. Ensure downloadable resources are accessible

## Monitoring and Analytics

The demonstration environment includes monitoring tools to track client engagement and identify areas of interest.

### 1. Activity Tracking

The system tracks:

- Pages viewed
- Time spent on each demonstration
- Interactive tools used
- Resources downloaded
- Navigation patterns

### 2. Analytics Dashboard

Access analytics at `/admin/analytics.php`:

- **Session Timeline**: Chronological view of client interactions
- **Engagement Hotspots**: Most viewed/used demonstrations
- **Interest Analysis**: Automatic categorization of client interests
- **Comparison**: Benchmark against similar clients
- **Follow-up Recommendations**: AI-generated suggestions for follow-up

### 3. Integration with CRM

The demonstration environment can integrate with CRM systems:

1. Configure CRM API settings in `/admin/settings.php`
2. Enable automatic activity logging to CRM
3. Set up notification rules for significant engagement

## Maintenance and Updates

### 1. Content Updates

Regular content updates should include:

- New case studies
- Updated compliance information
- Enhanced demonstration capabilities
- New industry-specific content
- Additional interactive tools

To update content:

```bash
# Pull latest content updates
git pull origin main

# Run content update script
php /var/www/demo-environment/admin/update-content.php

# Verify updated content
php /var/www/demo-environment/admin/verify-content.php
```

### 2. Performance Optimization

Regularly optimize performance:

1. Compress and optimize images
2. Minify CSS and JavaScript
3. Update caching configuration
4. Monitor server resources

```bash
# Run optimization script
php /var/www/demo-environment/admin/optimize-environment.php

# Generate performance report
php /var/www/demo-environment/admin/performance-report.php > /var/www/demo-environment/logs/performance.log
```

### 3. Security Updates

Maintain security with regular updates:

1. Apply security patches promptly
2. Update dependencies
3. Conduct periodic security scans
4. Review access logs for suspicious activity

```bash
# Check for security updates
php /var/www/demo-environment/admin/security-check.php

# Apply updates
composer update

# Run security scan
php /var/www/demo-environment/admin/security-scan.php > /var/www/demo-environment/logs/security-scan.log
```

## Troubleshooting

### Common Issues

1. **Blank or Incomplete Pages**
   - Check browser console for JavaScript errors
   - Verify all required assets are loaded
   - Check server error logs

2. **Slow Performance**
   - Review server resource utilization
   - Check for large unoptimized images
   - Verify caching configuration
   - Monitor database query performance

3. **Interactive Tools Not Working**
   - Verify JavaScript console for errors
   - Check API endpoint responses
   - Confirm calculation logic is functioning
   - Test with sample data

### Support Resources

- **Internal Wiki**: [https://wiki.greenaisolutions.com.au/demo-environment](https://wiki.greenaisolutions.com.au/demo-environment)
- **Support Team**: demo-support@greenaisolutions.com.au
- **Issue Tracker**: [https://github.com/green-ai-solutions/demo-environment/issues](https://github.com/green-ai-solutions/demo-environment/issues)

## Related Documentation

- [Client Demonstration Script](demonstration_script.md)
- [Portfolio Content Guidelines](portfolio_content_guidelines.md)
- [Case Study Template](case_study_template.md)
- [Interactive Tools Specification](interactive_tools_specification.md)

---

**Document Metadata**
- **Title**: Client-Facing Portfolio and Demonstration Environment Setup Guide
- **Version**: 1.0.0
- **Last Updated**: 2025-05-06
- **Owner**: Technical Team
- **Status**: Approved