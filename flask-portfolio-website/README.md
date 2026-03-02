# TTDS Assignment 4 — Flask Portfolio Website

A personal portfolio website built with **Flask** (Python backend) and the **Meyawo** Bootstrap theme. Features multiple sections including home, about, skills, projects, and contact. Includes a complete SCSS build pipeline via Gulp.

## Tech Stack

- **Backend** — Python, Flask
- **Frontend** — HTML5, CSS3, SCSS, Bootstrap 4, jQuery, Themify Icons
- **Build** — Gulp (SCSS compilation)

## Project Structure

```
├── 0010/
│   ├── app.py                # Flask application entry point
│   ├── Portfolio_Report.docx
│   └── portfolio/
│       ├── app.py            # Portfolio Flask app
│       ├── 0018.py           # Alternate version
│       └── assets/
│           ├── css/          # Compiled CSS
│           ├── js/           # JavaScript
│           ├── imgs/         # Portfolio images and icons
│           ├── scss/         # SCSS source files
│           │   ├── abstracts/    # Variables, mixins
│           │   ├── base/         # Base styles, typography
│           │   ├── components/   # Navbar, cards, buttons, etc.
│           │   └── layout/       # Header, footer, sections
│           └── vendors/      # Bootstrap, jQuery, Themify Icons
└── meyawo/
    ├── package.json          # Node.js dependencies
    ├── gulpfile.js           # Gulp build tasks
    ├── public_html/
    │   ├── index.html        # Main portfolio page
    │   ├── components.html   # UI component demo
    │   └── assets/           # CSS, JS, SCSS, images
    ├── README.txt
    └── LICENSE.txt
```

## Running the Portfolio

```bash
pip install flask
python 0010/portfolio/app.py
```

Open `http://localhost:5000` to view the portfolio.

### Building SCSS (optional)

```bash
cd meyawo
npm install
gulp
```
