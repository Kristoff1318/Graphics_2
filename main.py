from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

def stup(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def recursion_draw(p1, p2, p3, c):
    if (p1 != p2):
        draw_line(p1[0], p1[1], p2[0], p2[1], s, c)
        draw_line(p2[0], p2[1], p3[0], p3[1], s, c)
        draw_line(p1[0], p1[1], p3[0], p3[1], s, c)

        p1n = tuple( x//2 for x in stup(p1, p2) )
        p2n = tuple( x//2 for x in stup(p2, p3) )
        p3n = tuple( x//2 for x in stup(p1, p3) )

        c[0] += p1n[1]
        c[1] += p2n[0]
        c[2] += p3n[0]
        
        c[0] %= 256
        c[1] %= 256
        c[2] %= 256
        recursion_draw(p1n, p2n, p3n, c)


# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, YRES / 2, s, c) 
# draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);  
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, YRES/2, s, c);

# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);

# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);

# #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
# draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);

p1 = (0, 0)
p2 = (XRES//2, YRES-1)
p3 = (XRES-1, 0)




recursion_draw(p1, p2, p3, [72, 20, 194])

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
