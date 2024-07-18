"""Singer.io Target for the Snowflake data warehouse platform."""

from __future__ import annotations

import logging

__version__ = "0.0.0"

logging.getLogger('snowflake.connector').setLevel(logging.WARNING)
