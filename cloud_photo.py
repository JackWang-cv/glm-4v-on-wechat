import cloudinary
import cloudinary.uploader

# Configuration
cloudinary.config(
    cloud_name = "dsqtyrogq",
    api_key = "692895576253772",
    api_secret = "88IDVDKnb9jnutbVBNuMxVe7-Oo", # Click 'View Credentials' below to copy your API secret
    secure=True
)

def upload_image(image_path):
    response = cloudinary.uploader.upload(image_path)
    return response['url']

if __name__ == "__main__":
    image_url = upload_image('tmp/240719-211109.png')
    print(image_url)
