import cv2

def convert_to_grayscale(image_path):
    image = cv2.imread(image_path)
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite('grayscale_image.png', gray_image)
    return gray_image

def convert_to_binary(image, threshold_value, output_name):
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    
    # Menyimpan hasil biner
    cv2.imwrite(output_name, binary_image)

if __name__ == "__main__":
    image_path = './naruto.jpg' 
    gray_image = convert_to_grayscale(image_path)
    
    convert_to_binary(gray_image, 150, 'binary_image_150.png')
    convert_to_binary(gray_image, 180, 'binary_image_180.png')
