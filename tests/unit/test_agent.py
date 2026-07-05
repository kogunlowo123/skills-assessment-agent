"""Skills Assessment Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_design_assessment():
    """Test Design a skills assessment for a role or competency area."""
    tools = AgentTools()
    result = await tools.design_assessment(role="test", competencies="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_evaluate_submission():
    """Test Evaluate a completed skills assessment submission."""
    tools = AgentTools()
    result = await tools.evaluate_submission(assessment_id="test", submission="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_validate_skills():
    """Test Validate claimed skills through evidence and verification."""
    tools = AgentTools()
    result = await tools.validate_skills(employee_id="test", claimed_skills="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_benchmark_skills():
    """Test Benchmark employee skills against industry standards."""
    tools = AgentTools()
    result = await tools.benchmark_skills(employee_id="test", industry="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.skills_assessment_agent_agent import SkillsAssessmentAgentAgent
    agent = SkillsAssessmentAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
