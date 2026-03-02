# TTDS Assignment 4 — Flask Portfolio Website

A personal portfolio website built with **Flask** (Python backend) and the **Meyawo** Bootstrap 4 theme. Features home, about, skills, projects, and contact sections. Includes a complete SCSS build pipeline via Gulp for frontend customization.

## Use Case

Developers who want a clean, responsive personal portfolio with a Python/Flask backend — serving static pages through Flask's template engine with a professional Bootstrap theme and full SCSS source for easy styling customization.

## Features

- Multi-section portfolio: Home, About, Skills, Projects, Contact
- Responsive Bootstrap 4 layout (Meyawo theme)
- SCSS source files with organized architecture (abstracts, base, components, layout)
- Gulp build pipeline for SCSS compilation and asset management
- Themify Icons for consistent iconography

## Tech Stack

| Layer | Tools |
|---|---|
| Backend | Python 3.7+, Flask |
| Frontend | HTML5, CSS3, SCSS, Bootstrap 4, jQuery |
| Icons | Themify Icons |
| Build | Gulp, Node.js (for SCSS compilation) |

## Prerequisites

- Python 3.7 or higher
- Flask (`pip install flask`)
- Node.js + npm (only needed if modifying SCSS styles)

## Running the Portfolio

```bash
pip install flask
python 0010/portfolio/app.py
```

Open `http://localhost:5000` in your browser to view the portfolio.

## Rebuilding Styles (Optional)

Only needed if you modify the SCSS source files in `assets/scss/`:

```bash
cd meyawo
npm install
gulp
```

This compiles SCSS to CSS and outputs to the `assets/css/` directory.

## Project Structure

```
├── 0010/
│   ├── app.py                     # Flask entry point (alternate)
│   ├── Portfolio_Report.docx      # Assignment report
│   └── portfolio/
│       ├── app.py                 # Main Flask app (run this)
│       ├── 0018.py                # Group member alternate version
│       └── assets/
│           ├── css/               # Compiled CSS (ready to use)
│           ├── js/                # JavaScript files
│           ├── imgs/              # Portfolio images and icons
│           ├── scss/              # SCSS source files
│           │   ├── abstracts/     # Variables, mixins, functions
│           │   ├── base/          # Base styles, typography, resets
│           │   ├── components/    # Navbar, cards, buttons, badges
│           │   └── layout/        # Header, footer, section layouts
│           └── vendors/           # Bootstrap, jQuery, Themify Icons
└── meyawo/
    ├── package.json               # Node.js dependencies
    ├── gulpfile.js                # Gulp build tasks
    ├── public_html/
    │   ├── index.html             # Standalone HTML version
    │   ├── components.html        # UI component demo page
    │   └── assets/                # Theme assets
    ├── README.txt                 # Meyawo theme documentation
    └── LICENSE.txt
```

## Output & Results

- A fully functional portfolio website served at `http://localhost:5000`
- Responsive layout that works on desktop and mobile browsers
- The `meyawo/public_html/index.html` can also be opened directly in a browser without Flask (static version)

## Notes

- The compiled CSS (`assets/css/`) is already included — you do **not** need Node.js/Gulp unless modifying styles
- Edit `0010/portfolio/app.py` to update portfolio content (name, project descriptions, skills)
- To deploy publicly, consider using a WSGI server (Gunicorn) behind Nginx, or deploy to Heroku/Render
