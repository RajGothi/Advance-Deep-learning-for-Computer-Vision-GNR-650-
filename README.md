# GNR-650

## Assignment 1 (Overfit Resnet 18 model):  1_Resnet18_overfit.ipynb

- Took 100 images per samples of cifar-10 dataset.

- Resnet 18 architecture

- Overfit the model

-> Training accuracy: 99%~100%

-> Testing accuray: 46%

- Showed the magnitude of Kernels weights at different layers

- Visualized the Kernels at different layers.

- Additional : Visualize the Feature map of horse image at different layers


## Assignment 2 (EuroSAT Fine-Tuning and Visualization)
: Go to Assignment 2 Folder

This repository contains code and notebooks for different fine-tuning methods of the Vision Transformer (ViT) model on the EuroSAT dataset, along with visualization of attention maps.

## Fine-Tuning Notebooks

1. [2_ViT_B12_Last_Layer_FT.ipynb](2_ViT_B12_Last_Layer_FT.ipynb)
   - Fine-tunes the last fully connected layer of the ViT model.

2. [2_ViT_B12_Bottom_Layer_FT.ipynb](2_ViT_B12_Bottom_Layer_FT.ipynb)
   - Fine-tunes only the 8th to 11th transformer layers and the fully connected layer.

3. [2_ViT_B12_Full_Fine_tune.ipynb](2_ViT_B12_Full_Fine_tune.ipynb)
   - Fine-tunes all layers of the ViT model.

4. [2_ViT_B12_No_Fine_Tune.ipynb](2_ViT_B12_No_Fine_Tune.ipynb)
   - Does not perform fine-tuning on the ViT model.

## Visualization

5. [Visualization.ipynb](Visualization.ipynb)
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

