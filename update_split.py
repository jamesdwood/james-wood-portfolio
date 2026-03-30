import re

with open("/tmp/split_ticket.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace blockquote stylings used in Doc360
content = content.replace("::: (Info) (", "!!! info\n    ").replace("::: (Warning) (", "!!! warning\n    ").replace(":::(Warning) (", "!!! warning\n    ")
content = re.sub(r"\)\s*:::", "\n", content, flags=re.MULTILINE)

header = """# Shop, book, exchange, and cancel Split Tickets in SilverCore

!!! abstract "Portfolio Context"
    **Role:** Lead Technical Writer  
    **Context:** This implementation guide explains how to handle "Split Ticketing" in our booking API. Split Ticketing is a uniquely complex UK rail business logic where a customer takes one continuous journey but holds multiple tickets to circumvent high through-fares. Managing partial refunds, order exchanges, and payment statuses across disconnected logical reservations required tight coordination with backend developers to document accurately.

"""

parts = content.split("---", 2)
if len(parts) >= 3:
    content_without_frontmatter = parts[2].strip()
else:
    content_without_frontmatter = content.strip()

new_content = header + "\n" + content_without_frontmatter

with open("/Users/james.wood/workspaces/portfolio/docs/samples/implementation-guide.md", "w", encoding="utf-8") as f:
    f.write(new_content)
