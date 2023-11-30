from sketchpy import canvas

obj = canvas.color_sketch_from_svg("toothless.svg",scale=1130)

obj.draw(x_offset= 110,y_offset=300)