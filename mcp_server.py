"""
MCP Server for Frontal Cerebral Regional Tissue Oxygenation (NIRS rSO2) Skill.
Exposes JSON-RPC Model Context Protocol tools for prefrontal hemodynamics and cognitive oxygen extraction.
"""

import sys
import json
from typing import Dict, Any
from client import CerebralTissueOxygenationClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_cerebral_oxygenation",
                "description": "Calculates frontal cerebral regional tissue oxygen saturation (rSO2), Fractional Tissue Oxygen Extraction (FTOE), and hemodynamic reserve score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "frontal_rso2_pct": {
                            "type": "number",
                            "description": "Frontal cortex near-infrared tissue oxygen saturation in percentage (e.g. 68.5%)."
                        },
                        "systemic_spo2_pct": {
                            "type": "number",
                            "description": "Peripheral arterial pulse oximetry saturation in percentage (e.g. 98.0%).",
                            "default": 98.0
                        },
                        "baseline_rso2_pct": {
                            "type": "number",
                            "description": "Optional resting baseline rSO2 percentage."
                        },
                        "etco2_mmhg": {
                            "type": "number",
                            "description": "Optional end-tidal carbon dioxide in mmHg."
                        }
                    },
                    "required": ["frontal_rso2_pct"]
                }
            }
        ]
    }


def handle_request(client: CerebralTissueOxygenationClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_cerebral_oxygenation":
            base_val = args.get("baseline_rso2_pct")
            if base_val is not None:
                base_val = float(base_val)

            et_val = args.get("etco2_mmhg")
            if et_val is not None:
                et_val = float(et_val)

            res = client.evaluate_cerebral_oxygenation(
                frontal_rso2_pct=float(args.get("frontal_rso2_pct", 68.0)),
                systemic_spo2_pct=float(args.get("systemic_spo2_pct", 98.0)),
                baseline_rso2_pct=base_val,
                etco2_mmhg=et_val
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = CerebralTissueOxygenationClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
