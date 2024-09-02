#!/usr/bin/env python3

import re
import argparse

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

# Function to create Warp YAML theme file
def create_warp_theme(colors, output_file):
    with open(output_file, 'w') as file:
        # Write the color scheme in Warp YAML format
        file.write('name: Custom Theme\n')
        file.write(f'accent: #{colors["accent"]}\n')
        file.write(f'cursor: #{colors["cursor"]}\n')
        file.write(f'background: #{colors["background"]}\n')
        file.write(f'foreground: #{colors["foreground"]}\n')
        file.write('details: darker\n')
        file.write('terminal_colors:\n')
        file.write('  bright:\n')
        file.write(f'    black: #{colors["black"]}\n')
        file.write(f'    blue: #{colors["blue"]}\n')
        file.write(f'    cyan: #{colors["cyan"]}\n')
        file.write(f'    green: #{colors["green"]}\n')
        file.write(f'    magenta: #{colors["magenta"]}\n')
        file.write(f'    red: #{colors["red"]}\n')
        file.write(f'    white: #{colors["white"]}\n')
        file.write(f'    yellow: #{colors["yellow"]}\n')
        file.write('  normal:\n')
        file.write(f'    black: #{colors["black"]}\n')
        file.write(f'    blue: #{colors["blue"]}\n')
        file.write(f'    cyan: #{colors["cyan"]}\n')
        file.write(f'    green: #{colors["green"]}\n')
        file.write(f'    magenta: #{colors["magenta"]}\n')
        file.write(f'    red: #{colors["red"]}\n')
        file.write(f'    white: #{colors["white"]}\n')
        file.write(f'    yellow: #{colors["yellow"]}\n')

# Main function
def main():
    parser = argparse.ArgumentParser(description='Convert CSS to Warp YAML theme')
    parser.add_argument('css_file', help='Path to the CSS file')
    parser.add_argument('output_file', help='Path to the output YAML file')
    args = parser.parse_args()

    colors = extract_colors(args.css_file)
    create_warp_theme(colors, args.output_file)

if __name__ == '__main__':
    main()
