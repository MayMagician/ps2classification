# ps2classification

This project aims to build a MobileNetV2 classifier, pre-trained on ImageNet, that is able to identify PS2 games given an image of the game itself.

The dataset used for demonstration was manually collected and organized:

- 1000 screenshots each from 5 different classes/PS2 games (for a total of 5000 screenshots). The screenshots were obtained by 5 videos by using the custom script [imagesGenerator.py](imagesGenerator.py). More informations about the games are in [gamesInfo.md](gamesInfo.md).
- Of these screenshots, for each class, 700 were used for training, 150 for validation and 150 for test.
- The screenshots were divided as follows:

dataset/

train/ → ffx/, gow/, kh/, gt4/, sotc/

test/ → ffx/, gow/, kh/, gt4/, sotc/

val/ → ffx/, gow/, kh/, gt4/, sotc/

The project wants to highlight the potential of **transfer learning**: MobileNetV2 is a pre-trained model, which is proven to be efficient on extremely domain-specific applications, such as old generation videogames.

The dataset used was limited and for demonstration use only, so the model's potential at larger scale is unknown. However, the process is designed to be generalizable, making it straightforward to expand the dataset and add new classes.
