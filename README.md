# Skills Assessment Agent

[![CI](https://github.com/kogunlowo123/skills-assessment-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/skills-assessment-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Human Resources | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Skills assessment agent that designs and administers competency assessments, validates skill claims, benchmarks against industry standards, generates skill profiles, and provides development recommendations.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `design_assessment` | Design a skills assessment for a role or competency area |
| `evaluate_submission` | Evaluate a completed skills assessment submission |
| `validate_skills` | Validate claimed skills through evidence and verification |
| `benchmark_skills` | Benchmark employee skills against industry standards |
| `generate_development_plan` | Generate a development plan based on assessment results |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/assessments/design` | Design assessment |
| `POST` | `/api/v1/assessments/evaluate` | Evaluate submission |
| `POST` | `/api/v1/assessments/validate-skills` | Validate skills |
| `POST` | `/api/v1/assessments/benchmark` | Benchmark skills |
| `POST` | `/api/v1/assessments/development-plan` | Generate development plan |

## Features

- Assessment Design
- Skill Validation
- Industry Benchmarking
- Profile Generation
- Development Recommendations

## Integrations

- Hackerrank
- Codility
- Pluralsight Skills
- Skillsoft
- Workday Skills

## Architecture

```
skills-assessment-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── skills_assessment_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Assessment Platform + Skills Taxonomy + LLM**

---

Built as part of the Enterprise AI Agent Platform.
