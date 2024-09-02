#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# Function to extract colors from CSS
def extract_colors(css_file):
    colors = {}
    with open(css_file, 'r') as file:
        content = file.read()
        # Use regular expressions to find color definitions
        matches = re.findall(r'([a-zA-Z-]+):\s*#([0-9a-fA-F]{6})', content)
        for match in matches:
            colors[match[0]] = match[1]
    return colors

# Function to create iTerm2 color scheme file
def create_iterm_scheme(colors, output_file):
    with open(output_file, 'w') as file:
        # Write the color scheme in iTerm2 format
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n')
        file.write('<plist version="1.0">\n')
        file.write('<dict>\n')
        for key, value in colors.items():
            file.write(f'<key>{key}</key>\n<string>#{value}</string>\n')
        file.write('</dict>\n')
        file.write('</plist>\n')

# Example usage
css_file = 'theme.css'
output_file = 'theme.itermcolors'
colors = extract_colors(css_file)
create_iterm_scheme(colors, output_file)
