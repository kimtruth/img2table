from PIL import Image
from os.path import splitext

def rgb2hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def img2table(img):
	im  = img.load()
	width  = img.size[0]
	height = img.size[1]

	html = '<table border=0 cellpadding=0 cellspacing=0 bgcolor=ffffff>'
	for y in range(0, height):
		html += '<tr height=1>'
		for x in range(0, width):
			html += '<td bgcolor={0} width=1></td>'.format(rgb2hex(im[x, y]))
		html += '</tr>'
	html += '</table>'

	return html

def main():
	img_name = raw_input("Input Your Image Name : ")
	output_name = splitext(img_name)[0] + '.html'

	check_resize = raw_input("Do You Want to Resize? (Y/N) : ").lower()
	img = Image.open(img_name)
	
	if check_resize == 'y':
		ratio = input("Resize Percent (??%) Only Int : ") / 100.0
		img = img.resize( [int(ratio * s) for s in img.size] )

	output = img2table(img)

	f = open(output_name, 'w')
	f.write(output)
	f.close()

if __name__ == '__main__':
	main()