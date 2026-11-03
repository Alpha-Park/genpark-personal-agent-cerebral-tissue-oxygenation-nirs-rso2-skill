---
name: genpark-personal-agent-cerebral-tissue-oxygenation-nirs-rso2-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for evaluating frontal cerebral regional tissue oxygenation (rSO2), Fractional Tissue Oxygen Extraction (FTOE), and mental workload reserve.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Frontal Cerebral Regional Tissue Oxygenation (rSO2) Skill

A sovereign personal agent capability for assessing prefrontal microvascular perfusion, cognitive metabolic oxygen extraction, and intellectual endurance via near-infrared spectroscopy (NIRS) metrics.

## Core Capabilities
- **Regional Oxygen Saturation ($rSO_2$)**: Tracks local oxyhemoglobin / total hemoglobin ratio in the frontal cortex.
- **Fractional Tissue Oxygen Extraction (FTOE)**: Quantifies the balance between systemic delivery and brain tissue extraction.
- **Frontal Oxygenation Reserve Index**: 0-100 score indicating mental stamina and resistance to cognitive desaturation.
- **Cognitive Ergonomics & Recovery**: Provides environmental air quality checks and structured ventilatory breaks.

## Fast Invocation
```python
from client import CerebralTissueOxygenationClient

client = CerebralTissueOxygenationClient()
res = client.evaluate_cerebral_oxygenation(
    frontal_rso2_pct=69.5,
    systemic_spo2_pct=99.0,
    baseline_rso2_pct=70.0
)
print("Frontal rSO2:", res["frontal_rso2_pct"], "%")
print("Extraction (FTOE):", res["fractional_tissue_oxygen_extraction_ftoe"])
print("Reserve Score:", res["prefrontal_oxygenation_reserve_score"])
```
