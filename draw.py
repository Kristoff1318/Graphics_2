from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    x = x0 #-B
    y = y0 #A
    dx = x1 - x0
    dy = y1 - y0
   
    p = 2*dy - dx #decision parameter 
    #Octant 1
    if (dy <= dx and dy > 0):
        while(x <= x1):
            plot(screen, color, x, y)
            x += 1
            p += 2*dy
            if (p > 0):
                p -= 2*dx
                y += 1

    #Octant 5
    if (dy >= dx and dy < 0):
        while(x >= x1):
            plot(screen, color, x, y)
            x -= 1
            p -= 2*dy
            if (p > 0):
                p += 2*dx
                y -= 1


    p = 2*dy + dx #decision parameter 
    #Octant 8
    if (-dy <= dx and dy < 0):
        while(x <= x1):
            plot(screen, color, x, y)
            x += 1
            p -= 2*dy
            if (p > 0):
                p -= 2*dx
                y -= 1
    
    #Octant 4
    if (dy <= -dx and dy > 0):
        while(x >= x1):
            plot(screen, color, x, y)
            x -= 1
            p += 2*dy
            if (p > 0):
                p += 2*dx
                y += 1
    

    p = -2*dx + dy
    #Octant 2
    if (dy >= dx and dx > 0):
        while(y <= y1):
            plot(screen, color, x, y)
            y += 1
            p += 2*dx
            if (p > 0):
                p -= 2*dy
                x += 1
    
    #Octant 6
    if (-dy >= -dx and dx < 0):
        while(y >= y1):
            plot(screen, color, x, y)
            y -= 1
            p -= 2*dx
            if (p > 0):
                p += 2*dy
                x -= 1
    

    p = dy + 2*dx
    #Octant 7
    if (-dy >= dx and dx > 0):
        while(y >= y1):
            plot(screen, color, x, y)
            y -= 1
            p += 2*dx
            if (p > 0):
                p += 2*dy
                x += 1
    
    #Octant 3
    if (dy >= -dx and dx < 0):
        while(y <= y1):
            plot(screen, color, x, y)
            y += 1
            p -= 2*dx
            if (p > 0):
                p -= 2*dy
                x -= 1
        
    #Horizontal
    if (dy == 0):
        if(dx < 0):
            while(x >= x1):
                plot(screen, color, x, y)
                x -= 1
        else:
            while(x <= x1):
                plot(screen, color, x, y)
                x+= 1
    
    #Vertical
    if (dx == 0):
        if (dy < 0):
           while (y >= y1):
               plot(screen, color, x, y)
               y -= 1
        else:
            while (y <= y1):
                plot(screen, color, x, y)
                y += 1
    









#     from display import *

# def draw_line( x0, y0, x1, y1, screen, color ):
#     x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
#     x = x0
#     y = y0 
#     dx = x1 - x0
#     dy = y1 - y0
#     p = 2*dy - dx #decision parameter 

#     #Octant 1
#     if (dy <= dx and dy > 0):
#         while(x <= x1):
#             plot(screen, color, x, y)
#             x += 1
#             p += 2*dy
#             if (p > 0):
#                 p -= 2*dx
#                 y += 1

#     #Octant 5
#     elif (dy >= dx and dy < 0):
#         while(x >= x1):
#             plot(screen, color, x, y)
#             x -= 1
#             p -= 2*dy
#             if (p > 0):
#                 p += 2*dx
#                 y -= 1

#     #Octant 8
#     elif (-dy <= dx and dy < 0):
#         while(x <= x1):
#             plot(screen, color, x, y)
#             x += 1
#             p -= 2*dy
#             if (p > 0):
#                 p -= 2*dx
#                 y -= 1
    
#     #Octant 4
#     elif (dy <= -dx and dy > 0):
#         while(x >= x1):
#             plot(screen, color, x, y)
#             x -= 1
#             p += 2*dy
#             if (p > 0):
#                 p += 2*dx
#                 y += 1
    
#     #Octant 2
#     elif (dy >= dx and dx > 0):
#         while(y <= y1):
#             plot(screen, color, x, y)
#             y += 1
#             p += 2*dx
#             if (p > 0):
#                 p -= 2*dy
#                 x += 1
    
#     #Octant 6
#     elif (-dy >= -dx and dx < 0):
#         while(y >= y1):
#             plot(screen, color, x, y)
#             y -= 1
#             p -= 2*dx
#             if (p > 0):
#                 p += 2*dy
#                 x -= 1
    
#     #Octant 7
#     elif (-dy >= dx and dx > 0):
#         while(y >= y1):
#             plot(screen, color, x, y)
#             y -= 1
#             p += 2*dx
#             if (p > 0):
#                 p += 2*dy
#                 x += 1
    
#     #Octant 3
#     elif (dy >= -dx and dx < 0):
#         while(y <= y1):
#             plot(screen, color, x, y)
#             y += 1
#             p -= 2*dx
#             if (p > 0):
#                 p -= 2*dy
#                 x -= 1
        
#     #Horizontal
#     elif (dy == 0):
#         d = 1 if dx > 0 else -1
#         while (x <= x1 * d):
#             plot(screen, color, x, y)
#             x += d 
    
#     #Vertical
#     elif (dx == 0):
#         d = 1 if dy > 0 else -1
#         while (y <= y1 * d):
#             plot(screen, color, x, y)
#             y += d 
    