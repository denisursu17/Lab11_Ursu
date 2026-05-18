def make_html_tag(tag, content, **attrs):
    attributes = " ".join(
        f'{k.replace("_", "")}="{v}"' for k, v in attrs.items()
    )
    if attributes:
        return f"<{tag} {attributes}>{content}</{tag}>"
    return f"<{tag}>{content}</{tag}>"
print(make_html_tag('p', 'Hello World'))