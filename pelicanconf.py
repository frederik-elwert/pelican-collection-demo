AUTHOR = "Frederik Elwert"
SITENAME = "Pelican Collection Demo"
SITEURL = ""

THEME = "pelican-collection-theme"
PATH = "content"

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "en"

# Collection Builder settings
COLLECTION_ITEM_META = [
    {"label": "Label", "value": "label"},
    {"label": "Artist", "value": "artist"},
    {"label": "Type", "value": "object_type"},
    {"label": "Location", "value": "location"},
    {"label": "Current Location", "value": "current_location"},
    {"label": "Date", "value": "_date"},
    {"label": "Source", "value": "source", "type": "link"},
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
