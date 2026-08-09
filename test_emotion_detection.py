'''Testing for emotion_detection.py'''

# import function
from EmotionDetection import emotion_detector

# Test for joy
print("Testing joy:")
print(emotion_detector("I am glad this happened"))
print()
# Test for anger
print("Testing anger:")
print(emotion_detector("I am really mad about this"))
print()
# Test for disgust
print("Testing disgust:")
print(emotion_detector("I feel disgusted just hearing about this"))
print()
#Test for sadness
print("Testing sadness:")
print(emotion_detector("I am so sad about this"))
print()
#Test for fear
print("Testing fear:")
print(emotion_detector("I am really afraid that this will happen"))
