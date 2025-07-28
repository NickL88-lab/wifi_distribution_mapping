import cv2
import random

def detect_domain(img,length_x, length_y):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh_image = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0

    for i, contour in enumerate(contours):
        if i == 0:
            continue
        epsilon = 0.001*cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        x, y, w, h = cv2.boundingRect(approx)

        area = w * h

        if len(approx) == 4:

            if area > max_area:

                maximum = []
                max_area = area
                maximum = [contour, x, y, w, h]

    x = maximum[1]
    y = maximum[2]
    w = maximum[3]
    h = maximum[4]

    x_mid = int(x + w / 2)
    y_mid = int(y + h / 2)

    # Length to Pixel Ratio along X and Y
    #LPR_x = length_x/(x+w)
    #LPR_y = length_y/(y+h)
    LPR_x = length_x / (w)
    LPR_y = length_y / (h)
    LPRs = []
    LPRs.append(LPR_x)
    LPRs.append(LPR_y)

    # Top Left Vertex Coordinates
    coord = []
    coord.append(x)
    coord.append(y)

    # Legths along X and Y
    lengths = []
    lengths.append(w)
    lengths.append(h)

    cv2.rectangle(img, [x,y], [x + w, y + h], (255,0,0), 2)
    coordinates = (x_mid, y_mid)
    colour = (0, 0, 0)
    font = cv2.FONT_HERSHEY_DUPLEX

    # cv2.putText(img, "Domain Detected", (x, y_mid-30), font, 1, colour, 1)
    # cv2.putText(img, "Top Left Corner Coordinates:"+str(x)+", "+str(y), (x, y_mid), font, 1, colour, 1)
    # cv2.putText(img, "Length Along X: "+str(x+w), (x, y_mid + 30), font, 1, colour, 1)
    # cv2.putText(img, "Length Along Y: "+str(y+h), (x, y_mid + 60), font, 1, colour, 1)
    # cv2.putText(img, "Length to Pixel Ratio along X: "+str(length_x/(x+w))+" mm/pixel", (x, y_mid + 90), font, 1, colour, 1)
    # cv2.putText(img, "Length to Pixel Ratio along Y: "+str(length_y/(y+h))+" mm/pixel", (x, y_mid + 120), font, 1, colour, 1)
    #
    # cv2.imshow("Calibration", img)
    # cropped_image = img[y:y+h,x:x+w]
    # cv2.imshow("Cropped Image", cropped_image)
    # cv2.imwrite("Periodicity_Detection/CroppedImage.png", cropped_image)
    print(coordinates)

    return coord, lengths, LPRs


def point_in_rectangle (point, min, max):
    # Check if the point is inside the rectangle
    if min[0] <= point[0] <= max[0] and min[1] <= point[1] <= max[1]:
        return True
    else:
        return False

def is_green(pixel):
    green_threshold = 100
    if pixel[1] > green_threshold and pixel[1] > pixel[0] and pixel[1] > pixel[2]:
        return True
    else:
        return False


def are_nearby(pixel_coords, pixel_list, max_distance = 10):

    # Iteriamo su ogni coppia di coordinate nella lista di pixel
    for coord in pixel_list:
        # Calcoliamo la distanza Euclidea tra il pixel dato e il pixel nella lista
        distance = ((pixel_coords[0] - coord[0]) ** 2 + (pixel_coords[1] - coord[1]) ** 2) ** 0.5
        # Se la distanza è minore o uguale alla distanza massima considerata "vicina", restituisci True
        if distance <= max_distance:
            return True

    # Se nessun pixel è "vicino", restituisci False
    return False


def get_black_pixels(image):
    # Load image in gray scale
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get image dimension
    height, width = img.shape

    pixel_neri = []

    # Scan all pixels
    for y in range(height):
        for x in range(width):
            pixel_value = img[y, x]

            if pixel_value == 0:
                pixel_neri.append((x, y))

    return pixel_neri


def random_numbers_generator(min, max, samples):
    random_numbers = []
    for _ in range(samples):
        random_number = random.randint(min, max)
        random_numbers.append(random_number)
    return random_numbers