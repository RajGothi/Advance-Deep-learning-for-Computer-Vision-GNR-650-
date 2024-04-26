# GNR-650

# Assignment 1 (Overfit Resnet 18 model):  

[1_Resnet18_overfit.ipynb](1_Resnet18_overfit.ipynb):

- Took 100 images per samples of cifar-10 dataset.

- Resnet 18 architecture

- Overfit the model

-> Training accuracy: 99%~100%

-> Testing accuray: 46%

- Showed the magnitude of Kernels weights at different layers

- Visualized the Kernels at different layers.

- Additional : Visualize the Feature map of horse image at different layers


# Assignment 2 (Vision Transformer Fine-Tuning and Feature map Visualization)
: Go to Assignment 2 Folder

This repository contains code and notebooks for different fine-tuning methods of the Vision Transformer (ViT) model on the EuroSAT dataset, along with visualization of attention maps.

## Fine-Tuning Notebooks

1. [2_ViT_B12_Last_Layer_FT.ipynb](Assignment_2/2_ViT_B12_Last_Layer_FT.ipynb)
   - Fine-tunes the last fully connected layer of the ViT model.

2. [2_ViT_B12_Bottom_Layer_FT.ipynb](Assignment_2/2_ViT_B12_Bottom_Layer_FT.ipynb)
   - Fine-tunes only the 8th to 11th transformer layers and the fully connected layer.

3. [2_ViT_B12_Full_Fine_tune.ipynb](Assignment_2/2_ViT_B12_Full_Fine_tune.ipynb)
   - Fine-tunes all layers of the ViT model.

4. [2_ViT_B12_No_Fine_Tune.ipynb](Assignment_2/2_ViT_B12_No_Fine_Tune.ipynb)
   - Does not perform fine-tuning on the ViT model.

## Visualization

5. [Visualization.ipynb](Assignment_2/Visualization.ipynb)
   - Visualizes attention maps for different labels and models.

## Model Performance

### Epoch: 10

| Model                    | Train Accuracy | Validation Accuracy | Test Accuracy |
|--------------------------|----------------|----------------------|---------------|
| Only Last Layer Fine-Tune ViT | 98.70%         | 96.48%               | 95.96%        |
| Bottom Layer Fine-Tune ViT    | 99.53%         | 97.04%               | 97.11%        |
| All Layer Fine-Tune ViT       | 91.48%         | 91.85%               | 90.74%        |
| Do Not Fine-Tune ViT         | 13.55%         | 15.22%               | 13.92%        |

## Observations

### Last Layer Fine-Tuning:
- Achieved a high validation accuracy of 95.96% quickly.
- Efficient and competitive performance.

### Bottom Layer Fine-Tuning:
- Outperformed last layer fine-tuning with a validation accuracy of 97.33%.
- Captured complex features effectively.

### All Layer Fine-Tuning:
- Initially lower performance but gradually improved.
- Requires more training time.

### Visualization Comparision:

- Last layer fine-tuning and no fine-tuning exhibit similar attention maps across all transformer layers in the model. This is because we freeze all the transformer layers while fine-tuning.
- Across all models, the initial layers of the transformer consistently show better attention map visualizations. This suggests that these layers focus on capturing low-level and fundamental features in the images, which are essential for understanding the dataset.
- The attention map visualizations in the all layer fine-tuning case are not as informative compared to the others, as this strategy requires more training epochs.

# Assignment 3 (Jigsaw and Patch prediction self-supervised(SSL) task)
Go to Assigment 3 folder

## Self-Supervised Techniques:

1. [Jigsaw_pretext_CIFAR10.ipynb](Assignment_3/Jigsaw_pretext_CIFAR10.ipynb)
   - Learn image feature representation through solving Jigsaw puzzle of jumbled patches of images.
   - Defined Custom CNN model to handle 32 * 32 images.
   - Jigsaw creation
      - Resize the given CIFAR-10 32 * 32 Image to 128 * 128 image shape.
      - Do center crop with 105 * 105 image shape.
      - Divide the image into 3 * 3 image patch, where Each patch size is 32 * 32.
      - Pass all 9, 32 * 32 image to model and predict the permutation index.
   - Permutation Creation:
      - Choose the 1000 permutation of value 9 such that hamming distance between choose permutation is greater than 0.9
   - Downstream task : Image Classification.
   - GradCam Analysis

   [Jigsaw_inference.ipynb](Assignment_3/Jigsaw_inference.ipynb)
   - Jigsaw SSL and Downstream Task Inference on Test dataset
   
3. [Patch_Prediction_CIFAR10.ipynb](Assignment_3/Patch_Prediction_CIFAR10.ipynb)
   - Learn image feature representation via finding the relative patch location of patches of images.
   - Used resnet-18 model architecture.
   - Resized the given Image to 96 * 96 shape and divide into 3 * 3 patches.
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





# Paper Review 1:

[Paper: ViViT: A Video Vision Transformer Paper Review](GNR_650__Paper_Review_1.pdf)

[Paper Link](https://arxiv.org/abs/2103.15691)


# Paper Review 2:
[Paper:Universal Domain Adaptation through Self-Supervision](GNR_650__Paper_Review_2.pdf)

[Paper Link](https://proceedings.neurips.cc/paper/2020/file/bb7946e7d85c81a9e69fee1cea4a087c-Paper.pdf)

# Project Title:
- Visual Entities Empowered Zero-Shot Image-to-Text Generation Transfer Across Domains
