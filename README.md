# Encoder-Decoder LSTM Machine Translation Model

## Overview

This repository contains the implementation of a machine translation model using Encoder-Decoder architecture with Long Short-Term Memory (LSTM) cells. The model is designed to translate text from one language to another, making use of the sequential and contextual information provided by LSTMs.

## Requirements

Make sure to install the required dependencies before running the code. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Dataset

The model is trained on a parallel corpus of source and target language sentences. The dataset used for training can be customized, and it's important to preprocess the data appropriately before training the model.

## Model Architecture

The architecture consists of an Encoder and a Decoder, both utilizing LSTM cells. The Encoder processes the input sequence and produces a fixed-size context vector. The Decoder then generates the output sequence based on this context vector.

## Training

To train the model, run the following command:

```bash
python train.py --data_path path/to/dataset --epochs 10 --batch_size 64
```

You can customize the training parameters according to your dataset and computing resources.

## Inference

Once the model is trained, you can use it for translation. Run the following command:

```bash
python translate.py --model_path path/to/model --input_text "Hello, how are you?"
```

Replace the `input_text` with the sentence you want to translate.

## Evaluation

Evaluate the performance of the model using appropriate metrics. You can use the following command:

```bash
python evaluate.py --model_path path/to/model --data_path path/to/test_dataset
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Sahith Edula

Feel free to reach out for any questions or contributions.

Happy translating! 🌍📚
