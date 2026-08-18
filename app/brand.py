"""User-facing product identity for the BixingAI fork.

Keep MIT credit to the MoneyPrinterTurbo upstream in About text. Do not
use this module to hide that history in licenses or source headers.
"""

from pathlib import Path

PRODUCT_NAME = "B-roll"
PRODUCT_TAGLINE = "A BX tool from BixingAI"
GITHUB_URL = "https://github.com/bixingai/vidgen"
LOGO_PATH = Path(__file__).resolve().parent.parent / "resource" / "public" / "logo.png"
GITHUB_ISSUES_URL = f"{GITHUB_URL}/issues"
GITHUB_RELEASES_API_URL = (
    "https://api.github.com/repos/bixingai/vidgen/releases/latest"
)
GITHUB_RELEASES_PAGE_URL = f"{GITHUB_URL}/releases/latest"
