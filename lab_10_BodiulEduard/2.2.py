def make_html_tag(tag_name,content,**attributes):
    attrs = ""
    for key, value in attributes.items():
        if key == "class_":
            key = "class"
        attrs += f' {key}="{value}"'
    return f"<{tag_name}{attrs}>{content}</{tag_name}>"
print(make_html_tag('p', 'Hello World'))