egg_boxes = 4
per_omelette = 4
eggs_per_box = 6

omelettes = (eggs_per_box * egg_boxes) // per_omelette

output = "You can make {} omlettes with {} boxes of eggs".format(omelettes, egg_boxes)
print(output)

