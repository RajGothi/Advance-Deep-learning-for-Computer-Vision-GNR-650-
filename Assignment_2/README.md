# EuroSAT Fine-Tuning and Visualization

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

