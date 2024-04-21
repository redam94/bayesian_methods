from pathlib import Path

order = [
    "introduction.md",
    "review_of_probability_theory.md",
    "bayes_theorem.md",
]

markdown_file_paths = {file.name: file for file in Path("app/static").glob("*.md")}


string = "\n\n".join([markdown_file_paths[file].read_text() for file in order if file in markdown_file_paths.keys()])
with open("static_html.md", "w") as f:
    f.write(string)