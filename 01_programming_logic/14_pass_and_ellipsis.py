"""
Pass and Ellipsis as placeholders (when we want to leave empty code blocks)
"""
value = True

if value:
    pass  # Pass
elif not value:
    ...  # Ellipsis
else:
    print("Bye")
