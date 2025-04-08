#!/usr/bin/env python3

import nbformat as nbf

def create_notebook_from_py(py_file, ipynb_file):
    """Convert a Python file to Jupyter notebook with proper cell separation."""
    
    # Read the Python file
    with open(py_file, 'r') as f:
        content = f.read()
    
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Split content into cells based on function definitions and comments
    cells = []
    current_cell = []
    in_markdown = False
    markdown_lines = []
    
    for line in content.split('\n'):
        # Handle markdown-style comments
        if (line.startswith('"""') or line.startswith("'''")) and not in_markdown:
            if current_cell:
                cells.append(('\n'.join(current_cell), 'code'))
                current_cell = []
            in_markdown = True
            continue
        
        if in_markdown:
            if line.endswith('"""') or line.endswith("'''"):
                in_markdown = False
                cells.append(('\n'.join(markdown_lines), 'markdown'))
                markdown_lines = []
            else:
                markdown_lines.append(line)
            continue
        
        # Handle code cells
        if line.startswith('def ') or line.startswith('if __name__'):
            if current_cell:
                cells.append(('\n'.join(current_cell), 'code'))
                current_cell = []
        
        current_cell.append(line)
    
    # Add the last cell if it exists
    if current_cell:
        cells.append(('\n'.join(current_cell), 'code'))
    
    # Create notebook cells
    for content, cell_type in cells:
        if content.strip():  # Only create cells for non-empty content
            if cell_type == 'code':
                nb.cells.append(nbf.v4.new_code_cell(content))
            else:
                nb.cells.append(nbf.v4.new_markdown_cell(content))
    
    # Write the notebook
    with open(ipynb_file, 'w') as f:
        nbf.write(nb, f)

if __name__ == "__main__":
    create_notebook_from_py('insightplate_analysis.py', 'Final-InsightPlate.ipynb')
