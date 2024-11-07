
# Finding Scenes in Learning Videos
## Overview

**Finding Scenes in Learning Videos** is a project that enhances the searchability and usability of educational videos by automatically generating detailed and structured metadata. Leveraging state-of-the-art Vision Language Models (VLMs) and Large Language Models (LLMs), the pipeline extracts both visual and auditory content from YouTube videos, enabling users to search for specific scenes based on comprehensive information about the video content. This pipeline is particularly useful for educators, students, and content creators looking to streamline the process of finding specific information within long-format video content.

This repo is a fork of the original repository in cooperation with the Fraunhofer Institute.

## Features

- **Automatic Metadata Generation:** Creates rich, searchable metadata by processing a YouTube video link, allowing users to navigate and find specific scenes or topics within the video.
- **Scene Detection:** Automatically segments videos into meaningful scenes using advanced visual and auditory analysis.
- **Key Frame Extraction:** Identifies significant frames within each scene to optimize metadata generation, ensuring efficient and high-quality content analysis.
- **Comprehensive Metadata Structure:** Captures detailed information such as video descriptions, scene captions, key concepts, questions, resources, and much more.
- **User-Friendly API:** Allows users to input a YouTube link and receive metadata, supporting seamless integration into other applications.
- **JSON Output:** Returns metadata in a structured JSON format, making it easy to parse, manipulate, and use in various applications.

## Installation

### Python Dependencies

It is recommended to set up a [virtual environment](https://docs.python.org/3/library/venv.html) to manage dependencies.

```bash
pip install -r requirements.txt
```

### Non-Python Dependencies

#### Arch

```bash
sudo pacman -S ffmpeg
```

#### Ubuntu

```bash
sudo apt-get install ffmpeg
sudo apt install imagemagick
```

Additionally, configure ImageMagick permissions:

```bash
sudo sh -c "cat /etc/ImageMagick-6/policy.xml | sed 's/none/read,write/g' > /etc/ImageMagick-6/policy.xml"
```

## Running the Pipeline

You can run the pipeline either locally or using Google Colab.

### Running Locally

1. **Start the FastAPI Server:**

   ```bash
   uvicorn main:app --reload
   ```

2. **Submit a YouTube Link:**

   Access the API endpoint via your browser or use tools like `curl` or `Postman` to submit a YouTube link and receive the corresponding metadata.

### Using the Colab Pipeline

Open the `colab_pipeline.ipynb` notebook in [Google Colab](https://colab.research.google.com/) and follow the instructions to input your YouTube video link and generate metadata.

## Methodology

The pipeline is designed to automatically generate metadata for educational videos, capturing essential details to enhance searchability and usability. The process follows these steps:

1. **Video Downloading:** Utilizes `YT-DLP` to robustly download YouTube videos.
2. **Audio Transcript Extraction:** Employs `Pytubefix` to extract audio transcripts and additional metadata from the video.
3. **Scene Detection:** Uses `PySceneDetect` to segment the video into scenes, identifying significant scene boundaries through changes in visual properties.
4. **Key Frame Extraction:** Leverages `Katna` to select key frames within each scene based on metrics like brightness, contrast, and color changes.
5. **Metadata Generation:**
   - **Vision Language Models (VLMs):** Processes key frames and audio transcripts to generate initial metadata.
   - **Large Language Models (LLMs):** Contextualizes and enriches the metadata with comprehensive descriptions for each scene and the entire video.
6. **JSON Metadata Output:** Compiles all generated data into a structured JSON object, providing detailed metadata for each scene and the video as a whole.

### Pipeline Goals

- **Ease of Use:** Users only need to input a YouTube link to interact with the pipeline, which is also available as an API.
- **Enhanced Searchability:** Meaningful scene segmentation makes each part of the video easily searchable.
- **Efficient Metadata Creation:** Key frame selection optimizes the metadata generation process, avoiding unnecessary processing of every frame.
- **Contextual Metadata Content:** Combines visual data from key frames with auditory data from transcripts to create in-depth metadata.
- **Structured Output Format:** The JSON metadata format facilitates integration into other applications and platforms.

## Example Metadata Structure

The metadata is structured in JSON format, organized to provide rich information for each video and scene.

```json
{
  "MetaDataObject": {
    "youtube_title": "str",
    "youtube_description": "str",
    "published_date": "str",
    "youtube_video_id": "str",
    "youtube_thumbnail_url": "str",
    "youtube_rating": "str",
    "youtube_views": "str",
    "youtube_age_restricted": "str",
    "youtube_keywords": ["str"],
    "youtube_author": "str",
    "youtube_channel_id": "str",
    "youtube_length": "int",
    "url": "str",
    "llm_description": "str",
    "learning_resource_type": "str",
    "intended_end_user_role": "str",
    "context": "str",
    "difficulty_level": "str",
    "discipline": "str",
    "educational_level": "str",
    "target_audience_age": "str",
    "typical_learning_time": "str",
    "scene_objects": ["SceneObject"]
  },
  "SceneObject": {
    "duration": "str",
    "scene_start": "str",
    "scene_end": "str",
    "title": "str",
    "caption": "str",
    "key-concepts": "str",
    "questions": "str",
    "text": "str",
    "resources": "str",
    "language": "str",
    "video_type": "str"
  }
}
```

*Note: Some fields may contain inaccuracies due to current limitations in the metadata generation process.*

## Evaluation

To assess the pipeline's accuracy, a manually annotated dataset containing captions for 10 learning videos was used. The evaluation metrics include BLEU, METEOR, ROUGE-L, CIDEr, and SPICE. While the model's scores are slightly lower than existing video captioning methods, this highlights areas for improvement in terms of relevance and accuracy.

| Metric  | Score  |
|---------|--------|
| BLEU@1  | 0.244  |
| BLEU@2  | 0.121  |
| BLEU@3  | 0.071  |
| BLEU@4  | 0.047  |
| METEOR  | 0.067  |
| ROUGE-L | 0.184  |
| CIDEr   | 0.075  |
| SPICE   | 0.071  |

## Future Work

- **Model Enhancement:** Use larger, more specialized VLMs and LLMs for improved metadata quality.
- **Fine-Tuning:** Tailor models for educational video contexts to better capture nuances.
- **Audio Analysis Integration:** Use audio analysis to improve scene categorization and metadata relevance.
- **Semantic Search Integration:** Enhance content retrieval with semantic search and embedding models.
- **Quality Assessment:** Develop methods to assess and ensure the quality of generated metadata.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to the following open-source tools and libraries used in this project:

- FastAPI
- YT-DLP
- Pytubefix
- PySceneDetect
- Katna
- Idefics2-8B
- Mistral-7B-Instruct-v0.3


## Citation

If you use this project in your research, please cite it as follows:

```
@inproceedings{finding_scenes_2024,
  title={Finding Scenes in Learning Videos},
  author={Hamdad, Samy and Laule, Veit and Malek, Limin},
  booktitle={AWT Project SS 24},
  year={2024},
  organization={OpenAI}
}
```
