"""
Frontal Cerebral Regional Tissue Oxygenation (NIRS rSO2) & Microvascular Engine.
Provides deterministic, zero-dependency modeling of regional cerebral oxygen saturation (rSO2),
cerebral fractional tissue oxygen extraction (FTOE), and prefrontal hemodynamic reserve.
"""

from typing import Dict, Any, List, Optional


class CerebralTissueOxygenationClient:
    """
    Deterministic client for calculating cerebral regional tissue oxygenation (rSO2) via NIRS.
    Evaluates prefrontal microvascular perfusion, cognitive oxygen consumption, and fractional extraction.
    """

    def __init__(self):
        pass

    def evaluate_cerebral_oxygenation(
        self,
        frontal_rso2_pct: float,
        systemic_spo2_pct: float = 98.0,
        baseline_rso2_pct: Optional[float] = None,
        etco2_mmhg: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Evaluates cerebral oxygen saturation metrics:
        - FTOE = (SpO2 - rSO2) / SpO2
        - Baseline delta = rSO2 - baseline_rso2
        Normative adult values:
        - Resting rSO2: 60% - 78%
        - FTOE: 0.24 - 0.38
        """
        if frontal_rso2_pct <= 0 or frontal_rso2_pct > 100.0:
            return {"error": "Invalid frontal rSO2: must be between 0 and 100"}
        if systemic_spo2_pct <= 0 or systemic_spo2_pct > 100.0:
            return {"error": "Invalid systemic SpO2: must be between 0 and 100"}

        ftoe = round((systemic_spo2_pct - frontal_rso2_pct) / systemic_spo2_pct, 3)

        delta_baseline = None
        if baseline_rso2_pct is not None:
            delta_baseline = round(frontal_rso2_pct - baseline_rso2_pct, 1)

        # Frontal Oxygenation Reserve Index (0 - 100):
        # rSO2 65-75% -> 85-95.
        # rSO2 < 55% -> < 50 (Cerebral desaturation / fatigue).
        if 62.0 <= frontal_rso2_pct <= 76.0:
            score = 85.0 + min(15.0, (frontal_rso2_pct - 62.0) * 0.7)
        elif frontal_rso2_pct > 76.0:
            score = 90.0 - (frontal_rso2_pct - 76.0) * 1.5
        elif frontal_rso2_pct >= 55.0:
            score = 55.0 + ((frontal_rso2_pct - 55.0) / 7.0) * 30.0
        elif frontal_rso2_pct >= 45.0:
            score = 25.0 + ((frontal_rso2_pct - 45.0) / 10.0) * 30.0
        else:
            score = max(5.0, 25.0 - (45.0 - frontal_rso2_pct) * 1.5)

        resilience_score = round(min(100.0, max(5.0, score)), 1)

        if frontal_rso2_pct >= 64.0 and ftoe <= 0.35:
            tier = "OPTIMAL_PREFRONTAL_OXYGENATION"
            interp = f"Robust frontal tissue oxygenation (rSO2 {frontal_rso2_pct}%, FTOE {ftoe}); adequate microvascular supply matching metabolic demand."
            guidance = "Cognitive hemodynamics are optimal. Prime state for high-bandwidth analytical synthesis."
        elif frontal_rso2_pct >= 58.0:
            tier = "MILD_COGNITIVE_OXYGEN_EXTRACTION_ELEVATION"
            interp = f"Modest drop in rSO2 ({frontal_rso2_pct}%, FTOE {ftoe}); elevated metabolic oxygen consumption under mental workload."
            guidance = "Sustained mental workload detected. Ensure adequate hydration, posture realignment, and brief micro-pauses."
        elif frontal_rso2_pct >= 50.0:
            tier = "PREFRONTAL_HYPOPERFUSION_FATIGUE"
            interp = f"Significant reduction in regional oxygenation (rSO2 {frontal_rso2_pct}%); high fractional extraction indicating fatigue or cerebral vasoconstriction."
            guidance = "Cerebral oxygen saturation depressed. Step away from screen, perform deep ventilatory breathing, and hydrate."
        else:
            tier = "CRITICAL_CEREBRAL_DESATURATION"
            interp = f"Severe prefrontal desaturation (rSO2 {frontal_rso2_pct}% < 50%); risk of cognitive sluggishness, syncope, or hypoxia."
            guidance = "Acute desaturation alert. Cease intense tasks immediately; verify ambient air quality and rest in a well-ventilated space."

        return {
            "frontal_rso2_pct": frontal_rso2_pct,
            "systemic_spo2_pct": systemic_spo2_pct,
            "fractional_tissue_oxygen_extraction_ftoe": ftoe,
            "delta_from_baseline_pct": delta_baseline,
            "etco2_mmhg": etco2_mmhg,
            "prefrontal_oxygenation_reserve_score": resilience_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
