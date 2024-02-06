#!/usr/bin/env python
# coding: utf-8

import os

import bibtexparser
import pandas as pd
from TexSoup import TexSoup


# Functions for parsing the BibLaTeX bibliography

def parse_biblatex_file(filepath):
    parser = bibtexparser.bparser.BibTexParser(ignore_nonstandard_types=False)
    with open(filepath) as f:
        bib = bibtexparser.load(f, parser=parser)

    bib_data = {}
    for entry in bib.entries:
        key = entry["ID"]
        val = {k: v for k, v in entry.items() if k != "ID"}
        bib_data[key] = val
    print(f"Found {len(bib_data)} entries in the BibLaTeX file.")
    return bib_data


# Functions for parsing the LaTeX report

URL_COUNTER = 1


def replace_symbols(text):
    replacements = [
        ("{", ""),
        ("}", ""),
        ("\_", "_"),
        (r"\textbar", "-"),
        (r"\&", "&"),
    ]
    for before, after in replacements:
        text = text.replace(before, after)
    return text


def text_to_url(text, bib_data):
    global URL_COUNTER
    try:
        entry = bib_data[text]
    except KeyError:
        entry = None
    try:
        url = entry["url"]
    except (TypeError, KeyError):
        try:
            url = "https://doi.org/" + entry["doi"]
        except (TypeError, KeyError):
            url = None

    if url:
        tooltip = replace_symbols(entry.get("title", "Title not found"))
        text = f'<a href="{url}" target="_blank" class="tooltip">[{URL_COUNTER}]<span class="tooltiptext">{tooltip}</span></a>'
        URL_COUNTER += 1
    return text


def parse_tabular(tabular, bib_data):
    entries = []
    sep = "§§"
    text = sep.join(tabular.text)
    rows = text.split(r"\\")
    header = rows[0]
    col_names = [name.replace(sep, "").strip() for name in header.split("&")]
    col_names[0] = col_names[0].rsplit("\n")[1]
    for row in rows[1:]:
        record = []
        cols = row.split("&")
        if len(cols) > 2:
            for col in cols:
                items = [text.strip().replace("\n", " ") for text in col.split(sep)]
                entry = [text_to_url(text, bib_data) for text in items if text != ""]
                entry = " ".join(entry)
                record.append(entry)
            entries.append(record)
    print(f"Found {len(entries)} records in a table.")
    return col_names, entries


def parse_latex_file(filepath, bib_data):
    with open(filepath) as f:
        soup = TexSoup(f)
    tables = soup.find_all("xltabular")
    print(f"Found {len(tables)} tables in the LaTeX file.")
    # for i, table in enumerate(tables, 1):
    #    print(i, str(table)[:150])
    #    print()
    parsed_tables = [parse_tabular(t, bib_data) for t in tables]
    return parsed_tables


# Functions for creating the HTML file


def table_to_html(data):
    col_names, rows = data
    out = []
    out.append('<div class="cont">')
    out.append('<table class="sortable">')
    # table head
    out.append("<thead>")
    out.append("<tr>")
    out.append("<th>#</th>")
    out.append("\n".join(f"<th>{name}</th>" for name in col_names))
    out.append("</tr>")
    out.append("</thead>")
    # table body
    out.append("<tbody>")
    for i, row in enumerate(rows, 1):
        out.append("<tr>")
        out.append(f"<td>{i}</td>")
        for col in row:
            out.append("<td>")
            out.append(col)
            out.append("</td>")
        out.append("</tr>")
    out.append("</tbody>")
    out.append("</table>")
    out.append("</div>")
    html_table = "\n".join(out)
    return html_table


