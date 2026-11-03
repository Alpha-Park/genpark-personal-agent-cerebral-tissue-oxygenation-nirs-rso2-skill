"""
Example Usage: Frontal Cerebral Regional Tissue Oxygenation (NIRS rSO2).
Demonstrates non-invasive calculation of cerebral FTOE and oxygenation reserve.
"""

from client import CerebralTissueOxygenationClient


def main():
    client = CerebralTissueOxygenationClient()
    print("=== Frontal Cerebral Regional Tissue Oxygenation (rSO2) Demo ===")

    # Test Case 1: Healthy alert baseline
    res1 = client.evaluate_cerebral_oxygenation(
        frontal_rso2_pct=69.5,
        systemic_spo2_pct=99.0,
        baseline_rso2_pct=70.0,
        etco2_mmhg=38.5
    )
    print("\nTest Case 1: Healthy Alert Baseline")
    print(f"  Frontal rSO2: {res1['frontal_rso2_pct']}% | Systemic SpO2: {res1['systemic_spo2_pct']}%")
    print(f"  Fractional Extraction (FTOE): {res1['fractional_tissue_oxygen_extraction_ftoe']}")
    print(f"  Delta from Baseline: {res1['delta_from_baseline_pct']}%")
    print(f"  Oxygenation Reserve Score: {res1['prefrontal_oxygenation_reserve_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Intense cognitive load / prolonged screen marathon
    res2 = client.evaluate_cerebral_oxygenation(
        frontal_rso2_pct=56.0,
        systemic_spo2_pct=97.0,
        baseline_rso2_pct=68.0
    )
    print("\nTest Case 2: Mental Exhaustion / High Extraction")
    print(f"  Frontal rSO2: {res2['frontal_rso2_pct']}% | FTOE: {res2['fractional_tissue_oxygen_extraction_ftoe']}")
    print(f"  Delta from Baseline: {res2['delta_from_baseline_pct']}%")
    print(f"  Reserve Score: {res2['prefrontal_oxygenation_reserve_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
