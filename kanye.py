from PIL import Image
im = Image.open("Kanye.jpg")
pix = im.load()

DARKBLUE = (0,51,76)
RED = (217,26,33)
LIGHTBLUE = (112,150,158)
YELLOW = (252,227,166)


catch = im.getdata()
catch=list(im.getdata())
'''
for i in catch:
intensity=(i[0] + i[1] +i[2])
print (intensity)
'''
new_list = []

for i in catch:
	red = i[0]
	green = i[1]
	blue = i[2]
	intensity = (red+green+blue)

	if intensity <182:
		new_list.append (DARKBLUE)
	elif intensity >= 182 and intensity < 364:
		new_list.append (RED)
	elif intensity >= 364 and intensity < 546:
		new_list.append(LIGHTBLUE)
	elif intensity >= 546:
		new_list.append (YELLOW)
test= im.putdata(new_list)
im.show(test)
