import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_dominant_joy(self):
        result = emotion_detector("I am glad this happened")

        return self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_dominant_anger(self):
        result = emotion_detector("I am really mad about this")

        return self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_dominant_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")

        return self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_dominant_sadness(self):
        result = emotion_detector("I am so sad about this")

        return self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_dominant_fear(self):
        result = emotion_detector("I am really afraid that this will happen")

        return self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()