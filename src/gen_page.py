import os
from htmlnode import HTMLNode
from markdown_blocks import markdown_to_html_node

template = "./template.html"
markdown_file = "./content/index.md"

def extract_title(markdown):
    file = open(markdown, "r")
    heading = file.readline()
    print (heading)
    file.close()

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")

extract_title(markdown_file)
