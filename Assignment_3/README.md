## Self-Supervised Techniques:

1. [Jigsaw_pretext_CIFAR10.ipynb](Jigsaw_pretext_CIFAR10.ipynb)
   - Learn image feature representation through solving Jigsaw puzzle of jumbled patches of images.
   - Defined Custom CNN model to handle 32 * 32 images.
   - Jigsaw creation
      - Resize the given CIFAR-10 32*32 Image to 128 * 128 image shape.
      - Do center crop with 105 * 105 image shape.
      - Divide the image into 3 * 3 image patch, where Each patch size is 32 * 32.
      - Pass all 9, 32 * 32 image to model and predict the permutation index.
   - Permutation Creation:
      - Choose the 1000 permutation of value 9 such that hamming distance between choose permutation is greater than 0.9
   - Downstream task : Image Classification.
   - GradCam Analysis

   [Jigsaw_inference.ipynb](Jigsaw_inference.ipynb)
   - Jigsaw SSL and Downstream Task Inference on Test dataset
   
3. [Patch_Prediction_CIFAR10.ipynb](Patch_Prediction_CIFAR10.ipynb)
   - Learn image feature representation via finding the relative patch location of patches of images.
   - Used resnet-18 model architecture.
   - Resized the given Image to 96 * 96 shape and divide into 3*3 patches.
   - Pass the center patch and neighbour patch to the model and it will predict the relative patch position with respect to center position.
   - Downstream task : Image Classification.
   - Inference on Test dataset.
   - GradCam Analysis

     
## Model Performance

| Model                    | Validation Accuracy | Test Accuracy |
|--------------------------|----------------------|---------------|
| Jigsaw SSL |       95%          |    95%     |   
| Jigsaw SSL - Downstream Classification Task                 |    67%     |   67% 
| Relative patch location SSL                       |  98%       |    97%
| Relative patch location SSL - Downsteam Classification Task                          |   74%     | 74%

