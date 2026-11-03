# Frontal Cerebral Regional Tissue Oxygenation (NIRS rSO2) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive calculation of frontal cerebral tissue oxygen saturation (rSO2), Fractional Tissue Oxygen Extraction (FTOE), and cognitive endurance kinetics.

```mermaid
flowchart TD
    FrontalNIRS["Multi-Wavelength Prefrontal NIRS Sensors"] --> BeerLambert["Modified Beer-Lambert HbO2/HbR Absorption"]
    BeerLambert --> rSO2_FTOE["rSO2 Saturation & FTOE Extraction Modeling"]
    rSO2_FTOE --> ReserveScore["Prefrontal Oxygenation Reserve Engine"]
    ReserveScore --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **NIRS Standard Equations**: Implements validated spectroscopic equations for regional cerebral oxygenation.
- **Cognitive Exhaustion Stratification**: Quantitative evaluation of microvascular supply vs demand in intense work.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CerebralTissueOxygenationClient

client = CerebralTissueOxygenationClient()
result = client.evaluate_cerebral_oxygenation(
    frontal_rso2_pct=69.5,
    systemic_spo2_pct=99.0,
    baseline_rso2_pct=70.0
)
print("Frontal rSO2:", result["frontal_rso2_pct"], "%")
print("Classification:", result["classification"])
```

## License
Apache-2.0
