"""
Base Scraper (Abstract)
=======================
Defines the interface that all platform scrapers must implement.
Enforces consistent structure across different platform adapters.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl


class ScrapedUser(BaseModel):
    """
    Strict data contract for B2B leads. 
    Enforces validation on critical fields to prevent pipeline pollution.
    """
    username: str = Field(..., min_length=1, description="Primary identifier (usually company ID or slug)")
    display_name: Optional[str] = Field(None, description="Decision maker name")
    profile_url: Optional[str] = Field(None, description="Valid URL to the lead's profile")
    scraped_at: str = Field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    def to_dict(self) -> dict:
        return self.model_dump(mode='json')


class ScrapeResult(BaseModel):
    """Container for a full scrape operation result."""
    users: list[ScrapedUser] = Field(default_factory=list)
    pages_scraped: int = 0
    errors: list[str] = Field(default_factory=list)
    started_at: str = Field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    completed_at: Optional[str] = None
    duration_seconds: float = 0.0

    def finalize(self, start_time: float) -> None:
        """Mark the result as complete with timing info."""
        import time
        self.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.duration_seconds = round(time.time() - start_time, 2)

    @property
    def success(self) -> bool:
        return len(self.users) > 0


class BaseScraper(ABC):
    """
    Abstract base class for platform scrapers.

    Subclass this to implement scraping for a specific platform.
    The interface enforces:
      1. Authentication (if required)
      2. Scraping logic
      3. Clean shutdown
    """

    @abstractmethod
    async def authenticate(self) -> bool:
        """
        Login to the platform if authentication is required.

        Returns:
            True if login succeeded or no login needed, False otherwise.
        """
        ...

    @abstractmethod
    async def scrape(self) -> ScrapeResult:
        """
        Execute the scraping operation.

        Returns:
            A ScrapeResult containing all extracted users and metadata.
        """
        ...

    @abstractmethod
    async def shutdown(self) -> None:
        """Clean up browser resources and sessions."""
        ...
