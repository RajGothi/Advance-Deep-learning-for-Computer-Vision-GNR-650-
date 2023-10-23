## Self-Supervised Techniques:

1. [Jigsaw_pretext_CIFAR10.ipynb](Jigsaw_pretext_CIFAR10.ipynb)
   - Learn image feature representation through solving Jigsaw puzzle of jumbled patches of images.

   [Jigsaw_inference.ipynb](Jigsaw_inference.ipynb)
   - Jigsaw SSL Inference on Test dataset
   
3. [Patch_Prediction_CIFAR10.ipynb](Patch_Prediction_CIFAR10.ipynb)
   - Learn image feature representation via finding the relative patch location of patches of images.
     
## Model Performance

| Model                    | Validation Accuracy | Test Accuracy |
|--------------------------|----------------------|---------------|
| Jigsaw SSL |       95%          |    95%     |   
| Jigsaw SSL - Downstream Classification Task                 |    67%     |   67% 
| Relative patch location SSL                       |  98%       |    97%
| Relative patch location SSL - Downsteam Classification Task                          |   74%     | 74%

