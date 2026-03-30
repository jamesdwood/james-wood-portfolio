import re
import os

# --- SPLIT TICKETING ---
with open("/tmp/split_ticket.md", "r", encoding="utf-8") as f:
    split_content = f.read()

split_content = split_content.replace("::: (Info) (", "!!! info\n    ").replace("::: (Warning) (", "!!! warning\n    ").replace(":::(Warning) (", "!!! warning\n    ")
split_content = re.sub(r"\)\s*:::", "\n", split_content, flags=re.MULTILINE)

split_header = """# Shop, book, exchange, and cancel Split Tickets in SilverCore

!!! abstract "Portfolio Context"
    **Role:** Lead Technical Writer  
    **Context:** This implementation guide explains how to handle "Split Ticketing" in our booking API. Split Ticketing is a uniquely complex UK rail business logic where a customer takes one continuous journey but holds multiple tickets to circumvent high through-fares. Managing partial refunds, order exchanges, and payment statuses across disconnected logical reservations required tight coordination with backend developers to document accurately.

"""

split_parts = split_content.split("---", 2)
split_final = split_header + "\n" + (split_parts[2].strip() if len(split_parts) >= 3 else split_content.strip())

with open("/Users/james.wood/workspaces/portfolio/docs/samples/implementation-guide.md", "w", encoding="utf-8") as f:
    f.write(split_final)


# --- SILVERONE ---
with open("/tmp/silverone.md", "r", encoding="utf-8") as f:
    so_content = f.read()

so_content = so_content.replace("::: (Info) (", "!!! info\n    ").replace("::: (Warning) (", "!!! warning\n    ").replace(":::(Warning) (", "!!! warning\n    ")
so_content = re.sub(r"\)\s*:::", "\n", so_content, flags=re.MULTILINE)

so_header = """# Platform Architecture: The SilverOne API

!!! abstract "Portfolio Context"
    **Role:** Lead Technical Writer  
    **Context:** This conceptual guide introduces our unified Open Sales and Distribution Model (OSDM) implementation. It explains to developers how multiple legacy railway integrators are aggregated behind a single asynchronous REST standard.
    **Key Skills:** Information architecture, distilling highly complex multi-tier architectural concepts into digestible explanations, applying industry standards (OSDM) to proprietary models.

"""

so_parts = so_content.split("---", 2)
so_final = so_header + "\n" + (so_parts[2].strip() if len(so_parts) >= 3 else so_content.strip())

with open("/Users/james.wood/workspaces/portfolio/docs/samples/conceptual-overview.md", "w", encoding="utf-8") as f:
    f.write(so_final)
