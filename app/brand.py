"""User-facing product identity for B-roll.

Keep the MIT license and the original copyright notice in LICENSE.
"""

from pathlib import Path

PRODUCT_NAME = "B-roll"
PRODUCT_TAGLINE = "A BX tool from BixingAI"
GITHUB_URL = "https://github.com/bixingai/b-roll"
LOGO_PATH = Path(__file__).resolve().parent.parent / "resource" / "public" / "logo.png"
GITHUB_ISSUES_URL = f"{GITHUB_URL}/issues"
GITHUB_RELEASES_API_URL = (
    "https://api.github.com/repos/bixingai/b-roll/releases/latest"
)
GITHUB_RELEASES_PAGE_URL = f"{GITHUB_URL}/releases/latest"
