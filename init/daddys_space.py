def christmas_tree(height):
	# Draw the tree
	for i in range(height):
		spaces = " " * (height - i - 1)
		stars = "*" * (2 * i + 1)
		print(spaces + stars)
	
	# Draw the trunk
	trunk_spaces = " " * (height - 1)
	print(trunk_spaces + "|")

# Create a tree with height 7
christmas_tree(7)

