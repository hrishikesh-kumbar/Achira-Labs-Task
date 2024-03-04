gen_images.py : In this code, I created a program that generates images of randomly altered shapes. It takes a folder of images (.tif format) and user-specified parameters like output folder and number of images to generate. The program reads the input images, scales and rotates them randomly, then attempts to place them non-overlapping within a new image. If a suitable placement isn't found after several attempts, the image is skipped for that particular position. Finally, the program saves the generated collages with unique filenames in the specified output folder. I ahve mostly used PIL (Pillow) package for this code. (THE CODE CAN GENERATE MORE THAN 1000 IMAGES, I HAVE ONLY ATTACHED 50 IMAGES IN THE REPO BUT IT CAN GENERATE ANY NUMBER OF IMAGES WHICH IS SPECIFIED)   


Image generation and Image detection : I have tried using the generated images from the previous code to train the  deep learning model for shape identification. In this attempt i have used YOLO (You only look once) model. 


CNN : In this attempt I have used CNN model for image detection. I have tried various approaches but failed to detect any shapes. In this code i have tried to train the model to detect the individual shape first and then try predicting. 


NOTE : The first code works perfectly well. The deep learning methods which I have tried have failed to detect due to the following issue :: Annotation problem - It is very time consuming to annote/ label each generated image and task was to complete in 3 days. Also the YOLO and CNN are pre - trained deep learning models which are trained on objects/shapes which can be seen everyday and the shapes which the problem statement have are a little unique and the models are not previously not trained on it.    
