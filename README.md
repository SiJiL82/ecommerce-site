# Ecommerce Site - Mini Sew N Sew
This project is an e-commerce site allowing the purchase of physical goods.
The site has bee configured to be a store front for my sister's real business - Mini Sew N Sew, as her existing site is lacking many features
she wanted to implement, and is unusable on mobile devices as the site is not responsive.  
This project aims to fix the existing issues she has, by implementing a fully responsive, fully customisable design that she can use and iterate
on in the future to improve her business presence.  

# Table of Contents
- [Ecommerce Site - Mini Sew N Sew](#ecommerce-site---mini-sew-n-sew)
- [Table of Contents](#table-of-contents)
- [Design](#design)
  - [Business Logic](#business-logic)
  - [SEO](#seo)
  - [User Stories](#user-stories)
    - [Key stories:](#key-stories)
  - [Site Wireframes](#site-wireframes)
- [Features](#features)
  - [Navigation Bar](#navigation-bar)
  - [Home Page](#home-page)
  - [Authentication](#authentication)
  - [FAQ Page](#faq-page)
  - [Request a Product](#request-a-product)
  - [Events Page](#events-page)
  - [Product Pages](#product-pages)
  - [Shopping Basket](#shopping-basket)
  - [Checkout Page](#checkout-page)
  - [Newsletter Signup](#newsletter-signup)
  - [Misc](#misc)
- [Testing](#testing)
  - [User Story Testing](#user-story-testing)
  - [Validation](#validation)
- [Deployment](#deployment)
  - [Prerequisites](#prerequisites)
  - [Instructions](#instructions)
- [Issues](#issues)
  - [Known Bugs](#known-bugs)
- [Future Developments](#future-developments)
- [Credits](#credits)

# Design
## Business Logic
- What do users need?
  - View all our products and get information on them.
  - Purchase our products.
  - Raise requests for custom products.
  - Contact us for help.
  - Get info about the company to increase trustworthiness.
  - A user account, with profile, order history etc.
- How do we meet those needs?
  - Products are viewable by visiting the shop page.
    - Products can be filtered down into categories, to help find the product the user is looking for.
    - Each product has its own standalone details page, with more information etc.
  - The site implements a full ecommerce solution, with typical functionality such as a basket and online checkout process.
  - Customer can raise, view, ammend and delete requests for custom products on a simple to use form.
  - Links to contact the site owners are included in the footer of every page. Additionally the request form can be used if that is the applicable to the nature of their contact.
  - The homepage includes an overview of the company, including images and the company vision.
  - Users can create an account on the site, where orders are saved and can be viewed on subsequent visits.
- How do we make these features easy to use and understand?
  - A navbar at the top of every page ensures a consistent journey around the site, and uses intuitively named pages to improve the user experience.
  - Content is presented in a clear, concise manner, with simple to understand terminology.
  - Colours and styling have been chosen to ensure content is clear and easy to read.
- How do we demonstrate expertise, authoritativeness and trustworthiness in the content?
  - Well written copy, which has been spelling and grammar checked improves the experience for the user.
  - Features such as product reviews allow customers to leave genuine feedback on the products, enhancing trustworthiness for other users.
- How do we help users discover the areas of the site?
  - The intuitively laid out navbar exists on every page of the site, which should encourage users to visit the different pages.
  - If a user visits a non-existent page, a custom 404 error page includes links to the homepage and shop, encouraging them to visit those pages.
  - The site features newsletter signup functionality, encouraging users to come back to the site when new products or features are added.
- What marketing strategies do we implement to increase site visits and purchases?
  - Social media accounts to be used along side the main site:
    - Promote specific products.
    - Highlight events / markets we are visiting.
    - Inform people about new products.
    - Post polls / questions about products people would be interested in seeing.
  - Send out a regular newsletter to subscribers with a summary of what's new, and what's upcoming.
## SEO
SEO keyword research to help the site appear high in rankings:
- ### Topics:
- Handmade
- Clothing
- Custom
- For children
- Durable
- Clothing types
- ### Potential keywords / phrases
- Handmade children's clothing
- Custom clothing for children
- Handmade custom clothing
- Made to order
- Long lasting
- Care and attention
- Lovingly crafted
- Quality fabrics
- Clothes
- Babies / Children
- Dresses, Dungarees, Jumpers, Leggings, Rompers, Skirts
## User Stories
An agile process was used during the development to track and iterate on features for the site, using GitHub [project](https://github.com/users/SiJiL82/projects/1)  
### Key stories:  

## Site Wireframes
[DesignWireframes](docs/design_wireframes.md)  

# Features
## Navigation Bar
## Home Page
## Authentication
## FAQ Page
## Request a Product
## Events Page
## Product Pages
## Shopping Basket
## Checkout Page
## Newsletter Signup
## Misc
Email obfuscation - email addresses displayed on the site are protected from scraping by bots, but are still interactable by humans.  

# Testing
## User Story Testing
## Validation

# Deployment
## Prerequisites
## Instructions

# Issues
## Known Bugs
Presently there are no known bugs with the site.
# Future Developments
Customise the AllAuth account management forms (sign up, sign in etc.) so they fit the site style. 
# Credits
- Inspiration for the site design and theme colours taken from the existing website https://www.minisewnsew.com/ however no code/modules etc. were taken from the site - this project was written from scratch just using the site themes and existing product imagery to populate the site, as it is going to be a direct replacement for the existing site.
- [Django Email Obfuscator](https://github.com/morninj/django-email-obfuscator) - used to obfuscate sensitive links such as emails and telephone numbers
- [XML Sitemaps](https://www.xml-sitemaps.com/) - sitemap.xml generated with this tool.
- 