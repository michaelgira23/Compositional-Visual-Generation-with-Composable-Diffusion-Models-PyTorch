from diffusers import StableDiffusionImageVariationPipeline
from PIL import Image
from torchvision import transforms
import datetime
import torch as th

device = "cuda:0"
sd_pipe = StableDiffusionImageVariationPipeline.from_pretrained(
	"lambdalabs/sd-image-variations-diffusers",
	revision="v2.0",
	)
sd_pipe = sd_pipe.to(device)

im = Image.open("inputs/beach.png")
tform = transforms.Compose([
		transforms.ToTensor(),
		transforms.Resize(
				(224, 224),
				interpolation=transforms.InterpolationMode.BICUBIC,
				antialias=False,
				),
		transforms.Normalize(
			[0.48145466, 0.4578275, 0.40821073],
			[0.26862954, 0.26130258, 0.27577711]),
])
inp = tform(im).to(device).unsqueeze(0)

generator = th.Generator("cuda").manual_seed(2)
out = sd_pipe(inp, guidance_scale=4, num_images_per_prompt=1, generator=generator)
for i, image in enumerate(out["images"]):
	filename = f'{str(datetime.datetime.now())}-{i}.png'
	filename = filename.replace(' |', ',')
	filename = filename.replace(':', '-')
	filename = filename.replace('/', '-')
	image.save(filename)
	# image.save(f'palm-out/{filename}'))
