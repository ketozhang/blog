from datetime import date
from pathlib import Path

POST_PATH = Path(__file__).parent.parent / "_posts"

# Parse date from user input, default is today
date = date.today()
if user_date := input(f"Enter date (YYYY-MM-DD) [default: {date}]: "):
    date = user_date

title = input("Enter title: ")
assert title, "Title cannot be empty"
fname = f'{date}-{"-".join(title.lower().split(" "))}.md'
frontmatter = f"""title: "{title}"\nlayout: post"""
print(POST_PATH / fname)
print(frontmatter)

with open(POST_PATH / fname, "w") as f:
    f.write(f"---\n{frontmatter}\n---")