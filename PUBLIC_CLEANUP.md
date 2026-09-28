# Public Repository Cleanup

This file documents changes made when converting the original local Django project into a standalone public GitHub repository.

## Removed

- Original `.git/` directory and commit history
- `.DS_Store` and machine-specific metadata
- Hard-coded Django `SECRET_KEY`
- Precise street address from the old portfolio homepage
- Obsolete school email address
- Placeholder résumé experience, awards, and interest text inherited from the starter theme
- Hard-coded development-only `localhost` and `127.0.0.1` navigation
- Old Google Drive document/folder links
- Unused `static/index/` theme package
- Unrouted duplicate template `img_storage.html`

## Added / improved

- Environment-based Django configuration
- `.env.example`
- GitHub-oriented `.gitignore`
- `requirements.txt`
- Root `/` route
- Cleaner homepage and project index
- Django route-based internal navigation
- Basic route tests
- Model cleanup for the legacy COVID-19 data model
- README and third-party license notice

## Preserved

- Django application structure
- Original detailed COVID-19 visualization write-up
- Project figures and screenshots used by the write-up
- Portfolio profile image that is intentionally part of the public site presentation
- Original project attribution and external public data-source references

## Important

This cleaned repository should be initialized as a **new Git repository** rather than restoring the old `.git` directory. That prevents removed secrets or obsolete personal information from surviving in Git history.
