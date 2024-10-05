def rgbToGrayscale(rgbValues):
    grayscaleValues = []
    for r, g, b in rgbValues:
        # Grayscale = 0.299*R + 0.587*G + 0.114*B
        gray = round(0.299 * r + 0.587 * g + 0.114 * b)
        grayscaleValues.append(gray)
    return grayscaleValues

# Grayscale to Biner Conversion
def grayscaleToBinary(grayscaleValues, threshold):
    binaryValues = []
    for gray in grayscaleValues:
        # If > threshold, set to 1, else 0
        binaryValues.append(1 if gray > threshold else 0)
    return binaryValues

# Input RGB array
rgbValues = [
    (255, 255, 0),  # Yellow
    (255, 102, 0),  # Orange
    (0, 255, 0),    # Green
    (0, 255, 255),  # Cyan
    (204, 102, 204),# Violet
    (255, 255, 255),# White
    (0, 0, 0),      # Black
    (102, 255, 204),# Turquoise
    (153, 102, 51)  # Brown
]

# RGB to Grayscale Conversion
grayscaleValues = rgbToGrayscale(rgbValues)
print("Grayscale Values:", grayscaleValues)

# Grayscale to Biner Conversion => Threshold 150
binaryValues150 = grayscaleToBinary(grayscaleValues, 150)
print("Binary Values (Threshold 150):", binaryValues150)

# Grayscale to Biner Conversion => Threshold 180
binaryValues180 = grayscaleToBinary(grayscaleValues, 180)
print("Binary Values (Threshold 180):", binaryValues180)
