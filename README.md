# AERG editable website

## Open and edit
Open index.html in a modern browser. The website is self-contained; navigation uses hash routes, so no server or build process is needed.
Click “Edit website” at the bottom right. Click outlined headings and paragraphs to edit them. “Save in browser” stores edits locally. “Download edited website” exports a standalone HTML copy containing your edits. “Reset edits” restores the original draft.
The editor covers marked text, not all navigation labels, cards or page structures. Edit app.js and styles.css for structural changes. The self-contained index.html embeds those files; use build.py after source changes to rebuild it.

## Pages
Home, About, Work, five focus-area detail views, Journal, three sample articles, Contact, draft Privacy and a missing-page view.

## Deployment
Upload index.html to a static web host. No installation or framework is required. This is a front-end website, not a hosted deployment or CMS. Hash routes do not provide the same separate-page SEO as server-rendered pages.

## Contact form
The form validates inputs and downloads an enquiry draft on the visitor’s device. It DOES NOT send email or save submissions to a server. Provide a verified destination address and backend before enabling live submissions. No donation processing is included.

## Before publication
Approve all copy; provide legal name/status, founding details, team, real geography, verified projects, impact evidence, email and social links. Replace the draft privacy notice based on your actual hosting and processing. Review accessibility, image suitability and local requirements.

## Design and assets
This is an original AERG adaptation of the reference site's information architecture, not an exact visual clone or a copy of RAFT’s projects, trustees, text or branding.
Reference inspected: https://raft.org.in/ and its about.html, work.html, blog.html and contact.html pages.
Bundled illustrative forest photograph: https://images.unsplash.com/photo-1448375240586-882707db888b
Google Fonts: DM Sans and Manrope, with system-font fallbacks. Fonts need internet access; the image is bundled.

## Verification
Tested in headless Chromium at desktop width 1440 and mobile width 390: focus filtering, article navigation, inline editing, portable edited export, enquiry draft download, mobile navigation and horizontal overflow. No JavaScript errors were observed in these tests. This does not constitute a full accessibility or cross-browser audit.
