import warnings
from diffusers.utils import deprecate
warnings.filterwarnings("ignore", category=FutureWarning, module="diffusers.models.transformers.transformer_2d")

from flask import Flask, render_template, request, send_file
from diffusers import AutoPipelineForText2Image
import torch
from PIL import Image
import io
import base64
import os
import uuid

app = Flask(__name__)

# Load the pre-trained model
pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
pipe.to("cuda")

@app.route("/", methods=["GET", "POST"])
def index():
    img_data = None
    img_id = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        # Generate the image
        image = pipe(prompt=prompt, num_inference_steps=2, guidance_scale=0.2).images[0]
        if not isinstance(image, Image.Image):
            image = Image.fromarray(image)

        # Save the image to a BytesIO object
        img_io = io.BytesIO()
        image.save(img_io, "PNG")
        img_io.seek(0)

        # Encode the image to base64
        img_data = base64.b64encode(img_io.getvalue()).decode()

        # Save the image to a temporary file
        img_id = str(uuid.uuid4())
        with open(f"static/{img_id}.png", "wb") as img_file:
            img_file.write(img_io.getvalue())

    return render_template("index.html", img_data=img_data, img_id=img_id)

@app.route("/download/<img_id>")
def download(img_id):
    file_path = f"static/{img_id}.png"
    if not os.path.exists(file_path):
        return "Image not found", 404

    return send_file(file_path, mimetype="image/png", as_attachment=True, download_name="generated_image.png")

if __name__ == "__main__":
    app.run(debug=True)
