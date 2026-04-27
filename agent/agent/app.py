# Simple Deterministic Reflection Agent (CLI)

import pandas as pd

# Load TSV file
df = pd.read_csv("../tree/reflection-tree.tsv", sep="\t")

# Convert rows into dictionary
nodes = {}
for _, row in df.iterrows():
    nodes[row["id"]] = row.to_dict()

state = {
    "axis1": {"internal": 0, "external": 0},
    "axis2": {"contribution": 0, "entitlement": 0},
    "axis3": {"self": 0, "balanced": 0, "altro": 0},
    "answers": {}
}

def get_node(node_id):
    return nodes.get(node_id)

current = "START"

while current:
    node = get_node(current)

    if node["type"] == "start":
        current = "A1_OPEN"

    elif node["type"] == "question":
        print("\n" + node["text"])
        options = node["options"].split("|")
        
        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")

        choice = int(input("Choose option: ")) - 1
        answer = options[choice]

        state["answers"][node["id"]] = answer

        # Move to next manually (simple logic for demo)
        if node["id"] == "A1_OPEN":
            current = "A1_D1"
        elif node["id"] == "A2_OPEN":
            current = "A2_D1"
        elif node["id"] == "A3_OPEN":
            current = "A3_D1"

    elif node["type"] == "decision":
        # simple routing (kept minimal for demo)
        if node["id"] == "A1_D1":
            if state["answers"]["A1_OPEN"] in ["Productive", "Mixed"]:
                current = "A1_Q_HIGH"
            else:
                current = "A1_Q_LOW"

        elif node["id"] == "A2_D1":
            current = "A2_Q_CONTRIB"

        elif node["id"] == "A3_D1":
            current = "A3_R_SELF"

    elif node["type"] == "reflection":
        print("\n💭 Reflection:")
        print(node["text"])
        current = node.get("target")

    elif node["type"] == "bridge":
        current = node.get("target")

    elif node["type"] == "summary":
        print("\n📊 Summary:")
        print(node["text"])
        current = "END"

    elif node["type"] == "end":
        print("\n✔ Session Complete")
        break
