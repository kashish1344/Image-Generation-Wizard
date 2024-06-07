# Image Generation Wizard

Welcome to **Image Generation Wizard**! This innovative web application allows you to generate stunning images from text prompts using a state-of-the-art deep learning model. Simply describe your vision, and let our AI bring your imagination to life.

## Features

- **Text-to-Image Generation**: Enter a text prompt and generate an image based on your description.
- **Responsive Design**: Enjoy a seamless user experience across devices with our modern, responsive UI.
- **Downloadable Art**: Easily download your generated artwork with a single click.

## Demo


https://github.com/kashish1344/Image-Generation-Wizard/assets/83247791/8de2d693-ed2d-4536-a456-2ee2bea71498

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- [PyTorch](https://pytorch.org/get-started/locally/)
- [Diffusers](https://huggingface.co/docs/diffusers/installation)
- Flask

### Installation

1. **Clone the repository**:
    ```bash
    git clone [https://github.com/yourusername/Image-Generation-Wizard.git](https://github.com/kashish1344/Image-Generation-Wizard.git)
    cd image-generation-wizard
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

5. **Navigate to** `http://127.0.0.1:5000/` **in your web browser**.

## Usage

1. Enter your text prompt in the input field.
2. Click on the **Create Masterpiece** button.
3. Wait for the image to be generated.
4. Click the download icon at the top-right corner of the image to save it to your device.

## Code Overview

### `app.py`

- **Libraries**:
    - `warnings`, `deprecate`: Suppresses future warnings from the `diffusers` library.
    - `Flask`: For creating the web application.
    - `AutoPipelineForText2Image`: To load the pre-trained text-to-image model.
    - `torch`: PyTorch library for tensor computations.
    - `PIL`: Python Imaging Library for image processing.
    - `io`, `base64`, `os`, `uuid`: Standard libraries for file handling and encoding.

- **Routes**:
    - **`/` (GET, POST)**: Main route to display the form and generate images.
    - **`/download/<img_id>` (GET)**: Route to handle image download requests.

- **Functions**:
    - **`index`**: Handles the form submission, generates the image from the text prompt, encodes it, and saves it to a temporary file.
    - **`download`**: Sends the generated image file to the user for download.

### `templates/index.html`

- **HTML Template**: Provides a responsive and modern UI for the application.
- **CSS**: Includes custom styles to enhance the visual appeal of the application.
- **JavaScript**: Adds interactivity and animations to the UI elements.

## Screenshots

![Home Page](static/screenshot1.png)
![Generated Image](static/screenshot2.png)

## Future Enhancements

- **Multiple Image Generation**: Allow users to generate multiple images from a single prompt.
- **Customization Options**: Provide options to customize the generated images (e.g., style, color scheme).
- **Gallery**: Create a gallery to showcase the best user-generated images.

## Contributing

We welcome contributions from the community. If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the [Hugging Face](https://huggingface.co/) team for their amazing `diffusers` library.
- Inspired by the creativity of the open-source community.
