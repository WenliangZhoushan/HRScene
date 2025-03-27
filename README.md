# HRScene

TODO: put a logo here

## Outlines
- [⭐ About HRScene](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-about-mathvista)
- [🏆 Leaderboard 🏆](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-leaderboard-)
  - [Contributing the Leaderboard](https://github.com/WenliangZhao/HRScene/blob/main/README.md#contributing-the-leaderboard)
  - [Leaderboard on the testmini subset](https://github.com/WenliangZhao/HRScene/blob/main/README.md#leaderboard-on-the-testmini-subset)
  - [Leaderboard on the test subset](https://github.com/WenliangZhao/HRScene/blob/main/README.md#leaderboard-on-the-test-subset)
- [📊 Dataset Examples](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-dataset-examples)
- [📖 Dataset Usage](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-dataset-usage)
  - [Data Source](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-dataset-usage)
  - [Data Downloading](https://github.com/WenliangZhao/HRScene/blob/main/README.md#data-downloading)
  - [Data Format](https://github.com/WenliangZhao/HRScene/blob/main/README.md#data-format)
  - [Data Visualization](https://github.com/WenliangZhao/HRScene/blob/main/README.md#data-visualization)
  - [Usage Demos](https://github.com/WenliangZhao/HRScene/blob/main/README.md#usage-demos)
- [🔮 Evaluations on HRScene](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-evaluations-on-mathvista)
  - [Requirements (Optional)](https://github.com/WenliangZhao/HRScene/blob/main/README.md#requirements-optional)
  - [Downloading Images (Optional)](https://github.com/WenliangZhao/HRScene/blob/main/README.md#downloading-images-optional)
  - [Evaluation Pipelines](https://github.com/WenliangZhao/HRScene/blob/main/README.md#evaluation-pipelines)
- [📝 Evaluation Scripts of Our Models](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-evaluation-scripts-of-our-models)
  - [Evaluating Multimodal Bard](https://github.com/WenliangZhao/HRScene/blob/main/README.md#evaluating-multimodal-bard)
  - [Evaluating Chain-of-Thought GPT-4](https://github.com/WenliangZhao/HRScene/blob/main/README.md#evaluating-chain-of-thought-gpt-4)
  - [Evaluating Program-of-Thought GPT-4](https://github.com/WenliangZhao/HRScene/blob/main/README.md#evaluating-program-of-thought-gpt-4)
  - [Evaluating More Settings](https://github.com/WenliangZhao/HRScene/blob/main/README.md#evaluating-more-settings)
  - [Evaluating Large Multimodal Models](https://github.com/WenliangZhao/HRScene/blob/main/README.md#evaluating-large-multimodal-models)
- [📈 Evaluation Results](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-evaluation-results)
- [📜 License](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-license)
- [☕ Stay Connected!](https://github.com/WenliangZhao/HRScene/blob/main/README.md#coffee-stay-connected)
- [✅ Cite](https://github.com/WenliangZhao/HRScene/blob/main/README.md#white_check_mark-cite)
- [🧠 Related Work](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-related-work)
- [🤝 Contributors](https://github.com/WenliangZhao/HRScene/blob/main/README.md#-contributors)


## ⭐ About HRScene

TODO: 加点介绍的文字，然后可以放一个paper里那个饼状图，然后再放一下performance的图

## 🏆 Leaderboard 🏆

### Contributing the Leaderboard

TODO: 网站弄好了放这里

### Leaderboard on the WhiteBackground Task

TODO: 没删，留着方便改

| **#** | **Model**                            | **Method** | **Source**                                                   | **Date**   | **ALL**  | **FQA** | **GPS** | **MWP** | **TQA** | **VQA** | **ALG** | **ARI** | **GEO** | **LOG** | **NUM** | **SCI** | **STA** |
| ----- | ------------------------------------ | ---------- | ------------------------------------------------------------ | ---------- | -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| -     | **Human Performance\***              | -          | [Link](https://arxiv.org/abs/2310.02255)                     | 2023-10-03 | **60.3** | 59.7    | 48.4    | 73.0    | 63.2    | 55.9    | 50.9    | 59.2    | 51.4    | 40.7    | 53.8    | 64.9    | 63.9    |
| 1     | **OpenAI o1 🥇**                      | LMM 🖼️      | [Link](https://openai.com/index/learning-to-reason-with-llms/) | 2024-09-12 | **73.9** | -       | -       | -       | -       | -       | -       | -       | -       | -       | -       | -       | -       |


### Leaderboard on the ComplexGrid Task

| **#** | **Model**                            | **Method** | **Source**                                                   | **Date**   | **ALL**  | **FQA** | **GPS** | **MWP** | **TQA** | **VQA** | **ALG** | **ARI** | **GEO** | **LOG** | **NUM** | **SCI** | **STA** |
| ----- | ------------------------------------ | ---------- | ------------------------------------------------------------ | ---------- | -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| -     | **Human Performance\***              | -          | [Link](https://arxiv.org/abs/2310.02255)                     | 2023-10-03 | **60.3** | 59.7    | 48.4    | 73.0    | 63.2    | 55.9    | 50.9    | 59.2    | 51.4    | 40.7    | 53.8    | 64.9    | 63.9    |
| 1     | **OpenAI o1 🥇**                      | LMM 🖼️      | [Link](https://openai.com/index/learning-to-reason-with-llms/) | 2024-09-12 | **73.9** | -       | -       | -       | -       | -       | -       | -       | -       | -       | -       | -       | -       |

### Leaderboard on the RealWorld Task

| **#** | **Model**                            | **Method** | **Source**                                                   | **Date**   | **ALL**  | **FQA** | **GPS** | **MWP** | **TQA** | **VQA** | **ALG** | **ARI** | **GEO** | **LOG** | **NUM** | **SCI** | **STA** |
| ----- | ------------------------------------ | ---------- | ------------------------------------------------------------ | ---------- | -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| -     | **Human Performance\***              | -          | [Link](https://arxiv.org/abs/2310.02255)                     | 2023-10-03 | **60.3** | 59.7    | 48.4    | 73.0    | 63.2    | 55.9    | 50.9    | 59.2    | 51.4    | 40.7    | 53.8    | 64.9    | 63.9    |
| 1     | **OpenAI o1 🥇**                      | LMM 🖼️      | [Link](https://openai.com/index/learning-to-reason-with-llms/) | 2024-09-12 | **73.9** | -       | -       | -       | -       | -       | -       | -       | -       | -       | -       | -       | -       |


## 📊 Dataset Examples

Examples of our newly annotated datasets: **WhiteBackground**, **ComplexGrid**, and **RealWorld**:

### WhiteBackground

question: "Is it daytime?", answer: "[ "no", "no", "no", "no", "no", "no", "no", "no", "no", "no" ]"

<p align="center">
    <img src="example_images/whitebackground.jpg" width="60%"> <br>
</p>

### ComplexGrid

caption: "A nice living room has chairs and a love seat.", answer: "row: 1, col: 1"

<p align="center">
    <img src="example_images/complexgrid.jpg" width="60%"> <br>
</p>

### RealWorld

question: "Where is the awning-tricycle in the image? \n(A) The upper left corner \n(B) The upper right corner \n(C) The lower left corner \n(D) The lower right corner \n(E) The image does not feature the awning-tricycle", answer: "B"

<p align="center">
    <img src="example_images/realworld.jpg" width="60%"> <br>
</p>

## 📖 Dataset Usage

### Data Source

TODO: 哪里收集来的

### Data Downloading

TODO: 我会写

### Data Format

TODO: 我会写

#### WhiteBackground

#### ComplexGrid

#### RealWorld

## 🔮 Evaluations on HRScene

TODO: 我也会研究那个EvalAI

## 📝 Evaluation Scripts of Our Models

TODO: 需要可以加

## 📈 Evaluation Results

TODO: 是不是和上面的leaderborad重了？

## 📜 License

TODO: 等Aashrith收集完我加

## :white_check_mark: Cite

TODO: 等paper挂arxiv我加

## 🧠 Related Work

TODO: 要留着吗？

## 🤝 Contributors

TODO: 可以把标过数据的都加上？
