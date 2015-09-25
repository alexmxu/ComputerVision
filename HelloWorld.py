import cv2


cv2.destroyAllWindows()

images = ["Blowhole013.jpg",  "Pioneer0067.jpg", "Blowhole021.jpg", "Pioneer0093.jpg", "garden.jpg", "Coins1.jpg", "Puzzle1.jpg", "ghostrider.jpg", "Coins2.jpg", "Puzzle2.jpg", "gorge.jpg", "DollarCoin.jpg", "SnowLeo1.jpg", "redDoor.jpg", "SnowLeo2.jpg", "sampleRed.jpg", "Pioneer0005.jpg", "SnowLeo3.jpg", "shops.jpg", "Pioneer0012.jpg", "SnowLeo4.jpg", "swans.jpg", "Pioneer0029.jpg", "frame0017.jpg", "waterfall.jpg", "Pioneer0063.jpg", "frame0019.jpg"]

for image in images:
    image = cv2.imread("TestImages/" + image)
    cv2.imshow("Slideshow", image)
    cv2.waitKey(0)