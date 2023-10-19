import os
import random

path = '../CIFAR-10-images/train'
count = 1
class_to_id = {}
id_counter = 1
with open('../Data/image_class_label_cifar10.txt','w') as f1, open('../Data/images_cifar.txt','w') as f2, open('../Data/train_test_split_cifar.txt','w') as f3:
     for class_folder in os.listdir(path):
        class_folder_path = os.path.join(path, class_folder)
        
        # Check if it's a directory (to exclude any files)
        if os.path.isdir(class_folder_path):
            label = class_folder  # Use the folder name as the label
            
            if label not in class_to_id:
                class_to_id[label] = id_counter
                id_counter += 1
            
            # Walk through the class folder to collect image file paths
            for root, _, files in os.walk(class_folder_path):
                for file in files:
                    image_path = os.path.join(root, file)
                    
                    split = random.randint(0, 10)
                    if split<8:
                        flag=1
                    else:
                        flag=0

                    # Write the image location and label to the respective text files
                    f2.write(f"{count}"+ "\t" + image_path + '\n')
                    f1.write(f"{count}" + "\t" + f"{class_to_id[label]}" + '\n') 
                    f3.write(f"{count}" + "\t" + f"{flag}" + '\n') 
                    count+=1 