"""Test configuration for Skills Assessment Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "skills-assessment-agent", "category": "Human Resources"}
