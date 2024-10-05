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

# def getDynamicRGBValues():
#     rgbValues = []
#     count = int(input("Berapa banyak RGB yang ingin dikonversi? "))
    
#     for i in range(count):
#         rgb = input(f"Masukkan nilai RGB ke-{i+1} (format: R,G,B): ")
#         r, g, b = map(int, rgb.split(','))
#         rgbValues.append((r, g, b))
    
#     return rgbValues

# Static Input RGB
rgbStaticValues = [
    (255, 255, 0),  
    (255, 102, 0),  
    (0, 255, 0),    
    (0, 255, 255),  
    (204, 102, 204),
    (255, 255, 255),
    (0, 0, 0),      
    (102, 255, 204),
    (153, 102, 51)  
]

# Dynamic Input RGB
# rgbDynamicValues = getDynamicRGBValues()

rgbValues = rgbStaticValues

# RGB to Grayscale Conversion
grayscaleValues = rgbToGrayscale(rgbValues)
print("Grayscale Values:", grayscaleValues)

# Grayscale to Biner Conversion => Threshold 150
binaryValues150 = grayscaleToBinary(grayscaleValues, 150)
print("Binary Values (Threshold 150):", binaryValues150)

# Grayscale to Biner Conversion => Threshold 180
binaryValues180 = grayscaleToBinary(grayscaleValues, 180)
print("Binary Values (Threshold 180):", binaryValues180)
