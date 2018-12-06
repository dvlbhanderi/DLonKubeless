from keras.models import load_model
from keras.preprocessing import image
import numpy as np

def predImg(event, context):
    from keras.models import load_model
    from keras.preprocessing import image
    import numpy as np
    #from keras.utils.data_utils import get_file

    #weights_path = get_file('cnn_yelp_model1.hdf5', 'https://github.com/dvlbhanderi/DLonKubeless/blob/master/cnn_yelp_model1.hdf5')
    #url = "https://github.com/dvlbhanderi/DLonKubeless/blob/master/cnn_yelp_model1.hdf5"    
    
    test_image = image.load_img('C:/Users/Dhaval Bhanderi/Desktop/bundles/kubeless_windows-amd64/pred4.jpg', target_size = (64, 64))
    classifier = load_model('C:/Users/Dhaval Bhanderi/Desktop/bundles/kubeless_windows-amd64/cnn_yelp_model1.hdf5')
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)

    result = classifier.predict(test_image)
    print(result)

    if result[0][0] == 1:
        prediction = 'drink'
        print("This is s Drink")
        return "Drink"
    elif result[0][1] == 1:
        prediction = 'food'
        print("This is a Food")
        return "Food"
    elif result[0][2] == 1:
        prediction = 'inside'
        print("This is a Inside view")
        return "Inside"
    elif result[0][3] == 1:
        prediction = 'menu'
        print("This is a Menu")
        return "Menu"
    elif result[0][4] == 1:
        prediction = 'outside'
        print("This is a Outside view")
        return "Outside"
    else:
        print('Oouuu....am sorry!!')
        return "Sorry"
