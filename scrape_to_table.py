import requests
from bs4 import BeautifulSoup

# Fetch the URL
url = "https://qwik.builder.io/docs/guides/react-cheat-sheet/"
response = requests.get(url)
html_content = response.text

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all section names represented by <h2> tags
section_names = []
sections = soup.find_all('h2')
for tag in sections:
    qwik_h3 = tag.find_next_sibling('h3')
    qwik = qwik_h3.find_next_sibling('div').find('pre').find('code')
    react_h3 = qwik_h3.find_next_sibling('h3')
    react_div = react_h3.find_next_sibling('div')
    react = react_div.find('pre').find('code')

    section_names.append({
        "name": tag.text.strip(),
        "qwik": qwik,
        "react": react
    })

# NOTE This is futile with the standard Markdown dialects. Let's generate an HTML table instead.
html_table = """
<table>
    <thead>
        <th>Aspect</th>
        <th>Qwik</th>
        <th>React</th>
    </thead>
<tbody>"""
for row in section_names:
    html_table += f"""<tr>
        <td>{row['name']}</td>
        <td><pre>{row['qwik']}</pre></td>
        <td><pre>{row['react']}</pre></td>
    </tr>"""

html_table += """</tbody>
</table>
"""

# Define your own action. This is just a placeholder.
if __name__ == '__main__':
    # Print the markdown table
    print(html_table)