def tables_to_html(tex_data):
    html_tables = [table_to_html(table) for table in tex_data]

    html_template = """<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Biomedical knowledge graphs</title>
<script src="sorttable.js"></script>
<style>
body {{
    margin: 2vh 4vw;
    background-color: white;
}}
h1 {{
    color: #333;
    margin-top: 2em;
    margin-bottom: 1em;
    font-size: 1.2em;
    font-family: sans-serif;
}}
h2 {{
    color: #333;
    margin-top: 1.5em;
    margin-bottom: 0.75em;
    margin-left: 1em;
    font-size: 1em;
    font-family: sans-serif;
}}
.intro {{
    margin-left: 1em;
    margin-right: 1em;
    font-family: sans-serif;
}}
.cont {{
    margin-left: 1em;
    margin-right: 1em;
    max-height: 70vh;
    overflow-x: hidden;
    overflow-y: auto;
    border: solid #ddd 1px;
    box-shadow: 0 0 8px rgba(0, 0, 0, 0.25);
}}
table {{
    width: 100%;
    margin: 0;
    padding: 0;
    border-collapse: collapse;
    border: solid #ddd 1px;
    font-size: 0.8em;
    font-family: sans-serif;
}}
table thead tr {{
    background-color: #0c6533;
    color: #fff;
    text-align: left;
}}
table thead {{
    position: sticky;
    top: 0;
    z-index: 999;
}}
table th {{
    padding: 10px 12px;
}}
table td {{
    padding: 10px 12px;
}}
table tbody tr {{
    border-bottom: 1px solid #ddd;
}}
table tbody tr:hover {{
    background-color: #ccc!important;
    border-bottom: 1px solid #ccc!important;
}}
table tbody tr:nth-of-type(even) {{
    background-color: #f8f8f8;
}}
table tbody tr:nth-of-type(odd) {{
    background-color: #f1f1f1;
}}
table tbody td:nth-child(1) {{
    font-weight: 300;
}}
table tbody td:nth-child(2) {{
    font-weight: 600;
}}
a {{
    color: #007859;
}}
.tooltip {{
    position: relative;
    display: inline-block;
}}
.tooltip .tooltiptext {{
    visibility: hidden;
    z-index: 1;
    position: absolute;
    width: 30em;
    left: -13em;
    top: 1.5em;
    padding: 5px;
    border-radius: 3px;
    background-color: #333;
    color: white;
}}
.tooltip:hover .tooltiptext {{
    visibility: visible;
}}
</style>
</head>
<body>
<h1>Introduction</h1>
<div class="intro">
<p>This website supplements the PDF report
<a href="https://github.com/robert-haas/awesome-biomedical-knowledge-graphs/blob/main/target/bmkg.pdf">A survey of biomedical knowledge graphs and of resources to construct them</a>.
</p>
<p>
All tables contained in the report are provided here in a more user-friendly way, for example by allowing to sort tables by a chosen column and to open references directly in a new browser tab.
Other content of the report is not included here, in particular a section about various knowledge graph definitions encountered in practice.
</p>
</div>
<h1>Projects that provide biomedical knowledge graphs</h1>
{table_bkgs}
<h1>Resources for creating biomedical knowledge graphs</h1>
<h2>File formats</h2>
{table_formats}
<h2>Databases</h2>
{table_databases}
<h2>Ontologies and controlled vocabularies</h2>
{table_ontologies}
<h2>Tools</h2>
{table_tools}
<br>
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">
<a property="dct:title" rel="cc:attributionURL" href="https://github.com/robert-haas/awesome-biomedical-knowledge-graphs">Awesome biomedical knowledge graphs</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/robert-haas">Robert Haas</a> is licensed under <a href="http://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a>
</p>
</body>
</html>
"""

    html_text = html_template.format(
        table_databases=html_tables[3],
        table_ontologies=html_tables[0],
        table_bkgs=html_tables[1],
        table_tools=html_tables[4],
        table_formats=html_tables[2],
    )
    return html_text


# Read the LaTeX report and the BibLaTeX bibliography
name = "bmkg"
source_filepath_tex = f"{name}.tex"
source_filepath_bib = f"{name}.bib"
target_filepath = os.path.join("..", "target", f"{name}.html")

bib_data = parse_biblatex_file(source_filepath_bib)
tex_data = parse_latex_file(source_filepath_tex, bib_data)


# Create the HTML file
html_text = tables_to_html(tex_data)
with open(target_filepath, "w") as f:
    f.write(html_text)
