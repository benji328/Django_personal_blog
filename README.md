# Django Personal Portfolio & Project Blog

A cleaned public archive of an early personal portfolio/blog built with **Python and Django**. The site combines a portfolio-style landing page with longer project write-ups, including a COVID-19 geographic data-visualization project.

This repository is intentionally separate from my Java and Python/data-science repositories because the blog is a complete Django web application with its own routing, templates, static assets, and project history.

## What the site contains

- A Django-powered portfolio/blog landing page
- A project index
- A detailed write-up on **Geographical Data Visualization for High-Dimensional Symbolic Data**
- Supporting notes describing the COVID-19 dataset and project context
- Static technical figures from the original data-visualization work
- Basic Django models, routing, tests, and admin support

## Project structure

```text
.
├── blog/                  # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── home/                  # Portfolio landing page app
│   ├── templates/home/
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── posts/                 # Project/blog pages
│   ├── migrations/
│   ├── templates/posts/
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── static/
│   ├── home/              # Portfolio CSS/JS and profile assets
│   └── posts/             # Article CSS/JS and technical figures
├── .env.example
├── .gitignore
├── LICENSE-NOTICE.md
├── PUBLIC_CLEANUP.md
├── requirements.txt
└── manage.py
```

## Running locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd django-personal-blog
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure local environment variables

Copy `.env.example` values into your shell/environment, or set the variables manually.

For local development, the defaults in `settings.py` are sufficient to start the app. For any real deployment, set a **new strong** `DJANGO_SECRET_KEY` and turn debug mode off.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open:

```text
/
```

## Main routes

| Route | Purpose |
| --- | --- |
| `/` | Portfolio/blog landing page |
| `/home/` | Alternate landing-page route retained for compatibility |
| `/posts/projects/` | Project index |
| `/posts/COVID19_Map/` | Detailed COVID-19 visualization write-up |
| `/posts/data_storage/` | Dataset and project-context notes |
| `/admin/` | Standard Django admin |

## Historical context

This project began as an early web-development project and was maintained over several years. The original site mixed personal portfolio content with a longer technical write-up about geographic visualization of high-dimensional COVID-19 data.

The public GitHub version focuses on the **software and project-writing portions** of the site rather than treating the old landing page as a current résumé.

## Public cleanup performed

Before preparing this repository for GitHub, I cleaned the original project to avoid publishing stale or sensitive development material. The public version:

- removes the old nested `.git` history;
- removes the original hard-coded Django secret key;
- moves deployment-sensitive configuration to environment variables;
- removes a precise personal street address and obsolete school email from the old homepage;
- removes placeholder résumé sections inherited from the original Bootstrap theme;
- replaces hard-coded `localhost` / `127.0.0.1` navigation with Django URL routing;
- removes old Google Drive document links from the public archive;
- removes unused theme assets and dead templates;
- adds dependency documentation, tests, `.gitignore`, and public-release notes.

See [`PUBLIC_CLEANUP.md`](PUBLIC_CLEANUP.md) for more detail.

## Security note

The original project contained a hard-coded Django development `SECRET_KEY`. That value is **not included in this cleaned repository** and should be considered exposed if it was ever used elsewhere. Do not reuse it.

The public version uses:

```text
DJANGO_SECRET_KEY
DJANGO_DEBUG
DJANGO_ALLOWED_HOSTS
```

for environment-specific settings.

## Third-party front-end assets

The visual design uses assets derived from **Start Bootstrap Resume** / Bootstrap and related open-source front-end components. Their existing copyright/license headers are retained in the distributed CSS/JavaScript where applicable.

See [`LICENSE-NOTICE.md`](LICENSE-NOTICE.md).

## Status

This repository is best understood as a **cleaned archive / portfolio project**, not a production-ready hosted service. The application is intentionally small and keeps the original technical article content while improving repository organization and public-release hygiene.
