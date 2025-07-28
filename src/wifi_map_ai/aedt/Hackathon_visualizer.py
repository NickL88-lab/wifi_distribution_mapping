import cv2
from Rectangle_Detection import is_green, are_nearby, get_black_pixels




def show_coordinates(event, x, y, flags, param):
    selected_point = param[0]
    walls_pixels = param[1]

    if event == cv2.EVENT_LBUTTONDOWN:
        if is_green(img[x,y]) and not are_nearby((x, y), walls_pixels, max_distance=25):
            print(f"Pixel Coordinates: ({x}, {y})")
            selected_point.append((x,y))

        else:
            print(f"This position is part of the wall, please select another point!")

img = cv2.imread("Hackathon3_images\\house_installation_cut.png")
walls_pixels = get_black_pixels(img)
selected_point = []
cv2.namedWindow("Floorplan")
# Associate a function to mouse events manager
cv2.setMouseCallback("Floorplan", show_coordinates, [selected_point, walls_pixels])
cv2.imshow("Floorplan", img)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()